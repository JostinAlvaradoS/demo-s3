# Guion de conducción — Sesión 3

**Repo de demo:** este mismo (`~/dev/demo-s3`). Monorepo de login hecho a medida para la sesión:
`web/` en TypeScript, `api/` en Python, `infra/` en Terraform. Tres stacks que **no comparten
convenciones**, que es justo lo que hace falta para que la jerarquía de memoria y los globs tengan
sentido en vez de ser un ejemplo de juguete.

**Dos avisos de confidencialidad:**

- **Nunca abrir `claude` en el repo del programa durante la sesión:** `MAPA_EVALUACION.md` contiene
  los enunciados del examen.
- **No compartir este repo tal cual con los participantes.** La carpeta `.instructor/` trae los IDs
  de los ítems de examen y sus respuestas. Si querés entregárselo, `rm -rf .instructor` en una copia
  primero.

## Cómo está armado el repo

**Todo está en `main`, ya configurado.** No se escribe nada en vivo: cada artefacto está escrito, se
muestra en pantalla y se explica. Lo que sí es en vivo es el **comportamiento** — `/memory`, la carga
de reglas, el ruteo entre skills. Eso no se puede contar, hay que verlo pasar.

| Qué | Dónde | Qué enseña |
|---|---|---|
| `CLAUDE.md` raíz | raíz | Solo lo transversal, y un `@import` |
| `docs/usuarios-de-prueba.md` | `docs/` | El archivo que el raíz importa en vez de duplicar |
| `web/CLAUDE.md` · `api/CLAUDE.md` · `infra/CLAUDE.md` | cada carpeta | Convenciones que **se contradicen entre sí** |
| 3 reglas | `.claude/rules/` | Una empatada, dos imposibles para un `CLAUDE.md` de directorio |
| 2 commands | `.claude/commands/` | Uno pelado, uno con `$ARGUMENTS` y `allowed-tools` |
| 2 skills | `.claude/skills/` | Una sin `fork`, una con `fork` |

Si algo se ensucia durante la sesión: `git checkout .` y todo vuelve.

## Antes de empezar (una sola vez)

Instalar la skill **rival** a nivel usuario. Es la mitad del ejercicio de cierre.

```bash
mkdir -p ~/.claude/skills
cp -r ~/dev/demo-s3/.instructor/brutalist-branding ~/.claude/skills/
```

| Nivel | Skill | Qué representa |
|---|---|---|
| Proyecto — `.claude/skills/` (versionado) | `sofka-branding` · `scaffold-endpoint` | Lo recibe todo el que clona |
| Usuario — `~/.claude/skills/` (tu máquina) | `brutalist-branding` | Tu preferencia personal. No la recibe nadie |

Comprobar con `/skills` que las tres cargan y de qué nivel viene cada una.

> ⚠️ Mientras `brutalist-branding` esté instalada, **todo pedido visual tuyo en cualquier repo** sale
> en brutalismo neón salvo que digas "Sofka". Si preparás material con marca, sacala y volvé a
> ponerla antes de la sesión.

## Bloque 1 — Memoria (0:12 – 0:35)

`cd ~/dev/demo-s3 && claude` desde la **raíz**.

### Paso 1 — `/memory`, y la sorpresa no es que esté vacío

Correrlo antes de explicar nada. Lo que aparece: el `CLAUDE.md` raíz, **más el archivo que importa**.
Lo que **no** aparece: `web/CLAUDE.md`, `api/CLAUDE.md`, `infra/CLAUDE.md`.

> *"Este repo tiene cuatro `CLAUDE.md`. ¿Por qué `/memory` me muestra uno?"*

Esa selectividad es todo el bloque. Y de paso queda instalado `/memory` como **la herramienta de
diagnóstico**: cuando el comportamiento es inconsistente entre sesiones, esto es lo primero que se
corre. Ese es el `EX-040`.

### Paso 2 — los cuatro archivos en pantalla, en orden

Abrirlos y leer una línea de cada uno. Lo que hay que hacer notar:

- **Raíz** — solo lo transversal: qué es cada carpeta, que no se cruzan fronteras, commits en
  español. **Nada de TypeScript, nada de Python, nada de Terraform.**
