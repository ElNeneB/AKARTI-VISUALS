# Estado — Casa Nacho, Punta Sal (Perú)

`/automatico` crea `estado-<propiedad>.md` desde esta plantilla y lo mantiene solo. Las dos primeras líneas las lee la guardia: sin `puerta_A_nota: 9` o `10` y `calidad_kling: std|pro|4k` no se puede generar.

puerta_A_nota: 
calidad_kling: std
presupuesto_creditos: 36
saldo_inicial: 

## Fase actual
- [ ] 1 Auditoría + Lista definitiva (puerta A)
- [ ] 2 Recorte, subida, generación, puerta B
- [ ] 3 Premiere + puerta C

## Lista definitiva (puerta A: nota __/10)
| # | Foto (ID) | Espacio | Prompt | Recorte 16:9 | media_id | job_id | Puerta B | In / Out |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

Plano de apertura: __
Sonido: OFF — Créditos aprobados: __

## Datos de edición
- Versión (demo/final) y marca de agua (posición, opacidad):
- Formatos:
- Personalidad y duración objetivo:
- Música (ruta o "pausar"):
- Carpeta de exportación:

## Descartes
- Foto __: motivo

## Pendientes / reintentos (van todos en un solo batch)
-

## Corrida desatendida (7/10/2026)
- Modo teaser, desatendido. Link: https://www.airbnb.com.pe/rooms/1203050830696236472
- Fotos preauditadas (hoja 123, zona Punta Sal, personalidad playa-luminosa): 6, 20, 33, 18, 19, 22, 45, 24, 8, 9, 16, 17, 21, 23, 38, 39, 58, 26, 54, 27, 55, 30, 34, 67, 68, 74.
- Nota: usar solo el set de día. Dormitorios principales 69 y 70 son verticales.

## PARADA (7/10/2026)
- Hecho: estado creado (std, 36 créditos); 89 fotos descargadas en teasers/casa-nacho-punta-sal/fotos; `akarti.py identificar` sin ninguna coincidencia con rescate-6oct/ (no hay clips reutilizables, hay que generar los 3).
- Bloqueo: el MCP de Higgsfield requiere autorización (OAuth) y la sesión no es interactiva, así que no se puede subir ni generar. Premiere y headroom tampoco conectaron (el render automático no necesita Premiere).
- Falta: autorizar Higgsfield (/mcp en una sesión interactiva) y volver a lanzar `/automatico casa-nacho-punta-sal teasers/casa-nacho-punta-sal/fotos teaser`. Retoma desde auditoría + puerta A (puerta_A_nota aún vacía).
- No se gastaron créditos. No se agregó fila a registro.csv ni líneas a aprendizajes.md porque no hubo teaser.
