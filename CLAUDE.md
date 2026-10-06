# Akarti Visuals: reglas de trabajo

Recorridos en video con IA para propiedades de Airbnb. Las reglas completas están en `skills/` (copias de las skills de claude.ai: `no-gastar`, `cocinando-lo-demas`, `calidad`, `juez-akarti`, `director-akarti`). Si cambias una, cambia también la de claude.ai.

## Reglas de ahorro (siempre)
- **Un chat por fase** (auditoría → generación → Premiere). El estado de cada propiedad vive en `estado-<propiedad>.md` (plantilla: `estado-PLANTILLA.md`). Al terminar una fase, actualizar el archivo y pedir un chat nuevo.
- **Kling 3.0: std, 16:9, 4 s, sonido OFF** (`sound: "off"`, 6 créditos por clip). Preguntar siempre la calidad antes de generar y sacar el costo con `get_cost: true`.
- **Un solo `generate_video_batch`**, terminar el turno y esperar el "listo" de Enrique; **una** llamada a `jobs_wait`. Nunca `show_generations`. Los reintentos van todos juntos.
- **Imágenes:** auditar con `python3 herramientas/akarti.py hoja-fotos`, juzgar clips con `juez-clip` (hoja 2x2), medir audio con `audio`. Nunca 4 imágenes por clip.
- **Inicio seguro:** ORBIT 20° con camarotes o patrones repetidos; AXIS LOCK + descripción del cuarto en cuartos chicos.
- **Modelo:** Opus para auditar y juzgar; Sonnet para subir, generar y Premiere.
- **Respuestas cortas:** el juez escribe solo los criterios que fallan; el director no escribe "prompt para Claude Code" si el mismo Claude ejecuta.
