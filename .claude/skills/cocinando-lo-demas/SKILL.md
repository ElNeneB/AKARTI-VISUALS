---
name: "cocinando-lo-demas"
description: "Criterios para descartar fotos de una propiedad Airbnb y formato de entrega: veredicto del set, descartes con motivo y tabla Lista definitiva con prompt de cámara por foto."
---

# SKILL COCINANDO LO DEMAS

Usar al auditar el set de fotos de una propiedad para un recorrido de Akarti Visuals (paso 2 y 3 de la skill `no-gastar`).

## Descartes

Descartar por criterio propio, sin pedir permiso, e informar después qué se quitó y por qué:

- Duplicados
- Personas en cuadro
- Espejos como sujeto de la foto
- Distorsión de gran angular
- Iluminación inconsistente
- Tomas aéreas o de dron
- Bodegones (detalles u objetos) sin espacio que recorrer

## Entrega

1. **Primero, el veredicto:** decir si el set sirve o no para un recorrido.
2. **Si sirve:** listar las fotos descartadas, cada una con su motivo.
3. **Después, la tabla "Lista definitiva"** con estas columnas: #, Foto (ID), Espacio, Prompt (DOLLY / ORBIT / AXIS LOCK / CRANE), Recorte 16:9 (Sí / —), Final (Sí / —).

Un clip = una habitación. Nunca planear una transición continua entre cuartos (la IA derrite las paredes).

## Inicio seguro (para no gastar en reintentos)

Antes de elegir los movimientos, leer `aprendizajes.md` y aplicar sus reglas confirmadas y lo que ya pasó o falló en espacios parecidos.

Elegir desde el primer intento la versión que se sabe que aguanta, en vez de esperar al reintento:

- **ORBIT a 20°** si el cuarto tiene camarotes, patrones repetidos, persianas, estanterías, cabeceras con listones o cerámicos con dibujo. El arco de 30° o 45° queda solo para espacios amplios y con pocos patrones. (El 6/10, un ORBIT a 30° deformó y hubo que repetirlo a 20°; los clips que empezaron directo en 20° pasaron sin reintentos.)
- **AXIS LOCK con descripción del cuarto** en cuartos chicos o con muebles altos (camarotes, roperos grandes): poner al inicio del prompt una frase breve con los materiales, los muebles principales y las ventanas o puertas reales del cuarto, en positivo, antes del texto fijo de AXIS LOCK. (El 6/10, el dormitorio del camarote necesitó 3 intentos.)
- En la tabla, marcar estos clips en la columna de prompt como "ORBIT 20°" o "AXIS LOCK + descripción", con la frase de descripción escrita.

## Fotograma final (DOLLY y AXIS LOCK)

Kling 3.0 acepta una imagen de inicio y una final por el mismo precio. En DOLLY y AXIS LOCK se pasa como final un recorte centrado de la **misma** foto, un 12 % más cerrado (`python3 herramientas/akarti.py final-push FOTO_169.jpg FINAL.jpg 12`). Así Kling solo interpola un avance entre dos imágenes reales y la geometría queda anclada. Marcar "Sí" en la columna Final.

- En ORBIT y CRANE va sin final, porque la vista cambia de lado o de altura y un recorte no la representa.
- **En prueba desde el 6/10:** el juez anota en `aprendizajes.md` cada clip con final. Si un DOLLY o AXIS LOCK con final deforma o queda sin movimiento, el reintento se hace sin final (o con 8 %), y se anota.

## Prompts de cámara

Solo se usan estos cuatro movimientos. Formular todo en positivo (Kling 3.0 no tiene negative prompt; las negaciones empeoran el resultado). Nunca usar "first-person".

DOLLY:
Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

ORBIT (el arco es el dial: 45° más movimiento, 30° equilibrio, 20° si se deforman patrones repetidos):
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a wide 45 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

AXIS LOCK:
Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

CRANE (aún sin validar en la práctica):
Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a motorized vertical column crane, its base bolted flat to the floor. The camera body physically rises straight upward along that column at continuous linear speed, gaining height while the lens stays frozen pointing dead ahead, zero pitch, zero tilt, the optical axis stays perfectly horizontal and parallel to the floor for the entire shot, horizon locked dead level. The camera holds one fixed horizontal position, no forward or sideways travel, pure vertical translation only. As the camera gains height the beamed ceiling progressively enters the top of frame while the floor exits the bottom. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear. Ground-mounted machine-driven camera path, empty unoccupied room, solid static architecture, single room, one continuous shot.