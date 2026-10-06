# Biblioteca de sonido de Akarti

Quita la única parada de `/automatico` (música) y le da a Akarti un sonido de marca. Los archivos de audio van en tu computadora (no en git, por tamaño y licencias); aquí solo vive el índice.

## Música (`musica/indice.csv`)
6 a 8 pistas instrumentales con licencia comercial, 45 a 90 s, una o dos por personalidad (cálida/rústica, moderna/minimalista, playa/luminosa, lujo/nocturna). Para cada pista nueva:

```
python3 herramientas/akarti.py bpm biblioteca/musica/ARCHIVO.mp3
```

y copia `bpm` y `primer_beat_s` al índice. El editor elige la pista por `personalidad`, y `montaje` corta sobre ese BPM.

## Room tone (`room-tone/indice.csv`)
3 pistas de 60 s o más: interior silencioso, ciudad lejana y mar. Van bajo todo el montaje entre −18 y −24 dB por debajo de la música (los clips de Kling vienen sin sonido).
