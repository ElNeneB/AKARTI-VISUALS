---
name: juez-akarti
description: "Juez de calidad de Akarti Visuals: califica de 1 a 10 la Lista definitiva, cada clip generado y el video final con 10 criterios verificables, y decide si se avanza (9 o 10), se repite mejor o se descarta. Usar siempre que haya que aprobar trabajo de un recorrido antes de pasar a la siguiente etapa, en modo manual o dentro de la skill automatico."
---

# Juez de calidad de Akarti Visuals

Se usa en tres puertas del flujo: después de armar la Lista definitiva (puerta A), después de generar cada clip (puerta B) y después de exportar el video (puerta C). Nada pasa a la siguiente etapa sin nota aprobatoria.

## Cómo se calcula la nota

- Cada puerta tiene 10 criterios. Cada criterio cumplido suma 1 punto.
- **Aprueba con 9 o 10** (más de 8). Con 8 o menos se repite.
- Los criterios marcados **(crítico)** hunden la nota: si uno falla, la nota máxima es 5, aunque el resto esté perfecto.
- Cada criterio necesita evidencia concreta: el segundo del clip, el nombre del fotograma, la fila de la tabla o el valor medido. **Un criterio que no se pudo verificar cuenta como fallo**, nunca como acierto. Esto evita que el juez se apruebe a sí mismo por defecto.

## Puerta A — Lista definitiva (antes de gastar créditos)

1. El veredicto del set está escrito explícitamente (sirve / no sirve).
2. Cada foto descartada tiene su motivo, tomado de los criterios de `cocinando-lo-demas`.
3. **(crítico)** Ninguna foto que sigue en la lista cae en un criterio de descarte.
4. **(crítico)** Un clip = una habitación; ningún clip plantea una transición entre cuartos.
5. Solo se usan DOLLY, ORBIT, AXIS LOCK o CRANE, con el prompt tal cual está en `cocinando-lo-demas` (la variante de sentido del ORBIT cuenta como válida).
6. **(crítico)** La línea "Secuencia de movimientos" cumple las reglas de ritmo de `cocinando-lo-demas`: nunca dos clips seguidos de la misma familia (DOLLY y AXIS LOCK son la misma familia, Avance), ningún movimiento en más de la mitad de los clips (excepción de teaser de 3 clips con dos ORBIT opuestos), al menos 3 movimientos distintos si hay 4 clips o más, dos ORBIT en sentidos opuestos y apertura sin DOLLY. Una "excepción por inicio seguro" escrita junto a la línea se acepta. Si la línea no está, cuenta como fallo (el orden de los espacios lo manda el criterio 7).
7. El orden sigue el recorrido lógico: entrada o exterior → sala → comedor → cocina → dormitorios → baños → terraza o piscina.
8. Cada movimiento tiene una línea que justifica por qué sirve para ese espacio.
9. Las fotos verticales están marcadas con "Sí" en Recorte 16:9.
10. Está identificado el plano más fuerte para la apertura del video.

## Puerta B — Cada clip generado

Revisar los fotogramas de 0,5 s, 2 s y 3,5 s junto a la foto original en **una sola imagen**: la hoja 2x2 que arma `python3 scripts/akarti.py juez-clip CLIP.mp4 FOTO.jpg` (arriba: foto | 0,5 s; abajo: 2 s | 3,5 s). Nunca mostrar los 4 cuadros como imágenes separadas. Si hay que juzgar varios clips, conviene hacerlo en un subagente que devuelva solo la nota y los criterios que fallan, para que las imágenes no se queden en el chat principal. Si un criterio no se puede decidir con la hoja, se abre en grande solo el cuadro en duda.

Los clips vienen sin sonido (sonido OFF, ver `calidad`). El audio se revisa recién en la puerta C.

**Juez en dos niveles (puerta B):** la primera revisión de cada clip la hace Sonnet (agente `akarti-juez-rapido`). Opus (agente `akarti-juez`) solo vuelve a juzgar los clips en la frontera: nota 8 o 9, o con algún criterio que quedó sin verificar. Una nota de 10, o una de 7 o menos, la decide Sonnet. Los criterios y la regla de evidencia son los mismos en los dos niveles.

**Memoria:** después de la puerta B, agregar una línea por clip en `aprendizajes.md` con: fecha, propiedad, espacio y rasgos (tamaño, muebles altos, patrones), movimiento, si llevó final, nota y resultado.

