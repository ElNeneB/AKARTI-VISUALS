# Estado — ALU Luxe - Dúo de 8 habitaciones con vista al mar en Larcomar (Lima) — TEASER

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 800.91

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C (puerta C: 7/10 REPITE, ver Notas)

## Lista definitiva (puerta A: nota 10/10)

Veredicto: el set SIRVE para teaser (3 espacios interiores de día con vista al mar, sin personas). Numeración verificada por contenido con hojas de 6: las candidatas previas NO coinciden con el contenido de las 109 fotos (1 = collage, 6 = plano, 14 = sala con vista al mar, 22 = pasillo con ascensor, 28 = terraza/sala con silla colgante, 30 = sillón junto al vidrio, 39 = comedor, 62 = silla junto a ventana, 85 = dormitorio twin, 89/90 = baño, 98 = estudio). Vecinas revisadas: 07-10, 15-16, 31-36, 40-45.

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_14 | Sala (sofás de cuero miel, mesa de centro de vidrio y madera, TV, ventanal y mampara al mar) — APERTURA | DOLLY (P1) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | start 298d598e-a69d-4c29-9ff4-2023cd7b2698 / end 2fa02f60-520a-4e6a-8769-ea5865fcfc64 | 43ccaeef-0ff2-4894-8238-fd4ba3b2edf8 | 10 PASA (Opus: 7 y 8 medidos con ffmpeg, avance lineal ~0,13 %/cuadro de 0,04 a 4,0 s, desplazamiento 0 px, sin saltos) | |
| 2 | foto_41 | Comedor (mesa de vidrio, sillas blancas con respaldo de listones de madera, lámpara de globos, sala y mar al fondo) | ORBIT 20° (P2) | Sí (3:2 → 16:9) | — | 38a01861-b62e-4d7f-a063-f679f3960c92 | 783b532e-35ea-4ae0-90ba-c1e6a67b187a | 5 REPITE (1,2,4: mesa y sillas cambian, puerta corrediza y balcón nuevos a 3,5 s) -> AXIS LOCK + descripción + final. R2 (clip2_foto_41_r2): 6 REPITE (7,8,9,10: a 2 s pared, techo, mesa y respaldo con manchas verde-gris inventadas; 0,5 y 3,5 s limpios; geometría y habitación fieles). Cambio para el reintento: escalera agotada (AXIS LOCK + descripción + final ya usados); ESCALAR a Enrique o probar final-push menor (6 %) / sin final conservando la descripción | |
| 3 | foto_43 | Dormitorio principal con ventanal al mar | AXIS LOCK + descripción (P3) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | start 813696b6-98b5-4802-b621-d97dcbda6f95 / end 4c5288f2-ee5b-4f34-9083-9bb825d69ced | 35f8eeef-443f-482d-983a-ad2435bdbc92 | 10 PASA (Opus: 7 y 8 medidos con ffmpeg, avance lineal ~0,13 %/cuadro de 0,04 a 4,0 s, desplazamiento 0 px, sin saltos) | |

Plano de apertura: foto_14 (sala), el más fuerte: profundidad desde los sofás hasta el ventanal con el Pacífico, luz pareja de día.
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sin sonido; el final no cambia el precio). Presupuesto aprobado 36.

Justificación de movimientos:
- P1 DOLLY + final (sala): avance frontal hacia el ventanal; sala amplia pero con vidrio y mampara al balcón, y en aprendizajes la sala con ventanal de casa-kailani deformó con ORBIT y AXIS LOCK sin ancla, mientras el DOLLY con final pasó con 10. El final fija la geometría.
- P2 ORBIT 20° (comedor): la mesa es un sujeto central claro para orbitar y la paralaje de las sillas contra la sala y el mar da profundidad; los respaldos de listones son patrón repetido → 20° desde el inicio (regla confirmada).
- P3 AXIS LOCK + descripción + final (dormitorio): cabecera de listones horizontales y cortinas enrollables (patrones) → descripción del cuarto al inicio y final de 12 % como red de seguridad (camarote 7/10: 10/10 con final). Movimiento distinto al del clip anterior.

Prompts:
- P1 DOLLY: Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.
- P2 ORBIT 20°: Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.
- P3 AXIS LOCK + descripción: Spacious master bedroom with warm honey wood floor and white walls, a low dark-wood bed with a horizontally grooved wood headboard and matching nightstand with a glowing lamp, white bedding with gray cushions and a gray knit throw, two framed beige prints above the bed, a white upholstered accent chair by the window, and a full-width glass window wall with rolled-up white shades opening to the Pacific Ocean and green treetops, a black wall-mounted TV at the right edge. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

Comandos (fase 2, no gastan créditos):
- `python3 herramientas/akarti.py recorte169 teasers/alu-luxe-duo-de/sel teasers/alu-luxe-duo-de/169`  (sel/ ya tiene foto_14, foto_41 y foto_43)
- `python3 herramientas/akarti.py final-push teasers/alu-luxe-duo-de/169/foto_14.jpg teasers/alu-luxe-duo-de/169/foto_14_final.jpg 12`
- `python3 herramientas/akarti.py final-push teasers/alu-luxe-duo-de/169/foto_43.jpg teasers/alu-luxe-duo-de/169/foto_43_final.jpg 12`

JUEZ — Puerta A — alu-luxe-duo-de — Lista definitiva
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7 (sala → comedor → dormitorio), 8, 9 (todas 3:2 marcadas Sí), 10 (foto_14)

