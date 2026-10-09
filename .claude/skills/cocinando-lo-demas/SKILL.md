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
3. **Después, la tabla "Lista definitiva"** con estas columnas: #, Foto (ID), Espacio, Prompt (DOLLY / ORBIT / AXIS LOCK / CRANE, con arco y sentido si es ORBIT), Familia (Avance / Lateral / Vertical), Por qué este movimiento (una línea), Recorte 16:9 (Sí / —), Final (Sí / —).
4. **Debajo de la tabla, la línea "Secuencia de movimientos"** con el orden de los clips, por ejemplo: `ORBIT 30° izq→der · AXIS LOCK · ORBIT 30° der→izq · DOLLY`. Antes de entregar, revisarla contra las reglas de ritmo de abajo. Si alguna falla, se corrige la tabla antes de entregarla.

Un clip = una habitación. Nunca planear una transición continua entre cuartos (la IA derrite las paredes).

## Ritmo de movimientos (regla obligatoria en teasers y videos)

Un video donde todos los clips se mueven igual se siente automático y delata la IA. El movimiento se elige por espacio, pero el conjunto tiene que alternar.

### Las tres familias

Para el ojo del espectador, lo que cuenta es hacia dónde viaja la cámara, no el nombre del prompt. DOLLY y AXIS LOCK avanzan los dos hacia adelante: son la misma familia y en pantalla se ven como el mismo movimiento.

| Familia | Movimiento | Qué siente el espectador | Mejor en | Evitar en |
|---|---|---|---|---|
| Avance | AXIS LOCK | Entrar al espacio, profundidad, recorrido | Salas o terrazas largas, pasillos, cocinas lineales, cualquier cuarto con un punto de fuga claro al fondo (ventana, vista) | Cuartos chicos con una pared cerca: no hay hacia dónde avanzar |
| Avance (pausa) | DOLLY | Respiro, casi quieto, contemplar | Dormitorios, baños, detalles con espacio, el plano antes del end card | La apertura: en los primeros 3 s se siente estático |
| Lateral | ORBIT | Volumen y paralaje: el espacio "se abre" alrededor de un objeto | Sala con sofá o mesa central, comedor, cama, piscina o jacuzzi | Espacios sin objeto central; con patrones repetidos bajar el arco (30° → 20°) |
| Vertical | CRANE | Revelación y escala: aparecen techo, vigas, altura | Techos altos con vigas, doble altura, fachadas | Techos bajos o planos. Aún sin validar: máximo 1 por video |

### Reglas

1. **Nunca dos clips seguidos de la misma familia.** DOLLY seguido de AXIS LOCK (o al revés) es una repetición.
2. **Ningún movimiento ocupa más de la mitad de los clips.** En un video de 4 clips, máximo 2 de cada uno. Excepción: en un teaser de 3 clips (el formato del modo automático) se permiten 2 ORBIT solo si van en sentidos opuestos y con otro movimiento en medio.
3. **Teaser o video de 4 clips o más: usar al menos 3 movimientos distintos** y las dos familias validadas (Avance y Lateral).
4. **Dos ORBIT en el mismo video van en sentidos opuestos.** El primero de izquierda a derecha; el siguiente de derecha a izquierda (variante abajo). Si hay un tercero, vuelve a izquierda a derecha con otro arco.
5. **La apertura nunca es DOLLY.** El primer clip lleva ORBIT o AXIS LOCK, que son los que tienen energía.
6. **El orden de los espacios no se cambia para cumplir el ritmo** (lo manda el recorrido lógico). Se cambia el movimiento del clip que rompe la regla, eligiendo el segundo movimiento que mejor le sirve a ese espacio según la tabla.
7. **Si un reintento del juez cambia el movimiento de un clip**, volver a revisar la Secuencia de movimientos con sus vecinos. Si el cambio crea una repetición de familia, el reintento usa ORBIT a 20° en vez de AXIS LOCK.

### Patrón base para empezar

Alternar Lateral y Avance, y dejar DOLLY como pausa (en los clips de Avance con final, el movimiento sale casi un zoom de 12 %: otra razón para no usar final donde no hace falta):

- 3 clips (teaser): ORBIT 30° izq→der · AXIS LOCK · ORBIT 30° der→izq. Alternativa si el espacio del medio no sirve para AXIS LOCK: AXIS LOCK · ORBIT 30° · DOLLY
- 4 clips: ORBIT 30° izq→der · AXIS LOCK · ORBIT 30° der→izq · DOLLY
- 5 clips: AXIS LOCK · ORBIT 30° izq→der · DOLLY · ORBIT 30° der→izq · AXIS LOCK
- 6 clips con techo alto: ORBIT 30° izq→der · AXIS LOCK · CRANE · ORBIT 30° der→izq · DOLLY · ORBIT 20° izq→der

8. **Inicio seguro y ritmo conviven.** El "Inicio seguro" decide el arco (ORBIT 20°) y la descripción del cuarto; el ritmo decide la familia. Si un cuarto chico obliga a AXIS LOCK + descripción y su vecino también es de la familia Avance, primero se cambia el movimiento del vecino. Si el vecino no admite otro movimiento, se deja y se escribe "excepción por inicio seguro" junto a la Secuencia de movimientos; el juez la acepta con esa nota.

El patrón es un punto de partida: si un espacio pide otro movimiento según la tabla, se ajusta mientras se cumplan las 8 reglas.

## Inicio seguro (para no gastar en reintentos)