1. **(crítico)** Paredes, marcos y líneas rectas no ondulan ni se doblan.
2. **(crítico)** Muebles y objetos no se derriten, no cambian de forma ni de lugar.
3. **(crítico)** No aparecen personas, animales ni objetos nuevos.
4. **(crítico)** Es la misma habitación de la foto: no aparecen cuartos, puertas ni ventanas nuevas.
5. El movimiento coincide con el prompt: DOLLY avanza, ORBIT muestra paralaje, AXIS LOCK va recto sin girar, CRANE sube sin inclinar el lente.
6. El horizonte se mantiene nivelado.
7. No hay temblor, respiración ni micro-saltos visibles.
8. Queda un tramo útil de velocidad constante de al menos 2 s después de recortar arranque y frenada.
9. Los bordes del encuadre se ven limpios, sin zonas borrosas inventadas.
10. Color y luz se mantienen fieles a la foto original.

## Puerta C — Video final exportado

1. **(crítico)** Ningún clip del montaje tiene deformaciones.
2. Las líneas arquitectónicas se ven rectas en todos los clips.
3. El color es consistente entre clips.
4. Los cortes caen sobre tiempos fuertes de la música.
5. No se ven arranques ni frenadas de cámara.
6. El audio no tiene pops, voces ni golpes generados por la IA.
7. Loudness integrado entre -15 y -13 LUFS y true peak de -1 dBTP o menos, medido (no estimado) con `python3 scripts/akarti.py audio VIDEO.mp4`.
8. Branding correcto: nombre de la propiedad al inicio y end card de Akarti Visuals con contacto.
9. **(crítico)** Marca de agua presente si es demo o teaser; ausente si es la versión final pagada.
10. Duración, formato y resolución dentro de lo pedido, y el plano más fuerte aparece en los primeros 3 s.

## Qué hacer según la nota

- **9 o 10: PASA.** Se avanza a la siguiente etapa.
- **8 o menos: REPITE.** El reintento tiene que cambiar algo dirigido al criterio que falló; repetir lo mismo da el mismo resultado. Máximo 2 reintentos por pieza.
- **Tras 2 reintentos sin aprobar: DESCARTAR o ESCALAR.** En modo manual se le informa a Enrique. En modo automático la pieza se marca y la corrida sigue con lo demás.

### Escalera de reintentos para clips (puerta B)

Cada reintento gasta créditos, así que antes de repetir se confirma que queda presupuesto aprobado. Se juzgan primero todos los clips del batch y después **todos los reintentos van juntos en un solo batch** (ver `calidad`), nunca uno por uno.

- ORBIT con deformación de patrones o muebles: arco 45° → 30° → 20°.
- DOLLY, AXIS LOCK o CRANE con geometría deformada: reintento 1 cambia a AXIS LOCK; reintento 2 agrega al inicio del prompt una descripción breve de la habitación real (materiales, muebles principales, ventanas), porque describir el cuarto ancla la escena.
- Movimiento nulo o equivocado: reintento 1 reescribe la parte de cámara describiendo la traslación física (riel, columna); reintento 2 cambia a AXIS LOCK.
- Antes de cambiar a AXIS LOCK, revisar los clips vecinos en la Secuencia de movimientos. Si algún vecino es de la familia Avance (DOLLY o AXIS LOCK), el cambio usa ORBIT a 20° en vez de AXIS LOCK, para no romper el ritmo. Todo cambio de movimiento actualiza la Secuencia de movimientos.
- Todo en positivo: nunca agregar negaciones al prompt para "corregir" (Kling 3.0 no tiene negative prompt).

### Reintentos en puertas A y C

No gastan créditos. En la puerta A se corrigen las filas que fallaron. En la puerta C se corrige la edición (cortes, niveles, color, marca de agua) sin regenerar clips, salvo que el fallo sea un clip deformado: ese clip vuelve a la puerta B.

## Formato de salida (corto, para gastar menos)

Se escriben solo los criterios que **fallan**, con su evidencia. Los aprobados van en una línea con sus números. La regla de evidencia no cambia: un criterio que no se pudo verificar cuenta como fallo y se escribe.

```
JUEZ — Puerta [A/B/C] — [propiedad] — [pieza]
Nota: X/10 → PASA / REPITE (intento n de 2) / DESCARTAR
✓ 1, 2, 3, 5, 6, 7, 9, 10
✗ 4. [criterio] — evidencia (segundo, fotograma o fila)
Cambio para el reintento: [qué se modifica y por qué] (solo si repite)
```

En la puerta B, la nota de cada clip se anota también en la columna "Puerta B" de `estado-<propiedad>.md`.
