# Investigación: por qué se gastan tantos créditos y cómo bajar el gasto sin perder calidad

Fecha: 6 de octubre de 2026. Datos sacados del historial real de Higgsfield (transacciones y generaciones) y de las skills de Akarti (`no-gastar`, `cocinando-lo-demas`, `calidad`, `juez-akarti`, `director-akarti`).

Hay **dos tipos de crédito** en juego, y el que se está quemando no es el de Higgsfield.

---

## 1. Higgsfield: el gasto es bajo, el problema es que se pierden créditos

### Lo que se gastó el 6 de octubre (el "video y medio")

| Hora (UTC) | Clips | Créditos | Detalle |
|---|---|---|---|
| 04:28 | 8 | 64 | 8 habitaciones en un batch (bien hecho) |
| 04:31 – 04:33 | 3 | 24 | **Reintentos**, uno por uno |
| 15:43 | 4 | 32 | 4 habitaciones nuevas, 0 reintentos |
| **Total** | **15** | **120** | 8 créditos por clip (Kling 3.0, std, 4 s, sonido ON) |

Los reintentos:
- Foto `3cab7d35` (dormitorio con camarote blanco): **3 intentos**: AXIS LOCK → AXIS LOCK describiendo el cuarto → DOLLY.
- Foto `e3cbac01`: ORBIT 30° → ORBIT 20°.

Los reintentos fueron el **20 % del gasto** (24 de 120 créditos). En el batch de las 15:43 ya se usó ORBIT 20° desde el principio y no hubo ningún reintento.

### Lo que de verdad cuesta dinero: créditos que vencen

- Plan Plus: 1.000 créditos por ciclo.
- Ciclo que terminó el 29 de septiembre: se usaron **154,62** y se **perdieron 845,38 (85 %)** con el "Subscription Credits Reset".
- Saldo de hoy: **879,31**. Si sigues a este ritmo, se vuelven a perder unos 750 en el próximo reinicio (alrededor del 29 de octubre).

### Precios reales (preguntados con `get_cost`, sin generar nada)

| Clip Kling 3.0 std 16:9 | Créditos |
|---|---|
| 4 s, sonido ON (lo que usas hoy) | 8 |
| 4 s, sonido OFF | 6 (−25 %) |
| 3 s, sonido OFF | 4,5 |

---

## 2. Claude: aquí se van los créditos "absurdos"

Esta sesión aparece con la **ventana de uso de 5 horas de Claude agotada** (se reinicia hoy a las 15:10, hora de Lima). Eso cuadra con tu queja: el que se consume es el límite de Claude, no Higgsfield.

> Limitación: no puedo leer la conversación anterior. Se hizo en la app de escritorio, no se guardó en la nube y no la puedo abrir desde aquí. El diagnóstico sale de cómo trabajan las skills y del rastro que dejó en Higgsfield (horarios, reintentos, llamadas).

### Cómo cobra Claude en una conversación con herramientas

**Cada** llamada a una herramienta (subir una foto, esperar un job, ver un fotograma, dar un paso en Premiere) vuelve a enviar **la conversación completa** al modelo. El costo crece así:

> **costo ≈ tamaño de la conversación × número de llamadas**

Todo lo que entra temprano (fotos, capturas, respuestas largas) se vuelve a pagar en cada llamada hasta el final del chat. Un video y medio en **un solo chat** es el peor caso, porque el chat crece sin parar y cada paso nuevo cuesta más que el anterior.

### Las fuentes de gasto, de mayor a menor

