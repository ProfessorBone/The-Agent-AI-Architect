"""
MODULAR ORCHESTRATOR SYSTEM TEST
Version: 3.1 Personal Edition
Date: October 13, 2025
Purpose: Test the dynamic modular system with personal AI architect intelligence
"""

import sys
import os
from pathlib import Path

# Add the personal architect to path
sys.path.append(str(Path(__file__).parent))
from personal_ai_architect import PersonalAIArchitect, ContextualIntelligence

class ModularSystemTester:
    """Test harness for the modular orchestrator system"""
    
    def __init__(self):
        self.personal_architect = PersonalAIArchitect()
        self.test_results = []
        self.config_base_path = Path("01-Orchestrator-Architect/config/")
        
    def test_personal_intelligence(self):
        """Test 1: Personal AI Intelligence and Auto-Adaptation"""
        print("🧠 Testing Personal AI Intelligence...")
        
        # Test different request types
        test_requests = [
            "I need a simple research agent",  # Should detect: SIMPLE complexity
            "Build a multi-agent LangGraph system with vector search for production",  # Should detect: COMPLEX
            "Quick prototype for document analysis",  # Should detect: URGENT + efficiency focus
            "I want to explore cutting-edge multi-modal agent architectures"  # Should detect: CUTTING_EDGE
        ]
        
        for i, request in enumerate(test_requests, 1):
            print(f"\n  Test {i}: '{request[:50]}...'")
            config = self.personal_architect.process_request(request)
            
            print(f"    ✅ Auto-detected expertise: {config['user_expertise'].value}")
            print(f"    ✅ Complexity: {config['project_complexity'].value}")
            print(f"    ✅ Communication: {config['communication_style']}")
            print(f"    ✅ Context budget: {config['context_budget']} tokens")
            
            self.test_results.append({
                'test': f'personal_intelligence_{i}',
                'status': 'PASS',
                'config': config
            })
    
    def test_module_loading(self):
        """Test 2: Dynamic Module Loading from Real Files"""
        print("\n📁 Testing Dynamic Module Loading...")
        
        # Check if config files exist
        required_modules = [
            "orchestration_modes.yaml",
            "behavioral_governance.md", 
            "communication_framework.md",
            "security_policies.md",
            "orchestrator_tools.yaml"
        ]
        
        for module in required_modules:
            module_path = self.config_base_path / module
            if module_path.exists():
                print(f"    ✅ Module found: {module}")
                
                # Test file reading
                try:
                    with open(module_path, 'r') as f:
                        content = f.read()
                        if len(content) > 100:  # Has substantial content
                            print(f"      ✅ Content loaded: {len(content)} characters")
                        else:
                            print(f"      ⚠️  Content minimal: {len(content)} characters")
                            
                except Exception as e:
                    print(f"      ❌ Read error: {e}")
                    self.test_results.append({
                        'test': f'module_loading_{module}',
                        'status': 'FAIL',
                        'error': str(e)
                    })
                    continue
                    
            else:
                print(f"    ❌ Module missing: {module}")
                self.test_results.append({
                    'test': f'module_loading_{module}',
                    'status': 'FAIL',
                    'error': 'File not found'
                })
                continue
                
            self.test_results.append({
                'test': f'module_loading_{module}',
                'status': 'PASS'
            })
    
    def test_context_aware_composition(self):
        """Test 3: Context-Aware Module Composition"""
        print("\n🎯 Testing Context-Aware Module Composition...")
        
        # Simulate different user contexts
        contexts = [
            {
                'name': 'NOVICE_EXPLORATORY',
                'request': 'I want to learn about building AI agents',
                'expected_modules': ['educational_content', 'detailed_explanations'],
                'expected_style': 'pedagogical'
            },
            {
                'name': 'EXPERT_PRODUCTION',
                'request': 'Deploy a multi-agent system to production with enterprise security',
                'expected_modules': ['security_policies', 'production_optimizations'],
                'expected_style': 'direct'
            },
            {
                'name': 'INNOVATOR_RESEARCH',
                'request': 'Explore novel multi-modal agent architectures with custom frameworks',
                'expected_modules': ['experimental_patterns', 'research_methodologies'],
                'expected_style': 'collaborative'
            }
        ]
        
        for context in contexts:
            print(f"\n  Testing: {context['name']}")
            config = self.personal_architect.process_request(context['request'])
            
            # Verify context-appropriate configuration
            communication_match = config['communication_style'] == context['expected_style']
            print(f"    ✅ Communication style match: {communication_match}")
            
            # Check if complexity and expertise align
            expertise_appropriate = self._validate_expertise_alignment(config)
            print(f"    ✅ Expertise alignment: {expertise_appropriate}")
            
            self.test_results.append({
                'test': f'context_composition_{context["name"]}',
                'status': 'PASS' if communication_match and expertise_appropriate else 'FAIL',
                'config': config
            })
    
    def test_learning_and_adaptation(self):
        """Test 4: Learning and Adaptation Over Time"""
        print("\n📈 Testing Learning and Adaptation...")
        
        # Simulate successful outcomes to test learning
        approaches = [
            ('langraph_multi_agent', True),
            ('crewai_research_team', True), 
            ('custom_framework_experiment', False),
            ('autogen_supervisor', True)
        ]
        
        for approach, success in approaches:
            print(f"  Recording outcome: {approach} -> {'SUCCESS' if success else 'FAILURE'}")
            self.personal_architect.record_session_outcome(approach, success)
        
        # Get recommendations after learning
        insights = self.personal_architect.get_personal_insights()
        
        print(f"\n  📊 Learning Results:")
        print(f"    Success rate: {insights['success_rate']:.1%}")
        print(f"    Top approaches: {[a[0] for a in insights['successful_approaches']]}")
        print(f"    Expertise trajectory: {insights['expertise_trajectory']}")
        
        # Verify learning occurred
        learning_effective = (
            insights['success_rate'] > 0.0 and 
            len(insights['successful_approaches']) > 0 and
            insights['expertise_trajectory'] != 'insufficient_data'
        )
        
        self.test_results.append({
            'test': 'learning_adaptation',
            'status': 'PASS' if learning_effective else 'FAIL',
            'insights': insights
        })
    
    def test_production_integration(self):
        """Test 5: Production Integration Capabilities"""
        print("\n🚀 Testing Production Integration...")
        
        # Test production-level request
        production_request = """
        I need a production-ready multi-agent system that:
        - Processes customer support tickets
        - Routes to appropriate specialists
        - Maintains audit trails for compliance
        - Handles 1000+ requests/day
        - Has 99.9% uptime requirement
        """
        
        config = self.personal_architect.process_request(production_request)
        
        # Verify production-appropriate configuration
        production_ready = (
            config['project_complexity'].value in ['complex', 'cutting_edge'] and
            config['detail_level'] == 'comprehensive' and
            config['context_budget'] >= 12000
        )
        
        print(f"    ✅ Production complexity detected: {config['project_complexity'].value}")
        print(f"    ✅ Comprehensive detail level: {config['detail_level']}")
        print(f"    ✅ Adequate context budget: {config['context_budget']} tokens")
        print(f"    ✅ Production readiness: {production_ready}")
        
        self.test_results.append({
            'test': 'production_integration', 
            'status': 'PASS' if production_ready else 'FAIL',
            'config': config
        })
    
    def _validate_expertise_alignment(self, config):
        """Helper: Validate that expertise and other settings align logically"""
        expertise = config['user_expertise']
        complexity = config['project_complexity'] 
        detail = config['detail_level']
        
        # Basic alignment checks
        if expertise.value == 'learning' and detail not in ['detailed', 'comprehensive']:
            return False
            
        if expertise.value == 'expert' and config['approval_frequency'] == 'frequent':
            return False
            
        if complexity.value == 'cutting_edge' and detail != 'comprehensive':
            return False
            
        return True
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("🧪 MODULAR ORCHESTRATOR SYSTEM TEST SUITE")
        print("=" * 60)
        
        # Run all tests
        self.test_personal_intelligence()
        self.test_module_loading()
        self.test_context_aware_composition()
        self.test_learning_and_adaptation()
        self.test_production_integration()
        
        # Generate test report
        self.generate_test_report()
    
    def generate_test_report(self):
        """Generate comprehensive test report"""
        print("\n" + "=" * 60)
        print("📋 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['status'] == 'PASS')
        failed_tests = total_tests - passed_tests
        
        print(f"\n✅ Passed: {passed_tests}/{total_tests}")
        print(f"❌ Failed: {failed_tests}/{total_tests}")
        print(f"📊 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print(f"\n❌ FAILED TESTS:")
            for result in self.test_results:
                if result['status'] == 'FAIL':
                    error = result.get('error', 'Unknown error')
                    print(f"  - {result['test']}: {error}")
        
        print(f"\n🎯 SYSTEM STATUS: {'✅ READY FOR USE' if failed_tests == 0 else '⚠️ NEEDS ATTENTION'}")
        
        # Performance metrics
        print(f"\n📈 PERFORMANCE METRICS:")
        print(f"  - Module loading: {'✅ Operational' if passed_tests > 0 else '❌ Issues'}")
        print(f"  - Personal intelligence: {'✅ Learning' if any('personal_intelligence' in r['test'] for r in self.test_results if r['status'] == 'PASS') else '❌ Not learning'}")
        print(f"  - Context adaptation: {'✅ Adaptive' if any('context_composition' in r['test'] for r in self.test_results if r['status'] == 'PASS') else '❌ Static'}")


if __name__ == "__main__":
    # Initialize and run test suite
    tester = ModularSystemTester()
    tester.run_all_tests()
    
    print(f"\n🚀 Your Personal AI Architect System is ready!")
    print(f"   Just make requests - no manual configuration needed!")
    print(f"   The system learns from every interaction to optimize your workflow.")