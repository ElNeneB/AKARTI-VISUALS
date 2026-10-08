# Estado — Eywa Lodge todo incluido IV (Saquena) — TEASER

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 776.75

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [x] 2 Recorte, subida, generación, puerta B
- [x] 3 Premiere + puerta C

## Lista definitiva (puerta A: nota 10/10)

Veredicto: el set SIRVE para teaser (3 espacios de día, sin personas ni comida: pasarela techada, sala de estar y dormitorio con ventanas a la selva). Numeración verificada por contenido con las hojas de 6 (21 fotos, todas 1440x960, 3:2 horizontal). La numeración previa de 16 fotos NO coincide; equivalencias reales: bungalow exterior = foto_03 (antes 2), pasarela techada = foto_16 (antes 11), sala = foto_05 (antes 4), dormitorio = foto_01 (antes 1) y foto_07 (antes 6, mismo cuarto sin cama).

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_16 | Pasarela techada (techo de palma sobre postes de madera, bungalows a la izquierda, selva al fondo) — APERTURA | AXIS LOCK + descripción (P1) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | c66ca16e-f3e0-4be0-9105-4e70229c1dcc (final fcf6a874-be4b-4992-9434-2cfc6c97cb41) | fa196ab9-2d3b-4fe0-bccf-533a4366008e | 10 PASA | |
| 2 | foto_05 | Sala de estar (sillones de mimbre con cojines de hojas, mesa de centro de vidrio, ventanas con malla a la selva) | ORBIT 20° (P2) | Sí (3:2 → 16:9) | — | 8ca66114-5c36-4e0a-bd2c-3015b4bfb93c | 7f79ba6c-5153-4c68-b59d-3f9eadaf5813 | 5 REPITE (Opus, intento 1 de 2); r2: 5 REPITE (Sonnet, intento 2 de 2, escalar) | |
| 3 | foto_01 | Dormitorio (cama doble blanca, paredes de tablas, ventanas con cortinas a la selva) | DOLLY (P3) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | a8975593-9b55-4f4a-a83a-dabafdb7da5a (final af507951-11a1-4c19-8d06-1fcef10263d8) | 4d519226-f70b-4190-8ff9-e319d1c06b0f | 10 PASA | |

Plano de apertura: foto_16 (pasarela), el más fuerte: punto de fuga central muy marcado bajo el techo de palma, luz pareja de día y presenta el lodge en la selva.
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sin sonido; el final no cambia el precio). Presupuesto aprobado 36.

Justificación de movimientos:
- P1 AXIS LOCK + descripción + final (pasarela): espacio lineal con punto de fuga central, ideal para avanzar recto por el eje sin girar. Hileras de postes y vigas y la palma del techo son patrón repetido → descripción al inicio y final de 12 % como red de seguridad (AXIS LOCK + descripción + final pasó con 10 en camarote y en alu-luxe).
- P2 ORBIT 20° (sala): la mesa de centro con los sillones en U es un sujeto central claro para orbitar, y los sillones de primer plano contra las ventanas dan paralaje. Mimbre, cojines estampados y malla son patrones → 20° desde el inicio (regla confirmada). Riesgo anotado: en aprendizajes, 3 ORBIT 20° en espacios grandes con aberturas al fondo inventaron puertas o cuartos; aquí no hay puertas en cuadro y el zócalo de tablas cierra el cuarto. Si deforma, la escalera es AXIS LOCK + descripción + final.
- P3 DOLLY + final (dormitorio): avance frontal hacia las ventanas con cortinas; paredes de tablas verticales (listones) → final de 12 % (DOLLY con final pasó con 10 en 3 de 3 casos). Movimiento distinto al clip anterior.

Prompts:
- P1 AXIS LOCK + descripción: Long covered wooden boardwalk under a thatched palm-leaf roof held by rows of round wooden posts and crossbeams, a straight plank walkway with simple wooden handrails on both sides, sandy ground with small green plants, thatched-roof wooden bungalows on stilts on the left, tall jungle trees at the far end in soft warm daylight. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.
- P2 ORBIT 20°: Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.
- P3 DOLLY: Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

Comandos (fase 2, no gastan créditos):
- `mkdir -p teasers/eywa-lodge-todo-incluido/sel && cp teasers/eywa-lodge-todo-incluido/fotos/{foto_16,foto_05,foto_01}.jpg teasers/eywa-lodge-todo-incluido/sel/`
- `python3 herramientas/akarti.py recorte169 teasers/eywa-lodge-todo-incluido/sel teasers/eywa-lodge-todo-incluido/169`
- `python3 herramientas/akarti.py final-push teasers/eywa-lodge-todo-incluido/169/foto_16.jpg teasers/eywa-lodge-todo-incluido/169/foto_16_final.jpg 12`
- `python3 herramientas/akarti.py final-push teasers/eywa-lodge-todo-incluido/169/foto_01.jpg teasers/eywa-lodge-todo-incluido/169/foto_01_final.jpg 12`

