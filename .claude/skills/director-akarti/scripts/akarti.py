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
  python3 akarti.py filtro-fotos CARPETA
      Pre-filtro sin mirar: duplicados, borrosas, baja resolución, verticales y
      luz distinta al resto. El auditor solo revisa lo que queda en duda.
  python3 akarti.py final-push FOTO_169.jpg SALIDA.jpg [PORCENTAJE=12]
      Fotograma final para DOLLY / AXIS LOCK: recorte centrado de la misma foto.
  python3 akarti.py bpm MUSICA.(mp3|wav|m4a)
      BPM y desfase del primer beat, para la biblioteca de música.
  python3 akarti.py montaje MONTAJE.json SALIDA.xml
      Línea de tiempo (XML de Final Cut 7, Premiere lo importa) con los clips
      recortados a beats enteros, música, room tone y end card.
  python3 akarti.py registrar PROPIEDAD MODO CLIPS REINTENTOS CREDITOS MINUTOS NOTA_C
      Agrega una fila a registro.csv (costo real por video).
"""
import csv
import datetime
import json
import math
import pathlib
import statistics
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


def gris(ruta, w, h):
    """Píxeles en escala de grises (0-255) de la imagen escalada a w x h."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ruta), "-vf",
                        f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
                       check=True, capture_output=True)
    return r.stdout


def tam(ruta):
    w, h = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                "stream=width,height", "-of", "csv=p=0", str(ruta)]).stdout.split(",")[:2]
    return int(w), int(h)


def filtro_fotos(carpeta):
    fotos = sorted(p for p in pathlib.Path(carpeta).iterdir()
                   if p.suffix.lower() in FOTOS and not p.name.startswith("hoja_"))
    datos = []
    for n, p in enumerate(fotos, 1):
        w, h = tam(p)
        px = gris(p, 9, 8)  # dHash de 64 bits
        dhash = sum(1 << i for i in range(64)
                    if px[(i // 8) * 9 + i % 8] > px[(i // 8) * 9 + i % 8 + 1])
        bw, bh = 384, 256
        g = gris(p, bw, bh)
        lap = [4 * g[y * bw + x] - g[y * bw + x - 1] - g[y * bw + x + 1]
               - g[(y - 1) * bw + x] - g[(y + 1) * bw + x]
               for y in range(1, bh - 1) for x in range(1, bw - 1)]
        datos.append({"n": n, "archivo": p.name, "w": w, "h": h, "dhash": dhash,
                      "nitidez": statistics.pvariance(lap), "luz": sum(g) / len(g)})
    nit_med = statistics.median(d["nitidez"] for d in datos)
    luz_med = statistics.median(d["luz"] for d in datos)
    for d in datos:
        marcas = []
        for o in datos:
            if o["n"] < d["n"] and bin(o["dhash"] ^ d["dhash"]).count("1") <= 6:
                marcas.append(f"DUPLICADO de Foto {o['n']}")
                break
        if d["nitidez"] < 0.35 * nit_med:
            marcas.append("BORROSA")
        if min(d["w"], d["h"]) < 720:
            marcas.append(f"BAJA_RES {d['w']}x{d['h']}")
        if d["h"] > d["w"]:
            marcas.append("VERTICAL (recorte 16:9: Sí)")
        if abs(d["luz"] - luz_med) > 0.30 * luz_med:
            marcas.append("LUZ_DISTINTA " + ("oscura" if d["luz"] < luz_med else "clara"))
        print(f"Foto {d['n']}: {d['archivo']}  " + (", ".join(marcas) or "ok"))


def final_push(foto, salida, pct="12"):
    f = 1 - float(pct) / 100
    w, h = tam(foto)
    run(["ffmpeg", "-v", "error", "-y", "-i", foto, "-vf",
         f"crop=iw*{f}:ih*{f}:(iw-iw*{f})/2:(ih-ih*{f})/2,scale={w}:{h}:flags=lanczos",
         "-q:v", "2", salida])
    print(f"{salida}  (final del avance: {pct} % más cerrado, {w}x{h})")


def bpm(musica):
    sr, hop = 8000, 80  # envolvente a 100 cuadros por segundo
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", musica, "-ac", "1", "-ar", str(sr),
                          "-f", "s16le", "-"], check=True, capture_output=True).stdout
    muestras = memoryview(pcm).cast("h")
    energia = [sum(abs(v) for v in muestras[i:i + hop]) for i in range(0, len(muestras) - hop, hop)]
    onset = [max(0, energia[i] - energia[i - 1]) for i in range(1, len(energia))]
    fps = sr / hop

    def ac(lag):
        return sum(onset[i] * onset[i - lag] for i in range(lag, len(onset)))

    lags = range(int(fps * 60 / 160), int(fps * 60 / 80) + 1)  # 80-160 BPM
    puntajes = {l: ac(l) for l in lags}
    mejor = max(puntajes, key=puntajes.get)
    a, b, c = (puntajes.get(mejor - 1, 0), puntajes[mejor], puntajes.get(mejor + 1, 0))
    ajuste = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) else 0
    periodo = mejor + ajuste
    fases = {f: sum(onset[int(round(f + k * periodo))]
                    for k in range(int((len(onset) - f) / periodo)))
             for f in range(int(periodo))}
    fase = max(fases, key=fases.get)
    print(json.dumps({"bpm": round(60 * fps / periodo, 1),
                      "primer_beat_s": round((fase + 1) / fps, 3)}))


def duracion(ruta):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", str(ruta)]).stdout)


