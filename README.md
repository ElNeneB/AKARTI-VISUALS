# Akarti Visuals: flujo de producción

## Cómo se usa
En Claude Code, abierto en esta carpeta:

```
/automatico <propiedad> <carpeta de fotos | link de Airbnb>
```

Hace una sola pregunta al inicio (calidad, presupuesto, datos de edición) y después corre solo. Solo se detiene si:
- el set de fotos no sirve;
- se pasó un link y hay que descargar las fotos;
- el costo supera el presupuesto;
- falta la música;
- Premiere no puede hacer un paso.

Para seguir, se vuelve a escribir el mismo comando.

## Qué hay en cada carpeta

| Ruta | Qué es |
|---|---|
| `.claude/skills/automatico/` | **El prompt único.** Dirige todo el recorrido |
| `.claude/skills/no-gastar/` | Orden fijo de fases y reglas de ahorro |
| `.claude/skills/cocinando-lo-demas/` | Descartes, Lista definitiva, prompts de cámara, inicio seguro |
| `.claude/skills/calidad/` | Reglas de clip de Kling (sonido OFF), batch y espera |
| `.claude/skills/juez-akarti/` | Puertas A, B y C |
| `.claude/skills/director-akarti/` | Edición premium en Premiere |
| `.claude/agents/` | Un agente por fase, cada uno con su modelo |
| `.claude/hooks/guardia-higgsfield.py` | Bloquea envíos fuera de las reglas antes de gastar |
| `.claude/settings.json` | Activa la guardia |
| `herramientas/akarti.py` | Hojas de fotos, hoja 2x2 del juez, recorte 16:9, medición de audio (necesita Python + ffmpeg) |
| `estado-PLANTILLA.md` | Plantilla del archivo de estado de cada propiedad |
| `AHORRO-CREDITOS.md` | La investigación de consumo de créditos (6/10/2026) |

## Flujo

```
/automatico
  └─ Pregunta única: calidad · presupuesto · datos de edición
  └─ 1. akarti-auditor (Opus)    → Lista definitiva + puerta A ≥ 9
  └─ 2. get_cost ≤ presupuesto   → sigue sin preguntar
  └─ 3. akarti-generador (Sonnet) → 1 batch, sonido OFF, 1 espera, hojas 2x2
  └─ 4. akarti-juez (Opus)       → puerta B por clip
  └─ 5. reintentos en 1 batch (máx. 2 por clip; si no aprueba, se descarta y sigue)
  └─ 6. música (ruta, o se detiene con el prompt de Gemini)
  └─ 7. akarti-editor (Sonnet)   → Premiere según director-akarti
  └─ 8. akarti-juez (Opus)       → puerta C + reporte final
```
