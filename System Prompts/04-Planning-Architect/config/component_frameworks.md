# Component Frameworks - Planning Architect

**Module Type:** OPTIONAL (Context-Aware Loading)
**Load When:** Performing component decomposition, state schema design, or implementation sequencing
**Version:** 3.0
**Last Updated:** October 16, 2025

## Component Decomposition Framework

### Systematic Decomposition Process

Break down complex systems into implementable components with clear dependencies, interfaces, and build sequences.

```python
class ComponentDecompositionEngine:
    """Systematic component decomposition with dependency analysis"""

    def decompose_system(self, requirements, pattern):
        """Break down system into implementable components"""

        # Step 1: Identify primary components
        primary_components = self.identify_primary_components(requirements, pattern)

        # Step 2: Define component interfaces
        interfaces = self.define_component_interfaces(primary_components)

        # Step 3: Analyze dependencies
        dependencies = self.analyze_component_dependencies(primary_components)

        # Step 4: Determine build sequence
        build_sequence = self.determine_build_sequence(dependencies)

        # Step 5: Identify shared components
        shared_components = self.identify_shared_components(primary_components)

        return {
            'components': primary_components,
            'interfaces': interfaces,
            'dependencies': dependencies,
            'build_sequence': build_sequence,
            'shared_components': shared_components,
            'critical_path': self.identify_critical_path(dependencies),
            'parallel_opportunities': self.identify_parallel_tracks(dependencies)
        }

    def analyze_component_dependencies(self, components):
        """Create comprehensive dependency graph"""
        dependency_graph = {}

        for component in components:
            dependencies = []

            # Data dependencies
            if component.requires_data_from:
                dependencies.extend(component.requires_data_from)

            # Functional dependencies
            if component.calls_functions_from:
                dependencies.extend(component.calls_functions_from)

            # State dependencies
            if component.reads_state_from:
                dependencies.extend(component.reads_state_from)

            dependency_graph[component.name] = {
                'dependencies': dependencies,
                'dependency_type': self.classify_dependency_types(dependencies),
                'criticality': self.assess_dependency_criticality(component)
            }

        return dependency_graph
```

### Component Types

**Primary Component Types:**

1. **Agent Components**
   - Purpose: Autonomous decision-making entities
   - Responsibilities: Reasoning, action selection, tool usage
   - Dependencies: Tools, memory, LLM

2. **Node Components**
   - Purpose: Processing units in workflow
   - Responsibilities: Execute specific logic, transform state
   - Dependencies: State schema, other nodes

3. **Edge Components**
   - Purpose: Routing and flow control
   - Responsibilities: Conditional routing, state-based decisions
   - Dependencies: State schema, routing logic

4. **Tool Components**
   - Purpose: External functionality integration
   - Responsibilities: API calls, data retrieval, actions
   - Dependencies: External APIs, credentials

5. **State Components**
   - Purpose: Data structure and persistence
   - Responsibilities: State management, validation, transitions
   - Dependencies: Type system, validation rules

6. **Memory Components**
   - Purpose: Context and history management
   - Responsibilities: Store/retrieve context, conversation history
   - Dependencies: Storage backend, retrieval logic

### Decomposition Methodology

**Step-by-Step Process:**

1. **Identify Core Functionality**
   - What must the system do?
   - What are the primary user interactions?
   - What are the key workflows?

2. **Map to Component Types**
   - Which functionality maps to agents?
   - Which requires custom nodes?
   - What tools are needed?

3. **Define Interfaces**
   - What data flows between components?
   - What are the input/output contracts?
   - What are the API signatures?

4. **Analyze Dependencies**
   - Which components depend on others?
   - What is the dependency type (data, functional, temporal)?
   - Are there circular dependencies?

5. **Optimize Structure**
   - Can components be combined?
   - Are there reusable patterns?
   - How to minimize coupling?

---

## State Schema Design Excellence

### Optimal State Design Principles

Create optimal state structures that are type-safe, efficient, and maintainable.

