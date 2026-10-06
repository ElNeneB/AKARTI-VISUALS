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
  python3 akarti.py render MONTAJE.json SALIDA.mp4
      Render final sin Premiere: cortes en beat, estabilización (si ffmpeg tiene
      vidstab), look sobrio, título, marca de agua, end card, música + room tone
      y loudness a -14 LUFS / -1 dBTP. Lo usa el modo teaser.
  python3 akarti.py room-tone (interior|ciudad|mar) SALIDA.wav [SEGUNDOS=90]
      Room tone sintético y continuo para la capa de ambiente.
  python3 akarti.py airbnb-fotos LINK CARPETA
      Descarga las fotos del anuncio en el orden de la galería (Foto 01, 02...).
  python3 akarti.py identificar CARPETA_A CARPETA_B
      Encuentra fotos de A que ya están en B (por ejemplo, para reutilizar clips).
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


def calcular_tramos(m):
    """Tramos del montaje: cada clip recortado a beats enteros (medio compás si se
    puede, sin dos duraciones iguales seguidas cuando hay material) + end card."""
    beat = 60 / m["musica"]["bpm"] if m.get("musica") else 0.5
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

    return beat, tramos, t


def montaje(json_entrada, salida):
    from xml.sax.saxutils import escape
    m = json.load(open(json_entrada, encoding="utf-8"))
    fps = int(m.get("fps", 24))
    beat, tramos, t = calcular_tramos(m)
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
    print(f"{salida}  ({len(tramos)} tramos, {t:.2f} s, beat {beat:.3f} s)")
    for nombre, ini, n, frames in cortes:
        print(f"  {ini:6.2f} s  {nombre}: {n} beats ({frames} cuadros)")


def tiene_filtro(nombre):
    r = run(["ffmpeg", "-hide_banner", "-filters"]).stdout
    return re.search(rf"\s{nombre}\s", r) is not None


def lufs(ruta, inicio=0.0):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{inicio:.3f}", "-i", str(ruta),
                        "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    v = re.search(r"I:\s+(-?[\d.]+) LUFS", r.stderr[r.stderr.rfind("Summary:"):])
    return float(v.group(1)) if v else -70.0


