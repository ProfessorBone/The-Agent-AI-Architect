"""Main CLI application using Typer."""

import typer
from typing import Optional
from rich.console import Console
from rich.panel import Panel

from ..commands import (
    init_command,
    chat_command, 
    task_command,
    project_command,
    system_command
)

# Create the main Typer app
app = typer.Typer(
    name="agentic-coder",
    help="A comprehensive agentic AI coding system",
    add_completion=False,
    rich_markup_mode="rich"
)

console = Console()

# Add subcommands
app.command("init")(init_command)
app.command("chat")(chat_command)
app.command("task")(task_command)
app.command("project")(project_command)
app.command("system")(system_command)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, 
        "--version", 
        "-v",
        help="Show version information"
    ),
    verbose: Optional[bool] = typer.Option(
        False,
        "--verbose",
        help="Enable verbose output"
    )
):
    """
    Agentic Coder - A comprehensive agentic AI coding system.
    
    Build intelligent multi-agent systems for autonomous software development.
    """
    if version:
        from agentic_coder import __version__
        console.print(f"Agentic Coder version {__version__}")
        raise typer.Exit()
    
    if verbose:
        console.print("[dim]Verbose mode enabled[/dim]")


if __name__ == "__main__":
    app()