def montaje(json_entrada, salida):
    from xml.sax.saxutils import escape
    m = json.load(open(json_entrada, encoding="utf-8"))
    fps = int(m.get("fps", 24))
    beat = 60 / m["musica"]["bpm"]
    tramos, t = [], 0.0
    for c in m["clips"]:
        util = c["out"] - c["in"]
        n_max = max(2, int(util / beat + 1e-6))
        n = n_max - 1 if n_max % 2 and n_max > 2 else n_max  # medio compás en 4/4
        if tramos and n == tramos[-1]["beats"] and n_max > n:
            n = n_max  # rompe el ritmo de metrónomo (director-akarti)
        tramos.append({**c, "beats": n, "ini": t})
        t += n * beat
    if m.get("end_card"):
        n = max(2, round(m["end_card"]["duracion"] / beat))
        tramos.append({"archivo": m["end_card"]["archivo"], "in": 0.0, "beats": n,
                       "ini": t, "espacio": "End card", "imagen": True})
        t += n * beat
    total_f = round(t * fps)

    def fr(seg):
        return round(seg * fps)

    def archivo(i, ruta, es_audio=False, dur=None):
        ruta = pathlib.Path(ruta).resolve()
        dur = dur if dur is not None else (duracion(ruta) if ruta.exists() else 3600)
        medio = ("<audio><samplecharacteristics><depth>16</depth><samplerate>48000</samplerate>"
                 "</samplecharacteristics></audio>" if es_audio else
                 f"<video><samplecharacteristics><rate><timebase>{fps}</timebase></rate>"
                 f"<width>{m.get('ancho', 1920)}</width><height>{m.get('alto', 1080)}</height>"
                 "</samplecharacteristics></video>")
        return (f'<file id="f{i}"><name>{escape(ruta.name)}</name>'
                f"<pathurl>file://localhost{escape(ruta.as_posix())}</pathurl>"
                f"<rate><timebase>{fps}</timebase></rate><duration>{fr(dur)}</duration>"
                f"<media>{medio}</media></file>")

    def clipitem(i, nombre, ini_f, fin_f, in_f, f_xml, nivel_db=None):
        nivel = ""
        if nivel_db is not None:
            nivel = ("<filter><effect><name>Audio Levels</name><effectid>audiolevels</effectid>"
                     "<effecttype>audiolevels</effecttype><mediatype>audio</mediatype>"
                     "<parameter><parameterid>level</parameterid><name>Level</name>"
                     f"<value>{10 ** (nivel_db / 20):.4f}</value></parameter></effect></filter>")
        return (f'<clipitem id="c{i}"><name>{escape(nombre)}</name>'
                f"<rate><timebase>{fps}</timebase></rate><start>{ini_f}</start><end>{fin_f}</end>"
                f"<in>{in_f}</in><out>{in_f + fin_f - ini_f}</out>{f_xml}{nivel}</clipitem>")

    v, cortes = [], []
    for i, c in enumerate(tramos):
        ini_f, fin_f = fr(c["ini"]), fr(c["ini"] + c["beats"] * beat)
        dur = c["beats"] * beat + 1 if c.get("imagen") else None
        v.append(clipitem(i, c.get("espacio", pathlib.Path(c["archivo"]).stem), ini_f, fin_f,
                          fr(c["in"]), archivo(i, c["archivo"], dur=dur)))
        cortes.append((c.get("espacio", c["archivo"]), c["ini"], c["beats"], fin_f - ini_f))
    mus = m["musica"]
    a1 = clipitem(100, "Música", 0, total_f, fr(mus.get("primer_beat_s", 0.0)),
                  archivo(100, mus["archivo"], es_audio=True), mus.get("db", 0))
    a2 = ""
    if m.get("room_tone"):
        rt = m["room_tone"]
        a2 = ("<track>" + clipitem(101, "Room tone", 0, total_f, 0,
                                   archivo(101, rt["archivo"], es_audio=True), rt.get("db", -20))
              + "</track>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4">'
           f"<sequence><name>{escape(m.get('nombre', 'Akarti'))}</name><duration>{total_f}</duration>"
           f"<rate><timebase>{fps}</timebase></rate><media><video><format><samplecharacteristics>"
           f"<rate><timebase>{fps}</timebase></rate><width>{m.get('ancho', 1920)}</width>"
           f"<height>{m.get('alto', 1080)}</height></samplecharacteristics></format>"
           f"<track>{''.join(v)}</track></video><audio><track>{a1}</track>{a2}</audio></media>"
           "</sequence></xmeml>\n")
    open(salida, "w", encoding="utf-8").write(xml)
    print(f"{salida}  ({len(tramos)} tramos, {t:.2f} s, {m['musica']['bpm']} BPM, beat {beat:.3f} s)")
    for nombre, ini, n, frames in cortes:
        print(f"  {ini:6.2f} s  {nombre}: {n} beats ({frames} cuadros)")


def registrar(propiedad, modo, clips, reintentos, creditos, minutos, nota_c):
    ruta = pathlib.Path(__file__).resolve().parent.parent / "registro.csv"
    nuevo = not ruta.exists()
    with open(ruta, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["fecha", "propiedad", "modo", "clips", "reintentos", "creditos",
                        "creditos_por_clip", "minutos", "nota_puerta_C"])
        w.writerow([datetime.date.today().isoformat(), propiedad, modo, clips, reintentos,
                    creditos, round(float(creditos) / max(int(clips), 1), 2), minutos, nota_c])
    print(f"Registrado en {ruta}")


if __name__ == "__main__":
    comandos = {"juez-clip": juez_clip, "hoja-fotos": hoja_fotos,
                "recorte169": recorte169, "audio": audio, "filtro-fotos": filtro_fotos,
                "final-push": final_push, "bpm": bpm, "montaje": montaje,
                "registrar": registrar}
    if len(sys.argv) < 2 or sys.argv[1] not in comandos:
        sys.exit(__doc__)
    comandos[sys.argv[1]](*sys.argv[2:])
