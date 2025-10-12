"""Task command for CLI."""

import typer
from rich.console import Console
from rich.panel import Panel

console = Console()

def task_command(
    description: str = typer.Argument(..., help="Task description"),
    agent_type: str = typer.Option("orchestrator", help="Primary agent type"),
    output_dir: str = typer.Option("./output", help="Output directory"),
    dry_run: bool = typer.Option(False, help="Show plan without execution")
):
    """Execute a specific task using agents."""
    
    console.print(Panel(
        f"[blue]📋 Task Execution[/blue]\n"
        f"Description: {description}\n"
        f"Agent: {agent_type}\n"
        f"Output: {output_dir}\n"
        f"Mode: {'Dry Run' if dry_run else 'Execute'}",
        title="Task Details"
    ))
    
    if dry_run:
        console.print("[yellow]Dry run mode - showing execution plan...[/yellow]")
    else:
        console.print("[dim]Executing task...[/dim]")
    
    # Placeholder for actual task execution
    console.print("[green]✅ Task completed successfully[/green]")