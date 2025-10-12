"""Init command for CLI."""

import typer
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

def init_command(
    name: str = typer.Argument(..., help="Project name"),
    template: str = typer.Option("basic", help="Project template"),
    force: bool = typer.Option(False, "--force", help="Overwrite existing project")
):
    """Initialize a new agentic-coder project."""
    
    project_path = Path(name)
    
    if project_path.exists() and not force:
        console.print(f"[red]Error: Directory '{name}' already exists. Use --force to overwrite.[/red]")
        raise typer.Exit(1)
    
    # Create project directory
    project_path.mkdir(exist_ok=force)
    
    console.print(Panel(
        f"[green]✅ Initialized new project: {name}[/green]\n"
        f"Template: {template}\n"
        f"Path: {project_path.absolute()}",
        title="Project Created"
    ))
    
    console.print("\n[dim]Next steps:[/dim]")
    console.print(f"  cd {name}")
    console.print("  agentic-coder chat")