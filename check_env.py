#!/usr/bin/env python3
"""
The Agent AI Architect - Environment Status Check
Version: 1.0
Date: October 15, 2025
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version meets requirements"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} (meets requirements)")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (requires Python 3.10+)")
        return False

def check_virtual_environment():
    """Check if running in virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        print(f"   Virtual env path: {sys.prefix}")
        return True
    else:
        print("⚠️  Not running in virtual environment")
        print("   Recommendation: source venv/bin/activate")
        return False

def check_core_packages():
    """Check if core packages are installed"""
    packages = [
        'langchain',
        'openai',
        'anthropic',
        'pydantic',
        'dotenv',
    ]
    
    print("\n📦 Core Package Status:")
    all_installed = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (not installed)")
            all_installed = False
    
    return all_installed

def check_project_structure():
    """Check project structure"""
    print("\n📁 Project Structure:")
    
    required_paths = [
        "System Prompts/01-Orchestrator-Architect",
        "System Prompts/02-Analyzer-Architect", 
        "agentic-coder",
        "venv",
        ".env.template"
    ]
    
    all_present = True
    for path in required_paths:
        if Path(path).exists():
            print(f"✅ {path}")
        else:
            print(f"❌ {path} (missing)")
            all_present = False
    
    return all_present

def check_env_file():
    """Check environment configuration"""
    print("\n🔧 Environment Configuration:")
    
    if Path(".env").exists():
        print("✅ .env file exists")
        
        # Check for required env vars
        from dotenv import load_dotenv
        load_dotenv()
        
        required_vars = [
            'OPENAI_API_KEY',
            'ANTHROPIC_API_KEY',
        ]
        
        for var in required_vars:
            value = os.getenv(var)
            if value and value != f"your_{var.lower()}_here":
                print(f"✅ {var} (configured)")
            else:
                print(f"⚠️  {var} (not configured)")
        
        return True
    else:
        print("⚠️  .env file not found")
        print("   Copy .env.template to .env and add your API keys")
        return False

def main():
    """Main status check"""
    print("🚀 The Agent AI Architect - Environment Status Check")
    print("=" * 50)
    
    checks = [
        check_python_version(),
        check_virtual_environment(),
        check_core_packages(),
        check_project_structure(),
        check_env_file()
    ]
    
    print("\n" + "=" * 50)
    
    if all(checks):
        print("🎉 Environment is ready for development!")
    else:
        print("⚠️  Some issues found. Please resolve them before proceeding.")
        print("\n💡 Quick fixes:")
        print("   1. Activate virtual environment: source venv/bin/activate")
        print("   2. Install dependencies: pip install -r requirements.txt")
        print("   3. Copy .env.template to .env and add API keys")
    
    print("\n📖 Next steps:")
    print("   - Review System Prompts documentation")
    print("   - Test with a simple agent implementation")
    print("   - Explore the agentic-coder framework")

if __name__ == "__main__":
    main()