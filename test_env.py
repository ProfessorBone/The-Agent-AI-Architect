#!/usr/bin/env python3
"""
Test Environment Variable Loading
This script verifies that VS Code is properly loading environment variables from .env
"""

import os
import sys

from dotenv import load_dotenv

# Load .env file
load_dotenv()

def test_env_loading():
    """Test if environment variables are loaded correctly"""
    print("🔍 Testing Environment Variable Loading")
    print("=" * 40)
    
    # Test variables from .env
    test_vars = [
        'OPENAI_API_KEY',
        'ANTHROPIC_API_KEY',
        'ENVIRONMENT',
        'DEBUG',
        'DEFAULT_LLM_MODEL'
    ]
    
    print("📋 Environment Variables Status:")
    for var in test_vars:
        value = os.getenv(var)
        if value:
            # Don't print actual API keys for security
            if 'API_KEY' in var:
                display_value = f"{value[:8]}..." if len(value) > 8 else "***"
            else:
                display_value = value
            print(f"✅ {var} = {display_value}")
        else:
            print(f"❌ {var} = Not set")
    
    print("\n🐍 Python Environment:")
    print(f"Python executable: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")
    
    print("\n🔧 VS Code Integration Status:")
    if os.getenv('VSCODE_INJECTION') == '1':
        print("✅ Running in VS Code integrated terminal")
    else:
        print("⚠️  Not detected as VS Code integrated terminal")
    
    if os.getenv('ENVIRONMENT') == 'development':
        print("✅ Development environment detected")
    else:
        print("⚠️  Environment not set to development")

if __name__ == "__main__":
    test_env_loading()    test_env_loading()