def render(json_entrada, salida):
    """Render del montaje con ffmpeg (versión demo / teaser sin Premiere)."""
    m = json.load(open(json_entrada, encoding="utf-8"))
    fps, W, H = int(m.get("fps", 24)), int(m.get("ancho", 1920)), int(m.get("alto", 1080))
    beat, tramos, total = calcular_tramos(m)
    base = pathlib.Path(json_entrada).resolve().parent
    tmp = base / (pathlib.Path(salida).stem + "_tmp")
    tmp.mkdir(exist_ok=True)
    vidstab = m.get("estabilizar", True) and tiene_filtro("vidstabdetect")
    look = m.get("look", "eq=contrast=1.04:brightness=-0.005:saturation=0.95")
    partes = []
    for i, c in enumerate(tramos):
        dur = c["beats"] * beat
        parte = tmp / f"{i:02d}.mp4"
        escala = (f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
                  f"crop={W}:{H},setsar=1,fps={fps}")
        if c.get("imagen"):
            run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{dur:.4f}", "-i", c["archivo"],
                 "-vf", escala + ",format=yuv420p", "-c:v", "libx264", "-crf", "16",
                 "-preset", "medium", "-an", str(parte)])
        else:
            filtros = escala
            if vidstab:
                trf = tmp / f"{i:02d}.trf"
                run(["ffmpeg", "-v", "error", "-y", "-ss", f"{c['in']:.4f}", "-t", f"{dur:.4f}",
                     "-i", c["archivo"], "-vf", f"vidstabdetect=shakiness=4:accuracy=15:result={trf}",
                     "-f", "null", "-"])
                filtros = (f"vidstabtransform=input={trf}:smoothing=20:zoom=0:optzoom=1:"
                           f"interpol=bicubic,{escala}")
            filtros += "," + look + ",format=yuv420p"
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{c['in']:.4f}", "-t", f"{dur:.4f}",
                 "-i", c["archivo"], "-vf", filtros, "-c:v", "libx264", "-crf", "16",
                 "-preset", "medium", "-an", str(parte)])
        partes.append(parte)
    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{p}'\n" for p in partes))
    video = tmp / "video.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
         "-c", "copy", str(video)])
    # capas: título (entrada y salida de 8 cuadros) y marca de agua (fuera del end card)
    fin_clips = tramos[-1]["ini"] if tramos[-1].get("imagen") else total
    entradas, grafo, ult = ["-i", str(video)], [], "[0:v]"
    n = 1
    if m.get("titulo"):
        entradas += ["-loop", "1", "-t", f"{total:.3f}", "-i", m["titulo"]]
        f8 = 8 / fps
        grafo.append(f"[{n}:v]format=rgba,fade=in:st=0.4:d={f8:.3f}:alpha=1,"
                     f"fade=out:st=3.0:d={f8:.3f}:alpha=1[ti]")
        grafo.append(f"{ult}[ti]overlay=0:0:enable='lt(t,{3.0 + f8:.3f})'[v{n}]")
        ult, n = f"[v{n}]", n + 1
    if m.get("marca_agua"):
        entradas += ["-loop", "1", "-t", f"{total:.3f}", "-i", m["marca_agua"]]
        grafo.append(f"{ult}[{n}:v]overlay=0:0:enable='lt(t,{fin_clips:.3f})'[v{n}]")
        ult, n = f"[v{n}]", n + 1
    # audio: música desde su primer beat + room tone continuo
    audios = []
    mus = m.get("musica") or {}
    if mus.get("archivo"):
        entradas += ["-ss", f"{mus.get('primer_beat_s', 0):.3f}", "-i", mus["archivo"]]
        audios.append(f"[{n}:a]atrim=0:{total:.3f},asetpts=N/SR/TB,afade=t=in:d=0.05,"
                      f"afade=t=out:st={max(total - 1.5, 0):.3f}:d=1.5,"
                      f"volume={-14 - lufs(mus['archivo'], mus.get('primer_beat_s', 0)):.2f}dB[mu]")
        n += 1
    rt = m.get("room_tone") or {}
    objetivo = -14 if mus.get("archivo") else -28
    if rt.get("archivo"):
        nivel_rt = (-14 + rt.get("db", -22)) if mus.get("archivo") else objetivo
        entradas += ["-stream_loop", "-1", "-i", rt["archivo"]]
        audios.append(f"[{n}:a]atrim=0:{total:.3f},asetpts=N/SR/TB,afade=t=in:d=0.3,"
                      f"afade=t=out:st={max(total - 1.0, 0):.3f}:d=1.0,"
                      f"volume={nivel_rt - lufs(rt['archivo']):.2f}dB[rt]")
        n += 1
    etiquetas = "".join(x for x in ("[mu]", "[rt]") if any(a.endswith(x) for a in audios))
    if audios:
        mezcla = (f"{etiquetas}amix=inputs={len(audios)}:normalize=0[mx]" if len(audios) > 1
                  else f"{etiquetas}anull[mx]")
        grafo += audios + [mezcla]
    mapa = ["-map", ult if grafo and ult != "[0:v]" else "0:v"]
    previo = tmp / "previo.mp4"
    cmd = ["ffmpeg", "-v", "error", "-y", *entradas]
    if grafo:
        cmd += ["-filter_complex", ";".join(grafo)]
    cmd += mapa + (["-map", "[mx]"] if audios else []) + [
        "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p",
        "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{total:.3f}", str(previo.with_suffix(".mov"))]
    run(cmd)
    previo = previo.with_suffix(".mov")
    if audios:  # loudness en dos pasadas (medido, no estimado)
        r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(previo), "-af",
                            f"loudnorm=I={objetivo}:TP=-1.5:LRA=11:print_format=json",
                            "-f", "null", "-"], capture_output=True, text=True)
        med = json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}") + 1])
        an = (f"loudnorm=I={objetivo}:TP=-1.5:LRA=11:measured_I={med['input_i']}:"
              f"measured_TP={med['input_tp']}:measured_LRA={med['input_lra']}:"
              f"measured_thresh={med['input_thresh']}:offset={med['target_offset']}:linear=true")
        run(["ffmpeg", "-v", "error", "-y", "-i", str(previo), "-c:v", "copy", "-af", an,
             "-ar", "48000", "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", salida])
    else:
        run(["ffmpeg", "-v", "error", "-y", "-i", str(previo), "-c:v", "copy", "-an",
             "-movflags", "+faststart", salida])
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{salida}  ({total:.2f} s, {len(tramos)} tramos, estabilizado: "
          f"{'sí' if vidstab else 'no (ffmpeg sin vidstab)'}, música: {'sí' if mus.get('archivo') else 'NO'})")
    if audios:
        audio(salida)


