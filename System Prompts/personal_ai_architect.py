"""
Personal AI Architect System - Adaptive Intelligence

Version: 3.1 Personal Edition
Date: October 13, 2025  
Architecture: Self-Learning Dynamic Module System

CORE PRINCIPLE: Learn from Faheem's patterns to provide maximum productivity advantage
- No manual role specification required
- Learns preferences automatically  
- Adapts to individual workflow patterns
- Optimizes for personal competitive advantage
"""
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import yaml
import json
import pickle
from enum import Enum
from collections import defaultdict, deque
import statistics

class UserExpertiseLevel(Enum):
    LEARNING = "learning"      # Still exploring concepts
    PROFICIENT = "proficient"  # Understands patterns well
    EXPERT = "expert"          # Advanced user, wants efficiency
    INNOVATOR = "innovator"    # Creating new patterns

class ProjectComplexity(Enum):
    SIMPLE = "simple"          # Single agent, basic tools
    MODERATE = "moderate"      # Multi-agent, standard patterns
    COMPLEX = "complex"        # Custom frameworks, integrations
    CUTTING_EDGE = "cutting_edge"  # Novel research, experimental

@dataclass
class UserBehaviorPattern:
    """Tracks user behavior to learn preferences"""
    user_id: str = "faheem"
    
    # Interaction History
    session_count: int = 0
    total_projects: int = 0
    successful_builds: int = 0
    
    # Preference Patterns
    preferred_communication_style: str = "direct"
    preferred_detail_level: str = "comprehensive"
    typical_project_complexity: ProjectComplexity = ProjectComplexity.MODERATE
    
    # Learning Indicators
    framework_familiarity: Dict[str, float] = field(default_factory=lambda: {
        "langraph": 0.0,
        "crewai": 0.0, 
        "autogen": 0.0,
        "custom": 0.0
    })
    
    # Time-based Patterns
    productive_hours: List[int] = field(default_factory=list)
    session_durations: deque = field(default_factory=lambda: deque(maxlen=20))
    
    # Success Patterns
    successful_approaches: Dict[str, int] = field(default_factory=dict)
    failed_approaches: Dict[str, int] = field(default_factory=dict)
    
    # Current Session Context
    current_session_start: datetime = field(default_factory=datetime.now)
    current_expertise_indicators: List[str] = field(default_factory=list)
    
    def update_session_start(self):
        """Start a new session"""
        self.current_session_start = datetime.now()
        self.session_count += 1
        self.current_expertise_indicators = []

