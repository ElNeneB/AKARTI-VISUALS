---
name: automatico
description: "Modo automático de Akarti Visuals: con un solo prompt (/automatico propiedad + carpeta de fotos o link de Airbnb) produce el recorrido completo de punta a punta: auditoría, Lista definitiva, generación en Kling 3.0 (sonido OFF) y edición en Premiere, aprobando cada etapa con juez-akarti y gastando lo mínimo de créditos de Higgsfield y de uso de Claude. Hace una sola pregunta al inicio y solo se detiene si algo no lo puede decidir solo. Si la corrida se corta, el mismo comando la retoma desde el archivo de estado."
---

# SKILL AUTOMÁTICO

Un solo prompt, todo el recorrido. Esta skill dirige y las demás hacen el trabajo:

| Skill | Qué pone |
|---|---|
| `no-gastar` | Orden fijo de las fases y el ahorro (un agente por fase, archivo de estado) |
| `cocinando-lo-demas` | Descartes, Lista definitiva, prompts de cámara e inicio seguro |
| `calidad` | Reglas de clip (std, 16:9, 4 s, **sonido OFF**), un solo batch y una sola espera |
| `juez-akarti` | Puertas A, B y C (pasa con 9 o 10) |
| `director-akarti` | Edición premium en Premiere |

Las reglas de esas skills no se relajan en modo automático. Lo único que cambia es que las aprobaciones de Enrique se piden **todas juntas al inicio**.

## Uso

```
/automatico <propiedad> <carpeta de fotos | link de Airbnb> [teaser]
```

- **Completo** (por defecto): un clip por habitación y el recorrido entero.
- **teaser**: para un prospecto que todavía no paga. Solo los 3 espacios más fuertes (el plano de apertura y dos más, con movimientos distintos) y un video de unos 15 s con marca de agua. Unos 18 créditos en std. Si el cliente compra, `/automatico <propiedad> <carpeta>` hace el recorrido completo y reutiliza los 3 clips aprobados.

Si `estado-<propiedad>.md` ya existe, la corrida **sigue desde donde quedó**; no se repite nada de lo hecho.

## Paso 0: una sola pregunta al inicio

Crear `estado-<propiedad>.md` desde `estado-PLANTILLA.md`. Hacer **una sola** pregunta con la herramienta de preguntas, solo de los datos que falten. Esta pregunta cumple la regla de `calidad` de preguntar la calidad antes de generar:

1. Calidad de Kling: std (recomendada), pro o 4k.
2. Presupuesto máximo de créditos de Higgsfield. Proponer: clips estimados × costo por clip + 25 % para reintentos.
3. Versión: demo con marca de agua (por defecto) o final. Si es demo: posición y opacidad de la marca de agua.
4. Formatos: 16:9 (por defecto) y/o 9:16.
5. Personalidad de la propiedad y duración objetivo.
6. Música: se elige sola de `biblioteca/musica/indice.csv` según la personalidad. Preguntar solo si la biblioteca no tiene pista para esa personalidad (ruta del archivo, o "pausar para generarla con Gemini").
7. Carpeta de exportación (por defecto `Claude-Edicion` en el escritorio).

Escribir las respuestas en el estado: `calidad_kling:`, `presupuesto_creditos:` y una sección "Datos de edición". Anotar el saldo inicial de Higgsfield (`balance`). Desde aquí la corrida no vuelve a preguntar, salvo en las paradas de abajo.

## Fases (cada una en su agente, para que el chat principal no crezca)

Si existen los agentes `akarti-auditor`, `akarti-generador`, `akarti-juez` y `akarti-editor` (Claude Code en la carpeta del proyecto), delegar en ellos: cada uno ya tiene su modelo fijo. Si no existen (chat de claude.ai), hacer la fase siguiendo la skill indicada. No abrir fotos ni fotogramas en el chat principal: eso lo hacen los agentes.

1. **Auditoría + puerta A** (`akarti-auditor`): hojas de 6 fotos, descartes, Lista definitiva con inicio seguro, nota de la puerta A ≥ 9 escrita como `puerta_A_nota:`.
   - Si el set **no sirve**: parar y reportar el motivo. Fin.
   - Si se pasó un **link**: entregar el veredicto y la lista de fotos para descargar, y parar (es el único paso que necesita a Enrique). Al volver con la carpeta, `/automatico <propiedad> <carpeta>` sigue desde aquí.