- **`web/CLAUDE.md`** — `strict` sin `any`, todo `fetch` por `src/api.ts`, tests con **vitest**.
- **`api/CLAUDE.md`** — `uv run`, sin lógica en `main.py`, tests con **pytest**.
- **`infra/CLAUDE.md`** — nombres `sofka-<entorno>-<recurso>`, nunca `apply` sin `plan`.

### Paso 3 — la pregunta que justifica la jerarquía

> *"¿Por qué no está todo esto junto en el raíz? Sería un archivo y se acabó."*

Y la respuesta está en dos líneas del propio repo: **`web` dice vitest y `api` dice pytest.** Juntas
en el raíz, se cargan **siempre las dos**, y el agente recibe el runner equivocado la mitad del
tiempo. El costo de mezclar no es estético ni de tokens: es **una instrucción incorrecta cargada en
el contexto equivocado**. Ese es el `PE-042` con el repo delante, y es más fuerte que "un `CLAUDE.md`
de 500 líneas es desordenado".

### Paso 4 — demostrar que la ubicación es el disparador

Dos pedidos y dos `/memory`:

| Pedido | `/memory` muestra |
|---|---|
| Un cambio en `api/app/auth.py` | raíz + **`api/CLAUDE.md`** |
| Un cambio en `web/src/login.ts` | raíz + **`web/CLAUDE.md`** |

Nunca los dos de directorio a la vez. **El disparador del `CLAUDE.md` de directorio es la ubicación
del trabajo**, y eso es exactamente lo que la pregunta guía va a contrastar contra los globs.

### Paso 5 — `@import`, con un caso real de duplicación

El raíz termina con:

```markdown
@docs/usuarios-de-prueba.md
```

Abrir `docs/usuarios-de-prueba.md`: los usuarios de prueba, las contraseñas y cómo agregar uno. Ese
contenido lo necesitan **el `CLAUDE.md` y el `README.md`**, y antes estaba escrito en los dos. Ahora
vive en un archivo y los dos apuntan ahí. `@import` no es un truco de sintaxis: **es para no tener
la misma verdad en dos lugares que se desincronizan.**

Mostrar en `/memory` que el archivo importado aparece listado, no escondido: lo que se importa se
carga, y **cuenta en el presupuesto de contexto igual que si lo hubieras pegado**. Por eso no se
importa el `README` completo ni un documento de 700 líneas.

### La pregunta que va a salir: "¿el personal no tapa al del proyecto?"

Sale siempre, y la respuesta corta es **no: no hay override, hay acumulación.** Los archivos
aplicables se cargan todos y quedan juntos en el contexto. Nada se pierde, nada se sobrescribe.

Claude Code distingue **tipos** de memoria —Managed/policy (de la organización, no se puede
excluir), User (`~/.claude/CLAUDE.md`), Project (`CLAUDE.md`, `.claude/CLAUDE.md`,
`.claude/rules/`) y Local (`CLAUDE.local.md`)— pero el tipo define **de dónde viene y si se puede
excluir**, no quién gana una pelea de contenido.

**El riesgo real no es la pérdida, es la contradicción.** Si tu archivo personal dice "los tests con
jest" y el del proyecto dice vitest, las dos instrucciones están en contexto y **el empate lo
resuelve el modelo, no una regla de precedencia**. Ahí sí el comportamiento se vuelve impredecible.

Y de ahí sale el criterio de diseño, que es lo que hay que dejar dicho:

| Archivo | De qué habla | Ejemplo |
|---|---|---|
| Personal (`~/.claude/CLAUDE.md`) | **Cómo quiero que me hablen** | idioma, tono, mostrame el plan antes de un cambio grande |
| Proyecto (`CLAUDE.md`) | **Cómo tiene que ser el código** | runner de tests, comandos, convenciones, límites |

Dominios que no se pisan. Si no se pisan, no hay empate que resolver.

> **Precisión que sí conviene dejar dicha:** el `PE-041` **no** dice que las instrucciones se pierdan
> por override. Dice que **el equipo no las recibe**: el que clona el repo no tiene tu `~/.claude/`.
> El problema es de **distribución**, no de que algo tape a algo. Son dos fallas distintas y el
> examen pregunta la segunda.
>
> **Y esto NO lo saques vos:** existe una precedencia documentada para la *configuración* de la
> herramienta, pero no es lo mismo que el contenido de los `CLAUDE.md` y pertenece a la Sesión 4.
> Si alguien pregunta por precedencia, la respuesta es "para el contenido de la memoria no hay
> ganador, se acumula; la precedencia de configuración la vemos el jueves". No abrir el tema.

