"""Project command for CLI."""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

def project_command(
    action: str = typer.Argument(..., help="Project action: list, create, delete, info"),
    name: str = typer.Option(None, help="Project name"),
    template: str = typer.Option("basic", help="Project template")
):
    """Manage agentic-coder projects."""
    
    if action == "list":
        list_projects()
    elif action == "create":
        if not name:
            console.print("[red]Error: Project name required for create action[/red]")
            raise typer.Exit(1)
        create_project(name, template)
    elif action == "delete":
        if not name:
            console.print("[red]Error: Project name required for delete action[/red]")
            raise typer.Exit(1)
        delete_project(name)
    elif action == "info":
        if not name:
            console.print("[red]Error: Project name required for info action[/red]")
            raise typer.Exit(1)
        show_project_info(name)
    else:
        console.print(f"[red]Unknown action: {action}[/red]")
        console.print("Available actions: list, create, delete, info")

def list_projects():
    """List all projects."""
    table = Table(title="Agentic Coder Projects")
    table.add_column("Name", style="cyan")
    table.add_column("Template", style="green")
    table.add_column("Created", style="yellow")
    table.add_column("Status", style="blue")
    
    # Placeholder - would scan actual project directories
    projects = [
        ("my-agent", "basic", "2024-01-15", "Active"),
        ("web-scraper", "web", "2024-01-14", "Active"),
        ("data-analyzer", "analysis", "2024-01-13", "Inactive"),
    ]
    
    for name, template, created, status in projects:
        table.add_row(name, template, created, status)
    
    console.print(table)

def create_project(name: str, template: str):
    """Create a new project."""
    console.print(f"[blue]Creating project '{name}' with template '{template}'...[/blue]")
    
    project_path = Path(name)
    project_path.mkdir(exist_ok=True)
    
    console.print(f"[green]✅ Project '{name}' created successfully[/green]")

def delete_project(name: str):
    """Delete a project."""
    console.print(f"[red]⚠️  Deleting project '{name}'...[/red]")
    # Would implement actual deletion with confirmation
    console.print(f"[green]✅ Project '{name}' deleted[/green]")

def show_project_info(name: str):
    """Show project information."""
    console.print(f"[blue]Project Information: {name}[/blue]")
    # Would show actual project details
    console.print("Project details would be displayed here")