2. **Costo:** sacar el costo exacto con `get_cost` (sonido OFF). Si el total entra en `presupuesto_creditos`, seguir sin preguntar, porque el presupuesto ya está aprobado. Si no entra, parar y mostrar la diferencia.
3. **Generación** (`akarti-generador`, modo ENVIAR_Y_ESPERAR): recorte 16:9, subida y **un solo** batch. Después, esperar sin gastar: una sola llamada `sleep 240` en Bash y luego una sola llamada a `jobs_wait`. Si quedan jobs en proceso, `sleep 60` y otra llamada a `jobs_wait`, como máximo 6 veces. Si `sleep` no está permitido, repetir `jobs_wait` dentro del agente (su contexto es chico). Después descarga los clips y arma la hoja 2x2 de cada uno.
4. **Puerta B en dos niveles:** primero `akarti-juez-rapido` (Sonnet) juzga todos los clips; después `akarti-juez` (Opus) vuelve a juzgar solo los que quedaron con nota 8 o 9 o con algún criterio sin verificar. Las notas van al estado y una línea por clip a `aprendizajes.md`.
5. **Reintentos:** todos los clips reprobados van juntos en **un solo** batch, con el cambio que indicó el juez y siempre dentro del presupuesto. Se repiten los pasos 3 y 4. Máximo 2 reintentos por clip. Un clip que no aprueba tras 2 reintentos se **marca como descartado** y la corrida **sigue** con los demás (regla de modo automático de `juez-akarti`). Si al descartarlo el recorrido se queda sin un espacio clave (sala, dormitorio principal o plano de apertura), anotarlo para el reporte final.
5b. **Upscale** (`akarti-generador`, modo MEJORAR): todos los clips aprobados en un solo envío, 1080p (2k si hay 9:16), y una sola espera.
6. **Música:** pista de la biblioteca o la ruta que dio Enrique; con eso se sigue sin parar. Si es "pausar", escribir el prompt de Gemini siguiendo `director-akarti`, guardarlo en el estado y parar. Al volver con la pista, `/automatico <propiedad>` sigue.
7. **Edición** (`akarti-editor`): plantilla maestra, `montaje-<propiedad>.json` y su XML con cortes en beat, y por MCP solo estabilización, color y exportación, según `director-akarti`. No escribe un "prompt para Claude Code" aparte. El room tone sale de una pista de librería porque los clips vienen sin audio.
8. **Puerta C** (`akarti-juez`): si falla, corregir la edición sin regenerar (máximo 2 veces). Si el fallo es un clip deformado, ese clip vuelve al paso 5.

## Paradas permitidas (las únicas)

- El set no sirve.
- Se pasó un link y hay que descargar las fotos.
- El costo supera el presupuesto aprobado.
- Falta la música: solo si la biblioteca no tiene pista para esa personalidad.
- Una función de Premiere no está disponible por MCP: proponer la alternativa manual, sin improvisar.
- Un error de una herramienta que no se resuelve en un reintento.

En cada parada: actualizar el estado, decir en 2 o 3 líneas qué falta, y que `/automatico <propiedad>` retoma la corrida.

## Reglas de ahorro que siempre se cumplen

- Sonido OFF, 4 s, 16:9 en todos los clips. En Claude Code, el hook `.claude/hooks/guardia-higgsfield.py` bloquea cualquier envío que no las cumpla.
- Nunca `show_generations`. Un solo batch para los clips y otro solo batch para los reintentos.
- Los agentes devuelven resúmenes cortos. El juez escribe solo los criterios que fallan.
- No mostrar imágenes en el chat principal.

## Reporte final

En 10 líneas o menos:
- la ruta del video exportado;
- las notas de las puertas A, B (por clip) y C;
- los clips descartados y por qué;
- los créditos gastados (saldo inicial menos saldo final) contra el presupuesto;
- lo que quedó pendiente.

Marcar la fase 3 en el estado y registrar la corrida con `python3 herramientas/akarti.py registrar ...`. Si quedan créditos y faltan menos de 7 días para el 29, recordarlo en el reporte.
