"""Global constants for agentic-coder."""

from enum import Enum
from typing import Final

# Version information
VERSION: Final[str] = "0.1.0"
NAME: Final[str] = "agentic-coder"
DESCRIPTION: Final[str] = "A comprehensive agentic AI coding system"

# Agent types
class AgentType(Enum):
    """Enumeration of agent types."""
    ORCHESTRATOR = "orchestrator"
    ANALYZER = "analyzer"
    PLANNER = "planner"
    CODER = "coder"
    TESTER = "tester"
    REVIEWER = "reviewer"
    COORDINATOR = "coordinator"

# Memory types
class MemoryType(Enum):
    """Enumeration of memory types."""
    WORKING = "working"
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PROCEDURAL = "procedural"

# Reasoning types
class ReasoningType(Enum):
    """Enumeration of reasoning types."""
    REACTIVE = "reactive"
    DELIBERATIVE = "deliberative"
    REFLECTIVE = "reflective"
    REACT = "react"

# Tool categories
class ToolCategory(Enum):
    """Enumeration of tool categories."""
    FILE_OPERATIONS = "file_operations"
    CODE_ANALYSIS = "code_analysis"
    GIT_OPERATIONS = "git_operations"
    CODE_EXECUTION = "code_execution"
    WEB_OPERATIONS = "web_operations"

# Learning types
class LearningType(Enum):
    """Enumeration of learning types."""
    EXPERIENCE_REPLAY = "experience_replay"
    META_LEARNING = "meta_learning"
    CURRICULUM = "curriculum"
    FINE_TUNING = "fine_tuning"

# Task status
class TaskStatus(Enum):
    """Enumeration of task statuses."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# Default values
DEFAULT_MAX_ITERATIONS: Final[int] = 10
DEFAULT_AGENT_TIMEOUT: Final[int] = 300
DEFAULT_WORKING_MEMORY_SIZE: Final[int] = 50
DEFAULT_EPISODIC_MEMORY_SIZE: Final[int] = 1000
DEFAULT_SEMANTIC_MEMORY_SIZE: Final[int] = 10000

# File extensions
SUPPORTED_CODE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp",
    ".cs", ".php", ".rb", ".go", ".rs", ".swift", ".kt", ".scala", ".clj",
    ".sh", ".bash", ".zsh", ".ps1", ".sql", ".r", ".m", ".pl", ".lua"
)

SUPPORTED_CONFIG_EXTENSIONS: Final[tuple[str, ...]] = (
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".xml"
)

SUPPORTED_DOC_EXTENSIONS: Final[tuple[str, ...]] = (
    ".md", ".txt", ".rst", ".adoc", ".tex"
)

# Directory patterns to ignore
IGNORED_DIRECTORIES: Final[tuple[str, ...]] = (
    "__pycache__", ".git", ".svn", ".hg", ".bzr", "node_modules", ".venv",
    "venv", "env", ".env", "build", "dist", ".tox", ".pytest_cache",
    ".mypy_cache", ".coverage", "htmlcov", ".idea", ".vscode", ".DS_Store"
)

# Default prompts
DEFAULT_SYSTEM_PROMPT: Final[str] = """
You are an expert AI software engineer with deep knowledge across multiple programming languages,
frameworks, and software engineering best practices. You work as part of a multi-agent system
to analyze, plan, code, test, and review software projects.

Key principles:
1. Write clean, maintainable, and well-documented code
2. Follow language-specific conventions and best practices
3. Consider security, performance, and scalability
4. Test thoroughly and handle edge cases
5. Collaborate effectively with other agents
6. Learn from experience and improve over time
"""

# Model configurations
DEFAULT_MODEL_CONFIGS: Final[dict] = {
    "gpt-4": {
        "max_tokens": 4096,
        "temperature": 0.7,
        "top_p": 0.9,
    },
    "gpt-3.5-turbo": {
        "max_tokens": 4096,
        "temperature": 0.7,
        "top_p": 0.9,
    },
    "codellama": {
        "max_tokens": 2048,
        "temperature": 0.3,
        "top_p": 0.8,
    }
}

# Error messages
ERROR_MESSAGES: Final[dict] = {
    "agent_timeout": "Agent operation timed out after {timeout} seconds",
    "invalid_agent_type": "Invalid agent type: {agent_type}",
    "memory_limit_exceeded": "Memory limit exceeded for {memory_type}",
    "tool_not_found": "Tool not found: {tool_name}",
    "file_not_found": "File not found: {file_path}",
    "permission_denied": "Permission denied: {operation}",
    "invalid_configuration": "Invalid configuration: {config_key}",
}

# Success messages
SUCCESS_MESSAGES: Final[dict] = {
    "agent_created": "Agent created successfully: {agent_type}",
    "task_completed": "Task completed successfully: {task_id}",
    "file_processed": "File processed successfully: {file_path}",
    "memory_updated": "Memory updated successfully: {memory_type}",
    "learning_completed": "Learning cycle completed successfully",
}

# API endpoints
API_ENDPOINTS: Final[dict] = {
    "health": "/health",
    "agents": "/api/v1/agents",
    "tasks": "/api/v1/tasks",
    "memory": "/api/v1/memory",
    "tools": "/api/v1/tools",
    "chat": "/api/v1/chat",
    "websocket": "/ws",
}