Antes de elegir los movimientos, leer `aprendizajes.md` y aplicar sus reglas confirmadas y lo que ya pasó o falló en espacios parecidos.

Elegir desde el primer intento la versión que se sabe que aguanta, en vez de esperar al reintento:

- **ORBIT a 20°** si el cuarto tiene camarotes, patrones repetidos, persianas, estanterías, cabeceras con listones o cerámicos con dibujo. El arco de 30° o 45° queda solo para espacios amplios y con pocos patrones. (El 6/10, un ORBIT a 30° deformó y hubo que repetirlo a 20°; los clips que empezaron directo en 20° pasaron sin reintentos.)
- **AXIS LOCK con descripción del cuarto** en cuartos chicos o con muebles altos (camarotes, roperos grandes): poner al inicio del prompt una frase breve con los materiales, los muebles principales y las ventanas o puertas reales del cuarto, en positivo, antes del texto fijo de AXIS LOCK. (El 6/10, el dormitorio del camarote necesitó 3 intentos.)
- En la tabla, marcar estos clips en la columna de prompt como "ORBIT 20°" o "AXIS LOCK + descripción", con la frase de descripción escrita.

## Fotograma final (DOLLY y AXIS LOCK)

Kling 3.0 acepta una imagen de inicio y una final por el mismo precio. Se pasa como final un recorte centrado de la **misma** foto, un 12 % más cerrado (`python3 herramientas/akarti.py final-push FOTO_169.jpg FINAL.jpg 12`). Así Kling solo interpola un avance entre dos imágenes reales y la geometría queda anclada. Marcar "Sí" en la columna Final.

**Confirmado con límite (prueba del 7/10, camarote, 12 créditos):** con final, DOLLY y AXIS LOCK pasaron de 5/10 a 10/10 (sin final, aparecían listones bajo la litera), pero el movimiento queda casi un zoom de 12 % sin paralaje y los dos salen casi iguales. Por eso:

- **Usar final solo en cuartos con camarotes, muebles altos o patrones que ya deformaron** (la red de seguridad).
- En cuartos amplios y sin riesgo, DOLLY y AXIS LOCK van sin final para conservar el avance con profundidad.
- Los clips con final salen a 1284x716: revisar en el montaje.

- En ORBIT y CRANE va sin final, porque la vista cambia de lado o de altura y un recorte no la representa.
- El juez anota en `aprendizajes.md` cada clip con final. Si un DOLLY o AXIS LOCK con final deforma o queda sin movimiento, el reintento se hace sin final (o con 8 %), y se anota.

## Prompts de cámara

Solo se usan estos cuatro movimientos. Formular todo en positivo (Kling 3.0 no tiene negative prompt; las negaciones empeoran el resultado). Nunca usar "first-person".

DOLLY:
Architectural visualization render, Unreal Engine cinematic style, interior real estate, single continuous room, no scene transition. Locked-off tripod camera on a rigid mount, axis lock, perfectly level horizon, minimal controlled forward creep, zero vertical movement, zero horizontal drift, no walking motion, no handheld shake, no breathing motion, rigid stable framing throughout, 8k resolution, photorealistic.

ORBIT (el arco es el dial: 45° más movimiento, 30° equilibrio, 20° si se deforman patrones repetidos):
Architectural visualization render of a luxury interior, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: a robotic motion-control arm mounted on a physical circular rail bolted to the floor. The camera body physically travels sideways along the curved rail from left to right, covering a wide 45 degree arc, while the lens simultaneously yaws in the opposite direction to keep the central subject pinned dead center in frame. The radius between lens and subject stays constant for the entire shot, the camera stays at one fixed height, horizon locked dead level, all motion confined to the horizontal plane. Strong parallax: foreground objects sweep across frame faster than the back wall, revealing new sightlines and spatial depth. Continuous linear speed on rails, empty unoccupied room, solid static architecture, single room, one continuous shot.

ORBIT, variante de sentido (der→izq): el mismo prompt, cambiando solo "from left to right" por "from right to left". Nada más del texto se toca.

AXIS LOCK:
Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a heavy steel dolly riding a single perfectly straight rail bolted flat to the floor. The camera body physically translates forward along that rail at continuous linear speed, tracking a dead straight line into the space. The lens stays frozen pointing dead ahead for the entire shot, zero yaw, the optical axis stays perfectly parallel to the rail, the camera holds one fixed height above the floor, horizon locked dead level, every frame keeps the exact same angle as the first. Vanishing point stays pinned to the same spot in frame throughout. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear, no new objects are introduced. Ground-mounted machine-driven camera path, empty unoccupied space, solid static architecture, single room, one continuous shot.

CRANE (aún sin validar en la práctica):
Architectural visualization render, Unreal Engine 5 path-tracing, volumetric lighting, sharp focus, 8k. Camera motion: the camera is bolted to a motorized vertical column crane, its base bolted flat to the floor. The camera body physically rises straight upward along that column at continuous linear speed, gaining height while the lens stays frozen pointing dead ahead, zero pitch, zero tilt, the optical axis stays perfectly horizontal and parallel to the floor for the entire shot, horizon locked dead level. The camera holds one fixed horizontal position, no forward or sideways travel, pure vertical translation only. As the camera gains height the beamed ceiling progressively enters the top of frame while the floor exits the bottom. The scene preserves the exact geometry, materials, colors and object placement of the source image, walls and furniture keep their original shape and position, no new rooms or openings appear. Ground-mounted machine-driven camera path, empty unoccupied room, solid static architecture, single room, one continuous shot.