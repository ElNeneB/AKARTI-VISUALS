#!/usr/bin/env python3
"""Guardia de Higgsfield (hook PreToolUse). Hace cumplir solo las reglas de ahorro.

Bloquea, antes de que se gaste un crédito:
  - Kling con sonido distinto de "off", duración distinta de 4 s o formato distinto de 16:9.
  - Generar sin estado-<propiedad>.md con la Puerta A aprobada (nota 9 o 10) y la calidad elegida.
  - show_generations (repite el prompt de cada clip y gasta tokens de más).
  - upscale_video a más de 30 fps (duplica el costo).
  - Cualquier envío que haga pasar el tope de presupuesto-corrida.json (si existe):
    cada envío suma su costo estimado aunque luego falle (cuenta de más, nunca de menos).
Las consultas de costo (get_cost: true) siempre pasan.
Saltar la regla del estado, solo si Enrique lo pide: AKARTI_SIN_ESTADO=1
"""
import glob
import json
import os
import re
import sys


def negar(motivo):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": motivo}}, ensure_ascii=False))
    sys.exit(0)


def params_de(p):
    if isinstance(p, str):
        try:
            p = json.loads(p)
        except ValueError:
            return {}
    return p if isinstance(p, dict) else {}


def revisar_clip(p, etiqueta):
    p = params_de(p)
    if p.get("get_cost"):
        return
    if not str(p.get("model", "")).startswith("kling"):
        return
    errores = []
    if str(p.get("sound", "on")).lower() != "off":
        errores.append('sound debe ser "off" (clip de 6 créditos en vez de 8)')
    if p.get("duration") != 4:
        errores.append("duration debe ser 4")
    if p.get("aspect_ratio") != "16:9":
        errores.append('aspect_ratio debe ser "16:9"')
    if errores:
        negar(f"Regla de Akarti en {etiqueta}: " + "; ".join(errores) +
              ". Corrige los parámetros y vuelve a enviar.")


COSTO_SEGUNDO = {"std": 1.5, "pro": 1.75, "4k": 3.0}  # Kling 3.0 sonido OFF (get_cost, 6/10)


def costo_clip(p):
    p = params_de(p)
    if not str(p.get("model", "")).startswith("kling"):
        return 2.0  # otro modelo de video: estimación conservadora
    return COSTO_SEGUNDO.get(str(p.get("mode", "std")), 3.0) * int(p.get("duration", 5))


ID_LLAMADA = None  # tool_use_id de la llamada actual (para no cobrar dos veces)


def cobrar(cwd, costo, detalle):
    """Suma el costo a presupuesto-corrida.json o niega si se pasa del tope."""
    ruta = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR", cwd), "presupuesto-corrida.json")
    if not os.path.exists(ruta):
        return
    with open(ruta, encoding="utf-8") as f:
        p = json.load(f)
    if ID_LLAMADA and any(h.get("id") == ID_LLAMADA for h in p.get("historial", [])):
        return  # el hook corrió dos veces para la misma llamada: ya está cobrada
    if p["comprometido"] + costo > p["tope"]:
        negar(f"Tope de la corrida: van {p['comprometido']:.2f} de {p['tope']} créditos y este "
              f"envío ({detalle}) cuesta {costo:.2f}. No se envía. Termina lo que esté a medias "
              "sin generar más y reporta.")
    p["comprometido"] = round(p["comprometido"] + costo, 2)
    p.setdefault("historial", []).append({"detalle": detalle, "creditos": costo, "id": ID_LLAMADA})
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=1)


def revisar_estado(cwd):
    if os.environ.get("AKARTI_SIN_ESTADO") == "1":
        return
    archivos = [f for f in glob.glob(os.path.join(cwd, "estado-*.md"))
                if "PLANTILLA" not in os.path.basename(f)]
    for f in archivos:
        t = open(f, encoding="utf-8").read()
        if (re.search(r"^puerta_A_nota:\s*(9|10)\b", t, re.M) and
                re.search(r"^calidad_kling:\s*(std|pro|4k)\b", t, re.M | re.I)):
            return
    negar("Falta el permiso para gastar: no hay un estado-<propiedad>.md con "
          "`puerta_A_nota: 9` (o 10) y `calidad_kling: std|pro|4k`. Hace la auditoría y "
          "la puerta A (skill no-gastar) y pregunta la calidad antes de generar.")


def main():
    global ID_LLAMADA
    d = json.load(sys.stdin)
    ID_LLAMADA = d.get("tool_use_id")
    herramienta = d.get("tool_name", "").split("__")[-1]
    entrada = d.get("tool_input", {})
    if herramienta == "show_generations":
        negar("show_generations repite el prompt completo de cada clip y gasta uso de "
              "Claude. Usa los job_id de estado-<propiedad>.md con jobs_wait.")
    if herramienta == "upscale_video":
        p = params_de(entrada.get("params"))
        if float(p.get("fps", 24)) > 30:
            negar("upscale_video a más de 30 fps duplica el costo. Usa fps: 24 (skill calidad).")
        cobrar(d.get("cwd", os.getcwd()), 0.1, "upscale 1 clip")
    if herramienta == "generate_video":
        p = params_de(entrada.get("params"))
        if not p.get("get_cost"):
            revisar_clip(p, "generate_video")
            if str(p.get("model", "")).startswith("kling"):
                revisar_estado(d.get("cwd", os.getcwd()))
            cobrar(d.get("cwd", os.getcwd()), costo_clip(p) * int(p.get("count", 1)),
                   "generate_video")
    elif herramienta == "generate_video_batch":
        reqs = entrada.get("requests", [])
        for r in reqs:
            revisar_clip(r.get("params"), f"el clip {r.get('index')}")
        if any(str(params_de(r.get("params")).get("model", "")).startswith("kling")
               for r in reqs):
            revisar_estado(d.get("cwd", os.getcwd()))
        cobrar(d.get("cwd", os.getcwd()), sum(costo_clip(r.get("params")) for r in reqs),
               f"batch de {len(reqs)} clips")


if __name__ == "__main__":
    main()
