#!/usr/bin/env python3
"""Ayudante de la corrida desatendida (akarti-noche.sh).

  python3 corrida.py lista        Cola de teasers pendientes (una línea por propiedad, separada por |)
  python3 corrida.py restante     Créditos que quedan del tope (presupuesto-corrida.json)
  python3 corrida.py resumen      Resumen final: teasers hechos, créditos y pendientes
"""
import csv
import json
import pathlib
import re
import sys
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PRESUPUESTO = RAIZ / "presupuesto-corrida.json"
RESERVA_TEASER = 36  # 3 clips + 3 reintentos (6 c/u) + upscale

PERSONALIDAD = [  # zonas completas, en orden de prioridad
    ("lodge-andino", ["ocosuyo", "ollantaytambo", "urubamba", "bongara", "saquena", "iquitos",
                      "san juan", "cashapampa", "huaylas", "huaraz", "valle sagrado", "lodge"]),
    ("campo-calido", ["cieneguilla", "pachacamac", "lurin", "chosica", "lurigancho",
                      "huarochiri", "cocachacra", "casa de campo", "hacienda"]),
    ("playa-luminosa", ["mancora", "pocitas", "vichayito", "punta sal", "canoas", "nuro",
                        "organos", "talara", "punta negra", "santa rosa", "contralmirante villar",
                        "punta mero", "playa", "frente al mar"]),
    ("moderno-urbano", ["lima", "san isidro", "miraflores", "san miguel", "barranco", "larcomar"]),
]


def ascii_(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()


def slug(nombre):
    palabras = re.findall(r"[a-z0-9]+", ascii_(nombre))
    return "-".join(palabras[:4]) or "propiedad"


def personalidad(zona, nombre):
    texto = ascii_(zona + " " + nombre)
    for clave, zonas in PERSONALIDAD:
        if any(re.search(rf"\b{re.escape(z)}\b", texto) for z in zonas):
            return clave
    return "playa-luminosa"


def propiedades():
    with open(RAIZ / "propiedades-teaser.csv", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    cab = filas[0]
    for fila in filas[1:]:
        d = dict(zip(cab, fila))
        if not d.get("Propiedad"):
            continue
        yield {"id": d["# hoja"].split(".")[0], "nombre": d["Propiedad"], "zona": d["Zona"],
               "link": d["Link Airbnb"], "veredicto": d["Veredicto"],
               "fotos": d["Fotos a descargar"].replace("|", "/"),
               "notas": d["Notas"].replace("|", "/")}


def hecho(s):
    return (RAIZ / "teasers" / s / f"teaser-{s}.mp4").exists()


def lista():
    vistos = set()
    for p in propiedades():
        if p["id"] == "181":  # mismo lodge que la fila 180: un solo recorrido combinado
            continue
        s = slug(p["nombre"])
        if s in vistos or hecho(s):
            continue
        vistos.add(s)
        extra = (" Combinar con el set de https://www.airbnb.com.pe/rooms/1445794061713160553 "
                 "(mismo lodge)." if p["id"] == "180" else "")
        print("|".join([p["id"], s, p["nombre"], p["zona"], p["link"],
                        personalidad(p["zona"], p["nombre"]), p["fotos"], p["notas"] + extra]))


def restante():
    if not PRESUPUESTO.exists():
        print(0)
        return
    p = json.loads(PRESUPUESTO.read_text(encoding="utf-8"))
    print(round(p["tope"] - p["comprometido"], 2))


def resumen():
    hechos = sorted((RAIZ / "teasers").glob("*/teaser-*.mp4")) if (RAIZ / "teasers").exists() else []
    p = json.loads(PRESUPUESTO.read_text(encoding="utf-8")) if PRESUPUESTO.exists() else {}
    print(f"Teasers listos: {len(hechos)}")
    for h in hechos:
        print(f"  {h.relative_to(RAIZ)}")
    if p:
        print(f"Créditos comprometidos: {p['comprometido']} de {p['tope']}")
    pendientes = sum(1 for _ in propiedades()) - len(hechos)
    print(f"Propiedades sin teaser: {pendientes}")


if __name__ == "__main__":
    comandos = {"lista": lista, "restante": restante, "resumen": resumen}
    if len(sys.argv) < 2 or sys.argv[1] not in comandos:
        sys.exit(__doc__)
    comandos[sys.argv[1]]()
