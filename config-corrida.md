# Configuración de la corrida desatendida (respuestas de Enrique del 6/10/2026)

`/automatico` en modo **desatendido** toma de aquí todas las respuestas del Paso 0 y **no pregunta nada**. Si algo lo bloquea, lo anota en el estado de la propiedad y termina, y la corrida sigue con la siguiente.

- **Calidad Kling:** std · 16:9 · 4 s · sonido OFF.
- **Tope total de créditos de Higgsfield:** 700 para todo (pendientes + teasers + producto final). Lo controla `presupuesto-corrida.json` con la guardia. **No empezar** una propiedad si lo que queda no alcanza para terminarla completa (reserva de 36 créditos por teaser). Nunca dejar trabajo a medias.
- **Modo:** teaser (los 3 espacios más fuertes, con movimientos distintos; unos 12 a 15 s con el end card).
- **Versión:** demo con marca de agua **diagonal repetida al 10 %** (`assets/marca/marca-agua-16x9.png`).
- **End card:** `assets/marca/end-card-16x9.png` (AKARTI · REAL ESTATE VISUALS · TU PROPIEDAD, EN MOVIMIENTO. · WhatsApp +51 908 812 483). Paleta carbón, hueso y champán; Cormorant Garamond + Jost. Nada de azul eléctrico.
- **Título:** nombre corto de la propiedad + zona, con `python3 herramientas/marca.py titulo "Nombre" "Zona" teasers/<slug>/titulo.png`.
- **Edición:** render automático con `python3 herramientas/akarti.py render` (sin Premiere).
- **Música:** biblioteca creada en Gemini (`biblioteca/musica/indice.csv`), elegida por personalidad. Si no hay pista, render sin música y anotarlo.
- **Room tone:** `biblioteca/room-tone/` (sintético: interior, ciudad, mar), entre −20 y −24 dB por debajo de la música.
- **Upscale:** 1080p, solo de los clips aprobados.
- **Salida:** `teasers/<slug>/teaser-<slug>.mp4` + `estado-<slug>.md` + una fila en `registro.csv`.
