#!/bin/bash
# 5 teasers editados en Premiere Pro (por MCP) y la hoja de Drive en verde.
# Uso (Terminal del Mac, dentro de la carpeta del proyecto):   ./akarti-premiere.sh
#
# Propiedades: Amantica Lodge, Casa MYKITA y Casablanca (las secuencias que quedaron a medias
# en el proyecto "casacasa" de Premiere) + Kassa Sunna y Casa Kailani (clips ya pagados).
# Pregunta todo al inicio y después corre sola. Si se corta, vuelve a ejecutarla y retoma.

set -u
cd "$(dirname "$0")" || exit 1
RAMA="claude/credit-consumption-optimization-sxlp0p"
IDS="180|156|121|141|188"
HOJA="https://docs.google.com/spreadsheets/d/1hNzMZOwaPviWK7i57kPDmpZGNrm7OREChj7Ezv5ZYDw/edit"
CORRIDA="corridas/premiere-$(date +%Y%m%d-%H%M)"
mkdir -p "$CORRIDA"
RESUMEN="$CORRIDA/resumen.txt"
decir() { echo "[$(date +%H:%M)] $*" | tee -a "$RESUMEN"; }

# ---------------------------------------------------------------- actualizar y preparar
if [ -z "${AKARTI_ACTUALIZADO:-}" ]; then
  git fetch -q origin "$RAMA" && git checkout -q "$RAMA" && git pull -q --no-rebase --no-edit origin "$RAMA" \
    || echo "Aviso: no pude actualizar la rama; sigo con lo que hay."
  export AKARTI_ACTUALIZADO=1
  exec "$0" "$@"
fi
if ! python3 -c "import PIL" 2>/dev/null; then
  [ -x .venv/bin/python3 ] || python3 -m venv .venv
  .venv/bin/python3 -c "import PIL" 2>/dev/null || .venv/bin/python3 -m pip install -q pillow
fi
[ -x .venv/bin/python3 ] && export PATH="$PWD/.venv/bin:$PATH"

# Contador del tope con el gasto REAL verificado en Higgsfield el 8/10 (168,9 de 700).
# La corrida anterior contaba de más (algunas tandas dos veces); se corrige una sola vez.
python3 - <<'PY'
import json, pathlib
p = pathlib.Path("presupuesto-corrida.json")
d = json.loads(p.read_text()) if p.exists() else {"tope": 700, "comprometido": 0, "historial": []}
if not d.get("recalibrado_8oct"):
    d.update(tope=700, comprometido=168.9, recalibrado_8oct=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1))
PY

# ---------------------------------------------------------------- preguntas (todas aquí)
echo
echo "=== Akarti Visuals · 5 teasers en Premiere ==="
python3 herramientas/corrida.py lista | grep -E "^($IDS)\|" | cut -d'|' -f3 | sed 's/^/  · /'
echo "Créditos disponibles del tope: $(python3 herramientas/corrida.py restante)"
echo
if ! claude mcp list 2>/dev/null | grep -qi premiere; then
  echo "Claude Code (terminal) todavía no tiene el conector de Premiere. Lo importo desde Claude Desktop:"
  claude mcp add-from-claude-desktop
  claude mcp list 2>/dev/null | grep -qi premiere || { echo "Sigue sin aparecer el conector de Premiere. Revísalo y vuelve a ejecutar."; exit 1; }
fi
read -r -p "¿Autorizas TODOS los permisos sin preguntar (la guardia y el tope siguen activos)? (s/n): " OK
[ "$OK" = "s" ] || { echo "Cancelado."; exit 0; }
read -r -p "¿Premiere abierto con el proyecto 'casacasa', Chrome abierto con tu sesión de Google, Mac enchufado y tapa abierta? (s/n): " OK
[ "$OK" = "s" ] || { echo "Prepáralo y vuelve a ejecutar."; exit 0; }
decir "Inicio. Desde aquí no pregunto nada más. Registro: $CORRIDA/"
caffeinate -dimsu -w $$ &

# ---------------------------------------------------------------- Claude (por Headroom si está)
CLAUDE=(claude -p --dangerously-skip-permissions --model sonnet)
if command -v headroom >/dev/null 2>&1; then
  # Misma protección de calidad que akarti-noche.sh: sin comprimir imágenes, MCP, skills ni agentes.
  export HEADROOM_COMPRESSORS="smart_crusher,kompress,code_aware,search,log,tabular,config,html"
  export HEADROOM_EXCLUDE_TOOLS="mcp__*,Skill,Agent,Task"
  CLAUDE=(headroom wrap claude --port 8788 --tool-search true --code-memory none --
          -p --dangerously-skip-permissions --model sonnet)
