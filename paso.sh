#!/usr/bin/env bash
# Uso: ./paso.sh N   (0 = main)
# Deshace lo que Claude tocó en el paso anterior, cambia a la rama del paso N
# y muestra el diff contra el paso N-1.
set -euo pipefail
RAMAS=(main s4/01-permisos s4/02-vigia-observa s4/03-vigia-avisa s4/04-vigia-impide s4/05-plan s4/06-mcp)
n=${1:?uso: ./paso.sh N}
git checkout -q -- .
git clean -fdq -- api/tests web/src          # solo lo que Claude creó: tests nuevos
git switch -q "${RAMAS[$n]}"
mkdir -p .claude/hooks && touch .claude/hooks/vigia.log
clear
printf '\n== Paso %s · %s ==\n\n' "$n" "${RAMAS[$n]}"
if (( n > 0 )); then
  git --no-pager diff --stat "${RAMAS[$((n-1))]}" HEAD
  echo
  git --no-pager diff "${RAMAS[$((n-1))]}" HEAD -- .claude/settings.json .mcp.json
fi
