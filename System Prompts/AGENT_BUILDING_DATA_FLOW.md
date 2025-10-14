# Agent Building with Dynamic Loading - Complete Data Flow

## 🔄 **Step-by-Step: How We Use Directory Files to Build Agents**

### **1. User Makes Request**
```python
user_request = "Create a LangGraph research agent with web search"
user_context = {
    'user_role': 'EXPERT',
    'orchestration_mode': 'STANDARD',
    'security_level': 'high'
}
```

### **2. Orchestrator Queries Module Registry**
```python
# Load module registry from YAML file
registry_path = Path('System Prompts/01-Orchestrator-Architect/config/module_registry.yaml')
registry = ModuleRegistry(registry_path)

# Registry loads ALL module metadata from YAML
with open(registry_path, 'r') as f:
    registry_data = yaml.safe_load(f)
    
# Now registry knows about all available modules:
# - injection_defense.md (security)
# - orchestration_core.md (governance) 
# - personality_core.md (communication)
# - langgraph_patterns.md (framework-specific)
# etc.
```

### **3. Context-Aware Module Selection**
```python
# Based on user context, select relevant modules
selected_modules = registry.select_modules({
    'agent_type': AgentType.ORCHESTRATOR,
    'user_role': 'EXPERT',           # → Skip pedagogical modules
    'orchestration_mode': 'STANDARD', # → Load standard modules
    'security_level': 'high',        # → Load security modules
    'framework': 'langgraph',        # → Load LangGraph-specific modules
    'features': ['web_search']       # → Load tool integration modules
})

# Result: Only 6 of 15 modules selected
# [orchestration_core, injection_defense, langgraph_patterns, 
#  tool_integration, efficiency_optimizations, audit_logging]
```

### **4. Dynamic File Loading & Composition**
```python
async def compose_agent_prompt(selected_modules: List[ModuleMetadata]) -> str:
    """
    Dynamically load and compose prompt from selected module files
    """
    
    # Start with bootstrap core (always loaded)
    bootstrap_path = Path('System Prompts/01-Orchestrator-Architect/01-Orchestrator-Architect-System-Prompt.md')
    with open(bootstrap_path, 'r') as f:
        core_prompt = f.read()
    
    # Load each selected module's content
    module_contents = {}
    for module in selected_modules:
        # Read actual file content
        with open(module.file_path, 'r') as f:
            content = f.read()
            
        # Verify integrity
        actual_hash = compute_sha256(content)
        if actual_hash != module.sha256_hash:
            raise SecurityError(f"Module {module.id} integrity check failed!")
            
        module_contents[module.id] = content
    
    # Compose final agent prompt
    final_prompt = f"""
{core_prompt}

## DYNAMICALLY LOADED MODULES

### Security Layer
{module_contents.get('injection_defense', '')}

### Orchestration Core  
{module_contents.get('orchestration_core', '')}

### Framework Patterns
{module_contents.get('langgraph_patterns', '')}

### Tool Integration
{module_contents.get('tool_integration', '')}

### Efficiency Optimizations
{module_contents.get('efficiency_optimizations', '')}

### Audit & Compliance
{module_contents.get('audit_logging', '')}
"""
    
    return final_prompt
```

### **5. Agent Instantiation with Live Content**
```python
# The agent gets the ACTUAL file contents as its prompt
agent_prompt = await compose_agent_prompt(selected_modules)

# Create the agent with this dynamic prompt
orchestrator_agent = OrchestratorAgent(
    prompt=agent_prompt,  # Contains real content from files
    model="llama-3.1-70b",
    context=user_context
)

# Agent now has all the knowledge from the loaded modules
```

## 📁 **Detailed Directory Usage**

### **File Structure We Actually Use**
```
System Prompts/01-Orchestrator-Architect/
├── 01-Orchestrator-Architect-System-Prompt.md     # ← ALWAYS loaded (bootstrap)
├── config/
│   ├── orchestrator.yaml                          # ← Defines loading rules
│   ├── module_registry.yaml                       # ← Module metadata & paths
│   ├── security/
│   │   ├── injection_defense.md                   # ← Loaded if security_level=high
│   │   ├── canary_monitoring.md                   # ← Loaded if user_role=ADMIN
│   │   └── audit_logging.md                       # ← Loaded if compliance required
│   ├── governance/
│   │   ├── orchestration_core.md                  # ← ALWAYS for orchestrator
│   │   ├── consensus_mechanisms.md                # ← Loaded for multi-agent tasks
│   │   └── approval_gates.md                      # ← Loaded if human-in-loop
│   └── communication/
│       ├── personality_core.md                    # ← ALWAYS loaded
│       ├── style_pedagogical.md                   # ← Loaded if user_role=NOVICE
│       └── style_professional.md                  # ← Loaded if user_role=EXPERT
```