```python
class StateSchemaDesigner:
    """Systematic state schema design with validation"""

    def design_optimal_state_schema(self, requirements, pattern):
        """Design optimal state structure for the system"""

        # Step 1: Identify state requirements
        state_requirements = self.identify_state_requirements(requirements)

        # Step 2: Design state structure
        state_structure = self.design_state_structure(state_requirements, pattern)

        # Step 3: Define data types
        data_types = self.define_data_types(state_structure)

        # Step 4: Create validation rules
        validation_rules = self.create_validation_rules(state_structure)

        # Step 5: Plan state transitions
        state_transitions = self.plan_state_transitions(state_structure, pattern)

        # Step 6: Design persistence strategy
        persistence = self.design_persistence_strategy(state_structure)

        return {
            'state_schema': state_structure,
            'data_types': data_types,
            'validation_rules': validation_rules,
            'state_transitions': state_transitions,
            'persistence_strategy': persistence,
            'optimization_notes': self.generate_optimization_notes(state_structure)
        }

    def design_state_structure(self, requirements, pattern):
        """Design optimal state structure based on pattern"""

        if pattern == 'ReAct':
            return {
                'input': 'str - User input/query',
                'agent_outcome': 'Union[AgentAction, AgentFinish] - Agent decision',
                'intermediate_steps': 'List[Tuple[AgentAction, str]] - Tool execution history',
                'chat_history': 'List[BaseMessage] - Conversation history (optional)',
                'metadata': 'Dict[str, Any] - Additional context'
            }

        elif pattern == 'Supervisor-Worker':
            return {
                'messages': 'List[BaseMessage] - Communication history',
                'next_agent': 'str - Next agent to execute',
                'current_task': 'str - Current task description',
                'task_results': 'Dict[str, Any] - Aggregated worker results',
                'supervisor_decision': 'str - Supervisor routing decision'
            }

        elif pattern == 'Hierarchical':
            return {
                'task_hierarchy': 'Dict[str, Any] - Task decomposition tree',
                'current_level': 'int - Current hierarchy level',
                'level_results': 'Dict[int, List[Any]] - Results per level',
                'aggregation_strategy': 'str - How to combine results',
                'coordination_state': 'Dict[str, Any] - Inter-level coordination'
            }

        # Custom pattern - design from requirements
        return self.design_custom_state_structure(requirements)
```

### Pattern-Specific State Schemas

**ReAct Pattern:**
```python
from typing import TypedDict, Union, List, Tuple
from langchain.schema import AgentAction, AgentFinish

class AgentState(TypedDict):
    input: str
    agent_outcome: Union[AgentAction, AgentFinish]
    intermediate_steps: List[Tuple[AgentAction, str]]
```

**Supervisor-Worker Pattern:**
```python
from typing import TypedDict, List, Dict, Any
from langchain.schema import BaseMessage

class SupervisorState(TypedDict):
    messages: List[BaseMessage]
    next_agent: str
    current_task: str
    task_results: Dict[str, Any]
```

**Hierarchical Pattern:**
```python
from typing import TypedDict, Dict, List, Any

class HierarchicalState(TypedDict):
    task_hierarchy: Dict[str, Any]
    current_level: int
    level_results: Dict[int, List[Any]]
    aggregation_strategy: str
    coordination_state: Dict[str, Any]
```

### State Design Best Practices

1. **Use TypedDict for LangGraph**
   - Required by LangGraph StateGraph
   - Provides type hints without runtime overhead
   - Clear state structure documentation

2. **Add Pydantic for Validation**
   - Runtime validation at boundaries
   - Rich error messages
   - Default values and constraints

3. **Keep State Minimal**
   - Only include necessary data
   - Avoid redundant information
   - Consider memory overhead

4. **Plan for Persistence**
   - How will state be checkpointed?
   - What needs to be persisted?
   - Serialization requirements?

5. **Consider State Evolution**
   - Will schema change over time?
   - Backward compatibility strategy?
   - Migration path for breaking changes?

---