fi
claude --help 2>/dev/null | grep -q -- "--chrome" && CHROME="--chrome" || CHROME=""

esperar_internet() {
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
    "${CLAUDE[@]}" "$@" < /dev/null > "$CORRIDA/$nombre.log" 2>&1
    codigo=$?
    if grep -qiE "usage limit|limit reached|rate.?limit|resets? (at|in)|overloaded" "$CORRIDA/$nombre.log"; then
      decir "  ⏸ $nombre: límite de uso de Claude. Espero 30 min y reintento ($intento/12)."; sleep 1800; continue
    fi
    if grep -qiE "API Error: 5[0-9][0-9]|connection_error|Failed to connect|nodename nor servname|ENOTFOUND|ECONNREFUSED" "$CORRIDA/$nombre.log"; then
      decir "  ⏸ $nombre: se cortó la conexión. Espero 5 min y reintento ($intento/12)."; sleep 300; continue
    fi
    break
  done
  if [ "$codigo" -eq 0 ]; then decir "  ✓ $nombre — quedan $(python3 herramientas/corrida.py restante) créditos"
  else decir "  ✗ $nombre (código $codigo)"; tail -n 3 "$CORRIDA/$nombre.log" | sed 's/^/      /' | tee -a "$RESUMEN"; fi
}

# ---------------------------------------------------------------- 5 teasers en Premiere
python3 herramientas/corrida.py lista | grep -E "^($IDS)\|" > "$CORRIDA/cola.txt"
while IFS='|' read -r ID SLUG NOMBRE ZONA LINK PERS FOTOS NOTAS; do
  QUEDA=$(python3 herramientas/corrida.py restante)
  if python3 -c "import sys; sys.exit(0 if float('$QUEDA') < 36 else 1)"; then
    decir "Quedan $QUEDA créditos: no alcanza para terminar otro teaser completo. Me detengo, sin dejar nada a medias."; break
  fi
  paso "premiere-$SLUG" \
"Usa la skill automatico en modo teaser y DESATENDIDO (lee config-corrida.md; no hagas ninguna pregunta), pero la EDICIÓN va en Adobe Premiere Pro por MCP (agente akarti-editor, modo PREMIERE), no con 'akarti.py render'. Propiedad: $NOMBRE (hoja $ID, zona $ZONA, personalidad musical $PERS). Link: $LINK. Auditoría previa, fotos a usar: $FOTOS. Notas: $NOTAS. Carpeta: teasers/$SLUG/. Estado: estado-$SLUG.md: si ya existe, RETÓMALO y reutiliza fotos, clips, job_id y upscales ya pagados; no regeneres nada aprobado. Revisa también rescate-6oct/ con 'akarti.py identificar'. Genera en Kling solo lo que falte (un solo batch, sonido OFF). En Premiere trabaja en el proyecto abierto 'casacasa': si ya hay una secuencia de esta propiedad (por ejemplo '<Nombre>_teaser_CLAUDE_v1'), duplícala como v2 y complétala en vez de empezar de cero. Reemplaza el end card viejo (el del WhatsApp en azul) por assets/marca/end-card-16x9.png; marca de agua assets/marca/marca-agua-16x9.png solo sobre los clips; título teasers/$SLUG/titulo.png (créalo con herramientas/marca.py); música de biblioteca/musica según la personalidad y room tone de biblioteca/room-tone; puntos de corte en beat calculados con 'akarti.py montaje'; Warp Stabilizer en cada clip; secuencia 1920x1080. Exporta H.264 1080p a teasers/$SLUG/teaser-$SLUG.mp4, mide con 'akarti.py audio' y pasa la puerta C (nota 9 o 10). Una fila en registro.csv y líneas en aprendizajes.md. Si el MCP de Premiere no responde o falta algo, anótalo en el estado y termina."
done < "$CORRIDA/cola.txt"

# ---------------------------------------------------------------- hoja de Drive en verde
python3 herramientas/corrida.py terminados > "$CORRIDA/terminados.txt"
if [ -s "$CORRIDA/terminados.txt" ]; then
  paso hoja-en-verde --chrome \
"Con Claude in Chrome abre $HOJA (Enrique ya inició sesión en Google) y ve a la pestaña 'Pasaron el check'. Pinta con relleno verde claro la celda del nombre (columna 'Propiedad') de CADA una de estas propiedades, una por línea: $(tr '\n' ';' < "$CORRIDA/terminados.txt"). No cambies ningún texto ni otras celdas. Si un nombre no aparece tal cual, búscalo por las primeras palabras. Al terminar, lista las celdas que pintaste."
fi

python3 herramientas/corrida.py resumen | tee -a "$RESUMEN"
decir "Fin. Teasers en teasers/<propiedad>/ · resumen en $RESUMEN"