| # | Fuente | Por qué es cara | Peso estimado |
|---|---|---|---|
| 1 | **Todo en un mismo chat** | Auditoría + generación + juez + Premiere de 1,5 propiedades se acumulan. Al final, cada llamada arrastra cientos de miles de tokens | Multiplica todo lo demás |
| 2 | **Imágenes en el chat** | Cada foto cuesta unos 1.600 tokens, y cada fotograma de 1280×720 unos 1.230. La puerta B pide foto + 3 fotogramas por clip: 15 clips × 4 = **60 imágenes (unos 80.000 tokens)** que se quedan en el chat. A eso se suman la auditoría (20–40 fotos) y las capturas de Chrome de la galería de Airbnb | Alto |
| 3 | **Esperar a Kling preguntando** | `jobs_wait` espera como máximo 15 s y un clip tarda unos 3 min (batch a las 04:28, siguiente acción a las 04:31). Eso son **unas 12 llamadas por batch**, cada una con el chat entero. Los 3 reintentos se hicieron por separado, así que el ciclo de espera se repitió 3 veces más | Alto |
| 4 | **Premiere paso a paso por MCP** | Docenas o cientos de llamadas (importar, colocar, estabilizar, color, audio, exportar), cada una con el chat entero | Alto |
| 5 | **Opus con esfuerzo alto para todo** | También se usa para tareas mecánicas: subir, esperar, ejecutar pasos | Medio-alto |
| 6 | **Respuestas largas** | El juez escribe 10 criterios con evidencia × 15 clips. El director entrega 8 secciones **más** un "prompt para Claude Code" que luego el mismo Claude ejecuta, o sea que se escribe el plan dos veces. El texto que Claude escribe es lo más caro por token | Medio |
| 7 | **Herramientas que devuelven mucho texto** | `show_generations` repite el prompt completo de cada clip (unos 7.000 tokens por 20 clips). El servidor de Higgsfield tiene más de 130 herramientas | Bajo-medio |

**Ejemplo de orden de magnitud** (ilustrativo, no medido): con un chat de 200.000 tokens de promedio y 300 llamadas se procesan unos 60 millones de tokens. Si el chat pesa la mitad y se hace la mitad de llamadas, el gasto baja **a la cuarta parte**.

---

## 3. Flujo optimizado: mismo resultado, mismas reglas de calidad

No se toca nada de lo que define la calidad: Kling 3.0 std, 16:9, 4 s, un clip por habitación, los cuatro movimientos, las 3 puertas del juez, hard cuts, Warp Stabilizer y −14 LUFS. Solo cambia **cómo** trabaja Claude.

### A. Un chat por fase, con un archivo de estado (el ahorro más grande)

Por cada propiedad se mantiene `estado-<propiedad>.md` con: la Lista definitiva, los media_id subidos, los job_id, la nota del juez por clip y los In/Out. Cada fase empieza en un **chat nuevo** que solo lee ese archivo:

1. Chat 1: auditoría + Lista definitiva (puerta A). Opus.
2. Chat 2: recorte, subida, generación y puerta B. Sonnet; Opus solo si un clip está en duda.
3. Chat 3: Premiere + puerta C. Sonnet.

Así ningún chat arrastra las fotos y fotogramas de las fases anteriores.

### B. Una imagen en vez de cuatro (o seis)

Ver `herramientas/akarti.py` (solo necesita Python y ffmpeg):

- `juez-clip CLIP.mp4 FOTO.jpg` arma una sola hoja 2×2 (foto | 0,5 s / 2 s | 3,5 s). Son unos 1.800 tokens en vez de unos 5.300: **−65 % por clip**, y se ven los mismos 4 cuadros.
- `hoja-fotos CARPETA` pone 6 fotos numeradas por imagen para la auditoría. Son **unas 5 veces menos tokens** que ver foto por foto. Si alguna está en duda (distorsión, espejo), solo esa se abre en grande.
- `recorte169 ENTRADA SALIDA` recorta a 16:9 en tu computadora antes de subir, sin que Claude tenga que mirar nada.
- `audio VIDEO.mp4` mide LUFS integrados y true peak y responde con texto (puerta C, criterio 7), sin capturas del medidor de Premiere.

Además, la puerta B se puede hacer en un **subagente**: él mira las hojas y le devuelve al chat principal solo la nota. Así las imágenes no se quedan en el chat principal.

### C. Generar sin preguntar a cada rato

1. **Un solo** `generate_video_batch` con todos los clips de la propiedad.
2. **No preguntar** si ya terminó: Claude termina su turno con "vuelve en 4 min". Cuando escribes "listo", hace **una** sola llamada a `jobs_wait`. Así pasan de unas 12 llamadas por batch a 1.
3. Nunca usar `show_generations` (repite todos los prompts). Los job_id ya están en el archivo de estado.
4. Si hay que repetir, **todos los reintentos van en un solo batch**, no uno por uno.

