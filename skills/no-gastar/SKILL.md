---
name: "no-gastar"
description: "Orden fijo para producir el recorrido de una propiedad de Akarti Visuals sin gastar de más (créditos de Higgsfield y uso de Claude): un chat por fase con archivo de estado, auditar fotos en hojas de 6, descartar, armar ruta de clips, generar en un solo batch y cortar en Premiere. También se usa cuando Enrique pasa el link de un anuncio de Airbnb (en vez de las fotos) para saber si la propiedad sirve antes de descargar nada."
---

# SKILL NO GASTAR

Usar siempre que Enrique pida preparar, revisar o producir el video de una propiedad para Akarti Visuals (servicio de video con IA para anfitriones de Airbnb). Regla central: no se gastan créditos de Higgsfield hasta tener la lista definitiva armada, y no se gasta uso de Claude en repetir, esperar o mirar de más.

## Un chat por fase (regla de ahorro principal)

Cada paso que da Claude vuelve a leer la conversación completa. Por eso cada fase va en un **chat nuevo**, y la información pasa de un chat a otro con el archivo `estado-<propiedad>.md` (plantilla abajo). Ese archivo guarda la Lista definitiva, los descartes, los media_id, los job_id, la nota del juez por clip y los In/Out.

| Fase | Pasos | Modelo |
|---|---|---|
| Chat 1 | 1, 2, 3 + juez puerta A | Opus (auditar y juzgar) |
| Chat 2 | Recorte, subida, 4 + juez puerta B | Sonnet (lo mecánico); el juez de la puerta B con Opus o en un subagente |
| Chat 3 | 5 + juez puerta C | Sonnet |

Al terminar cada fase: actualizar `estado-<propiedad>.md` y decirle a Enrique "Fase X lista. Abre un chat nuevo y pásame estado-<propiedad>.md". No seguir con la siguiente fase en el mismo chat.

## Orden fijo (no saltarse pasos)

1. **Auditar las fotos sin gastar créditos.** No generar nada, no subir nada a Higgsfield todavía. Para revisar el set, armar hojas de 6 fotos numeradas con `python3 scripts/akarti.py hoja-fotos CARPETA` y mirar las hojas, no foto por foto. Solo se abre una foto en grande si hay duda (distorsión, espejo, persona pequeña).
2. **Descartar.** Aplicar los criterios de la skill `cocinando-lo-demas`. Se pueden descartar fotos por criterio propio sin pedir permiso, pero siempre informando qué se quitó y por qué.
3. **Armar la ruta de clips.** Un clip por habitación, en el orden del recorrido, aplicando las reglas de inicio seguro de `cocinando-lo-demas` para no gastar en reintentos. Entregar la tabla "Lista definitiva" con el formato de `cocinando-lo-demas` y guardarla en `estado-<propiedad>.md`.
4. **Generar.** Recién aquí se gastan créditos. Recortar las fotos verticales con `python3 scripts/akarti.py recorte169 ENTRADA SALIDA`. Antes de generar, aplicar la skill `calidad`: preguntar la calidad, sonido OFF, un solo batch y una sola espera.
5. **Cortar en Premiere.** Hard cuts, sin disolvencias, recortando el arranque y la frenada de cada clip (las rampas de aceleración no se quitan por prompt). Higgsfield no estabiliza: si hace falta, Warp Stabilizer en Premiere (Subspace Warp, Smoothness 15-25%).

## Nota

Si Enrique pide generar sin haber pasado por los pasos 1 a 3, avisarle que falta la auditoría y hacerla primero.

## Auditoría desde link (antes de descargar)

Si Enrique pasa el link de un anuncio de Airbnb en vez de las fotos, hacer el paso 1 y el paso 2 directamente desde el anuncio, para que él solo descargue si la propiedad sirve.

1. Abrir el link con Claude in Chrome y entrar a la galería completa del anuncio ("Mostrar todas las fotos"). Para gastar menos capturas, alejar el zoom del navegador (por ejemplo, 50 %) y así ver varias fotos en cada captura. Bajar hasta el final para que carguen todas y revisarlas todas, no solo las de portada. No leer el texto completo de la página.
2. Numerar cada foto según su orden en la galería (Foto 1, Foto 2…) e indicar el espacio que muestra. Ese número es el ID mientras no haya archivos descargados.
3. Aplicar los criterios de descarte de `cocinando-lo-demas`, sin generar ni subir nada a Higgsfield.
4. Entregar:
   - **Veredicto:** si la propiedad sirve o no para un recorrido. Si no sirve, decir por qué y terminar ahí.
   - **Si sirve:** las fotos descartadas con su motivo, y la lista de fotos que Enrique debe descargar (número de galería + espacio).
5. Cuando Enrique pase las fotos descargadas, seguir desde el paso 3 del orden fijo como siempre.

## Herramientas (scripts/akarti.py, necesita Python y ffmpeg)

- `hoja-fotos CARPETA`: hojas de 6 fotos numeradas para auditar.
- `recorte169 ENTRADA SALIDA`: recorte al centro a 16:9, 1920x1080, antes de subir.
- `juez-clip CLIP.mp4 FOTO.jpg`: hoja 2x2 para la puerta B del juez.
- `audio VIDEO.mp4`: LUFS integrados y true peak medidos para la puerta C.

## Plantilla de estado-<propiedad>.md

```
# Estado — [Propiedad]
puerta_A_nota: 
calidad_kling: 

## Fase actual
- [ ] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C
## Lista definitiva (puerta A: nota __/10)
| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | media_id | job_id | Puerta B | In / Out |
Plano de apertura: __
Sonido: OFF — Créditos aprobados: __
## Descartes
- Foto __: motivo
## Pendientes / reintentos (van todos en un solo batch)
```