### Ítems de examen que quedan contestados acá

| Caso | Respuesta a fijar |
|---|---|
| `PE-041` — el sénior pone los estándares del equipo en `~/.claude/CLAUDE.md` | Funciona en su máquina y en ninguna otra. Va en `CLAUDE.md` versionado |
| `EX-040` — "aplica las convenciones en algunas sesiones y en otras no" | Está en un archivo de alcance local o de directorio. Diagnóstico: `/memory` |
| `PE-042` — monorepo con `CLAUDE.md` de 400+ líneas | Partirlo: lo transversal en el raíz, lo de cada stack en su directorio o en una regla |

Niveles completos, por si preguntan: `~/.claude/CLAUDE.md` (usuario) · `CLAUDE.md` raíz y
`.claude/CLAUDE.md` (proyecto, siempre cargados) · `subdir/CLAUDE.md` (por directorio) ·
`CLAUDE.local.md` (siempre cargado, no versionado) · `.claude/rules/*.md`.

## Bloque 2 — Reglas con globs (0:35 – 0:50)

Arrancar con la pregunta que deja el bloque anterior abierto:

> *"Ya tengo un `CLAUDE.md` por carpeta. ¿Para qué querría además una regla?"*

Y la respuesta son las tres reglas que ya están escritas en `.claude/rules/`. Se abren y se
explican; lo que se demuestra en vivo es cuál se carga y cuál no.

### Regla 1 — el caso empatado, para ser honesto

```yaml
---
paths: ["infra/**/*.tf"]
---
# Terraform
- Nombres de recurso: `sofka-<entorno>-<recurso>`.
- Todo recurso lleva tags `Proyecto` y `Entorno`.
- Nunca `terraform apply` sin `plan` revisado antes.
```

Decirlo explícito: **`infra/CLAUDE.md` haría casi lo mismo.** Casi — porque aplicaría también al
`terraform.tfvars.example` y a cualquier `.md` que caiga en `infra/`, y esto aplica **solo a los
`.tf`**. Es el `PE-044` literal.

### Regla 2 — la que ningún `CLAUDE.md` de directorio puede hacer

```yaml
---
paths: ["**/*.test.ts", "**/test_*.py"]
---
# Tests
- Un caso por comportamiento, no por método.
- El nombre del test describe el comportamiento esperado, en español.
- Sin mocks de lo que no es frontera del sistema.
```

**Este es el momento del bloque.** Mirar dónde están los tests en este repo:

- `web/src/login.test.ts` — **junto al código que prueba**
- `api/tests/test_auth.py` y `test_login_endpoint.py` — en su propia carpeta

Dos lenguajes, dos convenciones de ubicación, una sola política de testing. Con `CLAUDE.md` de
directorio harían falta **tres archivos** (`web/src/`, `api/tests/`, y el que venga después), y el de
`web/src/` aplicaría también a `login.ts` y `api.ts`, que no son tests. Es el `PE-006` exacto.

### Regla 3 — secretos, cruzando dos stacks

```yaml
---
paths: ["**/.env*", "**/*.tfvars"]
---
# Credenciales
- Nunca escribir valores reales. Los archivos `.example` llevan las claves con valor vacío.
- `*.tfvars` está en `.gitignore` salvo los `.example`. No lo saques de ahí.
```

Cruza `api/` e `infra/`, dos lenguajes que no comparten nada. Ningún directorio los contiene a los dos.

### Verificación — no se puede saltear

Tres pedidos, tres resultados distintos. Preguntar cada vez *"¿qué reglas tenés cargadas para este
archivo?"*:

| Archivo | Debe cargar |
|---|---|
| `web/src/login.test.ts` | La de tests. **No** la de Terraform |
| `infra/main.tf` | La de Terraform |
| `web/src/api.ts` | Ninguna de las tres |

### ⚠️ Gotcha verificado — la regla se engancha a las herramientas de archivo, NO a Bash

Probado contra Claude Code 2.1.263:

- Claude leyó el archivo con `cat` por Bash → **la regla NO se activó**. Confirmó que el archivo
  existe y que el glob matchea, pero el cuerpo de la regla nunca entró al contexto.
- Claude leyó el mismo archivo con la herramienta `Read` → **la regla se activó** y citó el
  contenido textualmente.

Consecuencias:

