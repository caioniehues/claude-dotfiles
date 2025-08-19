#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific analysis with brutal honesty
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any

class SavageCommandBenchmarker:
    """The PhD in roasting bad code"""
    
    def __init__(self):
        self.results = {}
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        
    def analyze_command_file(self, filename: str, content: str) -> Dict[str, Any]:
        """Brutally analyze a command file"""
        
        # Count token-hungry elements
        token_score = self._calculate_token_waste(content)
        
        # Complexity based on CLAUDE.md rules (>5 is bad)
        complexity_score = self._calculate_complexity(content)
        
        # MCP dependencies that may not exist
        mcp_deps = self._extract_mcp_dependencies(content)
        
        # Execution risks
        execution_risks = self._identify_execution_risks(content)
        
        # Functionality gaps
        gaps = self._identify_functionality_gaps(content)
        
        # Performance characteristics  
        performance = self._analyze_performance(content)
        
        return {
            'filename': filename,
            'token_waste_score': token_score,
            'complexity_score': complexity_score,
            'mcp_dependencies': mcp_deps,
            'execution_risks': execution_risks,
            'functionality_gaps': gaps,
            'performance_metrics': performance,
            'savage_rating': self._calculate_savage_rating(
                token_score, complexity_score, len(execution_risks), len(gaps)
            )
        }
    
    def _calculate_token_waste(self, content: str) -> int:
        """How many tokens does this thing waste?"""
        
        # Count verbose elements
        javascript_blocks = len(re.findall(r'```javascript.*?```', content, re.DOTALL))
        bash_blocks = len(re.findall(r'```bash.*?```', content, re.DOTALL))
        unnecessary_comments = len(re.findall(r'//.*', content))
        verbose_console_logs = len(re.findall(r'console\.log', content))
        template_literals = len(re.findall(r'`.*?`', content))
        
        # Estimate token waste
        base_tokens = len(content.split())
        
        # Penalties for verbose patterns
        waste_score = 0
        waste_score += javascript_blocks * 50  # Each JS block adds ~50 tokens
        waste_score += bash_blocks * 30
        waste_score += unnecessary_comments * 5
        waste_score += verbose_console_logs * 10
        waste_score += template_literals * 3
        
        return waste_score
    
    def _calculate_complexity(self, content: str) -> int:
        """CLAUDE.md complexity score - >5 is over-engineered garbage"""
        
        score = 0
        
        # Count complexity indicators
        mcp_calls = len(re.findall(r'mcp__.*?__', content))
        nested_blocks = content.count('<') - content.count('</')  # XML nesting
        conditional_logic = len(re.findall(r'if|else|switch|while|for', content))
        function_definitions = len(re.findall(r'function|const.*?=>', content))
        abstraction_layers = len(re.findall(r'interface|abstract|template', content))
        
        # CLAUDE.md scoring
        score += min(mcp_calls * 0.5, 5)  # Cap MCP impact
        score += min(nested_blocks * 0.1, 3)
        score += min(conditional_logic * 0.2, 4)
        score += min(function_definitions * 0.3, 4)
        score += abstraction_layers * 2  # Heavy penalty for abstractions
        
        return min(score, 30)  # Cap at 30
    
    def _extract_mcp_dependencies(self, content: str) -> List[str]:
        """Find MCP tools that probably don't exist"""
        
        mcp_pattern = r'mcp__([^_]+)__([^(\s]+)'
        matches = re.findall(mcp_pattern, content)
        
        deps = []
        for service, function in matches:
            deps.append(f"{service}::{function}")
        
        return list(set(deps))  # Deduplicate
    
    def _identify_execution_risks(self, content: str) -> List[str]:
        """What could go catastrophically wrong?"""
        
        risks = []
        
        # Check for risky patterns
        if 'await' in content and 'catch' not in content:
            risks.append("Unhandled async operations - will crash on first error")
            
        if 'setTimeout' in content or 'setInterval' in content:
            risks.append("Timer-based operations without cleanup - memory leaks guaranteed")
            
        if re.search(r'osascript|system|exec', content):
            risks.append("System calls without validation - security nightmare")
            
        if 'JSON.parse' in content and 'try' not in content:
            risks.append("JSON parsing without error handling - runtime explosion waiting")
            
        if re.search(r'\.log\(', content) and 'production' not in content.lower():
            risks.append("Debug logging in production command - performance drain")
            
        mcp_count = len(re.findall(r'mcp__', content))
        if mcp_count > 10:
            risks.append(f"MCP addiction - {mcp_count} dependencies, single point of failure")
            
        # Check for ADHD-specific risks
        if 'adhd' in content.lower():
            if 'hyperfocus' in content.lower() and 'timer' not in content.lower():
                risks.append("Hyperfocus management without actual timer implementation")
                
        return risks
    
    def _identify_functionality_gaps(self, content: str) -> List[str]:
        """What does this thing claim to do but actually can't?"""
        
        gaps = []
        
        # Check for promises without delivery
        if 'notification' in content.lower() and 'osascript' not in content:
            gaps.append("Claims notifications but no implementation")
            
        if 'timer' in content.lower() and not re.search(r'setTimeout|setInterval|timer:|osascript', content):
            gaps.append("Mentions timers but no actual timer mechanism")
            
        if 'environment' in content.lower() and 'process.env' not in content:
            gaps.append("Environment optimization claims without environment access")
            
        if 'pattern' in content.lower() and 'basic-memory' not in content:
            gaps.append("Pattern learning claims without persistent storage")
            
        if re.search(r'save|write|store', content) and not re.search(r'write_note|Write|Edit', content):
            gaps.append("Claims to save data but no actual persistence mechanism")
            
        return gaps
    
    def _analyze_performance(self, content: str) -> Dict[str, Any]:
        """Performance characteristics analysis"""
        
        mcp_calls = len(re.findall(r'mcp__.*?__', content))
        js_blocks = len(re.findall(r'```javascript.*?```', content, re.DOTALL))
        sequential_operations = len(re.findall(r'await.*\n.*await', content, re.DOTALL))
        
        # Estimate execution time based on patterns
        estimated_time = 0
        estimated_time += mcp_calls * 0.5  # 500ms per MCP call
        estimated_time += sequential_operations * 0.3  # Sequential penalty
        estimated_time += js_blocks * 0.1  # JS processing overhead
        
        return {
            'estimated_execution_time_seconds': estimated_time,
            'mcp_dependency_count': mcp_calls,
            'sequential_bottlenecks': sequential_operations,
            'token_efficiency': 'POOR' if len(content) > 5000 else 'ACCEPTABLE',
            'scalability': 'TERRIBLE' if mcp_calls > 15 else 'LIMITED'
        }
    
    def _calculate_savage_rating(self, tokens: int, complexity: int, risks: int, gaps: int) -> Dict[str, Any]:
        """The final brutal assessment"""
        
        # Scientific scoring
        total_score = 0
        total_score += min(tokens / 100, 10)  # Token waste factor
        total_score += complexity  # Complexity penalty
        total_score += risks * 2  # Risk multiplier
        total_score += gaps * 3   # Gap penalty is severe
        
        # Determine savage category
        if total_score >= 20:
            category = "DUMPSTER_FIRE"
            roast = "This command is an over-engineered monument to everything wrong with modern development"
        elif total_score >= 15:
            category = "HOT_MESS"
            roast = "Impressive token waste with a sprinkle of false promises"
        elif total_score >= 10:
            category = "QUESTIONABLE"
            roast = "Works in theory, probably crashes in practice"
        elif total_score >= 5:
            category = "MEDIOCRE"
            roast = "Not terrible, but not winning any architecture awards"
        else:
            category = "ACCEPTABLE"
            roast = "Surprisingly reasonable for once"
        
        return {
            'total_score': total_score,
            'category': category,
            'savage_roast': roast,
            'confidence_interval': f"{total_score - 2:.1f} to {total_score + 2:.1f}",
            'recommendation': self._get_recommendation(category)
        }
    
    def _get_recommendation(self, category: str) -> str:
        """Scientific recommendation"""
        
        recommendations = {
            'DUMPSTER_FIRE': 'DELETE IMMEDIATELY. Start over with a simple bash script.',
            'HOT_MESS': 'Major refactoring needed. Consider intervention.',
            'QUESTIONABLE': 'Needs cleanup and testing. Proceed with caution.',
            'MEDIOCRE': 'Minor improvements needed. Could be worse.',
            'ACCEPTABLE': 'Ship it, but monitor for issues.'
        }
        
        return recommendations.get(category, 'Unknown category')

if __name__ == "__main__":
    benchmarker = SavageCommandBenchmarker()
    print("SAVAGE COMMAND BENCHMARKER INITIALIZED")
    print("PhD in brutal honesty: ENGAGED")