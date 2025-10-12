# Simple Agent Example

This example demonstrates creating a simple agent using agentic-coder.

## Overview

A basic agent that can analyze code and provide suggestions.

## Usage

```python
from agentic_coder import AgentBuilder

# Create a simple analyzer agent
agent = AgentBuilder.create_agent(
    agent_type="analyzer",
    name="code_analyzer",
    description="Analyzes code for potential improvements"
)

# Use the agent
result = agent.analyze_file("example.py")
print(result.suggestions)
```

## Files

- `agent.py` - Main agent implementation
- `README.md` - This file