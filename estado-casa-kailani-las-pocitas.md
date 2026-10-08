# Estado — casa-kailani-las-pocitas (teaser, desatendido)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 837.07

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Lista definitiva (puerta A: nota 10/10)
Veredicto: el set SIRVE (teaser, 3 espacios, todos del set cálido de hora azul/anochecer; las áreas sociales interiores solo existen con esa luz). Numeración verificada por contenido con hojas de 6: no coincide con la del CSV (sala = 74, dormitorio vista mar = 71, terraza techada = 72).

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_74 | Sala (doble altura, sofá curvo, comedor y ventanal al mar al fondo) | ORBIT 20° (P1) | Sí (3:2 → 16:9) | — | 6e1b2e4d-797d-43cc-a46f-fe2a506a189e | a777fcfc-9fd6-47a0-bc72-9e798c1c43ed | 5 REPITE (4, 5, 2: aparecen cocina, puertas y baranda nuevas; la cámara retrocede en vez de orbitar). r1 AXIS LOCK: 5 REPITE (1, 2: manchas en muro y piso, sofá derecho se funde) | |
| 2 | foto_71 | Dormitorio vista mar | AXIS LOCK + descripción (P2) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | start 4986d1c8-b8d5-445b-98d7-de84fb6cc132 / final 9c66f352-ed60-4046-9089-6cf8e47848ab | 854e5740-dfa4-46b4-ae7d-2b57a6fe67ee | 5 REPITE (2, 3, 4: a 0,5-2 s aparece un panel de vidrio y un objeto rojo en el piso bajo el banco). r1 DOLLY: 10 PASA | |
| 3 | foto_72 | Terraza techada con salas, piscina y mar | DOLLY (P3) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | start 1ba202e4-79be-482a-8cb1-f317be060841 / final 5cd347e7-cdbe-40b6-8d94-8a04a1495807 | 727cf47d-1af3-4bfb-a14d-d51084bd09e1 | 10 PASA (Opus, puerta B: avance lineal medido cuadro a cuadro, escala 1,000→1,136 en 4 s a 0,0013-0,0015 por cuadro, deriva ≤1 px a 720p, sin saltos; útil 0,1-4,0 s) | |

Plano de apertura: foto_74 (sala), el más fuerte y amplio; profundidad de la doble altura hasta el mar.
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sin sonido; el final no cambia el precio). Presupuesto aprobado 36.

Justificación de movimientos:
- 1 Sala → ORBIT 20°: espacio amplio con mucha profundidad (primer plano de sofá curvo y mesa, fondo de comedor y ventanal) que da paralaje real; 20° y no 30° porque el cielo raso de cañas con vigas y las lámparas de mimbre son patrón repetido (regla confirmada).
- 2 Dormitorio → AXIS LOCK + descripción, con final: cuarto mediano con cielo de cañas y listones, ventilador y cortinas (patrones que ya deformaron en prop-1); avance recto hacia el ventanal al mar, con la frase del cuarto y final de la misma foto para anclar la geometría.
- 3 Terraza techada → DOLLY con final: pérgola de listones (patrón) y aprendizaje de amantica (ORBIT 20° en terraza techada inventó personas y un muro); un avance corto anclado con final es lo más seguro. Fondo abierto al mar, sin puertas donde aparezcan personas.
Movimientos distintos y sin repetir seguidos: ORBIT → AXIS LOCK → DOLLY. Orden lógico: sala → dormitorio → terraza.

P1 (ORBIT 20°):
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

P2 (AXIS LOCK + descripción):
A bedroom with a pale grey concrete-block wall, a cane-slat ceiling crossed by dark wooden beams with a ceiling fan, a double bed with beige linen and a wooden bench at its foot, two framed prints and two hanging wicker lamps above the bed, white linen curtains, a wooden armchair, and a floor-to-ceiling glass door opening onto a balcony with the ocean at dusk. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

P3 (DOLLY):
Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

