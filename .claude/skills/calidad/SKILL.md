---
name: "calidad"
description: "Reglas de clip de Kling 3.0 para Akarti Visuals (std, 16:9, 4 s, sonido OFF, un clip por habitación), forma de generar sin gastar de más (un solo batch, una sola espera) y obligación de preguntar la calidad antes de crear o generar nada."
---

# SKILL CALIDAD

Usar antes de generar o crear cualquier clip con Kling 3.0 en Higgsfield para Akarti Visuals.

## Paso obligatorio: preguntar la calidad

Antes de crear o generar nada, preguntar a Enrique con qué calidad se harán los videos con Kling (std, pro o 4k; son los modos que acepta Kling 3.0 vía Higgsfield). Usar la herramienta de preguntas con opciones. No asumir la calidad aunque "std" sea la habitual, y no generar hasta tener la respuesta. En `/automatico`, esta pregunta va dentro de la pregunta única del inicio, junto con el presupuesto, y la respuesta queda en `calidad_kling` y `presupuesto_creditos` del estado. Ese presupuesto es la aprobación del costo.

## Reglas de clip

- Un clip por habitación. Nunca una transición continua entre cuartos.
- Modelo: Kling 3.0. Modo: std, salvo que Enrique elija otra calidad en la pregunta anterior.
- Formato: 16:9.
- Duración: 4 segundos por clip.
- Sonido: OFF. Enviar siempre `sound: "off"`. El audio del video sale de la música y de un room tone de librería en Premiere, no de Kling. Sin sonido el clip std de 4 s cuesta 6 créditos en vez de 8 (25 % menos).
- Las fotos verticales se recortan a 16:9 ANTES de subirlas a Higgsfield, en la computadora de Enrique, con `python3 scripts/akarti.py recorte169 ENTRADA SALIDA` (está en la skill `no-gastar`). Claude no necesita mirar las fotos recortadas.

## Fotograma final y upscale

- Los clips con "Final: Sí" en la Lista definitiva llevan dos medias: la foto 16:9 como `start_image` y su `final-push` como `end_image`. El precio no cambia (6 créditos en std con sonido OFF).
- **Upscale solo de clips aprobados** en la puerta B, nunca de los reprobados. Usar `upscale_video` con `provider: bytedance`, `preset: aigc`, `fps: 24` (más de 30 duplica el costo), `width: 1280`, `height: 720` (salida de std), y `resolution: 1080p` para 16:9 o `2k` si también se entrega en 9:16. No permite consultar el costo antes; sumar un margen al presupuesto (prueba del 6/10: 0,08 créditos por clip de 4 s a 1080p y 24 fps). Se envían todos juntos y se espera una sola vez, igual que los clips.

## Antes de ejecutar

Confirmar con Enrique la calidad elegida, el número de clips y el costo en créditos. Sacar el costo real con `generate_video` y `get_cost: true` (no genera ni cobra), con los mismos parámetros que se van a usar, sonido OFF incluido. No reutilizar cifras de configuraciones anteriores. La cuenta de Enrique no tiene "unlimited mode" disponible para Kling 3.0, así que cada clip gasta créditos.

## Cómo generar sin gastar créditos de Claude

1. Enviar **todos** los clips de la propiedad en **un solo** `generate_video_batch`. Guardar los job_id en `estado-<propiedad>.md`.
2. Después de enviar, **no** preguntar a cada rato si ya terminaron.
   - En modo manual: terminar el turno con "Enviados N clips. Escríbeme 'listo' en unos 4 minutos." y, al recibir el "listo", hacer **una sola** llamada a `jobs_wait`.
   - En `/automatico`: **una sola** llamada `sleep 240` y luego **una sola** llamada a `jobs_wait`. Si quedan jobs en proceso, `sleep 60` y otra llamada a `jobs_wait`, como máximo 6 veces.
4. Nunca usar `show_generations`, porque repite el prompt completo de cada clip. Los job_id ya están en el archivo de estado.
5. Si hay reintentos, van **todos juntos** en un solo batch, nunca uno por uno.
6. Esta fase es mecánica: conviene hacerla con Sonnet, en un chat nuevo que solo lea `estado-<propiedad>.md`.
