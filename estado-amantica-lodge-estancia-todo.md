# Estado — Amantica Lodge: estancia todo incluido para 4 (Ocosuyo)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A) — 2026-10-07, modo teaser, sets `fotos` (21) + `fotos-b` (14) combinados
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Veredicto del set
**SIRVE (teaser).** Mismo lodge en los dos anuncios. Quedan 3 espacios fuertes con luz de día coherente: dos dormitorios con vista al lago y la terraza. Dos de los tres clips ya existen aprobados (rescate del 6/10, puerta B 10) y se reutilizan sin gastar créditos; solo hay que generar 1 clip nuevo (terraza).

## Lista definitiva (puerta A: nota 10/10)
| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | fotos/foto_21.jpg (= rescate 77cf387a…, = fotos/foto_01, fotos-b/foto_01) | Dormitorio principal con vista al lago (sol sobre el agua, techo de totora) | DOLLY (texto fijo de `cocinando-lo-demas`) — **REUTILIZADO**: `rescate-6oct/clips/06_hf_20261006_042828_21d7bdaf-f9be-4e6a-96d5-62efd2acd0a5.mp4` | — | — (ya aprobado sin final) | 77cf387a-ab08-41d1-ba8f-b631e94f675c | 21d7bdaf-f9be-4e6a-96d5-62efd2acd0a5 | 10 PASA (rescate) | |
| 2 | fotos/foto_20.jpg (= rescate 07374513…, = fotos-b/foto_04) | Dormitorio twin con ventanal al lago | AXIS LOCK (texto fijo de `cocinando-lo-demas`) — **REUTILIZADO**: `rescate-6oct/clips/01_hf_20261006_042828_b0b48bba-7b6d-4f39-944b-15f14185e502.mp4` | — | — (ya aprobado sin final) | 07374513-990c-46f9-a54b-9af247d46a1c | b0b48bba-7b6d-4f39-944b-15f14185e502 | 10 PASA (rescate) | |
| 3 | fotos/foto_07.jpg | Terraza techada sobre el lago (sillones, mesa de centro, pérgola de listones) | **ORBIT 20°** (prompt abajo) — NUEVO | — | — (ORBIT va sin final) | ef3a1c29-df53-4d64-a763-21d5dd13be93 | f60b0407-dba3-4703-839f-1bba9c41d573 | 5 REPITE (intento 1 de 2): aparecen personas (puerta del fondo a 2 s y 3,5 s) y una lámpara/muro nuevo a 3,5 s | | |

Justificación de cada movimiento:
- **#1 DOLLY:** cuarto amplio y profundo con el ventanal al fondo; el avance hacia la luz del lago es el plano más fuerte. Ya probado: puerta B 10.
- **#2 AXIS LOCK:** encuadre frontal y simétrico hacia el ventanal; el avance recto sin giro respeta la simetría de las dos camas. Ya probado: puerta B 10.
- **#3 ORBIT 20°:** terraza abierta con sillones en primer plano que dan paralaje contra el lago; el techo de listones radiales es un patrón repetido, por eso arco de 20° desde el primer intento (regla confirmada en `aprendizajes.md`).

Prompt #3 (ORBIT 20°, texto fijo con el arco en 20°):
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

Plano de apertura: #1 dormitorio principal con el sol sobre el lago (fotos/foto_21, DOLLY reutilizado).
Orden: dormitorio principal (DOLLY) → dormitorio twin (AXIS LOCK) → terraza (ORBIT 20°). Sin movimientos repetidos seguidos.
Sonido: OFF — Créditos esperados: 1 clip nuevo × 6 = **6 créditos** (std, sonido OFF) + upscale 1080p de los 3 aprobados (~0,1 c/u). Créditos aprobados: __
Nota: los clips reutilizados se generaron el 6/10 con sonido; en el teaser se usa solo la imagen.

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad): demo, diagonal repetida al 10 % (`assets/marca/marca-agua-16x9.png`)
- Formatos: 16:9
- Personalidad y duración objetivo: lodge-andino, 12 a 15 s con end card
- Música (ruta o "pausar"):
- Carpeta de exportación: teasers/amantica-lodge-estancia-todo/