Comandos listos (fase 2; ninguna elegida es vertical, todas son 3:2 y se recortan al centro a 16:9):
```
mkdir -p teasers/casa-kailani-las-pocitas/169
python3 herramientas/akarti.py recorte169 teasers/casa-kailani-las-pocitas/fotos/foto_74.jpg teasers/casa-kailani-las-pocitas/169/01_sala_74.jpg
python3 herramientas/akarti.py recorte169 teasers/casa-kailani-las-pocitas/fotos/foto_71.jpg teasers/casa-kailani-las-pocitas/169/02_dormitorio_71.jpg
python3 herramientas/akarti.py recorte169 teasers/casa-kailani-las-pocitas/fotos/foto_72.jpg teasers/casa-kailani-las-pocitas/169/03_terraza_72.jpg
python3 herramientas/akarti.py final-push teasers/casa-kailani-las-pocitas/169/02_dormitorio_71.jpg teasers/casa-kailani-las-pocitas/169/02_dormitorio_71_final.jpg 12
python3 herramientas/akarti.py final-push teasers/casa-kailani-las-pocitas/169/03_terraza_72.jpg teasers/casa-kailani-las-pocitas/169/03_terraza_72_final.jpg 12
```

JUEZ — Puerta A — casa-kailani-las-pocitas — Lista definitiva (teaser)
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
(3: 74, 71 y 72 revisadas en hoja; 72 abierta en grande, sin personas ni espejos. 5: prompts copiados de cocinando-lo-demas; ORBIT con arco 20° según el dial. 9: no hay verticales; las tres llevan recorte 3:2 → 16:9.)

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad):
- Formatos:
- Personalidad y duración objetivo:
- Música (ruta o "pausar"):
- Carpeta de exportación:

## Descartes
Modo teaser: solo entran los 3 espacios más fuertes del set cálido. Numeración de la carpeta (no la del CSV), verificada en hojas 1, 2, 3, 11, 12 y 13:
- Fotos 2, 10, 11, 12: logos e íconos de la galería (Airbnb, casa, globo, campana); bodegón, sin espacio que recorrer.
- Foto 13: figura humana ilustrada (persona en cuadro).
- Fotos 14, 18: toma aérea o de dron.
- Fotos 67, 69: letreros Kailani; bodegón sin espacio que recorrer.
- Foto 70 (comedor-sala cálido): persona pequeña junto al ventanal izquierdo y luz más oscura que el set (filtro); la sala queda cubierta por 74.
- Fotos 5, 73 (sala), 8, 65, 68 (escaleras y pasillo): verticales, duplicados de espacios con mejor toma horizontal o pasillos sin recorrido.
- Fotos 1, 3, 6: iluminación inconsistente (luz de día frente al set de hora azul).
- Fotos 61–64 (playa al atardecer) y 66 (ingreso de día): iluminación inconsistente con el set elegido.
- No elegidas por teaser (aptas, pero menos fuertes que 74/71/72): 4, 7, 77 (fachadas de noche), 9 (dormitorio cálido sin vista al mar), 15–17 (cocina cálida), 75, 76, 78 (parrilla, camastros y piscina de noche).
- Fotos 19–60 (hojas 4–10): no se abrieron para el teaser; según el CSV y el filtro son el set de día, aéreas, baños y dormitorios repetidos (iluminación inconsistente con el set cálido).

## Pendientes / reintentos (van todos en un solo batch)
- 2026-10-07: subido y enviado por conector claude_ai_Highsfield (costo 6 c/u, 18 total). Clip 1 reenviado aparte (primer intento rechazado por recomendación de preset, sin cobro). Antes BLOQUEADO: el conector Higgsfield pide autorización (OAuth) y la sesión es no interactiva. Recortes y finales ya listos en teasers/casa-kailani-las-pocitas/169/ (01_sala_74, 02_dormitorio_71 + _final, 03_terraza_72 + _final). Falta: subir, costo, batch, espera, descarga, juez-clip. No se gastó ningún crédito.
- Nota: `recorte169` recibe CARPETAS (entrada y salida), no archivos; los comandos de arriba no sirven tal cual. Se usó una carpeta temporal /tmp/kail_in y se renombró.

