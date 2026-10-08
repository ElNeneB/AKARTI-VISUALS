# Pendiente: playa-luminosa

- 2026-10-07: En gemini.google.com (sesión iniciada) se activó "Create music" y se envió el prompt exacto de playa-luminosa.
- Gemini se quedó en "Generating your track" más de 4 minutos sin entregar audio. Al recargar, el chat ya no existía ("Couldn't load this chat. It doesn't exist or was deleted"), así que no hubo nada que descargar.
- No se creó `playa-luminosa.mp3` ni se agregó fila a `indice.csv`.
- Para retomar: repetir la generación a mano en Gemini (Create music) con el prompt de `prompts-gemini.md`, guardar como `biblioteca/musica/playa-luminosa.mp3`, correr `python3 herramientas/akarti.py bpm biblioteca/musica/playa-luminosa.mp3` y agregar la fila (licencia=Gemini).

# Pendiente: moderno-urbano

- 2026-10-07: En gemini.google.com (sesión iniciada) se activó "Create music" y se envió el prompt exacto de moderno-urbano (110 BPM, F minor).
- Gemini estuvo en "Generating your track" unos 6 minutos y terminó con el error "Something went wrong while trying to generate the music. Please try again." No hubo audio que descargar.
- No se creó `moderno-urbano.mp3` ni se agregó fila a `indice.csv`.
- Para retomar: repetir la generación a mano en Gemini (Create music) con el prompt de `prompts-gemini.md` (sección moderno-urbano), guardar como `biblioteca/musica/moderno-urbano.mp3`, correr `python3 herramientas/akarti.py bpm biblioteca/musica/moderno-urbano.mp3` y agregar la fila (licencia=Gemini).