## Implementation Sequencing & Critical Path

### Build Sequence Optimization

Determine optimal implementation order with parallelization opportunities.

```python
class ImplementationSequencer:
    """Optimize implementation sequence with critical path analysis"""

    def optimize_build_sequence(self, components, dependencies):
        """Determine optimal build sequence with parallel opportunities"""

        # Step 1: Topological sort for dependency order
        sorted_components = self.topological_sort(components, dependencies)

        # Step 2: Identify critical path
        critical_path = self.identify_critical_path(sorted_components, dependencies)

        # Step 3: Find parallel opportunities
        parallel_tracks = self.identify_parallel_tracks(sorted_components, dependencies)

        # Step 4: Optimize for development efficiency
        optimized_sequence = self.optimize_for_efficiency(
            sorted_components, critical_path, parallel_tracks
        )

        # Step 5: Create phased implementation plan
        implementation_phases = self.create_implementation_phases(optimized_sequence)

        return {
            'build_sequence': optimized_sequence,
            'critical_path': critical_path,
            'parallel_tracks': parallel_tracks,
            'implementation_phases': implementation_phases,
            'estimated_timeline': self.estimate_implementation_timeline(implementation_phases),
            'risk_assessment': self.assess_implementation_risks(implementation_phases)
        }

    def create_implementation_phases(self, optimized_sequence):
        """Create phased implementation plan with milestones"""
        phases = []

        current_phase = {
            'phase_number': 1,
            'phase_name': 'Foundation',
            'components': [],
            'objectives': [],
            'validation_criteria': []
        }

        for component in optimized_sequence:
            if self.should_start_new_phase(component, current_phase):
                phases.append(current_phase)
                current_phase = self.create_new_phase(len(phases) + 1)

            current_phase['components'].append(component)
            current_phase['objectives'].extend(component.objectives)
            current_phase['validation_criteria'].extend(component.validation_criteria)

        phases.append(current_phase)

        return phases
```

### Phased Implementation Strategy

**Phase 1: Foundation**
- State schema definition
- Core data structures
- Basic type definitions
- Configuration setup

**Validation Criteria:**
- State schema compiles
- Types are correct
- No circular dependencies

**Phase 2: Core Components**
- Primary agents/nodes
- Essential tools
- Basic routing logic

**Validation Criteria:**
- Components instantiate successfully
- Tools execute without errors
- Basic workflow functions

**Phase 3: Integration**
- Connect components
- Implement edges/routing
- Add error handling
- State transitions

**Validation Criteria:**
- End-to-end workflow executes
- State updates correctly
- Errors handled gracefully

**Phase 4: Enhancement**
- Add advanced features
- Optimize performance
- Implement monitoring
- Add testing

**Validation Criteria:**
- All features functional
- Performance meets targets
- Tests pass

**Phase 5: Production Readiness**
- Security hardening
- Production configuration
- Documentation
- Deployment preparation

**Validation Criteria:**
- Security audit passed
- Documentation complete
- Ready for deployment

### Critical Path Analysis

**Identify Critical Components:**

1. **Must-have for MVP**
   - Core state schema
   - Primary workflow nodes
   - Essential tools

2. **Blocking Dependencies**
   - Components that block others
   - Long implementation time
   - High complexity

3. **Resource Constraints**
   - Components requiring specialized skills
   - External dependencies
   - Third-party integrations

**Optimization Strategies:**

- **Parallelize Non-Dependent Components**
  - Multiple developers can work simultaneously
  - Reduce overall timeline
  - Increase throughput

- **Prioritize Critical Path**
  - Focus on blocking components first
  - Ensure dependencies are ready
  - Minimize idle time

- **Risk Mitigation**
  - Identify high-risk components early
  - Add buffer time for complex items
  - Plan for contingencies

---

## Architectural Blueprint Structure

### Comprehensive Blueprint Template

Every blueprint MUST include these sections:

```python
architectural_blueprint = {
    'metadata': {
        'blueprint_id': str,
        'version': str,
        'created_at': datetime,
        'pattern': str,              # ReAct, Supervisor-Worker, Hierarchical, etc.
        'framework': str,            # langgraph, crewai, autogen
        'complexity': str,           # simple, medium, complex, enterprise
        'estimated_implementation_time': str
    },

    'overview': {
        'system_description': str,
        'primary_objectives': list,
        'key_features': list,
        'constraints': list,
        'assumptions': list
    },

    'architecture': {
        'pattern_implementation': {
            'pattern_type': str,
            'pattern_rationale': str,
            'framework_mapping': dict,
            'pattern_variations': list
        },

        'components': [
            {
                'component_id': str,
                'component_type': str,  # agent, node, edge, tool, state
                'name': str,
                'description': str,
                'responsibilities': list,
                'dependencies': list,
                'interfaces': dict,
                'implementation_notes': str
            }
        ],

        'state_schema': {
            'state_structure': dict,
            'data_types': dict,
            'validation_rules': list,
            'state_transitions': list,
            'persistence_strategy': str
        },

        'data_flow': {
            'flow_diagram': str,
            'data_transformations': list,
            'checkpoints': list,
            'error_handling': dict
        },

        'communication_protocols': {
            'inter_agent_communication': dict,
            'message_formats': dict,
            'coordination_mechanisms': list
        }
    },

    'implementation_plan': {
        'build_sequence': [
            {
                'phase': int,
                'phase_name': str,
                'components': list,
                'dependencies': list,
                'estimated_time': str,
                'validation_criteria': list
            }
        ],

        'critical_path': list,
        'parallel_tracks': list,
        'risk_mitigation': dict
    },

    'tool_integration': {
        'required_tools': [
            {
                'tool_name': str,
                'purpose': str,
                'integration_points': list,
                'configuration': dict
            }
        ],
        'api_integrations': list,
        'external_dependencies': list
    },

    '2025_technology_stack': {
        'blueprint_management': ['Git Registry', 'LangSmith'],
        'state_schema_tools': ['Pydantic', 'TypedDict'],
        'orchestration_framework': str,
        'testing_tools': ['Pytest', 'LangSmith Testing'],
        'monitoring_tools': ['LangSmith Monitoring', 'OpenTelemetry'],
        'visual_tools': ['Mermaid'],
        'justification': str
    },

    'security_design': {
        'authentication_strategy': dict,
        'authorization_model': dict,
        'data_protection': dict,
        'audit_logging': dict,
        'compliance_considerations': list
    },

    'quality_assurance': {
        'testing_strategy': dict,
        'validation_checkpoints': list,
        'performance_targets': dict,
        'monitoring_plan': dict
    },

    'evaluation_metrics': {
        'technical_soundness': float,
        'implementation_clarity': float,
        'completeness': float,
        'scalability': float,
        'maintainability': float,
        'security_compliance': float,
        'composite_score': float
    }
}
```

---

## Dependency Analysis Best Practices

### Types of Dependencies

1. **Data Dependencies**
   - Component A requires data produced by Component B
   - Example: Agent node requires state schema definition

2. **Functional Dependencies**
   - Component A calls functions from Component B
   - Example: Tool node requires tool definition

3. **Temporal Dependencies**
   - Component A must be built before Component B
   - Example: State schema before nodes that use it

4. **Resource Dependencies**
   - Component A requires external resource used by Component B
   - Example: Both components need same API

### Dependency Resolution Strategies

**1. Topological Sorting**
- Order components based on dependencies
- Ensures dependencies built first
- Detects circular dependencies

**2. Layered Architecture**
- Group components into layers
- Each layer depends only on lower layers
- Clear separation of concerns

**3. Dependency Injection**
- Components receive dependencies
- Loose coupling
- Easier testing

**4. Interface-Based Design**
- Define interfaces first
- Implement components independently
- Integrate via interfaces

---

**Usage:** Load this module when performing detailed component decomposition, state schema design, or implementation planning. Reference specific sections as needed for the current design task.