### D. Evitar los reintentos desde la Lista definitiva (ahorra en Higgsfield y en Claude)

Lo que se aprendió el 6/10, para aplicar desde el primer intento en la puerta A:

- ORBIT empieza en **20°** si el cuarto tiene camarotes, patrones repetidos, persianas, estanterías o cabeceras con listones. Con 20° el batch de las 15:43 salió sin reintentos.
- Los cuartos chicos o con muebles altos (como el camarote) empiezan directo en **AXIS LOCK con la descripción breve del cuarto al inicio del prompt**, que es el paso 2 de la escalera del juez. Así se salta el intento que se sabe que falla.

Cada reintento evitado ahorra 8 créditos de Higgsfield y un ciclo completo de Claude (esperar, sacar fotogramas, juzgar).

### E. Respuestas más cortas

- **Juez:** escribir solo `Nota X/10 → PASA/REPITE` y la evidencia de los criterios **que fallan**. Los aprobados se quedan en el archivo de estado como una lista de ✓.
- **Director:** si Claude va a ejecutar Premiere en el mismo flujo, **no** escribir el "Prompt para Claude Code" (es escribirse instrucciones a sí mismo). La tabla de edición con valores exactos es la instrucción.

### F. Usar o recortar los créditos de Higgsfield

- Con 879 créditos y el reinicio alrededor del 29/10, alcanzan para unos **110 clips**, más o menos **9 recorridos** de unas 12 habitaciones. Lo que no se use antes de esa fecha se pierde.
- Si en un mes normal solo produces 2 o 3 recorridos, conviene revisar si el plan Plus es el que te sirve.

### G. Audio OFF (aprobado por Enrique el 6/10)

El director usa el audio de Kling solo como room tone, entre −18 y −24 dB debajo de la música, y silencia los ruidos de la IA. Generar con sonido OFF todos los clips menos 1 o 2 (para sacar el ambiente) **baja 25 % el costo** en Higgsfield. **Aprobado:** desde el 6/10 todos los clips van con sonido OFF y el ambiente sale de una pista de librería en Premiere (ya actualizado en `calidad` y `director-akarti`).

---

## 4. Cambios sugeridos a las skills (para pegar en claude.ai → Skills)

- **no-gastar:** agregar el paso "Cada fase en un chat nuevo; el estado vive en `estado-<propiedad>.md`" y "Auditar con `hoja-fotos`, no foto por foto".
- **calidad:** agregar "Todos los clips en un solo `generate_video_batch`; después de enviar, terminar el turno y esperar el 'listo' de Enrique; una sola llamada a `jobs_wait`; nunca `show_generations`".
- **juez-akarti, puerta B:** "Revisar con la hoja 2×2 de `juez-clip` (una imagen por clip)", "Salida corta: nota + criterios que fallan", "Los reintentos van todos juntos en un batch".
- **cocinando-lo-demas:** agregar las reglas de inicio seguro de la sección D (ORBIT 20° con patrones repetidos; AXIS LOCK con descripción del cuarto en cuartos chicos o con camarotes).
- **director-akarti:** "Si Claude ejecuta la edición en el mismo flujo, omitir la sección 7 (Prompt para Claude Code)".

## 5. Ahorro esperado

| Cambio | Ahorro en Claude | Ahorro en Higgsfield |
|---|---|---|
| Un chat por fase + archivo de estado | El mayor; aproximadamente divide por 2–4 | — |
| Hoja 2×2 del juez + subagente | −65 % de imágenes en la puerta B | — |
| Hojas de 6 fotos para la auditoría | Unas 5 veces menos imágenes | — |
| No preguntar por los jobs | De unas 12 llamadas a 1 por batch | — |
| Sonnet para fases mecánicas | Mucho más barato por token | — |
| Inicio seguro en cuartos riesgosos | Menos ciclos | Unos −20 % (lo que se fue en reintentos el 6/10) |
| Sonido OFF (aprobado) | — | −25 % |

Los porcentajes de Higgsfield son exactos (salen del historial y de `get_cost`). Los de Claude son estimaciones según cómo se cobra cada llamada, porque no tengo el registro de la sesión anterior.
