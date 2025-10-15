# VS Code Configuration for The Agent AI Architect

This directory contains VS Code workspace configuration to optimize the development experience for The Agent AI Architect project.

## 🔧 Key Settings Enabled

### Python Environment Integration
- ✅ `python.terminal.useEnvFile: true` - Automatically loads .env variables in terminals
- ✅ `python.envFile: "${workspaceFolder}/.env"` - Points to project .env file
- ✅ `python.defaultInterpreterPath: "${workspaceFolder}/venv/bin/python"` - Uses project virtual environment
- ✅ `python.terminal.activateEnvironment: true` - Auto-activates venv in terminals

### Code Quality
- ✅ Black formatting on save
- ✅ Flake8 linting enabled
- ✅ Auto import organization
- ✅ Import completions from project paths

### Project Structure
- ✅ Multi-folder workspace (main project + agentic-coder)
- ✅ Python path includes both src directories
- ✅ Proper file associations and exclusions

## 📁 Files

- `settings.json` - Project-wide VS Code settings
- `../agent-ai-architect.code-workspace` - Multi-folder workspace definition

## 🚀 Usage

### Option 1: Open Workspace File
```bash
code agent-ai-architect.code-workspace
```

### Option 2: VS Code will automatically detect settings.json
- Open the project folder in VS Code
- Settings will be applied automatically
- Terminal will use .env file variables

### Option 3: Manual Setting (if needed)
1. Open VS Code Command Palette (Cmd+Shift+P)
2. Type "Preferences: Open Settings (JSON)"
3. Add: `"python.terminal.useEnvFile": true`

## ✅ Verification

After setup, you should see:
- Terminal automatically loads environment variables from .env
- Python interpreter points to venv/bin/python
- Code formatting and linting work automatically
- Import suggestions include project modules

## 🔑 Environment Variables

The configuration automatically loads these from `.env`:
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `LANGCHAIN_API_KEY`
- All other project environment variables

No more manual environment variable setup needed! 🎉