### **Real Example: Expert User Building LangGraph Agent**

**Input:**
```python
request = {
    'task': 'Create LangGraph research agent',
    'user_role': 'EXPERT', 
    'security_level': 'high',
    'framework': 'langgraph'
}
```

**Files Actually Loaded:**
```python
# 1. Bootstrap (ALWAYS)
bootstrap = load_file('01-Orchestrator-Architect-System-Prompt.md')  # 341 lines

# 2. Security (security_level=high)
security = load_file('config/security/injection_defense.md')          # 538 lines

# 3. Core Orchestration (agent_type=ORCHESTRATOR) 
governance = load_file('config/governance/orchestration_core.md')     # 643 lines

# 4. Framework Patterns (framework=langgraph)
patterns = load_file('config/patterns/langgraph_patterns.md')         # 387 lines

# 5. Expert Optimizations (user_role=EXPERT)
optimizations = load_file('config/optimizations/expert_features.md')  # 289 lines

# 6. Communication (ALWAYS, but professional style for EXPERT)
communication = load_file('config/communication/style_professional.md') # 234 lines

# Total: ~2,432 lines of RELEVANT content vs 8,500+ monolithic
```

**Files NOT Loaded (Token Savings):**
```python
# Skipped because user_role=EXPERT (not NOVICE)
❌ 'config/communication/style_pedagogical.md'      # 287 lines saved
❌ 'config/guidance/enhanced_explanations.md'       # 456 lines saved
❌ 'config/examples/beginner_templates.md'          # 623 lines saved

# Skipped because orchestration_mode=STANDARD (not CRITICAL)  
❌ 'config/security/enhanced_monitoring.md'         # 345 lines saved
❌ 'config/governance/emergency_protocols.md'       # 234 lines saved

# Skipped because framework=langgraph (not crewai)
❌ 'config/patterns/crewai_patterns.md'             # 412 lines saved
❌ 'config/patterns/autogen_patterns.md'            # 378 lines saved

# Total Saved: ~2,735 lines (50%+ reduction)
```

## 🔄 **Hot-Swapping: Real-Time File Updates**

### **When Performance Drops**
```python
# Monitor agent performance
if effectiveness_score < 0.6:
    print("⚠️  Agent struggling - swapping modules...")
    
    # Unload current modules
    await unload_module('complex_reasoning')
    
    # Load different file  
    fast_reasoning_content = load_file('config/reasoning/fast_reasoning.md')
    await load_module('fast_reasoning', fast_reasoning_content)
    
    # Agent now uses NEW file content without restart
    print("✅ Swapped to fast_reasoning module")
```

### **When Security Threat Detected**
```python
if security_risk_score > 0.7:
    print("🚨 Security threat detected - escalating...")
    
    # Load additional security files
    enhanced_security = load_file('config/security/enhanced_monitoring.md')
    threat_detection = load_file('config/security/active_defense.md')
    
    await load_modules([enhanced_security, threat_detection])
    
    print("🔒 Enhanced security modules loaded")
```

## 💡 **Key Insights: Directory → Agent Pipeline**

### **1. Files Are The Source of Truth**
- Every module is a **real markdown file** in the directory
- Module registry (`module_registry.yaml`) just points to the files
- Agent gets **actual file contents** as its knowledge

### **2. Dynamic = Selective File Loading** 
- We don't load ALL files every time
- Context determines WHICH files to read
- Saves 50-70% tokens by skipping irrelevant files

### **3. Hot-Swapping = Live File Replacement**
- Performance issues → swap to different files
- New requirements → load additional files  
- Agent behavior changes based on which files are loaded

### **4. Integrity = File Verification**
- SHA-256 hash ensures files haven't been tampered with
- Load-time verification prevents corrupted modules
- Audit trail tracks which files were used when

## 🎯 **Bottom Line**

**YES** - we absolutely use the files from the directory when building each agent. But we do it **intelligently**:

1. **Bootstrap Core**: Always load the main system prompt file
2. **Context Selection**: Choose relevant module files based on user/task
3. **Dynamic Composition**: Combine selected file contents into agent prompt
4. **Integrity Verification**: Ensure files haven't been corrupted
5. **Performance Monitoring**: Track which file combinations work best
6. **Hot-Swapping**: Replace files in real-time if performance drops

The **magic** is that we transform **static directory files** into **dynamic, adaptive agent intelligence** that learns and improves over time while maintaining the security and auditability of file-based configuration.
