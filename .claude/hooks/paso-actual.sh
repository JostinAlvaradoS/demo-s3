#!/usr/bin/env bash
rama=$(git -C "${CLAUDE_PROJECT_DIR:-.}" branch --show-current)
printf '{"systemMessage":"Paso · %s"}\n' "$rama"