## Descartes
Set `fotos` (21):
- Foto 01: duplicado de foto 21 (misma imagen; se usa la 21, que coincide con el clip del rescate)
- Foto 02: logo de Airbnb, no es foto del espacio
- Foto 03: persona en cuadro; paisaje sin espacio que recorrer
- Foto 04: persona en cuadro
- Foto 05: bodegón de comida
- Foto 06: toma aérea (además baja resolución 1440x649)
- Foto 08: misma terraza que la 7 al atardecer: iluminación inconsistente con el resto (día)
- Foto 09: dormitorio con distorsión de gran angular (cama cortada en primer plano a la derecha); además el teaser va con 3 espacios
- Fotos 10, 11, 12: íconos/ilustraciones (casa, globo, campana), no son fotos del espacio
- Foto 13: ilustración de una persona
- Foto 14: exterior al anochecer: iluminación inconsistente (filtro: luz oscura)
- Fotos 15, 16: baños (fuera del top 3 del teaser; el 16 con espejo y batas como sujeto)
- Foto 17: bodegón (clóset con toallas), sin espacio que recorrer
- Foto 18: bodegón de comida, duplicado de la 5
- Foto 19: cielo nocturno, paisaje sin espacio e iluminación inconsistente

Set `fotos-b` (14):
- Foto 01: duplicado de fotos/foto_21
- Foto 02: logo de Airbnb
- Foto 03: lodge desde el lago: paisaje sin espacio que recorrer (construcción lejana)
- Foto 04: duplicado de fotos/foto_20
- Foto 05: mismo dormitorio principal que la foto 21 (otro ángulo, misma chimenea y totora): duplicado de espacio
- Foto 06: misma terraza que fotos/foto_07; se prefiere la 7 por los sillones en primer plano (más paralaje)
- Foto 07: exterior al anochecer, duplicado de fotos/foto_14 e iluminación inconsistente
- Foto 08: noche, persona en cuadro, borrosa
- Foto 09: persona en el muelle; vertical
- Fotos 10, 11, 12: íconos/ilustraciones
- Foto 13: ilustración de una persona
- Foto 14: baño (fuera del top 3)

## Puerta A
JUEZ — Puerta A — amantica-lodge-estancia-todo — Lista definitiva (teaser)
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
(9: ninguna foto elegida es vertical; no hace falta `recorte169`.)

## Pendientes / reintentos (van todos en un solo batch)
- Generar solo #3 (fotos/foto_07.jpg, ORBIT 20°). #1 y #2 se copian del rescate (sin créditos) y pasan directo a upscale.

## Avance 2026-10-07 (desatendido)
- #3 terraza: media_id ef3a1c29-df53-4d64-a763-21d5dd13be93, job_id f60b0407-dba3-4703-839f-1bba9c41d573 (6 créditos, std, off). Clip: teasers/amantica-lodge-estancia-todo/clips/03_terraza_hf_20261007_161305_f60b0407.mp4; hoja: ..._juez.jpg. PENDIENTE puerta B (akarti-juez-rapido) y luego upscale.
- #1 y #2 copiados a clips/. Upscale 1080p enviado: #1 job 657e1dc0-8022-4512-bb7b-3483e43960f0, #2 job cec38f7b-6382-4579-90d6-61c26c88671d (en proceso, por descargar). Nota: foto_07 es 3:2 sin recorte (el estado dice que no hace falta).

- Puerta B #3 terraza (2026-10-07): nota 5, REPITE. Falla critico 3 (personas nuevas en la puerta del fondo a 2 s y 3,5 s; muro con lámpara nuevo a 3,5 s). Cambio para el reintento: ORBIT 20° ya es el mínimo de la escalera; pasar a AXIS LOCK con fotograma final (final-push, 12 %) para que el final fije la escena, y agregar al prompt 'empty unoccupied terrace, no people, no figures in doorways'. Va en el batch de reintentos.
