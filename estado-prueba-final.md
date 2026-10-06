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
| 30bfa8f9 (control) | AXIS LOCK + descripción | No | | |
| nuevo 0 | AXIS LOCK + descripción | Sí | | |
| d2a7951f (control) | DOLLY | No | | |
| nuevo 1 | DOLLY | Sí | | |
