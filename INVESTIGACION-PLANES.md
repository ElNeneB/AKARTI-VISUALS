# Investigación: qué plan conviene para automatizar Akarti (Claude vs Codex)

Fecha: 10 de octubre de 2026. Supuesto de volumen (respuesta de Enrique): **10+ recorridos completos por semana**, unos **45 al mes**, de 6 a 8 clips cada uno. Plan actual: **Claude Pro**, que se corta en la ventana de 5 horas. Acepta pagar API por uso si tiene un tope mensual.

Etiquetas: **[DATO]** = verificado en fuente primaria (link en §5) · **[EST]** = estimación con supuestos explícitos · **[OPINIÓN]**.

> Límite de esta investigación: la red de este entorno bloquea `openai.com`, `help.openai.com` y `developers.openai.com`. Los datos de OpenAI salen de los extractos que da el buscador de esas páginas oficiales, no de abrirlas. Están marcados con «(vía buscador)».

---

## 1. Veredicto

**Opción D: Claude Max 5x ($100) usado completo, sin Codex.** Por el mismo precio que A trae **$100 al mes en créditos de API**, que desde el 7-oct-2026 cubren `claude -p` y el Agent SDK, justo lo que usan `akarti-noche.sh` y `akarti-premiere.sh`. Así tienes dos bolsas de uso en un solo ecosistema y no migras nada.

---

## 2. Comparación A / B / C / D (45 recorridos al mes)

| | **A** Max 5x solo | **B** Pro + ChatGPT Plus | **C** Pro + ChatGPT Pro 100 | **D** Max 5x + sus créditos de API |
|---|---|---|---|---|
| Costo fijo al mes | $100 [DATO] | $20 + $20 = $40 [DATO] | $20 + $100 = $120 [DATO, vía buscador] | $100 [DATO] (+ excedente opcional con tope) |
| Capacidad | 5x la sesión de Pro + un límite semanal **sin cifra publicada** [DATO] | Pro (ya te queda corto) + Codex Plus: 15–150 mensajes locales cada 5 h con GPT-6 Sol [DATO, vía buscador] | Pro + Codex Pro 100: sin límite de 5 h, 5x el uso de Plus, tope semanal sin cifra [DATO, vía buscador] | A **más** $100 de API: unas 24 propiedades con el diseño actual o 50–65 optimizado [EST] |
| Compatibilidad con tu pipeline | Total | Parcial: skills portables con cambios; agentes, hook y Chrome hay que rehacerlos | Igual que B | Total. Hay que dar de alta Higgsfield como MCP directo para correr con clave de API |
| Migración | 0 h | 15–30 h [EST] | 15–30 h [EST] | 3–6 h [EST] |
| Mantenimiento al mes | ~1 h | 3–5 h (tres copias de cada skill) [EST] | 3–5 h [EST] | ~1 h [EST] |
| Probabilidad de chocar límites | Media-alta sin optimizar; media optimizado [EST] | Muy alta [EST] | Baja en Codex; media-alta en el lado de Claude Pro [EST] | Baja optimizado; media sin optimizar [EST] |
| Riesgo de romper el pipeline | Bajo | Alto | Alto | Bajo-medio (conectores con clave de API) |

### Por qué no B ni C

