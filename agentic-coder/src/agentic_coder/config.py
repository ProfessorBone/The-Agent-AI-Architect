"""Configuration management for agentic-coder."""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseSettings, Field
from pydantic_settings import SettingsConfigDict


class OpenAIConfig(BaseSettings):
    """OpenAI API configuration."""
    
    api_key: str = Field(..., env="OPENAI_API_KEY")
    org_id: Optional[str] = Field(None, env="OPENAI_ORG_ID")
    model: str = Field("gpt-4", env="OPENAI_MODEL")
    
    model_config = SettingsConfigDict(env_prefix="OPENAI_")


class VLLMConfig(BaseSettings):
    """vLLM configuration for local models."""
    
    api_base: str = Field("http://localhost:8000", env="VLLM_API_BASE")
    model_name: str = Field("codellama/CodeLlama-7b-Python-hf", env="VLLM_MODEL_NAME")
    
    model_config = SettingsConfigDict(env_prefix="VLLM_")


class Neo4jConfig(BaseSettings):
    """Neo4j database configuration."""
    
    uri: str = Field("bolt://localhost:7687", env="NEO4J_URI")
    username: str = Field("neo4j", env="NEO4J_USERNAME")
    password: str = Field(..., env="NEO4J_PASSWORD")
    database: str = Field("agentic_coder", env="NEO4J_DATABASE")
    
    model_config = SettingsConfigDict(env_prefix="NEO4J_")


class ChromaConfig(BaseSettings):
    """ChromaDB configuration."""
    
    host: str = Field("localhost", env="CHROMA_HOST")
    port: int = Field(8001, env="CHROMA_PORT")
    persist_directory: str = Field("./data/chroma_db", env="CHROMA_PERSIST_DIRECTORY")
    
    model_config = SettingsConfigDict(env_prefix="CHROMA_")


class LoggingConfig(BaseSettings):
    """Logging configuration."""
    
    level: str = Field("INFO", env="LOG_LEVEL")
    file_path: str = Field("./data/logs/agentic_coder.log", env="LOG_FILE_PATH")
    max_size: str = Field("10MB", env="LOG_MAX_SIZE")
    backup_count: int = Field(5, env="LOG_BACKUP_COUNT")
    
    model_config = SettingsConfigDict(env_prefix="LOG_")


class AgentConfig(BaseSettings):
    """Agent system configuration."""
    
    max_iterations: int = Field(10, env="MAX_ITERATIONS")
    timeout: int = Field(300, env="AGENT_TIMEOUT")
    enable_reflection: bool = Field(True, env="ENABLE_REFLECTION")
    enable_learning: bool = Field(True, env="ENABLE_LEARNING")
    max_concurrent_agents: int = Field(5, env="MAX_CONCURRENT_AGENTS")
    
    model_config = SettingsConfigDict(env_prefix="AGENT_")


class MemoryConfig(BaseSettings):
    """Memory system configuration."""
    
    working_memory_size: int = Field(50, env="WORKING_MEMORY_SIZE")
    episodic_memory_size: int = Field(1000, env="EPISODIC_MEMORY_SIZE")
    semantic_memory_size: int = Field(10000, env="SEMANTIC_MEMORY_SIZE")
    
    model_config = SettingsConfigDict(env_prefix="MEMORY_")


class ToolConfig(BaseSettings):
    """Tool system configuration."""
    
    enable_file_operations: bool = Field(True, env="ENABLE_FILE_OPERATIONS")
    enable_code_execution: bool = Field(True, env="ENABLE_CODE_EXECUTION")
    enable_web_search: bool = Field(False, env="ENABLE_WEB_SEARCH")
    sandbox_mode: bool = Field(True, env="SANDBOX_MODE")
    
    allowed_file_extensions: List[str] = Field(
        [".py", ".js", ".ts", ".md", ".txt", ".json", ".yaml", ".yml"],
        env="ALLOWED_FILE_EXTENSIONS"
    )
    blocked_directories: List[str] = Field(
        ["/etc", "/usr", "/bin", "/sbin", "/system"],
        env="BLOCKED_DIRECTORIES"
    )
    max_file_size: str = Field("10MB", env="MAX_FILE_SIZE")
    
    model_config = SettingsConfigDict(env_prefix="TOOL_")


class DevelopmentConfig(BaseSettings):
    """Development configuration."""
    
    debug: bool = Field(False, env="DEBUG")
    enable_profiling: bool = Field(False, env="ENABLE_PROFILING")
    cache_enabled: bool = Field(True, env="CACHE_ENABLED")
    cache_ttl: int = Field(3600, env="CACHE_TTL")
    
    model_config = SettingsConfigDict(env_prefix="DEV_")


class PerformanceConfig(BaseSettings):
    """Performance configuration."""
    
    batch_size: int = Field(10, env="BATCH_SIZE")
    embedding_batch_size: int = Field(100, env="EMBEDDING_BATCH_SIZE")
    
    model_config = SettingsConfigDict(env_prefix="PERF_")


class UIConfig(BaseSettings):
    """UI configuration."""
    
    rich_console_width: int = Field(120, env="RICH_CONSOLE_WIDTH")
    enable_progress_bars: bool = Field(True, env="ENABLE_PROGRESS_BARS")
    show_timestamps: bool = Field(True, env="SHOW_TIMESTAMPS")
    
    model_config = SettingsConfigDict(env_prefix="UI_")


class Settings(BaseSettings):
    """Main settings class that combines all configuration sections."""
    
    # Configuration sections
    openai: OpenAIConfig = Field(default_factory=OpenAIConfig)
    vllm: VLLMConfig = Field(default_factory=VLLMConfig)
    neo4j: Neo4jConfig = Field(default_factory=Neo4jConfig)
    chroma: ChromaConfig = Field(default_factory=ChromaConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    agent: AgentConfig = Field(default_factory=AgentConfig)
    memory: MemoryConfig = Field(default_factory=MemoryConfig)
    tool: ToolConfig = Field(default_factory=ToolConfig)
    development: DevelopmentConfig = Field(default_factory=DevelopmentConfig)
    performance: PerformanceConfig = Field(default_factory=PerformanceConfig)
    ui: UIConfig = Field(default_factory=UIConfig)
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    @classmethod
    def load_from_env(cls, env_file: Optional[str] = None) -> "Settings":
        """Load settings from environment file."""
        if env_file and Path(env_file).exists():
            return cls(_env_file=env_file)
        return cls()
    
    def get_data_dir(self) -> Path:
        """Get the data directory path."""
        return Path("./data")
    
    def get_config_dir(self) -> Path:
        """Get the configuration directory path."""
        return Path("./config")
    
    def ensure_directories(self) -> None:
        """Ensure all required directories exist."""
        directories = [
            self.get_data_dir(),
            self.get_data_dir() / "logs",
            self.get_data_dir() / "cache",
            self.get_data_dir() / "models",
            Path(self.chroma.persist_directory),
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings.load_from_env()