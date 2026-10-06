# Plantilla maestra de Premiere (se arma una sola vez)

Guárdala como `Akarti-Plantilla.prproj` en `Claude-Edicion`. Con esto el editor ya no arma el look, el branding ni el audio en cada video: solo importa el XML de `montaje`, estabiliza y exporta. Son muchas menos llamadas por MCP y todos los videos quedan con el mismo acabado.

## Bins
`01 Clips` · `02 Música` · `03 Room tone` · `04 Branding` · `05 Export`

## Secuencia `Akarti 16x9`
1920x1080, 24 fps (igual que los clips de Kling), píxel cuadrado, audio 48 kHz.

| Pista | Contenido fijo |
|---|---|
| V4 | Marca de agua (demo): PNG con la posición y opacidad aprobadas; se apaga en la versión final |
| V3 | Nombre de la propiedad: título MOGRT discreto con la tipografía de la marca, entrada de 8 cuadros |
| V2 | Capa de ajuste "LOOK" con Lumetri: un preset cálido y otro neutro-fresco (director-akarti) |
| V1 | Vacía: aquí entra el XML de `montaje` |
| A1 | Música (desde el XML) |
| A2 | Room tone (desde el XML, entre −18 y −24 dB por debajo de la música) |
| A3 | Riser o impacto opcional en la apertura y el cierre |
| Master | Loudness Radar o canal con limitador a −1 dBTP; meta de −14 LUFS |

End card de Akarti Visuals (2 a 3 s, con contacto) como PNG o MOGRT en `04 Branding`. `montaje` lo coloca al final si va en `end_card` del JSON.

## Secuencia `Akarti 9x16`
1080x1920, misma estructura, con reencuadre clip por clip (director-akarti). Usar los clips con upscale.

## Preset de exportación `Akarti H.264`
H.264, resolución de la secuencia, VBR 2 pasadas, 16 Mbps objetivo y 20 Mbps máximo (1080p), audio AAC 320 kbps. Guardarlo en Media Encoder con ese nombre.
