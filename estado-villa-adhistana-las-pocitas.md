# Estado — villa-adhistana-las-pocitas (teaser, desatendido)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 752.59

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [x] 2 Recorte, subida, generación, puerta B
- [x] 3 Premiere + puerta C (render akarti.py; puerta C 8/10 REPITE, pendiente música)

## Lista definitiva (puerta A: nota 10/10)

Veredicto: el set SIRVE para teaser. 80 archivos, pero solo ~45 son fotos reales de espacios (el resto son íconos de la galería de Airbnb). Numeración verificada por contenido con las 14 hojas de 6: NO coincide con la guía previa de 66 (p. ej. la vieja "46/38/42" ahora son duplicados o fotos de jardín). Todas las fotos útiles son 1440x960 (3:2 horizontal), HDR saturado y gran angular parejo. Se eligen 3 espacios de día, sin personas: piscina infinita al mar, cocina-comedor bajo techo de palma y dormitorio principal con dosel y vista al mar.

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_63 | Piscina infinita al mar (tumbonas en primer plano, daybed blanco, terraza techada de palma a la derecha, palmeras y océano) — APERTURA | DOLLY (P1) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | 7e5cc081-39d1-4bd8-a6e2-d267d501b48e / final 5f3ddce2-5e59-4edf-8e04-659c6e91cae5 | 5a855beb-0b40-4d5b-afa3-3ec1bfd04762 | 10 PASA | |
| 2 | foto_19 | Cocina-comedor bajo techo cónico de palma tejida (mesa de madera con 6 sillas, mueble de cocina largo, refrigerador de vidrio, puerta corrediza al patio) | AXIS LOCK + descripción (P2) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | f7ecc946-16fb-42b9-95b0-a553a70a519a / final 12530161-fb46-4cde-9fbc-b9ac9c6a2361 | a1c2375c-719f-4284-961f-69e424f4e8f9 | 10 PASA | |
| 3 | foto_26 | Dormitorio principal (cama con dosel de tul blanco, techo de palma con vigas redondas y ventilador, abertura a la piscina y el mar, tapiz mandala) | DOLLY (P3) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | c634caa5-816c-4899-a87a-de192b25da4b / final 6f6e537c-0ece-4b71-ab0d-6ac808c74c32 | ec6a37d8-0d7a-421d-9f16-3680480be8eb | 10 PASA | |

Plano de apertura: foto_63 (piscina infinita), el más fuerte del set: borde infinito curvo contra el océano, luz de día pareja, tumbonas que dan profundidad. Es el exterior de la villa, así que abre el recorrido (exterior → cocina-comedor → dormitorio).
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sin sonido; el final no cambia el precio). Presupuesto aprobado 36 (deja 18 para un batch de reintentos).

Justificación de movimientos (inicio seguro con `aprendizajes.md`):
- ORBIT no se usa: en aprendizajes, los 5 ORBIT 20° más recientes en espacios parecidos (terraza techada, salas grandes, comedor) sacaron 5 e inventaron puertas, personas o cuartos; DOLLY y AXIS LOCK con final de 12 % sacaron 10 en 6 de 7 casos. Los movimientos alternan DOLLY → AXIS LOCK → DOLLY, sin dos iguales seguidos.
- P1 DOLLY + final (piscina): avance frontal hacia el borde infinito y el mar; espacio abierto con profundidad natural. Mismo tipo de espacio que la terraza con piscina de casa-kailani (DOLLY + final, 10). Final como red de seguridad por las tumbonas de listones del primer plano y los flecos del techo de palma arriba a la derecha.
- P2 AXIS LOCK + descripción + final (cocina-comedor): techo de palma tejida con vigas radiales (patrón repetido) y 6 sillas (muebles que ya cambiaron de forma en el comedor de alu-luxe con ORBIT) → avance recto sin girar, con la descripción del cuarto al inicio para anclar la geometría.
- P3 DOLLY + final (dormitorio): avance hacia la abertura con vista a la piscina y el mar; el dosel de tul es un mueble alto y el techo tiene vigas repetidas → final de 12 % (DOLLY + final pasó con 10 en dormitorios de alu-luxe y eywa). Distinto del clip anterior.
- Distorsión del techo de paja: revisada en grande en 63, 19 y 26; las vigas se ven rectas y el recorte 16:9 al centro quita la franja superior más curvada. Se evitó foto_04 (flecos de paja en primer plano deformados por el gran angular).