1. **Al hacer la verificación en vivo, mirá la llamada de herramienta.** Si fue por `Bash` con `cat`,
   la regla no aparece y parece que la demo está rota. Pedí *"usá Read"* si hace falta.
2. Si tenés **auto mode** activo, esa es la causa: instruye a leer archivos por Bash. Desactivalo.
3. Y ahí el anti-patrón "ir por Bash" tiene una consecuencia dura y del tema de hoy: **si vas por
   Bash, tus reglas por path no se cargan.** Treinta segundos, y no hace falta la diapositiva 13.

**Matiz que responde la pregunta guía:** una regla **con** `paths` carga solo cuando Claude trabaja
con archivos que matchean; una regla **sin** `paths` carga **siempre**, igual que `CLAUDE.md`. La
diferencia con `subdir/CLAUDE.md` es *cuándo se carga*: **ubicación** vs. **archivo que matchea**.

**Ítems:** `PE-006` (tests dispersos) · `PE-044` (Terraform solo en `infra/`) · `EX-048` (tres tipos
de contenido → tres archivos de regla con su `paths`).

---

## Bloque 3 — Commands y skills (0:50 – 1:05)

Cuatro artefactos, todos ya escritos en `.claude/`. No se tipean en vivo: se muestran, se comparan
y se corren. Lo que se demuestra es el criterio, no el tecleo.

### 1. El command pelado — `/revisar-login`

```
.claude/commands/revisar-login.md    ← sin frontmatter, sin argumentos
```

Es un archivo `.md` con un prompt adentro y nada más. Correrlo. Su valor: **cruza las tres
carpetas** —`web/src/login.ts`, `api/app/auth.py`, `infra/`— que es exactamente lo que ningún
`CLAUDE.md` de directorio puede hacer. Ese es el `PE-004`: una checklist que dispara el humano.

### 2. El command con argumentos — `/tests`

```yaml
---
description: Corre los tests del stack que se indique y resume solo lo que falló
argument-hint: "[web|api|todo]"
allowed-tools: Bash(npm test*), Bash(uv run pytest*), Read
---
Corré los tests de: $ARGUMENTS
```

Correr `/tests api` y después `/tests` sin argumento. Tres cosas que quedan a la vista:

- **`$ARGUMENTS`** es la sustitución. Lo que el usuario tipea después del comando entra ahí.
- **`argument-hint`** es lo que se ve en el autocompletado. No cambia el comportamiento: cambia si
  alguien acierta a usarlo.
- **`allowed-tools` con patrones**, no con herramientas peladas: `Bash(npm test*)` y no `Bash`. Este
  command puede correr los tests y **nada más** — no puede hacer `git push` ni borrar un archivo.
  Es el mismo principio de mínimo privilegio que la Semana 5 va a exigir como política.

### 3. La skill de referencia — `sofka-branding`, sin fork

```
.claude/skills/sofka-branding/
├── SKILL.md                        129 líneas
└── references/
    ├── brand-manual.md             166 líneas
    └── web-design-system.md        377 líneas
```

*"¿Cuánto de esas 672 líneas está en el contexto ahora?"* → **119 palabras**, solo la `description`.
Capacidad bajo demanda, medida en líneas.

Y la pregunta que parece trampa: **¿por qué esta skill NO tiene `context: fork`?** Porque su
producto son **reglas que tienen que estar donde se hace el trabajo**. Forkeada, volvería un resumen
y la página saldría sin la paleta. Vacuna contra "fork siempre es mejor".

### 4. La skill generativa — `scaffold-endpoint`, con fork

```yaml
---
name: scaffold-endpoint
description: >
  Agrega un endpoint nuevo a la API de FastAPI siguiendo las convenciones ya establecidas...
context: fork
allowed-tools: [Read, Glob, Grep, Write]
argument-hint: "<nombre-del-endpoint>"
---
```

Su cuerpo la obliga a **cinco lecturas exploratorias antes de escribir nada**: el `api/CLAUDE.md`,
el `main.py` para copiar el estilo de rutas, el `auth.py` para ver dónde va la lógica, un Grep de
`HTTPException`, y un test existente para copiar la convención de nombres. Después escribe tres
archivos.

Correrla: `/scaffold-endpoint perfil` — o mejor, pedir *"agregá un endpoint de perfil de usuario"* y
que se active sola por la `description`.

