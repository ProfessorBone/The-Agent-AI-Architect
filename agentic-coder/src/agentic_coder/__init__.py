"""
Agentic Coder: A comprehensive agentic AI coding system.

This package provides a multi-agent system for autonomous software development,
featuring cognitive architecture, Graph RAG knowledge management, and advanced
reasoning capabilities.
"""

__version__ = "0.1.0"
__author__ = "Agentic Coder Team"
__email__ = "team@agentic-coder.dev"

from .agents import *
from .cognitive import *
from .knowledge import *
from .tools import *
from .models import *
from .data import *
from .utils import *

__all__ = [
    # Core modules
    "agents",
    "cognitive", 
    "knowledge",
    "tools",
    "models",
    "data",
    "utils",
    # Version info
    "__version__",
    "__author__",
    "__email__",
]