"""Server MCP de usuarios de prueba. Lo arranca Claude Code desde .mcp.json:
   uv run --directory api python mcp_usuarios.py
"""
import os
import pathlib

from mcp.server.fastmcp import FastMCP

RAIZ = pathlib.Path(__file__).resolve().parents[1]
DOC = RAIZ / os.environ.get("USUARIOS_PATH", "docs/usuarios-de-prueba.md")

mcp = FastMCP("usuarios")


@mcp.resource("usuarios://prueba")
def usuarios_prueba() -> str:
    """Catálogo completo de usuarios de prueba del login, tal como está documentado en el repo."""
    return DOC.read_text(encoding="utf-8")


@mcp.tool()
def buscar_usuario(correo: str) -> str:
    """Devuelve la contraseña de prueba y el propósito de UN usuario de prueba, buscado por correo exacto.

    Usar solo cuando ya se conoce el correo. Para saber qué usuarios existen, leer antes el
    resource usuarios://prueba en vez de llamar este tool varias veces.
    """
    for linea in DOC.read_text(encoding="utf-8").splitlines():
        if linea.startswith("|") and correo in linea:
            celdas = [c.strip().strip("`") for c in linea.strip().strip("|").split("|")]
            return f"correo={celdas[0]} · contraseña={celdas[1]} · uso={celdas[2]}"
    return f"No existe un usuario de prueba con correo {correo}."


if __name__ == "__main__":
    mcp.run()
