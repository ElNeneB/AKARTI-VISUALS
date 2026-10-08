#!/bin/bash
# Corrida desatendida de Akarti Visuals.
# Uso (en la Terminal del Mac, dentro de la carpeta del proyecto):   ./akarti-noche.sh
#
# 1. Pregunta TODO al inicio (tope de créditos, permisos, Mac listo).
# 2. Después corre sola, sin preguntar nada:
#    pendientes (prueba del fotograma final, música en Gemini, rescate de los clips del 6/10)
#    y luego un teaser por propiedad de propiedades-teaser.csv, hasta agotar el tope.
# 3. Si la cortas o se apaga el Mac, vuelve a ejecutarla: retoma donde quedó.

set -u
cd "$(dirname "$0")" || exit 1
RAMA="claude/credit-consumption-optimization-sxlp0p"
CORRIDA="corridas/$(date +%Y%m%d-%H%M)"
mkdir -p "$CORRIDA"
RESUMEN="$CORRIDA/resumen.txt"

decir() { echo "[$(date +%H:%M)] $*" | tee -a "$RESUMEN"; }

# ---------------------------------------------------------------- chequeos
for c in claude ffmpeg ffprobe python3 git caffeinate; do
  command -v "$c" >/dev/null 2>&1 || { echo "Falta '$c'. Instálalo y vuelve a ejecutar (ffmpeg: brew install ffmpeg)."; exit 1; }
done
# Actualizar y volver a arrancar con la versión nueva del script (una sola vez)
if [ -z "${AKARTI_ACTUALIZADO:-}" ]; then
  git fetch -q origin "$RAMA" && git checkout -q "$RAMA" && git pull -q origin "$RAMA" || echo "Aviso: no pude actualizar la rama $RAMA; sigo con lo que hay."
  export AKARTI_ACTUALIZADO=1
  exec "$0" "$@"
fi
# Pillow en un entorno propio del proyecto (.venv): el Python de Homebrew no deja
# instalar paquetes globales (PEP 668) y así no se toca el Python del sistema.
if ! python3 -c "import PIL" 2>/dev/null; then
  [ -x .venv/bin/python3 ] || python3 -m venv .venv || { echo "No pude crear el entorno .venv de Python."; exit 1; }
  .venv/bin/python3 -c "import PIL" 2>/dev/null || .venv/bin/python3 -m pip install -q pillow \
    || { echo "No pude instalar Pillow en .venv (revisa la conexión a internet)."; exit 1; }
fi
# Todo lo que corra después (incluido Claude) usa este python3
[ -x .venv/bin/python3 ] && export PATH="$PWD/.venv/bin:$PATH"
ffmpeg -hide_banner -filters 2>/dev/null | grep -q vidstabdetect || echo "Aviso: tu ffmpeg no tiene vidstab; los teasers saldrán sin estabilizar (brew reinstall ffmpeg lo suele traer)."
claude mcp list 2>/dev/null | grep -qi higgs || echo "Aviso: no veo el conector de Higgsfield en Claude Code. Revisa que estés con tu cuenta de claude.ai (claude /login)."

# ---------------------------------------------------------------- preguntas (todas aquí)
echo
echo "=== Akarti Visuals · corrida desatendida ==="
echo "Pendientes: prueba del fotograma final, música en Gemini, rescate de los clips del 6/10."
echo "Después: teasers de $(python3 herramientas/corrida.py lista | wc -l | tr -d ' ') propiedades pendientes, en orden de precio, hasta agotar el tope."
echo
if [ -f presupuesto-corrida.json ]; then
  echo "Hay una corrida anterior: quedan $(python3 herramientas/corrida.py restante) créditos del tope. Se retoma."
else
  read -r -p "Tope total de créditos de Higgsfield [700]: " TOPE; TOPE=${TOPE:-700}
  printf '{"tope": %s, "comprometido": 0, "historial": []}\n' "$TOPE" > presupuesto-corrida.json
