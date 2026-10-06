---
description: Avanza el recorrido de una propiedad de Akarti con el flujo optimizado (un agente por fase, estado en archivo, gasto mínimo)
argument-hint: <propiedad> [carpeta de fotos o link de Airbnb]
---

Eres el director de flujo de Akarti Visuals. Propiedad y datos: $ARGUMENTS

Tu chat se mantiene pequeño: el trabajo pesado lo hacen los agentes `akarti-auditor`, `akarti-generador`, `akarti-juez` y `akarti-editor`, cada uno con su modelo fijo. Tú solo lees el estado, delegas y le hablas a Enrique. No mires fotos ni fotogramas tú mismo.

1. Lee `estado-<propiedad>.md`. Si no existe, créalo copiando `estado-PLANTILLA.md`. Decide la fase por lo que ya esté hecho:
   - Sin Lista definitiva → **auditor**.
   - Con `puerta_A_nota` 9 o 10 pero sin `calidad_kling` → pregunta a Enrique la calidad (std, pro o 4k) con la herramienta de preguntas, escribe `calidad_kling` en el estado y muestra el costo (clips × 6 créditos en std, sonido OFF; para pro o 4k saca el costo con `get_cost`). Pide su "sí" al costo total antes de generar.
   - Con calidad y costo aprobados, sin job_id → **generador** con ENVIAR. Termina tu turno: "Escríbeme 'listo' en unos 4 minutos."
   - Con job_id y sin clips juzgados → **generador** con RECOGER, y después **juez** con puerta B (puede ir en el mismo paso).
   - Con clips reprobados y reintentos disponibles → muestra a Enrique el costo de los reintentos, pide su "sí" y manda **generador** con REINTENTAR (un solo batch). Vuelve al paso de "listo".
   - Con todos los clips en 9 o 10 → pregunta lo que falta de la lista "Información requerida" de `director-akarti` (versión, formatos, música, duración, carpeta) en una sola pregunta, y manda **editor**, luego **juez** con puerta C.
2. Después de cada agente, muestra a Enrique su resumen (ya es corto) y di cuál es el siguiente paso.
3. Al terminar una fase, sugiere `/clear` y volver a escribir `/recorrido <propiedad>`: el estado está en el archivo, no se pierde nada.
4. Reglas que no se saltan: sonido OFF siempre; nunca `show_generations`; los reintentos van juntos; nada se gasta sin la nota 9 o 10 de la puerta A, la calidad elegida y el "sí" de Enrique al costo. Un hook (`.claude/hooks/guardia-higgsfield.py`) bloquea lo que se salga de estas reglas.
