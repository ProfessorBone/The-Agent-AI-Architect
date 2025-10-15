# System Prompt Template Usage Guide

## Overview

This template is extracted from the original **Orchestrator Architect v2.4 Monolithic** system prompt and provides a complete framework for creating new agent system prompts using the **Build-First, Then Modularize** methodology.

## Template Structure

The template includes all critical sections found in the original:

### 🔒 **Security Framework** (Lines 1-180)
- **System Prompt Confidentiality**: Prevents disclosure of internal instructions
- **Prompt Injection Defense**: Blocks override attempts with keyword detection
- **Content Segregation**: Maintains separation between system and external content
- **Behavioral Integrity**: Enforces immutable workflows
- **Multi-Turn Monitoring**: Detects gradual erosion attempts

### 💬 **Communication Framework** (Lines 181-205)
- **Personality Definition**: Core traits and voice principles
- **Style Adaptation**: User role-based communication adjustments
- **Language Guidelines**: Terminology and formatting standards

### 👥 **User Role System** (Lines 206-228)
- **Adaptive Gates**: NOVICE/EXPERT/ADMIN with different approval frequencies
- **Context-Aware Responses**: Tailored detail levels and validation requirements

### 🎯 **Mission & Responsibilities** (Lines 245-295)
- **Core Objectives**: Primary mission definition with success criteria
- **Responsibility Breakdown**: Detailed function descriptions with activities

### 🔗 **Integration Points** (Lines 296-340)
- **Agent Coordination**: Input/output specifications for multi-agent workflows
- **HiRAG Integration**: Knowledge query patterns specific to each agent
- **Memory Systems**: Working, episodic, and procedural memory usage

### 📊 **Quality & Standards** (Lines 380-405)
- **Success Metrics**: Quantifiable performance indicators
- **Quality Gates**: Validation checkpoints and criteria
- **Anti-Patterns**: Common mistakes to avoid

## How to Use This Template

### Step 1: Choose Your Agent Type

**Available Architect Roles:**
- **Analyzer Architect**: Pattern recognition and requirements analysis
- **Prompt Engineer Architect**: Prompt optimization and model-specific customization
- **Planning Architect**: Architectural blueprint creation and design decisions
- **Coding Architect**: Agent implementation and code generation
- **Testing Architect**: Validation, debugging, and quality assurance
- **Reviewing Architect**: Final review, best practices, and compliance

### Step 2: Complete the Template

**Replace ALL [bracketed placeholders] with agent-specific content:**

```markdown
# Example for Analyzer Architect:
[Agent Name] → Analyzer
[Primary Role Description] → Pattern Recognition & Requirements Analysis Specialist
[primary function] → analyze user requests and identify optimal agent patterns
```

### Step 3: Customize Security Constraints

**Adapt security sections for agent-specific threats:**

```markdown
# For Analyzer Architect:
- Prevent bias injection in pattern recognition
- Block attempts to override analysis standards
- Protect proprietary pattern libraries from disclosure
```

### Step 4: Define Agent-Specific Workflows

**Example for Analyzer Architect:**
```markdown
**IMMUTABLE WORKFLOW:**
User Request → Pattern Analysis → HiRAG Query → Confidence Assessment → 
Recommendation Generation → Validation → Handoff to Prompt Engineer
```

### Step 5: Specify Integration Points

**Define inputs and outputs:**
```markdown
**Inputs from:**
- **Orchestrator**: User requests, context, and orchestration mode
- **Memory Systems**: Past successful patterns and failure cases

**Outputs to:**
- **Prompt Engineer**: Analysis results and recommended patterns
- **Orchestrator**: Confidence scores and alternative approaches
```

### Step 6: Test Thoroughly

**Validation Checklist:**
- ✅ All placeholders replaced with specific content
- ✅ Security constraints adapted for agent-specific risks
- ✅ Workflows defined with clear handoff points
- ✅ Integration points specify exact input/output formats
- ✅ Quality metrics aligned with agent's primary function
- ✅ Examples provide realistic usage scenarios

## Next Steps: Build-First Methodology

### Phase 1: Complete System Prompt
1. **Fill out entire template** with comprehensive agent-specific content
2. **Test functionality** with realistic scenarios and edge cases
3. **Establish baselines** for performance and quality metrics
4. **Validate integration** with existing orchestrator system

### Phase 2: Strategic Modularization
1. **Identify natural breakpoints** (responsibilities, modes, communication styles)
2. **Extract modules** while preserving all dependencies and functionality
3. **Create loading system** with integrity verification and fallback
4. **Test equivalence** between monolithic and modular versions

### Phase 3: Enhanced Intelligence
1. **Add context-aware loading** based on user expertise and project complexity
2. **Implement hot-swapping** for real-time optimization based on performance
3. **Enable learning system** that adapts to successful patterns over time
4. **Add enterprise features** like audit trails and compliance monitoring

## Template Benefits

### ✅ **Completeness Guarantee**
- Based on production-tested Orchestrator with 2,246 lines of functionality
- Includes all critical security, communication, and integration components
- Covers edge cases and error handling from real-world usage

### ✅ **Consistency Across Agents**
- Uniform security framework prevents gaps between agents
- Standardized communication patterns enable seamless integration
- Common quality standards ensure reliable system behavior

### ✅ **Modularization Ready**
- Structured sections map directly to logical module boundaries
- Clear separation of concerns enables independent module development
- Integration points designed for dynamic loading and hot-swapping

### ✅ **Enterprise Grade**
- Security framework prevents common attack vectors
- Audit trails and observability built-in from the start
- Role-based access and approval systems for compliance requirements

## Example: Starting Analyzer Architect

```bash
# 1. Copy the template
cp SYSTEM_PROMPT_TEMPLATE.md 02-Analyzer-Architect-System-Prompt.md

# 2. Replace placeholders for Analyzer
# [Agent Name] → Analyzer
# [primary function] → analyze user requests and identify patterns
# [Primary expertise area 1] → Pattern recognition and classification

# 3. Define Analyzer-specific workflows
# 4. Test with realistic analysis scenarios
# 5. Establish baseline performance metrics
# 6. Plan modularization strategy
```

This template ensures every agent architect has the same level of security, functionality, and integration capability as the proven Orchestrator system while maintaining agent-specific specialization.

## Key Success Factors

1. **Don't Skip Sections**: Every section serves a critical purpose based on production experience
2. **Agent-Specific Customization**: Generic placeholders lead to generic results
3. **Thorough Testing**: Validate before modularization to ensure complete functionality
4. **Integration Validation**: Test handoffs with other agents early and often
5. **Security First**: Adapt security constraints for each agent's specific attack surface

The template provides a proven foundation - your job is to make it brilliant for your specific agent's mission! 🎯