#!/usr/bin/env python3
"""Guardia de Higgsfield (hook PreToolUse). Hace cumplir solo las reglas de ahorro.

Bloquea, antes de que se gaste un crédito:
  - Kling con sonido distinto de "off", duración distinta de 4 s o formato distinto de 16:9.
  - Generar sin estado-<propiedad>.md con la Puerta A aprobada (nota 9 o 10) y la calidad elegida.
  - show_generations (repite el prompt de cada clip y gasta tokens de más).
  - upscale_video a más de 30 fps (duplica el costo).
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
    d = json.load(sys.stdin)
    herramienta = d.get("tool_name", "").split("__")[-1]
    entrada = d.get("tool_input", {})
    if herramienta == "show_generations":
        negar("show_generations repite el prompt completo de cada clip y gasta uso de "
              "Claude. Usa los job_id de estado-<propiedad>.md con jobs_wait.")
    if herramienta == "upscale_video":
        p = params_de(entrada.get("params"))
        if float(p.get("fps", 24)) > 30:
            negar("upscale_video a más de 30 fps duplica el costo. Usa fps: 24 (skill calidad).")
    if herramienta == "generate_video":
        p = params_de(entrada.get("params"))
        if not p.get("get_cost"):
            revisar_clip(p, "generate_video")
            if str(p.get("model", "")).startswith("kling"):
                revisar_estado(d.get("cwd", os.getcwd()))
    elif herramienta == "generate_video_batch":
        reqs = entrada.get("requests", [])
        for r in reqs:
            revisar_clip(r.get("params"), f"el clip {r.get('index')}")
        if any(str(params_de(r.get("params")).get("model", "")).startswith("kling")
               for r in reqs):
            revisar_estado(d.get("cwd", os.getcwd()))


if __name__ == "__main__":
    main()
