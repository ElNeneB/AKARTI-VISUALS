# Estado — Prueba de fotograma final (end_image) en DOLLY y AXIS LOCK

**Objetivo:** saber si poner como imagen final un recorte de la misma foto evita que Kling deforme la geometría. Se prueba con el dormitorio del camarote, que el 6/10 necesitó 3 intentos.
**Costo:** 2 clips × 6 créditos = **12 créditos** (std, 4 s, 16:9, sonido OFF).
**Dónde:** Claude Code en tu computadora, en la carpeta del proyecto. Este archivo es el estado de la prueba: la guardia lee sus líneas `puerta_A_nota` y `calidad_kling`.

## Prompt para pegar en Claude Code

```
Haz la prueba de estado-prueba-final.md. Calidad std, apruebo 12 créditos.
1. Descarga la foto del camarote (media 3cab7d35-6d05-424b-974b-c7f00b8b05b4 en Higgsfield) a prueba/camarote.jpg,
   recórtala con `python3 herramientas/akarti.py recorte169` si no es 16:9 y crea el final con
   `python3 herramientas/akarti.py final-push prueba/camarote.jpg prueba/camarote_final.jpg 12`. Sube el final.
2. En un solo generate_video_batch (kling3_0, std, 4 s, 16:9, sound off), con la foto como start_image y el final como end_image:
   - índice 0: el mismo prompt AXIS LOCK + descripción del job 30bfa8f9-781b-408b-b8fa-c2cc78255eaa
   - índice 1: el prompt DOLLY de cocinando-lo-demas
3. Espera una sola vez (sleep 240 y luego jobs_wait). Descarga los 2 clips nuevos y los 2 de control sin final
   (30bfa8f9-781b-408b-b8fa-c2cc78255eaa = AXIS LOCK; d2a7951f-2b25-4728-9e33-91190b7c5f81 = DOLLY).
4. Arma la hoja 2x2 de los 4 con `juez-clip` y júzgalos con akarti-juez-rapido (puerta B).
5. Escribe el resultado abajo, agrega 4 líneas a aprendizajes.md y dime en 5 líneas si el final mejora la geometría.
   Si mejora en los 2 movimientos, cambia "En prueba" por "Confirmado" en cocinando-lo-demas. Si empeora, quita la regla.
```

## Estado de la prueba (lo lee la guardia)

puerta_A_nota: 10
calidad_kling: std
presupuesto_creditos: 12

## Resultado
| Clip | Movimiento | Final | Nota puerta B | Comentario |
|---|---|---|---|---|
| 30bfa8f9 (control) | AXIS LOCK + descripción | No | 5 REPITE (Opus) | ✗2 crítico: de 3,5 s al final la cara inferior de la litera superior pasa de panel blanco liso (foto) a listones de madera oscura. ✗5: no va recto, deriva/gira a la derecha (centro de encuadre 0,50→0,54 a 3,5 s; el cuadro izquierdo sale y entra más puerta). ✗8: casi quieto 0–1,5 s y luego acelera hasta el final (diferencia por cuadro 0,42→4,66), sin 2 s de velocidad constante. Sin reintento: es control de la prueba; su reemplazo es nuevo 0. |
| nuevo 0 | AXIS LOCK + descripción | Sí | 10 PASA (Opus) | Geometría idéntica a la foto (encaje con zoom puro del original: dif. 3,2–3,4 contra 9,7–16,4 del control); bajo la litera sigue panel blanco, sin listones. Recto y centrado (escala 1,00→1,08 a 2 s→1,13 a 3,5 s). Velocidad constante 0–2,5 s y frenada suave al final. Ojo: es casi un zoom 2D sin paralaje y queda casi igual a nuevo 1 (el final manda más que el prompt). |
| d2a7951f (control) | DOLLY | No | 5 REPITE (Opus) | ✗2 crítico: a 3,5–4 s aparecen listones de madera oscura bajo la litera superior, donde la foto muestra panel blanco liso (cambia el material del mueble). Resto bien: avance real con paralaje (dif. contra zoom puro 12–17), recto, velocidad 1,1–1,5 sostenida 1–3,5 s, bordes y color limpios. Sin reintento: es control de la prueba; su reemplazo es nuevo 1. |
| nuevo 1 | DOLLY | Sí | 10 PASA (Opus) | Geometría idéntica a la foto (dif. contra zoom puro 2,2–2,8), panel blanco bajo la litera intacto, puerta de vidrio y escalera rectas. Velocidad perfectamente constante (0,86–0,93 por tramo de 0,5 s), bordes y color limpios. Ojo: avance sin paralaje real (equivale a un zoom de 12 %), menos profundidad que el control. |

## Conclusión (7/10/2026)
El final de 12 % arregla la geometría en los 2 movimientos (controles 5/10 → con final 10/10) pero quita el paralaje: queda casi un zoom y DOLLY y AXIS LOCK salen casi iguales. Decisión: regla "Confirmado solo como red de seguridad" en cuartos con literas o muebles altos; no en todos los clips. Los clips con final salen a 1284x716 (revisar en el montaje). Costo: 12 créditos.

PRUEBA_TERMINADA
