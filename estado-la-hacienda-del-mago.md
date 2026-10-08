puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 

# Estado — La Hacienda del Mago Cieneguilla (hoja 196, Cieneguilla)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A: 10/10, modo teaser, 3 clips)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Veredicto del set
SIRVE. Interiores profesionales con luz uniforme y exteriores de día muy fuertes (jardín, palmeras, capilla, cerros). Casi un tercio del set son eventos y bodas (fuera).

Nota de auditoría: la numeración de los archivos descargados (foto_01..foto_74) NO coincide con los IDs de la fila 196 de `propiedades-teaser.csv` (la descarga trae además logo de Airbnb, íconos y avatar). Los IDs de esta tabla son los números de archivo de `teasers/la-hacienda-del-mago/fotos/`, verificados mirando las hojas de 6.

## Lista definitiva (puerta A: nota 10/10) — modo teaser, 3 espacios
| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 60 | Exterior: casa, jardín, palmeras y capilla con cerros | AXIS LOCK + descripción | — | r1: Sí (12 %) | ced3822c (final) | 902c7cb5 (r1) | Original: Opus 8/10 REPITE (✗7 micro-saltos cada 8 cuadros, ✗8 sin meseta de velocidad). **r1 (clip1_foto60_r1.mp4): Opus 10/10 PASA** — escala medida 1,000→1,134 lineal (≈0,033/s de 0,2 a 4,0 s), energía de movimiento por cuadro 1,75–2,06 (±8 %, sin caídas; el original caía 30-40 %), deriva x/y ≤0,5 px, geometría, palmeras, capilla y quincho fieles en 0,5/2/3,5 s | 0,2 s / 4,0 s |
| 2 | 15 | Sala con chimenea (sala hundida, vigas, piano) | DOLLY | — | Sí (12 %) | | | 10 PASA | |
| 3 | 54 | Piscina con cascadas y camastros | ORBIT 20° | — | — | | | 10 PASA | |

Plano de apertura: foto 60 (jardín amplio con las dos palmeras, la capilla y los cerros: el plano más fuerte y más "campo-cálido" del set).
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sonido OFF); presupuesto aprobado 36.

### Justificación de cada movimiento
1. **Foto 60, AXIS LOCK + descripción, sin final:** exterior amplio y profundo, sin muebles altos ni patrones cerca; el avance recto por el césped hacia las palmeras da profundidad real. Sin final para conservar el paralaje (regla de `cocinando-lo-demas`: espacios amplios y sin riesgo van sin final). La descripción ancla palmeras, capilla y quincho.
2. **Foto 15, DOLLY con final 12 %:** sala con patrones (alfombra patchwork de cuero, vigas repetidas, mantel a rayas) y objetos en primer plano (teteras de cobre, planta). `aprendizajes.md`: DOLLY con final pasó 10/10 en todos los registros (sala alu-luxe, dormitorios, terrazas), mientras que AXIS LOCK y ORBIT en salas grandes con primer plano deformaron (kailani, eywa). Se eligió la foto 15 y no la 14 porque la 14 tiene una mesa de vidrio reflectante en primer plano (eywa: el vidrio en primer plano rompe el tramo medio).
3. **Foto 54, ORBIT 20°:** sujeto central claro (piscina y muro de cascadas), fondo de vegetación sin puertas ni aberturas (en amantica y kailani el ORBIT inventó personas y cuartos en puertas del fondo), sin muebles altos en primer plano. 20° desde el inicio por los listones de los camastros y la pérgola en el borde derecho. Sin final (ORBIT no lleva final).

### Prompts exactos (copiar tal cual)
**Clip 1 — foto 60 — AXIS LOCK + descripción (sin final):**
A wide sunlit green lawn in front of a Spanish colonial hacienda with terracotta tile roofs, two tall Canary date palms with textured trunks, a small white chapel with a stone bell tower and a wooden cart wheel in the center, a timber-framed covered quincho with a long dining table on the right, wooden sun loungers on the left, green mountains under a blue sky with light clouds behind. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

**Clip 2 — foto 15 — DOLLY (con final 12 %):**
Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

**Clip 3 — foto 54 — ORBIT 20° (sin final):**
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

### Comandos listos para la fase 2 (no ejecutados)
- Fotos elegidas copiadas en `teasers/la-hacienda-del-mago/seleccion/` (foto_15, foto_54, foto_60). Ninguna es vertical (60 y 15: 1440x960; 54: 1440x928); el recorte a 16:9 es solo el ajuste de formato del lote:
  `python3 herramientas/akarti.py recorte169 teasers/la-hacienda-del-mago/seleccion teasers/la-hacienda-del-mago/169`
- Final del clip 2:
  `python3 herramientas/akarti.py final-push teasers/la-hacienda-del-mago/169/foto_15.jpg teasers/la-hacienda-del-mago/169/foto_15_final.jpg 12`