Prompts:
- P1 DOLLY: Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.
- P2 AXIS LOCK + descripción: Open-air kitchen and dining pavilion under a tall conical roof of woven palm leaves with round natural timber rafters, a long wooden kitchen counter with a black stone top and a glass backsplash showing palms and a stone wall, a glass-front refrigerator on the left, a rectangular dark wooden dining table with six wooden chairs in the center, a wooden-framed sliding glass door on the right opening to a garden patio with white floor cushions, pale travertine floor, warm golden late-afternoon sunlight. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.
- P3 DOLLY: Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

Comandos (fase 2, no gastan créditos; ninguna elegida es vertical, pero las tres son 3:2 y pasan por recorte169):
- `mkdir -p teasers/villa-adhistana-las-pocitas/sel && cp teasers/villa-adhistana-las-pocitas/fotos/{foto_63,foto_19,foto_26}.jpg teasers/villa-adhistana-las-pocitas/sel/`
- `python3 herramientas/akarti.py recorte169 teasers/villa-adhistana-las-pocitas/sel teasers/villa-adhistana-las-pocitas/169`
- `mkdir -p teasers/villa-adhistana-las-pocitas/final && for f in foto_63 foto_19 foto_26; do python3 herramientas/akarti.py final-push teasers/villa-adhistana-las-pocitas/169/$f.jpg teasers/villa-adhistana-las-pocitas/final/$f.jpg 12; done`

### Juez — Puerta A — villa-adhistana-las-pocitas — Lista definitiva
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- 3: las 3 fotos revisadas en grande (sin personas, espejos ni reflejos con gente; luz de día en las tres). - 6: DOLLY → AXIS LOCK → DOLLY. - 7: exterior → cocina-comedor → dormitorio. - 9: no hay verticales en la lista; las 3:2 marcadas "Sí". - 10: apertura foto_63.

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad):
- Formatos:
- Personalidad y duración objetivo:
- Música (ruta o "pausar"):
- Carpeta de exportación:

## Descartes
- Fotos 02, 10, 11, 12, 13, 72-80: íconos o logo de la galería de Airbnb, no son espacios (bodegón sin espacio que recorrer).
- Fotos 36, 38, 39, 42, 46, 54, 57: duplicados (de 34, 35, 32, 34, 45, 44 y 49).
- Foto 21 (sala): persona en cuadro, reflejo del fotógrafo con la cámara en el vidrio de la cocina, a la derecha.
- Foto 03: toma aérea / de dron. Foto 08: toma en altura sobre el techo de palma.
- Fotos 14, 16, 17, 20, 52, 58, 60, 67, 68, 69: iluminación inconsistente (noche, atardecer o luces de color frente al set de día).
- Fotos 05, 07, 24, 25, 40: iluminación inconsistente (marcadas LUZ_DISTINTA clara por el filtro).
- Foto 04: distorsión de gran angular (flecos del techo de paja en primer plano deformados).
- Fotos 01, 28, 53: verticales; el recorte a 16:9 deja casi solo techo de paja o piso.
- Fotos 49, 61, 62: bodegones (jardín con estatua, tumbonas y sillas de bar en detalle) sin espacio que recorrer.
- Resto (06, 09, 15, 18, 22, 23, 27, 29-35, 37, 41, 43-45, 47, 48, 50, 51, 55, 56, 59, 63-66, 70, 71): válidas, pero quedan fuera por modo teaser (3 espacios). Reemplazos si un clip falla: foto_59 (piscina con daybed hacia los pabellones), foto_25 (mismo dormitorio, otro ángulo), foto_18 (comedor-cocina de frente).

## Pendientes / reintentos (van todos en un solo batch)
- Puerta C (reintento 1 de 2, sin créditos): re-render con `python3 herramientas/akarti.py render teasers/villa-adhistana-las-pocitas/montaje-villa-adhistana-las-pocitas.json ...` cuando exista la pista playa-luminosa en biblioteca/musica (ver PENDIENTE.md): agregar "musica" al JSON para cortes en beat y loudness a -14 LUFS / -1 dBTP. De paso, subir el contraste del título (titulo.png se pierde sobre la tumbona crema). No regenerar clips.