## Datos de edición
- Versión: demo, marca diagonal repetida 10 % (config-corrida.md)
- Formatos:
- Personalidad y duración objetivo: moderno-urbano, ~15 s
- Música (ruta o "pausar"):
- Carpeta de exportación:

## Descartes
- foto_01: collage (bodegón sin espacio que recorrer).
- foto_06: plano de planta (no es un espacio).
- foto_07: toma aérea de dron.
- foto_10: ilustración, no foto de la propiedad.
- foto_05, foto_08, foto_09: terraza curva (atardecer / día): personas en cuadro (gente en el malecón de Larcomar bajo la baranda).
- foto_32, foto_33, foto_34: cocina con vista al malecón y al parque: personas en cuadro.
- foto_31: vista del mar a través del vidrio (bodegón sin espacio que recorrer).
- foto_28: une terraza y sala (dos espacios en una toma, empuja a una transición entre cuartos).
- foto_22: pasillo con ascensor de acero (espejo como sujeto y transición entre espacios).
- foto_40: espejo como sujeto de la foto.
- foto_89, foto_90: baño con el espejo como sujeto.
- foto_30, foto_62, foto_42: bodegones (sillón, silla, mesa puesta) sin espacio que recorrer.
- foto_15, foto_16, foto_26: duplicados de la sala (se queda foto_14).
- foto_39: duplicado del comedor (se queda foto_41).
- foto_44, foto_45: duplicados del dormitorio principal (se queda foto_43).
- foto_35, foto_36, foto_85, foto_98: válidas (cocina, twin, estudio) pero fuera de los 3 espacios más fuertes del teaser; quedan para el recorrido completo.

## Pendientes / reintentos (van todos en un solo batch)
-

## Notas
- 2026-10-07: 109 fotos descargadas en teasers/alu-luxe-duo-de/fotos (la auditoría previa contó 104: verificar que los números coincidan). `identificar` contra rescate-6oct/fotos: sin coincidencias, se genera todo.
- Candidatas de la hoja 142: 1, 6, 14, 26, 28, 22, 89, 90, 30, 39, 62, 85, 98.
- 2026-10-07: enviados 3 clips std (18 cr, costo exacto 6/clip). Clip 2 reenviado tras rechazo por preset sugerido (sin cobro).
- 2026-10-07: RECOGER hecho. Clips en teasers/alu-luxe-duo-de/clips/ (clip1_foto_14, clip2_foto_41, clip3_foto_43 .mp4). Hojas 2x2: clip1_foto_14_juez.jpg, clip2_foto_41_juez.jpg, clip3_foto_43_juez.jpg (misma carpeta). Pendiente: puerta B (akarti-juez-rapido).
- 2026-10-07: REINTENTAR clip 2 (foto_41) AXIS LOCK + descripción + final-push 12 %: end media_id 15e18923-52a6-46fb-a86f-469ad609c04c, job_id bbba3f17-898b-4609-a748-001f6264fd0b (6 cr, total 24/36).
- 2026-10-07: reintento clip2 listo: clips/clip2_foto_41_r2.mp4, hoja clips/clip2_foto_41_r2_juez.jpg. Pendiente: puerta B (akarti-juez-rapido).
- 2026-10-07: MEJORAR hecho (upscale bytedance aigc 1080p, ~0,2 cr). Jobs 757030ef (clip 1) y 0fa01c5c (clip 3). Rutas: teasers/alu-luxe-duo-de/clips/clip1_foto_14_1080p.mp4 y clip3_foto_43_1080p.mp4. Clip 2 (comedor) DESCARTADO tras 2 reintentos (5 y 6), sin upscale.
- 2026-10-07: PUERTA C (akarti-juez, Opus) — teaser-alu-luxe-duo-de.mp4 — Nota 7/10 → REPITE (intento 1 de 2). ✓ 1, 2, 3, 5, 6, 8, 9 (marca DEMO diagonal confirmada por diferencia de cuadro a 5,5 s). ✗ 4: sin música, cortes sobre tiempos fuertes no verificables. ✗ 7: medido -27,8 LUFS / -16,5 dBTP (regla de juez-akarti: -15 a -13 LUFS; config-corrida.md no fija objetivo -28 sin música). ✗ 10: dura 9,5 s y config pide 12 a 15 s (1920x1080 24 fps y sala en 0 s sí cumplen). Cambio para el reintento (sin créditos): normalizar a -14 LUFS / ≤ -1 dBTP; poner la pista moderno-urbano cuando exista (biblioteca/musica/PENDIENTE.md) y cortar en sus tiempos fuertes; llevar a ≥12 s (end card 3 → 4,5 s y/o holds más largos). Si se decide aceptar sin música, que lo apruebe Enrique: la skill no tiene excepción.

## Cierre (2026-10-07, desatendido)
- Teaser: teasers/alu-luxe-duo-de/teaser-alu-luxe-duo-de.mp4 (11 s, 2 clips + end card 4,5 s, sin música). Puerta C: 7 (REPITE) antes de alargar el end card; no se re-juzgó.
- Comedor (foto_41) DESCARTADO: ORBIT 20° nota 5, AXIS LOCK+final nota 6.
- Pendientes: pista moderno-urbano (biblioteca/musica/PENDIENTE.md) para re-renderizar con música a -14 LUFS; decidir si se acepta con 2 clips; 11 s < 12-15 s objetivo.
- Créditos: 24 + 0,2 de upscale (presupuesto 36).
