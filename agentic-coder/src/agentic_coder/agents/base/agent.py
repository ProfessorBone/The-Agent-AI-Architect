"""
Base Agent Class

Provides the foundational functionality for all AI agents in the system.
"""

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents in the system.

    Provides core functionality including:
    - Configuration management
    - Logging setup
    - Basic agent lifecycle
    - System prompt loading
    - Status tracking
    """

    def __init__(self, agent_name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the base agent.

        Args:
            agent_name: Unique name for this agent
            config: Optional configuration dictionary
        """
        self.agent_name = agent_name
        self.config = config or {}
        self.status = "initialized"
        self.logger = logging.getLogger(f"agents.{agent_name}")

        # Agent state
        self.is_active = False
        self.capabilities = []
        self.dependencies = []

        self.logger.info(f"Initialized {agent_name} agent")

    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a task with this agent.

        Args:
            task: Task definition and parameters

        Returns:
            Task execution result
        """
        pass

    @abstractmethod
    def validate_capabilities(self) -> bool:
        """
        Validate that the agent has required capabilities.

        Returns:
            True if agent is ready, False otherwise
        """
        pass

    def load_prompt(self, prompt_path: str) -> str:
        """
        Load system prompt from file.

        Args:
            prompt_path: Path to the prompt file

        Returns:
            Loaded prompt content
        """
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            self.logger.error(f"Failed to load prompt from {prompt_path}: {e}")
            return ""

    def load_config_module(self, module_path: str) -> Dict[str, Any]:
        """
        Load configuration module from file.

        Args:
            module_path: Path to the configuration module

        Returns:
            Parsed configuration data
        """
        try:
            with open(module_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Basic parsing - in real implementation would parse markdown/YAML
            return {"content": content, "path": module_path}
        except Exception as e:
            self.logger.error(f"Failed to load config module from {module_path}: {e}")
            return {}

    def activate(self) -> bool:
        """
        Activate the agent for task execution.

        Returns:
            True if activation successful, False otherwise
        """
        if not self.validate_capabilities():
            self.logger.error("Agent capabilities validation failed")
            return False

        self.is_active = True
        self.status = "active"
        self.logger.info(f"Agent {self.agent_name} activated")
        return True

    def deactivate(self) -> None:
        """Deactivate the agent."""
        self.is_active = False
        self.status = "inactive"
        self.logger.info(f"Agent {self.agent_name} deactivated")

    def get_status(self) -> Dict[str, Any]:
        """
        Get current agent status.

        Returns:
            Status information dictionary
        """
        return {
            "name": self.agent_name,
            "status": self.status,
            "is_active": self.is_active,
            "capabilities": self.capabilities,
            "dependencies": self.dependencies,
        }