def room_tone(tipo, salida, segundos="90"):
    d = float(segundos)
    filtros = {
        "interior": f"anoisesrc=d={d}:c=brown:a=0.5,lowpass=f=380,highpass=f=40,volume=-6dB",
        "ciudad": f"anoisesrc=d={d}:c=brown:a=0.5,lowpass=f=260,highpass=f=35,"
                  f"tremolo=f=0.07:d=0.25,volume=-4dB",
        "mar": f"anoisesrc=d={d}:c=pink:a=0.5,bandpass=f=420:w=600,"
               f"tremolo=f=0.11:d=0.7,lowpass=f=1800,volume=-3dB",
    }
    if tipo not in filtros:
        sys.exit("Tipo: interior, ciudad o mar.")
    run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", filtros[tipo], "-ac", "2",
         "-ar", "48000", salida])
    print(salida)


def airbnb_fotos(link, carpeta):
    import urllib.request
    out = pathlib.Path(carpeta)
    out.mkdir(parents=True, exist_ok=True)
    ua = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
    req = urllib.request.Request(link, headers={"User-Agent": ua, "Accept-Language": "es-PE,es"})
    html = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
    html = html.replace("\\u002F", "/").replace("\\/", "/")
    urls, vistos = [], set()
    for u in re.findall(r"https://a0\.muscache\.com/im/pictures/[^\"'?\s\\]+?\.(?:jpe?g|png|webp)", html):
        clave = u.rsplit("/", 1)[-1]
        if clave not in vistos and "/user/" not in u and "/Portrait" not in u:
            vistos.add(clave)
            urls.append(u)
    if not urls:
        sys.exit("No se encontraron fotos (Airbnb pudo bloquear la descarga): usar Claude in Chrome.")
    for i, u in enumerate(urls, 1):
        destino = out / f"foto_{i:02d}.jpg"
        r = urllib.request.Request(u + "?im_w=1440", headers={"User-Agent": ua})
        destino.write_bytes(urllib.request.urlopen(r, timeout=60).read())
    print(f"{len(urls)} fotos en {out} (foto_01 = primera de la galería)")


def huella(ruta):
    w, h = tam(ruta)
    if w / h > 16 / 9:
        cw, ch = int(h * 16 / 9), h
    else:
        cw, ch = w, int(w * 9 / 16)
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ruta), "-vf",
                        f"crop={cw}:{ch},scale=9:8,format=gray", "-f", "rawvideo", "-"],
                       check=True, capture_output=True).stdout
    return sum(1 << i for i in range(64) if r[(i // 8) * 9 + i % 8] > r[(i // 8) * 9 + i % 8 + 1])


def identificar(carpeta_a, carpeta_b):
    def fotos(c):
        return sorted(p for p in pathlib.Path(c).iterdir() if p.suffix.lower() in FOTOS)
    hb = {p: huella(p) for p in fotos(carpeta_b)}
    for pa in fotos(carpeta_a):
        ha = huella(pa)
        mejor = min(hb, key=lambda p: bin(hb[p] ^ ha).count("1"), default=None)
        dist = bin(hb[mejor] ^ ha).count("1") if mejor else 64
        print(f"{pa.name} -> {mejor.name if mejor and dist <= 10 else 'sin coincidencia'}"
              f" (distancia {dist})")


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
                "registrar": registrar, "render": render, "room-tone": room_tone,
                "airbnb-fotos": airbnb_fotos, "identificar": identificar}
    if len(sys.argv) < 2 or sys.argv[1] not in comandos:
        sys.exit(__doc__)
    comandos[sys.argv[1]](*sys.argv[2:])
