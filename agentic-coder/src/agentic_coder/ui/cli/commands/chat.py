"""Chat command for CLI."""

import typer
from rich.console import Console
from rich.panel import Panel

console = Console()

def chat_command(
    model: str = typer.Option("gpt-4", help="LLM model to use"),
    memory: bool = typer.Option(True, help="Enable memory"),
    debug: bool = typer.Option(False, help="Enable debug mode")
):
    """Start interactive chat with agentic-coder."""
    
    console.print(Panel(
        "[green]🤖 Agentic Coder Interactive Chat[/green]\n"
        f"Model: {model}\n"
        f"Memory: {'Enabled' if memory else 'Disabled'}\n"
        "Type 'exit' to quit",
        title="Chat Session"
    ))
    
    console.print("\n[dim]Starting chat session...[/dim]")
    
    # Placeholder for actual chat implementation
    console.print("[yellow]Chat functionality will be implemented here[/yellow]")