fi
read -r -p "¿Autorizas TODOS los permisos sin preguntar (la guardia y el tope siguen activos)? (s/n): " OK
[ "$OK" = "s" ] || { echo "Cancelado."; exit 0; }
read -r -p "¿Mac enchufado, tapa abierta y Chrome abierto con sesión en gemini.google.com y la extensión Claude in Chrome? (s/n): " OK
[ "$OK" = "s" ] || { echo "Prepáralo y vuelve a ejecutar."; exit 0; }
echo
decir "Inicio. Desde aquí no pregunto nada más. Registro: $CORRIDA/"

caffeinate -dimsu -w $$ &   # el Mac no se duerme mientras corre

CLAUDE=(claude -p --dangerously-skip-permissions --model sonnet)
if command -v headroom >/dev/null 2>&1; then
  # Headroom ahorra tokens comprimiendo lo que Claude lee, pero en esta corrida NO toca
  # lo que define la calidad:
  #  - imágenes (el juez necesita ver las hojas 2x2 sin achicar ni convertir a texto)
  #  - respuestas de Higgsfield y demás MCP (job_id, costos y saldo exactos)
  #  - skills y reportes de los agentes (prompts de cámara y notas tal cual)
  # Read, Grep, Write y Edit ya están protegidos por defecto en Headroom. Lo que sí
  # comprime son los registros largos de Bash (ffmpeg, descargas), donde está el ahorro;
  # si Claude necesita el original, lo recupera con headroom_retrieve.
  export HEADROOM_COMPRESSORS="smart_crusher,kompress,code_aware,search,log,tabular,config,html"
  export HEADROOM_EXCLUDE_TOOLS="mcp__*,Skill,Agent,Task"
  # Puerto propio (8788) para no mezclar esta configuración con tu sesión de 'hc' (8787).
  CLAUDE=(headroom wrap claude --port 8788 --tool-search true --code-memory none --
          -p --dangerously-skip-permissions --model sonnet)
  echo "Headroom activo: la corrida ahorra tokens sin comprimir imágenes, Higgsfield ni skills."
else
  echo "Aviso: no encontré Headroom; la corrida usa Claude directo (sin compresión extra)."
fi
claude --help 2>/dev/null | grep -q -- "--chrome" && CHROME="--chrome" || CHROME=""
esperar_internet() {  # no gastar pasos mientras el Mac no tenga conexión
  local n=0
  until curl -s -m 10 -o /dev/null https://api.anthropic.com; do
    [ $n -eq 0 ] && decir "  ⏸ Sin internet. Espero a que vuelva la conexión…"
    n=$((n+1)); sleep 60
  done
}
paso() {  # paso NOMBRE [--chrome] "PROMPT"
  local nombre="$1"; shift
  if [ "$1" = "--chrome" ]; then shift; [ -n "$CHROME" ] && set -- "$CHROME" "$@"; fi
  decir "▶ $nombre"
  local intento codigo
  for intento in 1 2 3 4 5 6 7 8 9 10 11 12; do
    esperar_internet
    # < /dev/null: que Claude no se coma la cola de propiedades del bucle
    "${CLAUDE[@]}" "$@" < /dev/null > "$CORRIDA/$nombre.log" 2>&1
    codigo=$?
    # Límite de uso de Claude: esperar y repetir la MISMA propiedad (no saltarla)
    if grep -qiE "usage limit|limit reached|rate.?limit|resets? (at|in)|overloaded" "$CORRIDA/$nombre.log"; then
      decir "  ⏸ $nombre: límite de uso de Claude. Espero 30 min y reintento ($intento/12)."
      sleep 1800
      continue
    fi
    if grep -qiE "API Error: 5[0-9][0-9]|connection_error|Failed to connect|nodename nor servname|ENOTFOUND|ECONNREFUSED" "$CORRIDA/$nombre.log"; then
      decir "  ⏸ $nombre: se cortó la conexión. Espero 5 min y reintento ($intento/12)."
      sleep 300
      continue
    fi
    break
  done
  if [ "$codigo" -eq 0 ]; then
    decir "  ✓ $nombre — quedan $(python3 herramientas/corrida.py restante) créditos"
  else
    decir "  ✗ $nombre (código $codigo) — quedan $(python3 herramientas/corrida.py restante) créditos"
    tail -n 3 "$CORRIDA/$nombre.log" | sed 's/^/      /' | tee -a "$RESUMEN"
  fi
}