JUEZ — Puerta A — eywa-lodge-todo-incluido — Lista definitiva
Nota: 10/10 → PASA
✓ 1, 2, 3 (foto_16 marcada LUZ_DISTINTA por el filtro, verificada en hoja_03: luz de día pareja con foto_05 y foto_01, sombra del techo de palma), 4, 5, 6 (AXIS LOCK → ORBIT → DOLLY), 7 (exterior/pasarela → sala → dormitorio), 8, 9 (las 3 son 3:2, marcadas Sí), 10 (foto_16)

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad): demo, marca diagonal repetida 10 % (config-corrida.md)
- Formatos: 16:9
- Personalidad y duración objetivo: lodge-andino, ~12-15 s con end card
- Música (ruta o "pausar"): biblioteca/musica (lodge-andino.mp3 según indice.csv)
- Carpeta de exportación: teasers/eywa-lodge-todo-incluido/

## Descartes
- foto_02: logo de Airbnb, no es foto de la propiedad (bodegón sin espacio; además BORROSA).
- foto_03: bungalow exterior: iluminación inconsistente (más oscura que el set, filtro LUZ_DISTINTA); queda fuera de los 3 más fuertes.
- foto_04: letrero "ROOM 4" bajo el techo: detalle sin espacio que recorrer.
- foto_06: toma aérea de dron.
- foto_07: mismo dormitorio que foto_01 sin cama (duplicado) e iluminación inconsistente (oscura, contraluz).
- foto_08, foto_19: comida (bodegón).
- foto_09: persona en cuadro (cocinera) y comida.
- foto_10, foto_11, foto_12: íconos gráficos (casa, globo, campana), no son fotos (12 además duplicado según filtro).
- foto_13: personaje 3D ilustrado (persona, no es foto de la propiedad).
- foto_14, foto_17: persona en cuadro (bote en el río).
- foto_15: personas en cuadro (pueblo).
- foto_18: techo de la pasarela con letrero "BUNGALOWS": detalle, mismo espacio que foto_16 (duplicado).
- foto_20, foto_21: detalles (abanico y toalla en la cama; papel higiénico, además BORROSA).

## Pendientes / reintentos (van todos en un solo batch)
- Clip 2 (foto_05, sala) — reintento 1 de 2. Puerta B Opus: 5/10 REPITE. ✓ 1, 3, 4, 6, 7, 8, 9, 10. ✗ 2 (crítico): la mecedora de primer plano (a la derecha, delante de la mesa a 0,5 s) cruza el cuadro y a 3,5 s queda a la izquierda, a la profundidad de la mesa y con otra forma (balancines curvos a la vista, respaldo más bajo); la silla del borde izquierdo de la foto desaparece. ✗ 5: el giro es de unos 45-60° (a 0,5 s el sofá se ve de frente en diagonal; a 3,5 s la pared del fondo queda de frente y el sofá de perfil), no 20°. Movimiento medido (diferencia media por fotograma, 320 px): 4 → 12-16 desde 0,6 s → 8 al final; tramo constante ~3 s.
  Cambio: AXIS LOCK + descripción + final-push 12 % (ORBIT ya estaba en 20°, la escalera sigue con AXIS LOCK; describir la sala ancla la mecedora y las sillas). Costo 6 cr std (presupuesto 36, gastado 18).
  Final: `python3 herramientas/akarti.py final-push teasers/eywa-lodge-todo-incluido/169/foto_05.jpg teasers/eywa-lodge-todo-incluido/169/foto_05_final.jpg 12`
  Prompt: Open-air jungle lounge under a thatched palm-leaf roof on round wooden posts, waist-high wooden plank wall with wide screened openings onto dense green jungle, three rattan armchairs with white seat cushions and green palm-leaf pillows lined along the back wall, rattan loveseat with white cushions and two leaf-print pillows on the right, small rattan coffee table with a glass top and a wicker lantern in the center, tall wooden rocking chair standing still in the right foreground, wide-plank wooden floor, soft even daylight. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: camera bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along the rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead the entire shot, zero yaw, optical axis stays perfectly parallel to the rail, camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, every chair and the rocking chair keep their original shape and position. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.