## Notas de corrida
- Link: https://www.airbnb.com.pe/rooms/15531393 · Hoja 183 · zona Máncora · personalidad: playa-luminosa
- 80 fotos descargadas en teasers/villa-adhistana-las-pocitas/fotos (la auditoría previa habló de 66; numeración foto_NN).
- Fotos sugeridas por auditoría previa: 46,38,42,49,56,57,58,65,1,3,23,24,26,52,4,10,22,6,7,8,11,12,13,16,29. HDR saturado y gran angular uniforme; revisar distorsión en techo de paja.
- La numeración de la guía previa no coincide con los archivos (46, 38, 42, 57 son duplicados; 10-13 son íconos; 49 es jardín). La auditoría usa los números reales de foto_NN.
- identificar vs rescate-6oct/fotos: sin coincidencias → no hay clips reutilizables.
- Presupuesto: tope 700, comprometido 241.2 → alcanza.

- Enviado: 3 clips (18 créditos, costo verificado 6 c/u). Saldo inicial 752.59. Comprometido registrado en presupuesto-corrida.json.

- Puerta B (Sonnet): 10, 10, 10 → PASA los 3; ninguno en frontera.
- Puerta B (Opus, verificación de estabilidad): 10, 10, 10 → CONFIRMADO. Medido cuadro a cuadro (97 cuadros, 192x108): avance lineal a zoom 1,02 (0,5 s) → 1,06 (2 s) → 1,13 (4 s), deriva lateral/vertical 0 px, sin saltos (diferencia entre cuadros 0,75/0,97/0,85, máx 0,92/1,15/0,98). Hojas 2x2: sin objetos nuevos, sin ondulación en vigas de palma, sillas, dosel ni horizonte. Sin reintentos.
- Clips descargados en teasers/villa-adhistana-las-pocitas/clips (clipN_foto_NN.mp4); hojas 2x2 *_juez.jpg al lado. Pendiente: puerta B.

- MEJORAR: upscale 1080p (bytedance aigc) de los 3 clips; jobs 7033edcc, c18beeb6, fa68d91f. Descargados en teasers/villa-adhistana-las-pocitas/clips/clipN_foto_NN_1080.mp4 (originales intactos). Costo 0.3 registrado por la guardia en presupuesto-corrida.json (3 x 0.1).

### Juez — Puerta C — villa-adhistana-las-pocitas — teaser (Opus)
Nota: 8/10 → REPITE (intento 1 de 2)
✓ 1, 2, 3, 5, 6, 8, 9, 10
✗ 4. Cortes en tiempos fuertes de la música — no hay música (biblioteca sin pista playa-luminosa); cortes medidos en 3,0 / 6,5 / 9,5 s sin beat contra qué verificar → fallo.
✗ 7. Loudness — medido -27,5 LUFS / -17,7 dBTP (fuera de -15 a -13 LUFS); solo room tone mar -22 dB.
Evidencia de aprobados: 1-2 vigas, dosel, sillas y borde de piscina rectos en hoja de 24 cuadros (1,5 fps); 3 mismo look HDR cálido en los 3 clips (cocina más dorada, fiel a su foto); 5 avance lineal desde 0,1 s (zoom 1,02→1,13, Opus puerta B), sin frenada antes del corte; 6 astats max difference 0,0088, pico -17,7 dBFS, sin pops ni voces; 8 "Villa Adhistana · Las Pocitas · Máncora" a 0,5 s (bajo contraste) y end card con WhatsApp +51 908 812 483 de 9,5 a 15,5 s; 9 marca de agua diagonal "AKARTI VISUALS DEMO" visible a 0,5 y 6 s; 10 15,5 s, 1920x1080, 24 fps, piscina (plano más fuerte) en 0-3 s.
Cambio para el reintento: agregar la pista playa-luminosa (o la que Enrique apruebe) al montaje y re-render; ajustar contraste del título.


## Cierre de corrida (desatendida)
- Teaser entregado sin música (biblioteca sin playa-luminosa). Puerta C 8/10. Créditos: 18,3 (18 clips + 0,3 upscale) de 36.
- Para llegar a 9–10: generar playa-luminosa.mp3 (ver biblioteca/musica/PENDIENTE.md), agregar "musica" al montaje y repetir `akarti.py render`; subir contraste del título.