# ---------------------------------------------------------------- 1. pendientes
grep -q "PRUEBA_TERMINADA" estado-prueba-final.md 2>/dev/null || paso prueba-final \
"Modo desatendido: no hagas preguntas. Haz la prueba descrita en estado-prueba-final.md siguiendo su prompt (calidad std, 12 créditos aprobados). Al terminar escribe la línea PRUEBA_TERMINADA al final del archivo y aplica la conclusión en .claude/skills/cocinando-lo-demas/SKILL.md."

for pista in playa-luminosa campo-calido moderno-urbano lodge-andino; do
  grep -q "^$pista" biblioteca/musica/indice.csv 2>/dev/null || paso "musica-$pista" --chrome \
"Modo desatendido: no hagas preguntas. Con Claude in Chrome abre gemini.google.com (Enrique ya inició sesión) y genera la pista '$pista' con el prompt exacto de biblioteca/musica/prompts-gemini.md (sección $pista). Descarga el audio, muévelo a biblioteca/musica/$pista.mp3 (o la extensión que dé Gemini), mide con 'python3 herramientas/akarti.py bpm' y agrega la fila a biblioteca/musica/indice.csv (archivo,personalidad,bpm,primer_beat_s,duracion_s,licencia=Gemini). Si Gemini no permite crear o descargar música, escribe el motivo en biblioteca/musica/PENDIENTE.md y termina."
done

for t in interior ciudad mar; do
  [ -f "biblioteca/room-tone/$t.wav" ] || python3 herramientas/akarti.py room-tone "$t" "biblioteca/room-tone/$t.wav" 90 >/dev/null
done

[ -f rescate-6oct/LISTO ] || paso rescate-6oct \
"Modo desatendido: no hagas preguntas. Sigue los pasos de rescate-6oct.md: descarga los 15 clips y sus fotos de inicio con curl, arma la hoja 2x2 de cada uno y júzgalos con akarti-juez-rapido (Opus solo en la frontera). Anota la nota de cada uno en la tabla y crea el archivo rescate-6oct/LISTO. No generes nada en Higgsfield."

# ---------------------------------------------------------------- 2. teasers
python3 herramientas/corrida.py lista > "$CORRIDA/cola.txt"
while IFS='|' read -r ID SLUG NOMBRE ZONA LINK PERS FOTOS NOTAS; do
  QUEDA=$(python3 herramientas/corrida.py restante)
  if python3 -c "import sys; sys.exit(0 if float('$QUEDA') < 36 else 1)"; then
    decir "Quedan $QUEDA créditos: no alcanza para terminar otro teaser completo. Me detengo aquí, sin dejar nada a medias."
    break
  fi
  paso "teaser-$SLUG" \
"Usa la skill automatico en modo teaser y DESATENDIDO (lee config-corrida.md; no hagas ninguna pregunta). Propiedad: $NOMBRE (hoja $ID, zona $ZONA, personalidad musical $PERS). Link: $LINK. Auditoría previa, fotos a usar: $FOTOS. Notas: $NOTAS. Carpeta: teasers/$SLUG/. Estado: estado-$SLUG.md (créalo desde estado-PLANTILLA.md con calidad_kling: std y presupuesto_creditos: 36). Antes de generar, revisa con 'akarti.py identificar' si hay clips reutilizables en rescate-6oct/. Resultado: teasers/$SLUG/teaser-$SLUG.mp4, una línea en registro.csv y las líneas de aprendizajes.md. Si algo te bloquea, anótalo en el estado y termina."
done < "$CORRIDA/cola.txt"

# ---------------------------------------------------------------- 3. cierre
python3 herramientas/corrida.py resumen | tee -a "$RESUMEN"
# Sin subir nada a GitHub: la Mac no tiene permiso de escritura y pediría usuario y contraseña.
# Los registros quedan en corridas/ y el resumen en este mismo archivo.
decir "Fin. Teasers en teasers/<propiedad>/ · resumen en $RESUMEN"
