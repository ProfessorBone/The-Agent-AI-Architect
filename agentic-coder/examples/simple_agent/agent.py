"""
Simple agent example for agentic-coder.
"""

from agentic_coder.agents import BaseAgent
from agentic_coder.tools import ToolRegistry

class SimpleAnalyzerAgent(BaseAgent):
    """A simple code analyzer agent."""
    
    def __init__(self, name: str = "simple_analyzer"):
        super().__init__(name=name, agent_type="analyzer")
        self.tools = ToolRegistry.get_tools(["parser", "linter"])
    
    async def analyze_file(self, file_path: str) -> dict:
        """Analyze a file and return suggestions."""
        # Parse the file
        parse_result = await self.tools["parser"].execute(file_path)
        
        # Lint the file
        lint_result = await self.tools["linter"].execute(file_path)
        
        return {
            "file": file_path,
            "structure": parse_result,
            "issues": lint_result,
            "suggestions": self._generate_suggestions(parse_result, lint_result)
        }
    
    def _generate_suggestions(self, parse_result: dict, lint_result: dict) -> list:
        """Generate improvement suggestions."""
        suggestions = []
        
        # Example suggestion logic
        if lint_result.get("errors"):
            suggestions.append("Fix linting errors before proceeding")
        
        if parse_result.get("complexity", 0) > 10:
            suggestions.append("Consider breaking down complex functions")
        
        return suggestions

# Example usage
async def main():
    agent = SimpleAnalyzerAgent()
    result = await agent.analyze_file("example.py")
    
    print(f"Analysis for {result['file']}:")
    for suggestion in result['suggestions']:
        print(f"- {suggestion}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())