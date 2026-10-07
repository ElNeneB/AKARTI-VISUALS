#!/usr/bin/env python3
"""Identidad visual de Akarti Visuals (requiere Pillow: python3 -m pip install pillow).

Paleta: carbón cálido, blanco hueso y acento champán (sin azul eléctrico).
Tipografía: Cormorant Garamond (marca y títulos) + Jost (textos pequeños con tracking).

  python3 marca.py end-card SALIDA.png [ANCHO ALTO]
  python3 marca.py marca-agua SALIDA.png [ANCHO ALTO]
  python3 marca.py titulo "Nombre" "Zona" SALIDA.png [ANCHO ALTO]
"""
import math
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FUENTES = pathlib.Path(__file__).resolve().parent.parent / "assets" / "fuentes"
CARBON = (18, 17, 16)
CARBON_CLARO = (31, 29, 27)
HUESO = (237, 230, 218)
CHAMPAN = (184, 153, 106)

END_CARD = ["AKARTI", "REAL ESTATE VISUALS", "TU PROPIEDAD, EN MOVIMIENTO.",
            "WhatsApp +51 908 812 483"]


def fuente(nombre, tam, peso):
    f = ImageFont.truetype(str(FUENTES / nombre), tam)
    try:
        f.set_variation_by_axes([peso])
    except OSError:
        pass
    return f


def serif(tam, peso=500):
    return fuente("CormorantGaramond[wght].ttf", tam, peso)


def serif_italica(tam, peso=400):
    return fuente("CormorantGaramond-Italic[wght].ttf", tam, peso)


def sans(tam, peso=300):
    return fuente("Jost[wght].ttf", tam, peso)


def ancho_espaciado(d, texto, f, tracking):
    return sum(d.textlength(c, font=f) for c in texto) + tracking * (len(texto) - 1)


def texto_espaciado(d, centro_x, y, texto, f, color, tracking):
    """Dibuja texto centrado con espaciado entre letras (tracking en píxeles)."""
    x = centro_x - ancho_espaciado(d, texto, f, tracking) / 2
    for c in texto:
        d.text((x, y), c, font=f, fill=color)
        x += d.textlength(c, font=f) + tracking


def end_card(salida, ancho=1920, alto=1080):
    """End card con el logo oficial (emblema + AKARTI REAL ESTATE VISUALS), el lema y el WhatsApp."""
    ancho, alto = int(ancho), int(alto)
    k = alto / 1080
    fondo = Image.new("RGB", (ancho, alto), CARBON)
    luz = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(luz).ellipse([ancho * 0.18, alto * 0.02, ancho * 0.82, alto * 0.92], fill=255)
    luz = luz.filter(ImageFilter.GaussianBlur(int(260 * k)))
    fondo = Image.composite(Image.new("RGB", (ancho, alto), CARBON_CLARO), fondo, luz).convert("RGBA")
    d = ImageDraw.Draw(fondo)
    cx = ancho / 2
    _, _, lema, contacto = END_CARD
    logo = Image.open(FUENTES.parent / "marca" / "logo-akarti.png")
    alto_logo = int(500 * k)
    logo = logo.resize((int(logo.width * alto_logo / logo.height), alto_logo), Image.LANCZOS)
    y_logo = int(190 * k)  # el bloque va abajo, pegado al número
    fondo.alpha_composite(logo, (int(cx - logo.width / 2), y_logo))
    y_linea = y_logo + alto_logo + int(48 * k)
    d.line([cx - 70 * k, y_linea, cx + 70 * k, y_linea], fill=CHAMPAN, width=max(1, int(2 * k)))
    texto_espaciado(d, cx, y_linea + int(34 * k), lema, serif_italica(int(50 * k), 400),
                    CHAMPAN, int(5 * k))
    texto_espaciado(d, cx, alto * 0.875, contacto, sans(int(44 * k), 400), HUESO, int(6 * k))
    fondo.convert("RGB").save(salida)
    print(salida)


def marca_agua(salida, ancho=1920, alto=1080, opacidad=0.10):
    ancho, alto = int(ancho), int(alto)
    k = alto / 1080
    lado = int(math.hypot(ancho, alto)) + 200
    capa = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    f = sans(int(34 * k), 400)
    texto = "AKARTI VISUALS  ·  DEMO"
    paso_x = ancho_espaciado(d, texto, f, int(8 * k)) + 160 * k
    paso_y = 190 * k
    alfa = int(255 * opacidad)
    for fila, y in enumerate(range(0, lado, int(paso_y))):
        desfase = (fila % 2) * paso_x / 2
        x = -desfase
        while x < lado:
            texto_espaciado(d, x + paso_x / 2, y, texto, f, (255, 255, 255, alfa), int(8 * k))
            x += paso_x
    capa = capa.rotate(30, resample=Image.BICUBIC)
    l, t = (lado - ancho) // 2, (lado - alto) // 2
    capa.crop((l, t, l + ancho, t + alto)).save(salida)
    print(salida)


def titulo(nombre, zona, salida, ancho=1920, alto=1080):
    """Título discreto abajo a la izquierda, sobre fondo transparente, con sombra suave."""
    ancho, alto = int(ancho), int(alto)
    k = alto / 1080
    capa = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    x, y = int(96 * k), int(alto - 210 * k)
    f_nombre, f_zona = serif(int(62 * k), 500), sans(int(22 * k), 400)
    d.text((x, y), nombre, font=f_nombre, fill=HUESO + (255,))
    d.line([x, y + f_nombre.size * 1.18, x + 48 * k, y + f_nombre.size * 1.18],
           fill=CHAMPAN + (255,), width=max(1, int(2 * k)))
    zx = x
    for c in zona.upper():
        d.text((zx, y + f_nombre.size * 1.38), c, font=f_zona, fill=HUESO + (230,))
        zx += d.textlength(c, font=f_zona) + 7 * k
    sombra = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    sombra.putalpha(capa.getchannel("A").point(lambda a: int(a * 0.55)))
    sombra = sombra.filter(ImageFilter.GaussianBlur(int(10 * k)))
    Image.alpha_composite(sombra, capa).save(salida)
    print(salida)


if __name__ == "__main__":
    comandos = {"end-card": end_card, "marca-agua": marca_agua, "titulo": titulo}
    if len(sys.argv) < 3 or sys.argv[1] not in comandos:
        sys.exit(__doc__)
    comandos[sys.argv[1]](*sys.argv[2:])
