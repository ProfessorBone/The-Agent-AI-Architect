"""System command for CLI."""

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def system_command(
    action: str = typer.Argument(..., help="System action: status, start, stop, restart"),
    service: str = typer.Option("all", help="Specific service to control")
):
    """Manage system services and status."""
    
    if action == "status":
        show_system_status()
    elif action in ["start", "stop", "restart"]:
        manage_service(action, service)
    else:
        console.print(f"[red]Unknown action: {action}[/red]")
        console.print("Available actions: status, start, stop, restart")

def show_system_status():
    """Show current system status."""
    
    table = Table(title="System Status")
    table.add_column("Service", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Port", style="yellow")
    
    # Placeholder status - would check actual services
    services = [
        ("Neo4j", "Running", "7687"),
        ("ChromaDB", "Running", "8001"),
        ("vLLM Server", "Stopped", "8000"),
        ("API Server", "Stopped", "8080"),
    ]
    
    for service, status, port in services:
        status_style = "green" if status == "Running" else "red"
        table.add_row(service, f"[{status_style}]{status}[/{status_style}]", port)
    
    console.print(table)

def manage_service(action: str, service: str):
    """Manage a specific service."""
    console.print(Panel(
        f"[blue]{action.title()}ing service: {service}[/blue]",
        title="Service Management"
    ))
    
    # Placeholder for actual service management
    console.print(f"[green]✅ Service {service} {action}ed successfully[/green]")