- **El cuello de botella está en Claude, no en la falta de un segundo modelo.** Pro ya se agota con 1,5 recorridos en una ventana (6-oct, `AHORRO-CREDITOS.md`). Con B y C, Pro sigue haciendo la auditoría con Chrome y la orquestación.
- **Compatibilidad con Codex** (revisada, no supuesta):
  - **Skills.** Codex lee `SKILL.md` con `name` y `description` desde `.agents/skills` [DATO, vía buscador]. Tus 6 skills son portables, pero hay que cambiarles rutas y referencias a herramientas de Claude.
  - **Agentes.** `.claude/agents/*.md` con `model: opus/sonnet` no sirven. Codex usa TOML en `.codex/agents/` [DATO, vía buscador]. Hay que reescribir los 5 y volver a calibrar el juez con modelos GPT (tus notas 9/10 están afinadas con Claude).
  - **Hook de presupuesto (`guardia-higgsfield.py`).** Codex tiene hooks `PreToolUse` en `.codex/hooks.json` y se pueden poner sobre herramientas MCP [DATO, vía buscador]. Hay dos reportes de terceros en contra: los conectores de ChatGPT aparecen sin el prefijo `mcp__`, así que el filtro nunca saltaría (n8n-io/skills#50), y otro reporte dice que `updatedInput` no se acepta. Si la guardia falla en silencio, se va dinero en Higgsfield.
  - **Higgsfield.** El endpoint `https://mcp.higgsfield.ai/mcp` usa OAuth (fuentes secundarias). Codex soporta MCP por HTTP con OAuth en papel [DATO, vía buscador], pero hay bugs abiertos de inicialización HTTP y OAuth (openai/codex#11284, #20009) y **no hay instrucciones oficiales de Higgsfield para Codex**. Compatibilidad: **no verificada**.
  - **Premiere.** Hoy es un MCP local importado de Claude Desktop (`akarti-premiere.sh`). Si es stdio estándar, se puede declarar en `config.toml` de Codex. Compatibilidad: **probable, no probada**.
  - **Claude in Chrome** (auditoría y música en Gemini): no existe en Codex. Habría que rehacer ese paso.
- **El costo oculto de dos ecosistemas** [OPINIÓN]: hoy ya mantienes dos copias de cada skill (repo y claude.ai, y ya hay una desalineada: ver §2.1). Codex agrega una tercera. Además son dos tableros de límites y dos formatos de hook y de agente, y cada fallo hay que diagnosticarlo en dos lados. Para una persona sola, 3–5 h al mes de mantenimiento valen más que los $20 de diferencia.

### 2.1 Hallazgo de paso
La skill `calidad` subida a claude.ai dice «**con audio**». La del repo dice «**sonido OFF**». Con sonido el clip cuesta 8 créditos en vez de 6 (−25 %, `AHORRO-CREDITOS.md`). Vuelve a subir `skills-empaquetadas/calidad.skill`.

### 2.2 El costo que pesa más que el plan de Claude: Higgsfield
45 recorridos × 7 clips × 6 créditos = 1.890, más 25 % de reintentos ≈ **2.360 créditos al mes** [EST]. El plan Plus trae 1.000 por ciclo (`AHORRO-CREDITOS.md`). Según el blog de Higgsfield, Plus cuesta unos $49 (1.000 créditos) y Ultra unos $129 (3.000 créditos) [no es la página de precios: confírmalo antes de pagar]. **A ese volumen, Higgsfield cuesta más que Claude.**

---

## 3. Mapa de consumo por etapa y top 5 de ahorros

### 3.1 Qué se come el uso, de mayor a menor [EST]

Supuestos:
- Cada llamada a una herramienta reenvía todo el contexto. El piso de Claude Code (sistema, herramientas, CLAUDE.md, skill) son unos 20–30 mil tokens por llamada, y un ~90 % sale de caché.
- Imágenes: ⌈ancho/28⌉ × ⌈alto/28⌉ tokens; los modelos 4.7 y posteriores aceptan hasta 2576 px [DATO].

| # | Etapa | Qué gasta | Peso aprox. | Tipo |
|---|---|---|---|---|
| 1 | 5. Edición en Premiere por MCP | 40–80 llamadas (estabilizar, color y exportar clip por clip), con capturas si el MCP las devuelve, y el contexto crece en cada una | 35–45 % | Casi toda **determinista**: el montaje ya sale de `akarti.py montaje`; Warp Stabilizer y exportación se pueden hacer por ExtendScript/UXP. Solo mirar el color pide criterio |
| 2 | 1. Auditoría con Chrome | Capturas de pantalla: una de 1920×1080 cuesta **2.691 tokens** [DATO] y se vuelve a pagar en cada llamada siguiente; además corre con Opus | 20–30 % | **Mixta**: leer la página y bajar fotos es determinista (`akarti.py airbnb_fotos`, `get_page_text`); decidir si sirve pide criterio |
| 3 | 6. Juez | Reintentos (hasta 2 por pieza) y pase de Opus | 10–15 % | **Criterio**, con chequeos previos deterministas (duración, LUFS con `akarti.py audio`) |
| 4 | Orquestador `automatico` | Contexto largo acumulado entre fases | ~10 % | Determinista en su mayor parte: es una máquina de estados sobre `estado-*.md` |
| 5 | 4. Generación | Subida, batch y `jobs_wait` | 5–10 % | **Determinista** |
| 6 | 2 y 3. Descarte y Lista definitiva | Hojas de 6 (1536×768 = **1.540 tokens** [DATO, fórmula]) | ~5 % | Descarga, deduplicado por hash (`huella`) y recorte son deterministas; el descarte visual y los prompts de cámara piden criterio |

**Costo por propiedad a precio de API** [EST, ±2x]:
- Diseño actual: unos **$3–6**, con 2–4 M de tokens de entrada, casi todos de caché.
- Optimizado: unos **$1–2**.

Precios usados [DATO]:

| Modelo | Entrada | Lectura de caché | Salida |
|---|---|---|---|
| Opus 5.5 | $4 / MTok | $0,20 / MTok | $20 / MTok |
| Sonnet 5.5 | $2 / MTok | $0,10 / MTok | $10 / MTok |
| Haiku 5.5 | $0,10 / MTok | $0,01 / MTok | $0,50 / MTok |

### 3.2 Top 5 de ahorros (sirven con cualquier plan)

| # | Ahorro | Impacto estimado [EST] |
|---|---|---|
| 1 | **Premiere sin bucle del modelo.** `akarti.py montaje` arma el XML y un solo script ExtendScript/UXP importa, aplica Warp Stabilizer a cada clip y exporta con `Akarti H.264`. El modelo solo mira una hoja de fotogramas del resultado para la puerta C. Pasas de 40–80 llamadas a 3–5 | −30 a −40 % del total |
| 2 | **Auditoría sin capturas.** Texto de la página con `get_page_text`, fotos con `akarti.py airbnb_fotos` y el veredicto sobre hojas de 6. 25 fotos sueltas a 1920×1080 son unos 67 mil tokens; en 5 hojas, unos 7,7 mil (**−89 %** en imágenes, por fórmula) | −15 a −25 % |
| 3 | **Jueces y Lista definitiva como script directo a la API** (Messages API con la hoja 2x2 y respuesta JSON con nota y motivo), fuera de Claude Code. Una pasada de juez es la hoja (1.705 tokens) más la skill (unos 2.500): ~$0,01 con Sonnet 5.5 y ~$0,02 con Opus 5.5, **sin** el piso de 20–30 mil tokens de Claude Code. Con Max se paga con los $100 de créditos | −10 a −15 % del uso de la suscripción |
| 4 | **Modelo por tarea.** Haiku 5.5 para orquestador y generador (20 veces más barato que Sonnet por token), Sonnet para el juez rápido y el editor, Opus solo para el veredicto de auditoría, la frontera y la puerta C. Hoy `akarti-noche.sh` usa `--model sonnet` para todo | −10 a −20 % |
| 5 | **Contexto corto.** Un `claude -p` por fase y por propiedad, sin sesiones largas; el estado vive en `estado-*.md`. Las propiedades se agrupan por fase (todas las auditorías, después un batch de generación) y nunca dentro del mismo contexto | −10 a −20 % |

Ya los tienes y hay que mantenerlos: tope de 2 reintentos, un batch y una espera, hojas en vez de fotos sueltas, guardia de presupuesto.

---

## 4. Plan de 30 días

| Semana | Qué hacer | Métrica |
|---|---|---|
| **1** | Pasa a Max 5x. En `akarti-noche.sh` agrega `--output-format json` y guarda `total_cost_usd` por fase en `registro.csv` (es una estimación del cliente, pero sirve para comparar [DATO]). Antes y después de cada propiedad anota el % de `/usage`. Corre 5 recorridos **sin cambios**: es la línea base | % del límite semanal por propiedad y USD equivalente por propiedad |
| **2** | Día 8: reclama los $100 de créditos (piden 7 días en el plan [DATO]) y vincula una organización de Console con **tope de gasto** en el workspace. Aplica los ahorros 1 y 2 | Lo mismo, contra la semana 1. Meta: −40 % |
| **3** | Ahorro 3 (jueces por script con créditos de API) y ahorro 4. Prueba la corrida nocturna con `ANTHROPIC_API_KEY` y Higgsfield dado de alta como MCP directo (`claude mcp add --transport http …`), porque con clave de API los conectores de claude.ai pueden no cargarse: **verificarlo**. Recalibra el juez con 10 clips ya calificados (mismas notas ±1) | Créditos de API por propiedad; coincidencia del juez ≥ 90 % |
| **4** | Semana a volumen real (11 recorridos) | Las tres reglas de abajo |

### Reglas de decisión al día 30
- Si 11 × (% semanal por propiedad) supera el **80 %** del límite semanal, sube a Max 20x ($200, con $200 de API) o pasa más fases a la API.
- Si los créditos de API se acaban antes del día 25, optimiza más o permite excedente con tope (por ejemplo, $30).
- Si la nota media de la puerta C baja de 9 tras los cambios, vuelve a poner Opus solo en el paso que bajó.
- Codex solo vuelve a evaluarse si Higgsfield publica soporte oficial para Codex **y** la semana 4 muestra que Max 20x no alcanza. [OPINIÓN]

---

## 5. Fuentes (consultadas el 10-oct-2026)

**Anthropic**
- Precios de planes: https://claude.com/pricing (la página no tiene fecha)
- Plan Max (5x/20x, $100/$200, sesión de 5 h y límite semanal, sin cifras): https://support.claude.com/en/articles/11049741-what-is-the-max-plan («Updated this week»)
- Claude Code con Pro/Max (límites compartidos, sin estimaciones de prompts u horas): https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan («Updated this week»)
- Créditos de API de Max ($100/$200, para qué sirven y para qué no, vencen cada ciclo, 7 días para reclamar): https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans («Updated this week»)
- Agent SDK y `claude -p` con el plan (actualizaciones del 15-jun-2026 y del 7-oct-2026): https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
- Precios de API por modelo y descuento de Batch: https://platform.claude.com/docs/en/about-claude/pricing
- Costo de imágenes (⌈w/28⌉×⌈h/28⌉, tope de 2576 px): https://platform.claude.com/docs/en/build-with-claude/vision
- `total_cost_usd` en el modo headless: https://code.claude.com/docs/en/headless y https://code.claude.com/docs/en/agent-sdk/cost-tracking

**OpenAI (vía buscador; dominio bloqueado en este entorno)**
- Precios y límites de Codex (Plus: 15–150 mensajes locales cada 5 h con GPT-6 Sol; Pro sin límite de 5 h; página de hace ~7 días, cerca del 3-oct-2026): https://developers.openai.com/codex/pricing
- Niveles de ChatGPT Pro (Pro 100 = 5x Plus; Pro 200 nuevo ≈ 10x según soporte citado en el foro; congelado hasta el 29-oct-2026): https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
- Uso con GPT-6 Astra en Work y Codex: https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex
- Codex con el plan de ChatGPT: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- Skills: https://developers.openai.com/codex/skills · Subagentes: https://developers.openai.com/codex/subagents · Hooks: https://developers.openai.com/codex/hooks · MCP: https://developers.openai.com/codex/config-reference
- Bugs de MCP por HTTP y OAuth: https://github.com/openai/codex/issues/11284 y https://github.com/openai/codex/issues/20009
- Hooks que no saltan con conectores en Codex: https://github.com/n8n-io/skills/issues/50

**Higgsfield (no es la página de precios)**
- https://higgsfield.ai/blog/credits-vs-unlimited-ai-video-generation

**Datos propios del repo**
- `AHORRO-CREDITOS.md` (6-oct-2026): 6 créditos por clip sin sonido, plan Plus de 1.000 créditos, ventana de 5 h agotada con 1,5 recorridos.
- `registro.csv` y `presupuesto-corrida.json`.

### Datos que no están publicados (no se estimaron como hechos)
- Tokens o mensajes por ventana de 5 horas y por semana en Claude Pro y Max.
- Cifra del límite semanal de Codex en Plus y Pro.
- Multiplicador de Pro 500 frente a Plus.
- Si los conectores de claude.ai cargan en `claude -p` cuando corre con `ANTHROPIC_API_KEY`: se prueba en la semana 3.
