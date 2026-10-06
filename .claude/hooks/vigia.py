#!/usr/bin/env python3
"""Vigía de nombres de test. Uso: vigia.py observar|avisar|impedir. Lee el JSON del hook por stdin.

Convención (sacada de .claude/rules/tests.md, api/CLAUDE.md y web/CLAUDE.md):
  - api:  tests/test_<comportamiento>.py, funciones test_ + al menos tres palabras, en español.
  - web:  *.test.ts al lado del archivo que prueba; it('…') / test('…') en español.
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys

MODO = sys.argv[1] if len(sys.argv) > 1 else "observar"
LOG = pathlib.Path(__file__).with_name("vigia.log")
INGLES = {"should", "returns", "when", "works", "fails", "error", "invalid", "empty",
          "given", "then", "expect", "handles", "success"}


def rama() -> str:
    try:
        r = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        return r.stdout.strip() or "?"
    except OSError:
        return "?"


def es_test(ruta: str) -> bool:
    return bool(re.search(r"api/tests/test_[^/]+\.py$", ruta)) or ruta.endswith(".test.ts")


def nombres(ruta: str, texto: str) -> list[str]:
    if ruta.endswith(".py"):
        return re.findall(r"^\s*def\s+(test\w*)\s*\(", texto, re.M)
    return re.findall(r"\b(?:it|test)\(\s*['\"`]([^'\"`]+)['\"`]", texto)


def problemas(ruta: str, texto: str) -> list[str]:
    malos = []
    for n in nombres(ruta, texto):
        palabras = [p for p in re.split(r"[_\s]+", n.lower()) if p and p != "test"]
        if ruta.endswith(".py") and len(palabras) < 3:
            malos.append(n)
        elif set(palabras) & INGLES:
            malos.append(n)
    if ruta.endswith(".test.ts"):
        hermano = pathlib.Path(ruta[: -len(".test.ts")] + ".ts")
        if not hermano.exists():
            malos.append(f"falta {hermano.name} al lado")
    return malos


datos = json.load(sys.stdin)
evento = datos.get("hook_event_name", "?")
herramienta = datos.get("tool_name", "?")
entrada = datos.get("tool_input", {})
ruta = entrada.get("file_path", "")

if not ruta or not es_test(ruta):
    sys.exit(0)

if evento == "PostToolUse":                       # ya se escribió: se lee lo que quedó en disco
    p = pathlib.Path(ruta)
    texto = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
else:                                             # PreToolUse: lo que Claude QUIERE escribir
    texto = entrada.get("content") or entrada.get("new_string") or ""

malos = problemas(ruta, texto)
veredicto = f"✗ {', '.join(malos)}" if malos else f"✓ {len(nombres(ruta, texto))} tests"
sufijo = {"avisar": " · razón enviada", "impedir": " · BLOQUEADO"}.get(MODO, "") if malos else ""
with LOG.open("a", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now():%H:%M:%S} · {rama()} · {evento} · {herramienta} {ruta} → {veredicto}{sufijo}\n")

if not malos:
    sys.exit(0)

razon = (f"Nombres fuera de convención en {ruta}: {', '.join(malos)}. "
         "Regla del repo: test_<comportamiento>, al menos tres palabras, en español, "
         "describiendo el comportamiento esperado (ver .claude/rules/tests.md).")

if MODO == "observar":
    print(json.dumps({"systemMessage": f"vigía: {veredicto} en {ruta}"}))
    sys.exit(0)

if MODO == "avisar":
    print(json.dumps({"decision": "block", "reason": razon,
                      "systemMessage": f"vigía: {veredicto} · razón enviada a Claude"}))
    sys.exit(0)

print(razon, file=sys.stderr)                     # impedir: exit 2 frena el Write antes del disco
sys.exit(2)
