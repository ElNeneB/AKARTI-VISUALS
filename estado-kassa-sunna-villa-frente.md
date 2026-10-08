# Estado — Kassa Sunna, Villa frente a Las Pocitas, Máncora (teaser, desatendido)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 855.07

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Lista definitiva (puerta A: nota 10/10) — modo teaser, 3 clips

**Veredicto:** el set SIRVE (frente al mar, luz de día pareja en los espacios elegidos, buena variedad). Teaser con los 3 espacios más fuertes, todos de día y con el mar a la vista.

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_49 | Jardín frente al mar (exterior, APERTURA) | DOLLY | Sí | — | | | | |
| 2 | foto_17 | Dormitorio con vista al mar | ORBIT 20° | Sí | — | | | | |
| 3 | foto_44 | Terraza deck bajo pérgola, frente al mar | AXIS LOCK + descripción | Sí | Sí | | | | |

Justificación de cada movimiento:
1. foto_49 — DOLLY sin final: exterior amplio con palmeras en primer plano y el mar al fondo; el avance lento da profundidad sin hacer girar hojas de palmera (un ORBIT las deformaría). Espacio amplio y sin riesgo → sin final para conservar el paralaje.
2. foto_17 — ORBIT 20°: cuarto amplio pero con techo de caña, vigas radiales y muro de piedra laja (patrones repetidos) → arco de 20° desde el inicio (regla confirmada en `aprendizajes.md`); el paralaje entre la cama y las puertas abiertas al mar vende la vista.
3. foto_44 — AXIS LOCK + descripción, con final: avance recto hacia el mar por el deck; la pérgola de listones es patrón repetido y la terraza de amantica (pérgola de listones) inventó personas y un muro, así que se ancla con descripción + fotograma final 12 % (red de seguridad). Sin cambio de lado ni de altura.

Plano de apertura: foto_49 (jardín con hamaca, palmeras y el Pacífico; el plano más fuerte del set de día).
Orden: exterior → dormitorio → terraza (criterio 7). Movimientos sin repetir: DOLLY → ORBIT → AXIS LOCK.
Sonido: OFF — Créditos aprobados: __ (costo esperado 3 × 6 = 18 créditos en std).

### Archivos listos
- Recortes 16:9 (1920x1080): `teasers/kassa-sunna-villa-frente/recortes/foto_49.jpg`, `foto_17.jpg`, `foto_44.jpg` (ya corrido: `python3 herramientas/akarti.py recorte169 <carpeta con 49,17,44> teasers/kassa-sunna-villa-frente/recortes`). No hay verticales en la selección; las tres son 3:2 (1440x960) y se recortaron al centro.
- Fotograma final clip 3: `teasers/kassa-sunna-villa-frente/finales/foto_44_final.jpg` (`final-push` 12 %).

### Prompts (pegar tal cual; 16:9, 4 s, sonido OFF)
**Clip 1 — foto_49 — DOLLY**
Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

**Clip 2 — foto_17 — ORBIT 20°**
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

**Clip 3 — foto_44 — AXIS LOCK + descripción (imagen final: foto_44_final.jpg)**
Open-air wooden deck under a slatted cane pergola resting on dark wooden beams, four black wicker armchairs with white cushions around a dark wooden coffee table, a palm trunk rising through the deck, green lawn with a hammock beyond, rocky beach and the Pacific Ocean on the horizon, white house wall with a warm wall lamp on the right edge, the whole garden calm and empty. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

### Juez — Puerta A — kassa-sunna-villa-frente — Lista definitiva
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Datos de edición
- Versión: demo, marca de agua diagonal repetida 10 % (assets/marca/marca-agua-16x9.png)
- Formatos: 16:9
- Personalidad: playa-luminosa; teaser 12-15 s con end card
- Música: biblioteca/musica/indice.csv por personalidad; room tone mar
- Carpeta de exportación: teasers/kassa-sunna-villa-frente/

## Notas
- Hoja 141, zona Máncora, personalidad playa-luminosa. Sin cocina ni comedor. Fotos sugeridas: 2,3,4,5,6,7,8,10,11.

## Descartes
- Guía previa corregida: los números de la guía no coinciden con los archivos (foto_02 es el logo de Airbnb). Se revisaron las 58 en hojas de 6.
- foto_02, 10, 11, 12, 13, 52–58: íconos/ilustraciones (logo Airbnb, casita, globo, campana, avatar, regalo, peluche, etc.) — no son espacios (bodegón sin espacio).
- foto_07, 40, 51: tomas aéreas / de dron (51 además con personas en cuadro).
- foto_01, 04, 06, 15, 39, 41, 42, 43, 47, 48: iluminación inconsistente (atardecer / hora azul frente al resto de día). Piscina (04, 41) queda fuera por esto: no hay foto de piscina de día.
- foto_47: duplicado de foto_06. foto_19: duplicado de ángulo de foto_44 (se queda 44, con más profundidad hacia el mar).
- foto_23, 24, 32, 34–39, 42 (verticales): camarotes, baños y piscina de noche; no entran al teaser.
- foto_32–38: baños (espejos como sujeto, cuartos chicos) — fuera del teaser.
- foto_45, 50: bar/comedor exterior — fuera por guía (sin cocina ni comedor).
- foto_05 (sala de juegos), 08 (gimnasio), 09 (spa), 14 (terraza sala), 16, 18, 20, 25–31 (dormitorios), 21–24 (camarotes), 46 (azotea): válidas pero menos fuertes que las 3 elegidas para un teaser.

## Pendientes / reintentos (van todos en un solo batch)
-
