"""Custom exceptions for agentic-coder."""

from typing import Any, Dict, Optional


class AgenticCoderError(Exception):
    """Base exception for all agentic-coder errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class AgentError(AgenticCoderError):
    """Base exception for agent-related errors."""
    pass


class AgentTimeoutError(AgentError):
    """Raised when an agent operation times out."""
    pass


class AgentNotFoundError(AgentError):
    """Raised when a requested agent is not found."""
    pass


class InvalidAgentTypeError(AgentError):
    """Raised when an invalid agent type is specified."""
    pass


class AgentExecutionError(AgentError):
    """Raised when an agent fails to execute a task."""
    pass


class MemoryError(AgenticCoderError):
    """Base exception for memory-related errors."""
    pass


class MemoryLimitExceededError(MemoryError):
    """Raised when memory limits are exceeded."""
    pass


class MemoryCorruptionError(MemoryError):
    """Raised when memory data is corrupted."""
    pass


class MemoryNotFoundError(MemoryError):
    """Raised when requested memory is not found."""
    pass


class ToolError(AgenticCoderError):
    """Base exception for tool-related errors."""
    pass


class ToolNotFoundError(ToolError):
    """Raised when a requested tool is not found."""
    pass


class ToolExecutionError(ToolError):
    """Raised when a tool fails to execute."""
    pass


class ToolPermissionError(ToolError):
    """Raised when a tool operation is not permitted."""
    pass


class KnowledgeError(AgenticCoderError):
    """Base exception for knowledge-related errors."""
    pass


class GraphError(KnowledgeError):
    """Raised for graph database errors."""
    pass


class VectorStoreError(KnowledgeError):
    """Raised for vector store errors."""
    pass


class ModelError(AgenticCoderError):
    """Base exception for model-related errors."""
    pass


class ModelNotFoundError(ModelError):
    """Raised when a requested model is not found."""
    pass


class ModelTimeoutError(ModelError):
    """Raised when a model operation times out."""
    pass


class ModelConfigurationError(ModelError):
    """Raised when model configuration is invalid."""
    pass


class ConfigurationError(AgenticCoderError):
    """Raised for configuration-related errors."""
    pass


class ValidationError(AgenticCoderError):
    """Raised for data validation errors."""
    pass


class FileOperationError(AgenticCoderError):
    """Raised for file operation errors."""
    pass


class PermissionError(AgenticCoderError):
    """Raised for permission-related errors."""
    pass


class NetworkError(AgenticCoderError):
    """Raised for network-related errors."""
    pass


class DatabaseError(AgenticCoderError):
    """Raised for database-related errors."""
    pass


class SerializationError(AgenticCoderError):
    """Raised for serialization/deserialization errors."""
    pass


class LearningError(AgenticCoderError):
    """Raised for learning system errors."""
    pass


class ReasoningError(AgenticCoderError):
    """Raised for reasoning system errors."""
    pass


class WorkflowError(AgenticCoderError):
    """Raised for workflow execution errors."""
    pass


class TaskError(AgenticCoderError):
    """Raised for task execution errors."""
    pass


class TaskNotFoundError(TaskError):
    """Raised when a requested task is not found."""
    pass


class TaskTimeoutError(TaskError):
    """Raised when a task times out."""
    pass


class TaskCancelledError(TaskError):
    """Raised when a task is cancelled."""
    pass


class UIError(AgenticCoderError):
    """Raised for UI-related errors."""
    pass


class CLIError(UIError):
    """Raised for CLI-related errors."""
    pass


class APIError(UIError):
    """Raised for API-related errors."""
    pass