## Puerta A
```
JUEZ — Puerta A — la-hacienda-del-mago — Lista definitiva (teaser)
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
Evidencia: 1 veredicto "SIRVE" escrito; 2 cada descarte con motivo de `cocinando-lo-demas`; 3 fotos 60/15/54 sin personas, sin dron, luz de día uniforme, distorsión de gran angular leve; 4 un clip por espacio, sin transiciones; 5 prompts tal cual (ORBIT con el dial a 20°, AXIS LOCK con la frase de descripción al inicio); 6 AXIS LOCK → DOLLY → ORBIT; 7 exterior → sala → piscina; 8 justificación por fila; 9 sin verticales en la lista; 10 apertura = foto 60.

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad): demo, diagonal repetida 10 %
- Formatos: 16:9
- Personalidad y duración objetivo: campo-calido, 12 a 15 s
- Música (ruta o "pausar"):
- Carpeta de exportación: teasers/la-hacienda-del-mago/

## Descartes (IDs = número de archivo)
- 02, 10, 11, 12, 13: no son fotos del espacio (logo de Airbnb, íconos, avatar) — bodegones sin espacio que recorrer.
- 01, 07, 55, 56: tomas aéreas o elevadas de dron.
- 03, 43, 51 (atardecer) y 39, 42, 58 (noche): iluminación inconsistente.
- 18: sala con árbol de Navidad — iluminación/decoración inconsistente con el resto.
- 59–74: eventos y bodas (personas en cuadro, carpas, montajes de banquete); 60 se salva: es jardín limpio sin evento.
- 50: auto en cuadro (camino de jardín).
- 17 (detalle del piano), 26 (escritorio antiguo), 31 (estantería vertical), 40, 41 (puertas de jardín), 45 (juego vertical), 48 (casita de juegos vertical): bodegones sin espacio que recorrer.
- 28, 35: espejos como sujeto de la foto.
- 09, 27, 37, 47: baños (en teaser no entran; 47 además urinarios de eventos).
- 23: duplicado vertical del comedor 22.
- 14: duplicado de la misma sala que 15 (mesa de vidrio reflectante en primer plano).
- Aptos pero no elegidos por ser teaser (3 espacios): 04, 05, 06, 08, 16, 19–22, 24, 25, 29, 30, 32–34, 36, 38, 44, 46, 49, 52, 53, 57.

## Pendientes / reintentos (van todos en un solo batch)
- Clip 1 (foto 60), reintento 1 de 2 (juez Opus, puerta B 8/10, falla en c7 y c8: velocidad irregular). Cambio: mismo AXIS LOCK + descripción, ahora **con fotograma final `final-push` 12 %** (regla del proyecto para AXIS LOCK; en `aprendizajes.md` todos los clips con final mantuvieron velocidad pareja) y en la parte de cámara cambiar "at continuous linear speed" por "already gliding at a slow, even cruising speed in the very first frame and holding that exact same speed until the last frame". Todo en positivo. Costo estimado 6 créditos (quedan 18 del presupuesto de 36). Si el reintento 1 falla en c7/c8, el reintento 2 pasa a DOLLY con final 12 %.
  - **RESUELTO (2026-10-08):** reintento 1 aprobado por Opus 10/10 PASA. No hace falta reintento 2 (no se gasta). Usar `clips/clip1_foto60_r1.mp4` en el montaje. Puerta B completa: 3/3 clips aprobados.

## Fase 2 - Generación (2026-10-08)
- Recortes: teasers/la-hacienda-del-mago/169/ (foto_15, foto_54, foto_60, foto_15_final)
- media_id: foto_60=61a496aa-3c62-488a-acd8-7304dadecc55 | foto_15=9f70b36b-1cd2-4132-82e8-8443aa56ec89 | foto_15_final=f8ceb8ac-2c28-4e57-a74c-9088d6cf03b0 | foto_54=cb419f89-64af-4acd-9822-cc18acc92d75
- Costo exacto: 6 créditos por clip, total 18 (presupuesto 36)
- job_id: clip1=becd70d7-a5b9-4544-b9b0-adc63e3f01c9 | clip2=5b1b20f1-dc8f-41ab-b40b-981b2e24efc4 | clip3=ba8833f9-e211-4a12-97f2-15bf6c648229
- Nota: el batch devolvió una recomendación de preset ("IN THE DARK") en clips 1 y 3 sin crear jobs; se reenviaron con declined_preset_id (solo 3 jobs existen).
- Jobs completados (3/3). Clips: teasers/la-hacienda-del-mago/clips/clip1_foto60.mp4, clip2_foto15.mp4, clip3_foto54.mp4
- Hojas 2x2 para el juez: teasers/la-hacienda-del-mago/clips/clip1_foto60_juez.jpg, clip2_foto15_juez.jpg, clip3_foto54_juez.jpg
- Créditos gastados: 18 (3 x 6, std, sonido OFF). Pendiente: puerta B (akarti-juez-rapido).

## Reintento 1 - clip 1 (2026-10-08)
- final-push 12 %: teasers/la-hacienda-del-mago/169/foto_60_final.jpg | media_id final=ced3822c-1df2-48e9-99f2-34f66fd57eee
- job_id clip1_r1=902c7cb5-7b5b-4a50-a401-eaa409841431 (std, 16:9, 4 s, sonido OFF, AXIS LOCK + descripcion + final, "already gliding..."). Costo exacto 6 creditos. Total propiedad 24 de 36.
- Nota: el primer envio del batch dio timeout del MCP sin crear job (verificado en transactions); se reenvio una sola vez.
- Completado. Clip: teasers/la-hacienda-del-mago/clips/clip1_foto60_r1.mp4 | hoja 2x2: teasers/la-hacienda-del-mago/clips/clip1_foto60_r1_juez.jpg
- Creditos gastados reales en este reintento: 6 (propiedad 24 de 36). Puerta B del reintento (akarti-juez, Opus, desatendido): 10/10 PASA. Reintento 2 cancelado.
