#!/usr/bin/env python3
"""Herramientas de ahorro de Akarti Visuals (requiere ffmpeg y ffprobe en el PATH).

Cada comando junta en UNA sola imagen lo que antes se le mostraba a Claude en
varias, o devuelve un número en texto en vez de una imagen. Menos imágenes en
el chat = menos tokens en cada mensaje que sigue.

  python3 akarti.py juez-clip CLIP.mp4 FOTO.jpg [SALIDA.jpg]
      Hoja 2x2 para la puerta B: foto original | 0,5 s
                                  2 s          | 3,5 s
  python3 akarti.py hoja-fotos CARPETA [SALIDA_PREFIJO]
      Hojas de 3x2 fotos numeradas (fila por fila) para la auditoría.
  python3 akarti.py recorte169 CARPETA_ENTRADA CARPETA_SALIDA
      Recorta al centro a 16:9 y deja cada foto en 1920x1080 antes de subirla.
  python3 akarti.py audio VIDEO.mp4
      Loudness integrado (LUFS) y true peak (dBTP) medidos, para la puerta C.
"""
import json
import pathlib
import re
import subprocess
import sys

FOTOS = {".jpg", ".jpeg", ".png", ".webp"}
TILE_W, TILE_H = 768, 432  # 2x2 = 1536x864, una sola imagen (~1.800 tokens)


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def fit(label, w=TILE_W, h=TILE_H):
    """Encaja la imagen en un cuadro w x h sin deformarla (bandas negras)."""
    return (f"[{label}]scale={w}:{h}:force_original_aspect_ratio=decrease,"
            f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1")


def juez_clip(clip, foto, salida=None):
    salida = salida or str(pathlib.Path(clip).with_suffix("")) + "_juez.jpg"
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "csv=p=0", clip]).stdout)
    tiempos = [min(t, max(dur - 0.05, 0)) for t in (0.5, 2.0, 3.5)]
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", foto]
    for t in tiempos:
        cmd += ["-ss", f"{t:.2f}", "-i", clip]
    filtros = [fit("0:v") + "[a]"] + [fit(f"{i}:v") + f"[{c}]"
                                      for i, c in zip((1, 2, 3), "bcd")]
    filtros.append("[a][b][c][d]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[o]")
    cmd += ["-filter_complex", ";".join(filtros), "-map", "[o]",
            "-frames:v", "1", "-q:v", "3", salida]
    run(cmd)
    print(f"{salida}  (arriba: foto | 0,5 s · abajo: 2 s | 3,5 s)")


def hoja_fotos(carpeta, prefijo=None):
    fotos = sorted(p for p in pathlib.Path(carpeta).iterdir()
                   if p.suffix.lower() in FOTOS and not p.name.startswith("hoja_"))
    if not fotos:
        sys.exit("No hay fotos en la carpeta.")
    prefijo = prefijo or str(pathlib.Path(carpeta) / "hoja")
    w, h = 512, 384  # 3x2 = 1536x768 por hoja
    for n in range(0, len(fotos), 6):
        grupo = fotos[n:n + 6]
        cmd = ["ffmpeg", "-v", "error", "-y"]
        for p in grupo:
            cmd += ["-i", str(p)]
        for _ in range(6 - len(grupo)):  # rellena la última hoja con negro
            cmd += ["-f", "lavfi", "-i", f"color=black:s={w}x{h}"]
        filtros = [fit(f"{i}:v", w, h) + f"[t{i}]" for i in range(6)]
        filtros.append("".join(f"[t{i}]" for i in range(6)) +
                       "xstack=inputs=6:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0[o]")
        salida = f"{prefijo}_{n // 6 + 1:02d}.jpg"
        cmd += ["-filter_complex", ";".join(filtros), "-map", "[o]",
                "-frames:v", "1", "-q:v", "3", salida]
        run(cmd)
        print(salida)
        for i, p in enumerate(grupo):
            print(f"  Foto {n + i + 1}: {p.name}  (posición {i + 1}, fila por fila)")


def recorte169(entrada, salida):
    out = pathlib.Path(salida)
    out.mkdir(parents=True, exist_ok=True)
    for p in sorted(pathlib.Path(entrada).iterdir()):
        if p.suffix.lower() not in FOTOS or p.name.startswith("hoja_"):
            continue
        vf = ("crop='if(gt(iw/ih,16/9),ih*16/9,iw)':'if(gt(iw/ih,16/9),ih,iw*9/16)',"
              "scale=1920:1080")
        destino = out / (p.stem + ".jpg")
        run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-vf", vf, "-q:v", "2",
             str(destino)])
        print(destino)


def audio(video):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", video,
                        "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    resumen = r.stderr[r.stderr.rfind("Summary:"):]
    lufs = re.search(r"I:\s+(-?[\d.]+) LUFS", resumen)
    pico = re.search(r"Peak:\s+(-?[\d.]+) dBFS", resumen)
    if not lufs:
        sys.exit("No se pudo medir el audio (¿el video tiene pista de audio?).")
    i, tp = float(lufs.group(1)), float(pico.group(1)) if pico else None
    ok = -15 <= i <= -13 and tp is not None and tp <= -1
    print(json.dumps({"lufs_integrado": i, "true_peak_dbtp": tp,
                      "puerta_C_criterio_7": "✓" if ok else "✗"}, ensure_ascii=False))


if __name__ == "__main__":
    comandos = {"juez-clip": juez_clip, "hoja-fotos": hoja_fotos,
                "recorte169": recorte169, "audio": audio}
    if len(sys.argv) < 2 or sys.argv[1] not in comandos:
        sys.exit(__doc__)
    comandos[sys.argv[1]](*sys.argv[2:])
