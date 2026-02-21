from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console

from .builder import generate_brd
from .models import BRDRequest

app = typer.Typer(help="Generate Business Requirements Documents from structured input.")
console = Console()


@app.command()
def generate(input_file: Path, output_file: Path = Path("BRD.md")) -> None:
    """Generate a BRD markdown file from a JSON payload."""
    payload = json.loads(input_file.read_text())
    request = BRDRequest.model_validate(payload)
    response = generate_brd(request)
    output_file.write_text(response.markdown)
    console.print(f"[green]BRD generated:[/green] {output_file}")


if __name__ == "__main__":
    app()