**Lo que hay que hacer notar cuando termina:** volvió **un resumen de tres líneas**. Las cinco
lecturas, el Grep y el contenido intermedio ocurrieron en el subagente y **no están en el contexto
principal**. Eso es `context: fork`, y es el `PE-043` textual.

### El contraste, que es la lección del bloque

| | `sofka-branding` | `scaffold-endpoint` |
|---|---|---|
| Qué produce | **Reglas** para usar acá mismo | **Archivos**, un resultado final |
| Trabajo intermedio | No tiene | Cinco lecturas y un Grep, descartables |
| `context: fork` | **No** — el resumen perdería la paleta | **Sí** — solo importa el resultado |

Mismo mecanismo, decisión opuesta. **Y lo que decide no es el tamaño de la skill: es qué es su
producto.** Si el producto tiene que quedar en el contexto, no forkeás. Si el producto es un
artefacto y el camino es basura, forkeás.

> **Nota para el participante despierto.** `scaffold-endpoint` escribe archivos, o sea que tiene
> efectos. La guía de Claude Code recomienda para esos casos agregar `disable-model-invocation: true`
> para que **solo el usuario** pueda dispararla — y ahí es, a todos los efectos, un slash command
> con superpoderes. Decirlo si preguntan, y no antes: si lo pones al frente, embarrás la tabla de
> decisión que es criterio de salida.

---

## Ejercicio de cierre (1:05 – 1:15) — ⭐ el momento de la sesión

El repo trae `web/index.html`: el formulario de ingreso, HTML pelado, sin una sola línea de CSS.
Falta la página a la que se llega después de entrar — `main.ts` ya redirige a `/bienvenida.html`,
que no existe. Ese es el pedido natural.

### Corrida 1 — la que sorprende

Con `sofka-branding` a nivel proyecto y `brutalist-branding` a nivel usuario:

> *"creame `web/bienvenida.html` con css que diga bienvenidos"*

**Resultado verificado:** gana `brutalist-branding`. Fondo `#0a0a0a`, verde neón `#39ff14`, Courier
en mayúsculas, bordes magenta sin radio. **Nada de Sofka.** La skill de marca estaba ahí, en el
repo, versionada, y no hizo nada.

**Qué mirar, y en qué orden de confianza:**

1. **Los colores** y **la invocación de la skill que Claude Code muestra en pantalla** — eso es
   evidencia: pasó y se ve.
2. **La explicación en prosa** — el modelo suele nombrar por su cuenta la marca que aplicó, porque
   con dos skills reclamando el mismo terreno la elección queda visible. En una corrida real dijo:
   *"sofka-branding no aplicó porque no mencionaste Sofka"*. Pero **eso es testimonio, no traza**: es
   el modelo narrando su decisión después del hecho. Si no sale sola, se pregunta y listo.

No presentar la frase del modelo como prueba de mecanismo. La prueba es el A/B de las dos corridas.

Ahí se para la demo: **¿por qué perdió la skill del proyecto?** Dejar que tiren hipótesis. La que va
a salir es "porque la de usuario tiene prioridad". Es falsa.

### Corrida 2 — la contraprueba

El mismo pedido con **una palabra más**:

> *"creame `web/bienvenida.html` con css que diga bienvenidos **para Sofka**"*

**Resultado verificado:** gana `sofka-branding`. Gradiente navy, Poppins, logo `sofka_` con el
underscore naranja, CTA `#FF6B2B`, contraste AA. Mismo repo, mismas dos skills, una palabra.

### La lección, en tres golpes

1. **No hay prioridad por nivel.** Usuario no le gana a proyecto ni al revés. **El ruteo lo hace la
   `description`**, y nada más.
2. **La description de `sofka-branding` se autolimitó.** Su primera frase dice *"Use this skill
   ALWAYS when creating any visual asset... HTML page"*, pero la segunda condiciona el disparo a que
   el usuario mencione "Sofka". Ante la contradicción, el modelo se quedó con la condición más
   restrictiva. Quien la escribió creía decir "siempre"; el modelo leyó "solo si dicen Sofka".
   **Escribir una description es diseñar un ruteo, y se testea o se rompe.**
3. **El cierre de la tabla de decisión:** si la marca tiene que aplicar a *todo* lo visual del repo
   sin depender de que alguien diga la palabra mágica, **no puede vivir en una skill** — porque una
   skill depende de que el modelo la elija.