- Clip 2 r2 (clip2_foto_05_r2.mp4) — Puerta B juez rápido: 5/10 REPITE (intento 2 de 2, escalera agotada: ESCALAR/DESCARTAR, no hay más reintentos). ✓ avance recto (encuadre y puntos de fuga estables entre foto, 0,5 s y 3,5 s), mecedora y sillas conservan forma y posición en 0,5 s y 3,5 s, sin personas. ✗ 2 (crítico): a 2 s la mecedora de primer plano se ve translúcida y deformada, y el piso tiene manchas de vidrio/agua. ✗ 3 (crítico): a 2 s aparece una mesa de vidrio duplicada (fantasma) delante de la mesa de centro. Extremos (0,5 s y 3,5 s) limpios; el daño está en el medio del clip.
## Notas
- 2026-10-07: 21 fotos descargadas en teasers/eywa-lodge-todo-incluido/fotos (la auditoría previa contó 16: VERIFICAR POR CONTENIDO que las candidatas 2, 11, 4, 1, 6 coincidan). `identificar` contra rescate-6oct/fotos: sin coincidencias, se genera todo.
- Candidatas de propiedades-teaser.csv: 2 (bungalow exterior), 11 (pasarela techada), 4 (sala), 1 y 6 (mismo dormitorio). Descartes previos: 8,9,10,12 personas; 5 aérea; 7,14 comida; 3,13,15,16 detalles.
- 2026-10-07 (auditor): verificado por contenido; la numeración de 21 fotos no coincide con la previa. Mapeo real en la Lista definitiva. Ninguna foto vertical (todas 3:2 horizontales). Riesgo principal: ORBIT 20° en la sala (ver justificación).
- Personalidad: lodge-andino (biblioteca/musica/indice.csv: lodge-andino.mp3). Versión demo, marca diagonal 10 %.
- 2026-10-07 (generador): enviados 3 clips std, 6 cr c/u (18 total, registrado en presupuesto-corrida.json). Clip 2 se reenvió con declined_preset_id (preset IN THE DARK rechazado; sin cobro previo).
- 2026-10-07 (generador): clips descargados y hojas 2x2 listas en teasers/eywa-lodge-todo-incluido/clips/: clip1_foto_16_juez.jpg, clip2_foto_05_juez.jpg, clip3_foto_01_juez.jpg. Pendiente puerta B (akarti-juez-rapido).
- 2026-10-07 (juez-rapido): clip1 10 PASA, clip3 10 PASA, clip2 FRONTERA (pasa a akarti-juez Opus): crit. 2 sin verificar (silla del borde izquierdo de la foto desaparece y la mecedora de primer plano cambia de forma entre 0,5 s y 3,5 s; el arco parece mayor de 20°).
- 2026-10-07 (generador): reintento clip 2 enviado, job_id 536bc558-0c88-4533-8ab7-e0b879038356, final media_id 861a98b8-466f-46fc-9d83-3c2d5274b8f1 (start 8ca66114...), 6 cr std, registrado en presupuesto-corrida.json (gastado 24 de 36). Preset IN THE DARK rechazado.
- 2026-10-07 (generador): reintento clip 2 descargado: teasers/eywa-lodge-todo-incluido/clips/clip2_foto_05_r2.mp4; hoja 2x2: clip2_foto_05_r2_juez.jpg. Pendiente puerta B (akarti-juez).
- 2026-10-07 (generador): MEJORAR hecho (upscale bytedance aigc 1080p, ~0,2 cr). Jobs 19c3ae68 (clip 1) y d4ee0563 (clip 3). Rutas: teasers/eywa-lodge-todo-incluido/clips/clip1_foto_16_1080p.mp4 y clip3_foto_01_1080p.mp4. Clip 2 (sala) DESCARTADO tras 2 reintentos (5 y 5), sin upscale.

## Cierre (2026-10-07, desatendido, modo render)
- Teaser: teasers/eywa-lodge-todo-incluido/teaser-eywa-lodge-todo-incluido.mp4 (2 clips 1080p + end card 6 s, con lodge-andino.mp3 89,6 bpm y room tone interior -22 dB, marca diagonal 10 %). Montaje: montaje-eywa-lodge-todo-incluido.json.
- Sala (foto_05) DESCARTADA: ORBIT 20° nota 5 en 2 intentos.
- Clips de 4 s limitan la duración: se llegó a 12 s alargando el end card. Sin estabilización vidstab (ffmpeg sin vidstab). Puerta C hecha (akarti-juez), ver abajo.
- 2026-10-07: PUERTA C (akarti-juez, Opus) — teaser-eywa-lodge-todo-incluido.mp4 — Nota 10/10 → PASA. ✓ 1-10. Medido: -13,4 LUFS / -3,9 dBTP (akarti.py audio); 1920x1080, 24 fps, 12,1 s; cortes a 2,71 s y 6,08 s sobre beats 4 y 9 (89,6 bpm, compás); movimiento parejo sin arranques ni frenadas (diferencia por cuadro ~1-2, sin picos salvo los cortes); marca DEMO / AKARTI VISUALS diagonal visible en 1,5 s y 4,5 s; título "Eywa Lodge / Saquena" al inicio y end card con WhatsApp; pasarela (plano más fuerte) en 0 s. Registro: 24,2 cr (18 + 6 reintento + 0,2 upscale), 2 clips, 1 reintento.
