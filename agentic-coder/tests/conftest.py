"""Test configuration and fixtures."""

import pytest
from pathlib import Path
from typing import Generator

from agentic_coder.config import Settings


@pytest.fixture
def temp_config() -> Generator[Settings, None, None]:
    """Provide a temporary configuration for testing."""
    config = Settings()
    config.development.debug = True
    config.agent.max_iterations = 5
    config.memory.working_memory_size = 10
    yield config


@pytest.fixture
def sample_code_file(tmp_path: Path) -> Path:
    """Create a sample Python file for testing."""
    code_file = tmp_path / "sample.py"
    code_file.write_text("""
def hello_world():
    \"\"\"A simple hello world function.\"\"\"
    return "Hello, World!"

class Calculator:
    \"\"\"A simple calculator class.\"\"\"
    
    def add(self, a: int, b: int) -> int:
        return a + b
        
    def subtract(self, a: int, b: int) -> int:
        return a - b
""")
    return code_file


@pytest.fixture
def sample_project_dir(tmp_path: Path) -> Path:
    """Create a sample project directory structure."""
    project_dir = tmp_path / "sample_project"
    project_dir.mkdir()
    
    # Create main.py
    main_file = project_dir / "main.py"
    main_file.write_text("""
from calculator import Calculator

def main():
    calc = Calculator()
    result = calc.add(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()
""")
    
    # Create calculator.py
    calc_file = project_dir / "calculator.py"
    calc_file.write_text("""
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
        
    def subtract(self, a: int, b: int) -> int:
        return a - b
        
    def multiply(self, a: int, b: int) -> int:
        return a * b
        
    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
""")
    
    # Create README.md
    readme_file = project_dir / "README.md"
    readme_file.write_text("""
# Sample Project

A simple calculator project for testing.

## Features
- Basic arithmetic operations
- Error handling for division by zero
""")
    
    return project_dir


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing."""
    return {
        "content": "This is a mock response from the LLM.",
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 50,
            "total_tokens": 150
        }
    }