> **Lo que no puede depender de que el modelo elija, no va en una skill.**

### El remate — ejecutar la conclusión, no solo enunciarla

⚠️ **Este paso NO está verificado todavía.** Probarlo antes de la sesión.

Es el único momento en que se agrega un archivo delante de la sala, y son cuatro líneas:
`.claude/rules/paginas-web.md`

```yaml
---
paths: ["web/**/*.html", "web/**/*.css"]
---
# Páginas del front
- Toda página usa el design system de Sofka: paleta, tipografía Poppins y el logo `sofka_`.
- Consultar la skill `sofka-branding` antes de escribir estilos.
```

Y repetir la corrida 1 **sin decir "Sofka"**. Si la regla hace su trabajo, la página sale con marca
igual — porque la regla se carga **siempre** que se toca un HTML de `web/`, sin depender de que el
modelo elija nada.

Eso cierra el círculo completo de la sesión en un movimiento: **skill (probabilístico, lo elige el
modelo) → regla (determinista para el contexto, se carga por el archivo)**. Y es el puente exacto a
la Sesión 4: la misma lógica un nivel más abajo — lo que no puede fallar nunca no va en un prompt,
va en un hook.

### Variante opcional, si sobra tiempo

Romper el YAML de `brutalist-branding` (quitarle un guion al `---` de cierre) y repetir la corrida 1.
La skill **sigue cargando con todos los campos descartados**: el nombre cae al del directorio y la
description a la primera línea del cuerpo, así que matchea contra cualquier cosa.
**Romper siempre la rival, nunca la de marca.**

### Salidas de referencia

En `.instructor/salidas-ejercicio/` están los dos HTML de las corridas de prueba
(`bienvenidos.html` brutalista y `bienvenidos-sofka.html` con marca). Para mostrarlos lado a lado si
el vivo falla.

---

## Cierre del bloque — la tabla, sin leerla

Pedir tres casos reales de los repos de ellos y que la sala los ubique en voz alta. Es el criterio de
salida de la sesión.

| Mecanismo | Cuándo | La pregunta que lo decide |
|---|---|---|
| `CLAUDE.md` | Estándares que siempre aplican | ¿Vale para todo el proyecto, siempre? |
| `.claude/rules/` | Estándares que aplican a ciertos archivos | ¿Depende del tipo o la ruta del archivo? |
| Slash command | Un prompt que se repite y el usuario invoca | ¿Lo escribo yo cuando lo necesito? |
| Skill | Una capacidad bajo demanda, con sus propias herramientas | ¿Claude debería activarla solo, y aislada? |

**Ítems:** `PE-004` (checklist de revisión → command) · `PE-043` (skill con muchas lecturas
exploratorias → `context: fork`) · `EX-044` (skill que genera docs desde el código fuente).

---

## Bloque 4 — Práctica guiada (1:15 – 1:30)

En **el repo propio** de cada uno, no en este. Entregable: `CLAUDE.md` de proyecto corto + al menos
una regla con `paths` **verificada** sobre un archivo que matchea y otro que no.

> **Ojo con esto:** como no se tipeó nada en vivo, nadie tiene un template a mano cuando llega este
> bloque. Antes de largarlos, pegá en el canal las cuatro piezas mínimas —el `CLAUDE.md` raíz, un
> `subdir/CLAUDE.md`, una regla con `paths` y el bloque de frontmatter de una skill— o compartí una
> copia del repo **sin `.instructor/`**. Sin eso, los primeros cinco minutos de la práctica se van
> en recordar la sintaxis del frontmatter.

Mientras circulás, la pregunta útil no es "¿te funciona?" sino
**"¿por qué eso es una regla y no una línea del `CLAUDE.md`?"**.

---

## Qué NO enseñar hoy

Hooks, MCP y plan mode son Sesión 4. Si salen, anotalos y devolvelos a la pregunta guía de la
Sesión 4 en el cierre: *si una regla de negocio no puede fallar nunca, ¿por qué no alcanza con
escribirla en el system prompt?*

La diapositiva 13 del deck (herramientas nativas Grep/Glob/Edit) es `kata_023`, que el plan asigna
como **tarea** de la semana y el mapa ancla a la **Sesión 4**. El ejercicio de cierre le ocupa el
lugar y vale más. Sacarla del cuerpo; lo único que conviene rescatar son los 30 segundos del gotcha
de Bash dentro del Bloque 2.