## Notas de la corrida
- Fotos: teasers/casa-kailani-las-pocitas/fotos (79; la numeración de la galería no coincide con la del CSV, verificar por contenido).
- identificar vs rescate-6oct/fotos: sin coincidencias, se genera todo.
- Orden sugerido: set cálido/anochecer (sala 69/67, terraza techada 74, dormitorio vista mar 66, principal 5).

## Fase 2 — generación (2026-10-07)
- Clips descargados en teasers/casa-kailani-las-pocitas/clips/ (01_sala_74, 02_dormitorio_71, 03_terraza_72 .mp4). Costo real 18 créditos (presupuesto-corrida.json actualizado).
- Hojas juez: teasers/casa-kailani-las-pocitas/clips/01_sala_74_juez.jpg, 02_dormitorio_71_juez.jpg, 03_terraza_72_juez.jpg. Puerta B rápida hecha: 01=5 REPITE, 02=5 REPITE, 03=9 FRONTERA (pasa a akarti-juez). Cambio para el reintento: 01 pasa a AXIS LOCK + descripción de la sala (ORBIT ya está en 20°, el mínimo) con final-push 12 %; 02 pasa a DOLLY con final-push 12 % y descripción del cuarto. Reintentos juntos en un solo batch tras el juez Opus.

## Reintento r1 (2026-10-07, desatendido)
- Batch de 2 clips std, 12 créditos (total propiedad 30 de 36). Clip 1 sala AXIS LOCK + descripción + final-push 12 % (final media_id 374c0f58-f233-4d87-b8e7-480400e6fbab): job d8b9f660-ddd0-451a-a929-c68d0af65afa. Clip 2 dormitorio DOLLY + final-push: job 7208dab3-c5fb-4102-a7d5-f1e07bdedc3a. (Clip 1 reenviado con declined_preset_id tras recomendación de preset, sin cobro del primer intento.)
- Clips: teasers/casa-kailani-las-pocitas/clips/01_sala_74_r1.mp4, 02_dormitorio_71_r1.mp4; hojas *_r1_juez.jpg. Pendiente puerta B.

## Puerta B de los reintentos r1 (2026-10-07, juez rápido)
- 01_sala_74_r1: 5 REPITE (intento 2 de 2). Falla crítico 1: manchas verdosas y veteado nuevo en el muro de bloque y el piso a 2-3,5 s. Falla crítico 2: el sofá derecho con cojines rojos se funde, aparecen cojines grises y manchas en el piso a 2 s. Aprobados: 3, 4, 5, 6, 7 (diferencia entre cuadros máx 2,0, sin saltos). Cambio para el reintento: la escalera de AXIS LOCK ya se agotó (r1 llevó descripción y final); r2 pasa a DOLLY con final-push 8 % (el DOLLY de la terraza dio avance lineal limpio) y descripción de la sala al inicio. Cuesta 6 créditos: total 36 de 36.
- 02_dormitorio_71_r1: 10 PASA. Muro de bloque, marcos, cama, banco, ventilador y cortinas estables en 0,5, 2 y 3,5 s; sin el panel de vidrio ni el objeto rojo del intento anterior; avance lineal sin saltos (diferencia máx 1,7).

## Reintento r2 (2026-10-07, desatendido)
- 1 clip std, 6 créditos (total propiedad 36 de 36). Sala foto_74 DOLLY + descripción + final-push 8 % (final media_id 0166e369-bb73-4935-9684-4a2fc25ac2f1): job 555d7e6b-1420-4b62-a566-cc354c41273f (reenviado con declined_preset_id). Salida: clips/01_sala_74_r2.mp4. Pendiente puerta B (sin juzgar).
