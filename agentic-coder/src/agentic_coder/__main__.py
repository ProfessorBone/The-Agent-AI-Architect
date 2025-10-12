"""
Main entry point for the agentic-coder package.

This module provides the CLI interface and can be run with:
    python -m agentic_coder
"""

import sys
from typing import Optional

import typer
from rich.console import Console

from .ui.cli.app import app

console = Console()


def main(args: Optional[list[str]] = None) -> int:
    """Main entry point for the application."""
    try:
        if args is None:
            args = sys.argv[1:]
        
        # Run the Typer app
        app()
        return 0
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        return 1
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return 1


if __name__ == "__main__":
    sys.exit(main())