@dataclass 
class ContextualIntelligence:
    """Learns and adapts to user context automatically"""
    
    def __init__(self):
        self.behavior_file = Path("data/user_behavior.pkl")
        self.behavior = self.load_behavior_patterns()
        
    def load_behavior_patterns(self) -> UserBehaviorPattern:
        """Load existing behavior patterns or create new"""
        if self.behavior_file.exists():
            try:
                with open(self.behavior_file, 'rb') as f:
                    return pickle.load(f)
            except Exception:
                pass
        return UserBehaviorPattern()
    
    def save_behavior_patterns(self):
        """Persist learned patterns"""
        self.behavior_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.behavior_file, 'wb') as f:
            pickle.dump(self.behavior, f)
    
    def analyze_request(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze request to determine user expertise and needs automatically"""
        
        # Update session
        self.behavior.update_session_start()
        
        expertise_indicators = self._detect_expertise_indicators(request)
        complexity = self._assess_project_complexity(request, context)
        urgency = self._detect_urgency_level(request)
        
        # Learn from indicators
        self.behavior.current_expertise_indicators.extend(expertise_indicators)
        
        # Determine current expertise level
        current_expertise = self._calculate_current_expertise()
        
        # Adaptive configuration based on learned patterns
        config = {
            "user_expertise": current_expertise,
            "project_complexity": complexity,
            "urgency_level": urgency,
            "communication_style": self._adapt_communication_style(current_expertise, urgency),
            "detail_level": self._adapt_detail_level(current_expertise, complexity),
            "approval_frequency": self._adapt_approval_frequency(current_expertise, complexity),
            "context_budget": self._calculate_context_budget(complexity, urgency)
        }
        
        return config
    
    def _detect_expertise_indicators(self, request: str) -> List[str]:
        """Detect indicators of user expertise level from request"""
        indicators = []
        
        # Advanced framework knowledge
        advanced_terms = [
            "langraph", "crewai", "autogen", "llamaindex",
            "vector database", "embedding", "retrieval",
            "multi-agent", "hierarchical", "tool calling",
            "state management", "workflow orchestration"
        ]
        
        for term in advanced_terms:
            if term.lower() in request.lower():
                indicators.append(f"knows_{term.replace(' ', '_')}")
        
        # Technical sophistication
        if any(word in request.lower() for word in ["architecture", "pattern", "framework", "integration"]):
            indicators.append("technical_sophisticated")
            
        if any(word in request.lower() for word in ["optimize", "performance", "scalable", "production"]):
            indicators.append("performance_focused")
            
        # Efficiency indicators  
        if any(phrase in request.lower() for phrase in ["quick", "fast", "directly", "skip", "efficient"]):
            indicators.append("efficiency_focused")
            
        return indicators
    
    def _assess_project_complexity(self, request: str, context: Dict[str, Any]) -> ProjectComplexity:
        """Determine project complexity from request and context"""
        
        complexity_score = 0
        
        # Multi-agent indicators
        if any(word in request.lower() for word in ["multi-agent", "team", "coordination", "hierarchical"]):
            complexity_score += 2
            
        # Integration complexity
        if any(word in request.lower() for word in ["database", "api", "integration", "webhook", "pipeline"]):
            complexity_score += 1
            
        # Custom/Novel indicators  
        if any(word in request.lower() for word in ["custom", "novel", "experimental", "research", "new"]):
            complexity_score += 2
            
        # Production indicators
        if any(word in request.lower() for word in ["production", "enterprise", "scalable", "deployment"]):
            complexity_score += 1
            
        # Map score to complexity
        if complexity_score >= 4:
            return ProjectComplexity.CUTTING_EDGE
        elif complexity_score >= 3:
            return ProjectComplexity.COMPLEX  
        elif complexity_score >= 1:
            return ProjectComplexity.MODERATE
        else:
            return ProjectComplexity.SIMPLE
    
    def _detect_urgency_level(self, request: str) -> str:
        """Detect urgency from request language"""
        
        urgent_indicators = ["urgent", "asap", "quickly", "fast", "immediate", "now", "today"]
        if any(word in request.lower() for word in urgent_indicators):
            return "high"
            
        relaxed_indicators = ["explore", "experiment", "learn", "understand", "research"]  
        if any(word in request.lower() for word in relaxed_indicators):
            return "low"
            
        return "medium"
    
    def _calculate_current_expertise(self) -> UserExpertiseLevel:
        """Calculate current expertise based on accumulated patterns"""
        
        # Factor in session count and success rate
        if self.behavior.session_count < 5:
            base_level = UserExpertiseLevel.LEARNING
        elif self.behavior.successful_builds / max(self.behavior.total_projects, 1) > 0.8:
            base_level = UserExpertiseLevel.EXPERT
        else:
            base_level = UserExpertiseLevel.PROFICIENT
            
        # Adjust based on current session indicators
        advanced_indicators = sum(1 for ind in self.behavior.current_expertise_indicators 
                                if "technical" in ind or "performance" in ind or "knows_" in ind)
        
        if advanced_indicators >= 3 and base_level != UserExpertiseLevel.LEARNING:
            return UserExpertiseLevel.INNOVATOR
        elif advanced_indicators >= 2:
            return UserExpertiseLevel.EXPERT
            
        return base_level
    
    def _adapt_communication_style(self, expertise: UserExpertiseLevel, urgency: str) -> str:
        """Adapt communication style based on expertise and urgency"""
        
        if urgency == "high":
            return "direct"  # Always direct when urgent
            
        style_map = {
            UserExpertiseLevel.LEARNING: "pedagogical",
            UserExpertiseLevel.PROFICIENT: "informal", 
            UserExpertiseLevel.EXPERT: "direct",
            UserExpertiseLevel.INNOVATOR: "collaborative"
        }
        
        return style_map.get(expertise, "informal")
    
    def _adapt_detail_level(self, expertise: UserExpertiseLevel, complexity: ProjectComplexity) -> str:
        """Adapt detail level based on expertise and complexity"""
        
        # High complexity always needs comprehensive details
        if complexity in [ProjectComplexity.COMPLEX, ProjectComplexity.CUTTING_EDGE]:
            return "comprehensive"
            
        detail_map = {
            UserExpertiseLevel.LEARNING: "detailed",
            UserExpertiseLevel.PROFICIENT: "moderate",
            UserExpertiseLevel.EXPERT: "focused", 
            UserExpertiseLevel.INNOVATOR: "comprehensive"
        }
        
        return detail_map.get(expertise, "moderate")
    
    def _adapt_approval_frequency(self, expertise: UserExpertiseLevel, complexity: ProjectComplexity) -> str:
        """Adapt approval frequency based on expertise and complexity"""
        
        # Complex projects always need more checkpoints
        if complexity == ProjectComplexity.CUTTING_EDGE:
            return "frequent"
        elif complexity == ProjectComplexity.COMPLEX:
            return "standard"
            
        freq_map = {
            UserExpertiseLevel.LEARNING: "frequent",
            UserExpertiseLevel.PROFICIENT: "standard",
            UserExpertiseLevel.EXPERT: "minimal",
            UserExpertiseLevel.INNOVATOR: "collaborative"  # Ask for input on novel approaches
        }
        
        return freq_map.get(expertise, "standard")
    
    def _calculate_context_budget(self, complexity: ProjectComplexity, urgency: str) -> int:
        """Calculate optimal context budget"""
        
        base_budgets = {
            ProjectComplexity.SIMPLE: 4000,
            ProjectComplexity.MODERATE: 8000,  
            ProjectComplexity.COMPLEX: 12000,
            ProjectComplexity.CUTTING_EDGE: 16000
        }
        
        budget = base_budgets[complexity]
        
        # Reduce for urgent requests (focus on efficiency)
        if urgency == "high":
            budget = int(budget * 0.7)
        elif urgency == "low":
            budget = int(budget * 1.3)  # More context for exploration
            
        return budget
    
    def record_outcome(self, approach: str, success: bool, context: Dict[str, Any]):
        """Record outcome to learn from successes and failures"""
        
        self.behavior.total_projects += 1
        
        if success:
            self.behavior.successful_builds += 1
            self.behavior.successful_approaches[approach] = self.behavior.successful_approaches.get(approach, 0) + 1
        else:
            self.behavior.failed_approaches[approach] = self.behavior.failed_approaches.get(approach, 0) + 1
        
        # Update framework familiarity based on usage
        for framework in self.behavior.framework_familiarity:
            if framework in approach.lower():
                self.behavior.framework_familiarity[framework] += 0.1
        
        # Record session duration
        session_duration = (datetime.now() - self.behavior.current_session_start).total_seconds() / 3600
        self.behavior.session_durations.append(session_duration)
        
        # Save updated patterns
        self.save_behavior_patterns()
    
    def get_personalized_recommendations(self) -> Dict[str, Any]:
        """Get personalized recommendations based on learned patterns"""
        
        # Analyze successful patterns
        top_approaches = sorted(self.behavior.successful_approaches.items(), 
                               key=lambda x: x[1], reverse=True)[:3]
        
        # Analyze productive times
        avg_session_duration = statistics.mean(self.behavior.session_durations) if self.behavior.session_durations else 1.0
        
        # Framework recommendations based on familiarity
        recommended_frameworks = sorted(self.behavior.framework_familiarity.items(),
                                      key=lambda x: x[1], reverse=True)[:2]
        
        return {
            "successful_approaches": top_approaches,
            "optimal_session_duration": avg_session_duration,
            "recommended_frameworks": recommended_frameworks,
            "success_rate": self.behavior.successful_builds / max(self.behavior.total_projects, 1),
            "expertise_trajectory": self._calculate_expertise_trajectory()
        }
    
    def _calculate_expertise_trajectory(self) -> str:
        """Calculate if user is improving over time"""
        
        if len(self.behavior.session_durations) < 3:
            return "insufficient_data"
            
        recent_success = self.behavior.successful_builds / max(self.behavior.total_projects, 1)
        
        if recent_success > 0.8:
            return "mastery_level"
        elif recent_success > 0.6:
            return "improving_rapidly"  
        elif recent_success > 0.4:
            return "steady_progress"
        else:
            return "needs_support"


class PersonalAIArchitect:
    """Main orchestrator that learns and adapts to user automatically"""
    
    def __init__(self):
        self.intelligence = ContextualIntelligence()
        self.current_config = None
        
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process user request with automatic adaptation"""
        
        if context is None:
            context = {}
            
        # Analyze request and determine optimal configuration
        self.current_config = self.intelligence.analyze_request(request, context)
        
        print(f"🧠 Automatically configured for your current expertise level: {self.current_config['user_expertise'].value}")
        print(f"📊 Project complexity detected: {self.current_config['project_complexity'].value}")
        print(f"⚡ Communication style: {self.current_config['communication_style']}")
        
        return self.current_config
    
    def record_session_outcome(self, approach: str, success: bool):
        """Record session outcome for learning"""
        self.intelligence.record_outcome(approach, success, self.current_config or {})
        
        if success:
            print("✅ Success recorded - system learning from this approach")
        else:
            print("📝 Feedback recorded - system will adapt for better results")
    
    def get_personal_insights(self) -> Dict[str, Any]:
        """Get insights about your usage patterns and recommendations"""
        return self.intelligence.get_personalized_recommendations()


# Example usage for Faheem's personal system
if __name__ == "__main__":
    # Initialize personal AI architect
    architect = PersonalAIArchitect()
    
    # Example: Process a request automatically
    config = architect.process_request(
        "I need a multi-agent LangGraph system for production deployment with vector search",
        context={"time_of_day": datetime.now().hour}
    )
    
    print(f"\n🚀 Your personal AI architect automatically configured:")
    print(f"   Expertise Level: {config['user_expertise'].value}")
    print(f"   Communication: {config['communication_style']}")
    print(f"   Detail Level: {config['detail_level']}")
    print(f"   Context Budget: {config['context_budget']} tokens")
    
    # Simulate successful completion
    architect.record_session_outcome("langraph_multi_agent_production", success=True)
    
    # Get personal insights
    insights = architect.get_personal_insights()
    print(f"\n📈 Your Personal AI Advantage:")
    print(f"   Success Rate: {insights['success_rate']:.1%}")
    print(f"   Top Approaches: {[approach[0] for approach in insights['successful_approaches']]}")
    print(f"   Expertise Trajectory: {insights['expertise_trajectory']}")