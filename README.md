# Akarti Visuals: flujo de producción

## Cómo se usa
En Claude Code, abierto en esta carpeta:

```
/automatico <propiedad> <carpeta de fotos | link de Airbnb> [teaser]
```

Con `teaser` hace solo 3 clips y un video de unos 15 s con marca de agua, para prospectos que todavía no pagan.

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
| `.claude/agents/` | Un agente por fase, cada uno con su modelo (el juez en dos niveles: Sonnet y, para los casos de frontera, Opus) |
| `.claude/hooks/guardia-higgsfield.py` | Bloquea envíos fuera de las reglas antes de gastar |
| `.claude/settings.json` | Activa la guardia |
| `herramientas/akarti.py` | Filtro de fotos, hojas de fotos, recorte 16:9, fotograma final, hoja 2x2 del juez, BPM, montaje XML con cortes en beat, medición de audio y registro de costos (necesita Python + ffmpeg) |
| `aprendizajes.md` | Memoria de qué movimiento funciona en qué tipo de espacio |
| `biblioteca/` | Índice de música (con BPM) y room tone |
| `plantilla-premiere.md` | Cómo armar una sola vez la plantilla maestra de Premiere |
| `registro.csv` | Costo real por video (se crea en la primera corrida) |
| `estado-prueba-final.md` | Prueba pendiente del fotograma final (12 créditos) |
| `estado-PLANTILLA.md` | Plantilla del archivo de estado de cada propiedad |
| `AHORRO-CREDITOS.md` | La investigación de consumo de créditos (6/10/2026) |

## Flujo

```
/automatico
  └─ Pregunta única: calidad · presupuesto · datos de edición
  └─ 1. akarti-auditor (Opus)    → filtro de fotos + aprendizajes → Lista definitiva + puerta A ≥ 9
  └─ 2. get_cost ≤ presupuesto   → sigue sin preguntar
  └─ 3. akarti-generador (Sonnet) → 1 batch, sonido OFF, final en DOLLY/AXIS, 1 espera, hojas 2x2
  └─ 4. juez-rapido (Sonnet) → puerta B; akarti-juez (Opus) solo en la frontera → aprendizajes
  └─ 5. reintentos en 1 batch (máx. 2 por clip; si no aprueba, se descarta y sigue)
  └─ 5b. upscale a 1080p solo de los clips aprobados (1 batch)
  └─ 6. música de la biblioteca (se detiene solo si falta)
  └─ 7. akarti-editor (Sonnet)   → plantilla + XML con cortes en beat → estabilizar, color, exportar
  └─ 8. akarti-juez (Opus)       → puerta C + reporte final + registro.csv
```
