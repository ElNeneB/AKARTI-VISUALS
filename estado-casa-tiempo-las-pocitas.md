# Estado — Casa Tiempo, Las Pocitas, Máncora

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 

## Fase actual
- [x] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Lista definitiva (puerta A: nota 10/10)

Veredicto: el set SIRVE para teaser (3 espacios de luz de día, sin personas). Numeración verificada por contenido con hojas de 6: la lista de candidatas del CSV no coincide con el contenido (32/31 = camarotes, 50 = balcón del dormitorio, 51 = fachada, 2/11/12/13 no son fotos de la casa).

| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | Final | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | foto_17 | Sala techada (sofás blancos, cielo de esteras y vigas, cestos en la pared, mar al fondo) — APERTURA | DOLLY (P1) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | | | | |
| 2 | foto_08 | Estar interior (seccional gris, alfombra roja y azul, cuadro de madera, mampara al jardín) | ORBIT 20° (P2) | Sí (3:2 → 16:9) | — | | | | |
| 3 | foto_50 | Dormitorio principal: balcón con vista al mar | AXIS LOCK + descripción (P3) | Sí (3:2 → 16:9) | Sí (final-push 12 %) | | | | |

Plano de apertura: foto_17 (sala techada), el más fuerte: profundidad de los sofás hasta el mar, luz cálida de tarde.
Sonido: OFF — Créditos esperados: 3 clips × 6 = 18 (std, sin sonido; el final no cambia el precio). Presupuesto aprobado 36.

Justificación de movimientos:
- 1 Sala techada → DOLLY con final: cielo de esteras con vigas (patrón repetido) y terraza abierta con un ORBIT 20° que ya inventó personas y muros (amantica); el DOLLY con final pasó 10/10 en la terraza techada de casa-kailani. Avance corto y anclado.
- 2 Estar interior → ORBIT 20°: cuarto cerrado con el seccional como sujeto central y primer plano (alfombra, banquitos) que da paralaje; 20° por la alfombra geométrica (patrón). La mampara queda a la izquierda, fuera del centro del arco.
- 3 Balcón del dormitorio → AXIS LOCK + descripción, con final: espacio angosto con cielo de tablas (patrón) y baranda de vidrio; avance recto hacia el mar, la frase del espacio y el final de la misma foto anclan la geometría.
Movimientos distintos y sin repetir seguidos: DOLLY → ORBIT → AXIS LOCK. Orden lógico: sala → estar → dormitorio.

P1 (DOLLY): Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

P2 (ORBIT 20°): Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a gentle 20 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

P3 (AXIS LOCK + descripción): Covered upper-floor balcony with a pitched ceiling of warm wooden planks and beams, dark wooden deck floor with a grey rug, two round rattan papasan chairs with white cushions and a small rattan side table, a tall glass railing with a dark wooden handrail on the right, a large sliding glass door on the left open to a bedroom with a blue-covered bed, palm trees and a thatched roof below, white sand beach and turquoise ocean under a clear blue sky. Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

Comandos listos (fase 2; ninguna elegida es vertical, todas son 3:2 y se recortan al centro a 16:9):
```
mkdir -p teasers/casa-tiempo-las-pocitas/169
python3 herramientas/akarti.py recorte169 teasers/casa-tiempo-las-pocitas/fotos/foto_17.jpg teasers/casa-tiempo-las-pocitas/169/01_sala_17.jpg
python3 herramientas/akarti.py recorte169 teasers/casa-tiempo-las-pocitas/fotos/foto_08.jpg teasers/casa-tiempo-las-pocitas/169/02_estar_08.jpg
python3 herramientas/akarti.py recorte169 teasers/casa-tiempo-las-pocitas/fotos/foto_50.jpg teasers/casa-tiempo-las-pocitas/169/03_balcon_50.jpg
python3 herramientas/akarti.py final-push teasers/casa-tiempo-las-pocitas/169/01_sala_17.jpg teasers/casa-tiempo-las-pocitas/169/01_sala_17_final.jpg 12
python3 herramientas/akarti.py final-push teasers/casa-tiempo-las-pocitas/169/03_balcon_50.jpg teasers/casa-tiempo-las-pocitas/169/03_balcon_50_final.jpg 12
```

JUEZ — Puerta A — casa-tiempo-las-pocitas — Lista definitiva (teaser)
Nota: 10/10 → PASA
✓ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (3: 17, 08 y 50 abiertas en grande, sin personas, espejos ni dron; luz de día las tres, filtro "ok". 5: prompts copiados de cocinando-lo-demas; ORBIT con el dial en 20°. 7: sala → estar → dormitorio. 9: no hay verticales; las tres llevan recorte 3:2 → 16:9.)

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad):
- Formatos:
- Personalidad y duración objetivo:
- Música (ruta o "pausar"):
- Carpeta de exportación:

## Descartes
- foto_02, foto_11, foto_12, foto_13: no son fotos de la casa (logo de Airbnb, íconos, avatar).
- foto_01, foto_04, foto_40: personas en cuadro (huéspedes en reposeras / en la playa).
- foto_37, foto_38: espejo como sujeto (baños).
- foto_42, foto_44, foto_52: tomas aéreas en picado desde lo alto, sobre la piscina y la playa.
- foto_24, foto_18: iluminación inconsistente (atardecer y contraluz; el filtro las marca oscuras). 18 además repite el espacio de 17.
- foto_19: iluminación inconsistente (filtro: clara) y casi bodegón (recibidor con cuadro y consola).
- No elegidas para el teaser (sirven para el recorrido completo): foto_14 (mismo espacio que 17, sin mar), foto_21 y foto_22 (cocina, más débil: stickers en las refrigeradoras), foto_31 y foto_32 (camarotes, riesgo alto según aprendizajes), foto_51 (fachada sobre calle de tierra).

## Pendientes / reintentos (van todos en un solo batch)
- BLOQUEO fase 2 (2026-10-07): el MCP de Higgsfield requiere autenticación (OAuth) y la sesión es no interactiva. No se recortó, subió ni generó nada; 0 créditos gastados. Autorizar Higgsfield desde /mcp o la configuración de conectores y relanzar la fase 2.
