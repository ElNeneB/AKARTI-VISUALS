# Akarti Visuals

Recorridos en video con IA para propiedades de Airbnb (Kling 3.0 en Higgsfield + Premiere Pro).

## Un solo prompt
`/automatico <propiedad> <carpeta de fotos | link de Airbnb>` produce el recorrido de punta a punta (skill `.claude/skills/automatico`). Si la corrida se detiene, el mismo comando la retoma desde `estado-<propiedad>.md`.

## Reglas que no se saltan
- Kling 3.0: calidad elegida por Enrique (std por defecto), 16:9, 4 s, **sonido OFF**, un clip por habitación.
- Nada se genera sin la puerta A con nota 9 o 10, la calidad elegida y el presupuesto aprobado (`estado-<propiedad>.md`). El hook `.claude/hooks/guardia-higgsfield.py` lo hace cumplir.
- Un solo batch para los clips y otro para los reintentos; una sola espera; nunca `show_generations`.
- Imágenes: hojas de 6 fotos y hoja 2x2 por clip (`herramientas/akarti.py`), nunca en el chat principal.
- Cada fase en su agente (`.claude/agents/`): auditor con Opus; generador, editor y juez rápido con Sonnet; juez de Opus solo para los clips en la frontera y la puerta C.
- DOLLY y AXIS LOCK llevan fotograma final (`final-push`, en prueba). Upscale a 1080p solo de los clips aprobados.
- Memoria en `aprendizajes.md`, música y room tone de `biblioteca/`, montaje con `akarti.py montaje` sobre la plantilla maestra, costo por video en `registro.csv`.
- Tope por corrida en `presupuesto-corrida.json` (la guardia bloquea lo que lo pase). Corrida nocturna: `./akarti-noche.sh`, modo desatendido con `config-corrida.md`.
- Marca: Cormorant Garamond + Jost; carbón, hueso y champán; nada de azul eléctrico (`assets/marca/`).
- Si cambias una skill aquí, cámbiala también en claude.ai (o vuelve a subir su `.skill`).
