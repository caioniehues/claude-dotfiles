#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific measurement and brutal judgment of Claude commands

Measures:
- Token consumption (input + output)
- Execution complexity
- Success probability
- Composition compatibility
- CLAUDE.md compliance
- Time complexity estimation
"""

import json
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any
import statistics

@dataclass
class CommandMetrics:
    name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    complexity_score: int
    simplicity_violations: List[str]
    mcp_dependencies: List[str]
    java_violations: List[str]
    success_indicators: List[str]
    failure_indicators: List[str]
    composition_score: float
    maintainability_score: float
    claude_md_compliance: float

class CommandBenchmarker:
    def __init__(self):
        self.results = {}
        
    def analyze_command(self, file_path: str) -> CommandMetrics:
        """Brutally analyze a command file"""
        with open(file_path, 'r') as f:
            content = f.read()
        
        name = Path(file_path).stem
        
        # TOKEN ANALYSIS (Savage precision)
        input_tokens = self._estimate_tokens(content)
        output_tokens = self._estimate_output_tokens(content)
        
        # COMPLEXITY SCORING (Based on CLAUDE.md rules)
        complexity_score = self._calculate_complexity_score(content)
        
        # SIMPLICITY VIOLATIONS (Zero tolerance)
        violations = self._find_simplicity_violations(content)
        
        # JAVA VIOLATIONS (If Java-related)
        java_violations = self._find_java_violations(content) if 'java' in name else []
        
        # MCP DEPENDENCIES (Dependency hell check)
        mcp_deps = self._extract_mcp_dependencies(content)
        
        # SUCCESS/FAILURE INDICATORS
        success_indicators = self._find_success_indicators(content)
        failure_indicators = self._find_failure_indicators(content)
        
        # COMPOSITION SCORE (0-1)
        composition_score = self._calculate_composition_score(content)
        
        # MAINTAINABILITY SCORE (0-1)  
        maintainability_score = self._calculate_maintainability_score(content)
        
        # CLAUDE.MD COMPLIANCE (0-1)
        claude_compliance = self._calculate_claude_compliance(content)
        
        return CommandMetrics(
            name=name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            complexity_score=complexity_score,
            simplicity_violations=violations,
            mcp_dependencies=mcp_deps,
            java_violations=java_violations,
            success_indicators=success_indicators,
            failure_indicators=failure_indicators,
            composition_score=composition_score,
            maintainability_score=maintainability_score,
            claude_md_compliance=claude_compliance
        )
    
    def _estimate_tokens(self, content: str) -> int:
        """Estimate input tokens (brutal accuracy)"""
        # Rough tokenization: ~4 chars per token for code, ~6 for prose
        code_blocks = len(re.findall(r'```[^`]+```', content))
        code_chars = sum(len(block) for block in re.findall(r'```[^`]+```', content))
        prose_chars = len(content) - code_chars
        
        return int(code_chars / 4 + prose_chars / 6)
    
    def _estimate_output_tokens(self, content: str) -> int:
        """Estimate expected output tokens based on command complexity"""
        # Analysis based on typical Claude responses
        base_response = 100  # Basic response overhead
        
        # Add tokens based on complexity indicators
        if 'mcp__' in content:
            base_response += 50  # MCP tool usage adds complexity
        if 'thinking' in content.lower():
            base_response += 200  # Thinking blocks are verbose
        if 'sequential' in content.lower():
            base_response += 300  # Sequential thinking is very verbose
        if 'javascript' in content or 'python' in content:
            base_response += 150  # Code generation
        if len(content) > 10000:
            base_response += 200  # Complex commands generate complex responses
            
        return base_response
    
    def _calculate_complexity_score(self, content: str) -> int:
        """Calculate complexity based on CLAUDE.md rules (Merciless scoring)"""
        score = 1  # Base complexity
        
        # Count complexity drivers
        classes = len(re.findall(r'class \w+', content))
        interfaces = len(re.findall(r'interface \w+', content))
        patterns = len(re.findall(r'pattern|factory|strategy|observer', content, re.IGNORECASE))
        configs = len(re.findall(r'config|\.xml|\.yaml|\.properties', content))
        mcp_calls = len(re.findall(r'mcp__\w+', content))
        
        score += classes * 2
        score += interfaces * 1
        score += patterns * 3
        score += configs * 2
        score += mcp_calls * 1  # MCP adds operational complexity
        
        return score
    
    def _find_simplicity_violations(self, content: str) -> List[str]:
        """Find violations of simplicity principles (No mercy)"""
        violations = []
        
        # Check for over-engineering indicators
        if 'factory' in content.lower() and 'builder' in content.lower():
            violations.append("Factory + Builder pattern - probable over-engineering")
        
        if len(re.findall(r'interface \w+', content)) > 2:
            violations.append("Multiple interfaces without justification")
            
        if 'abstract' in content.lower():
            violations.append("Abstraction without 3+ concrete implementations")
            
        if content.count('```') > 20:
            violations.append("Excessive code examples - cognitive overload")
            
        if len(content) > 15000:
            violations.append("Command too long - violates comprehension limits")
            
        return violations
    
    def _find_java_violations(self, content: str) -> List[str]:
        """Find Java-specific violations (Clean code Nazi mode)"""
        violations = []
        
        # Check for Java anti-patterns
        if 'import .*\\*' in content:
            violations.append("Wildcard imports detected")
        
        if 'return null' in content:
            violations.append("Null returns instead of Optional")
            
        if len(re.findall(r'public \w+ \w+\([^)]{50,}', content)) > 0:
            violations.append("Methods with too many parameters")
            
        if 'extends.*extends' in content:
            violations.append("Deep inheritance hierarchy")
            
        return violations
    
    def _extract_mcp_dependencies(self, content: str) -> List[str]:
        """Extract MCP tool dependencies"""
        mcp_pattern = r'mcp__([^_]+)__([^(\s]+)'
        matches = re.findall(mcp_pattern, content)
        return [f"{tool}::{function}" for tool, function in matches]
    
    def _find_success_indicators(self, content: str) -> List[str]:
        """Find indicators of likely success"""
        indicators = []
        
        if 'checklist' in content.lower():
            indicators.append("Has validation checklist")
        if 'test' in content.lower():
            indicators.append("Includes testing guidance")
        if 'error' in content.lower() or 'exception' in content.lower():
            indicators.append("Has error handling")
        if 'thinking' in content.lower():
            indicators.append("Includes reasoning process")
        if 'simple' in content.lower():
            indicators.append("Emphasizes simplicity")
            
        return indicators
    
    def _find_failure_indicators(self, content: str) -> List[str]:
        """Find indicators of likely failure (Brutal honesty)"""
        indicators = []
        
        if content.count('TODO') > 3:
            indicators.append("Too many TODOs - incomplete implementation")
        if content.count('$') > 20:
            indicators.append("Over-templated - probably won't work out of box")
        if 'complex' in content.lower() and 'simple' not in content.lower():
            indicators.append("Glorifies complexity without simplicity balance")
        if len(re.findall(r'mcp__\w+', content)) > 10:
            indicators.append("MCP dependency hell - fragile")
        if content.count('```') == 0:
            indicators.append("No concrete examples - all theory")
            
        return indicators
    
    def _calculate_composition_score(self, content: str) -> float:
        """How well does this compose with other commands? (0-1)"""
        score = 0.5  # Baseline
        
        # Positive indicators
        if '$ARGUMENTS' in content:
            score += 0.2  # Accepts parameters
        if 'mcp__' in content:
            score += 0.1  # Uses standard tools
        if 'thinking' in content.lower():
            score += 0.1  # Includes reasoning
            
        # Negative indicators
        if 'hardcoded' in content.lower():
            score -= 0.3  # Hardcoded values
        if content.count('TODO') > 5:
            score -= 0.2  # Too many unknowns
        if len(content) > 20000:
            score -= 0.1  # Too complex to compose
            
        return max(0, min(1, score))
    
    def _calculate_maintainability_score(self, content: str) -> float:
        """How maintainable is this command? (0-1)"""
        score = 0.5  # Baseline
        
        # Good signs
        if content.count('#') > 10:  # Has structure
            score += 0.1
        if 'example' in content.lower():
            score += 0.1
        if len(re.findall(r'```\w+', content)) > 0:  # Has syntax highlighting
            score += 0.1
        if 'thinking' in content.lower():
            score += 0.1
            
        # Bad signs
        if len(content) > 15000:
            score -= 0.2  # Too long
        if content.count('TODO') > 3:
            score -= 0.1  # Incomplete
        if len(self._extract_mcp_dependencies(content)) > 8:
            score -= 0.2  # Too many dependencies
            
        return max(0, min(1, score))
    
    def _calculate_claude_compliance(self, content: str) -> float:
        """Compliance with CLAUDE.md principles (0-1)"""
        score = 0.5  # Baseline
        
        # Check for CLAUDE.md compliance indicators
        if 'simple' in content.lower():
            score += 0.15
        if 'mcp__basic-memory' in content:
            score += 0.1  # Uses memory properly
        if 'final' in content:
            score += 0.1  # Java immutability
        if 'complexity' in content.lower():
            score += 0.1  # Considers complexity
        if 'thinking' in content.lower():
            score += 0.1  # Uses thinking
            
        # Violations
        if 'wildcard' in content and 'never' not in content.lower():
            score -= 0.2
        if 'null' in content and 'not null' not in content.lower():
            score -= 0.1
        if score < 0:
            score = 0
            
        return min(1, score)

# Test instances for benchmarking
test_commands = [
    'ultrathink-interactive.md',
    'ultrathink-full-mcp.md', 
    'reasoning-wrapper.md',
    'adhd-hyperfocus-guardian.md',
    'java-clean-code-generator.md'
]

if __name__ == "__main__":
    benchmarker = CommandBenchmarker()
    
    print("🔬 SAVAGE COMMAND BENCHMARKER")
    print("=" * 60)
    print("Scientifically measuring and brutally judging commands...")
    print()
    
    results = []
    base_path = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands/"
    
    for cmd in test_commands:
        print(f"🔍 Analyzing: {cmd}")
        try:
            metrics = benchmarker.analyze_command(base_path + cmd)
            results.append(asdict(metrics))
            print(f"   Tokens: {metrics.total_tokens}")
            print(f"   Complexity: {metrics.complexity_score}")
            print(f"   Violations: {len(metrics.simplicity_violations)}")
            print()
        except Exception as e:
            print(f"   ❌ FAILED: {e}")
            print()
    
    # Calculate aggregate statistics
    if results:
        total_tokens = [r['total_tokens'] for r in results]
        complexity_scores = [r['complexity_score'] for r in results]
        
        stats = {
            'total_commands_analyzed': len(results),
            'token_stats': {
                'mean': statistics.mean(total_tokens),
                'median': statistics.median(total_tokens),
                'stdev': statistics.stdev(total_tokens) if len(total_tokens) > 1 else 0,
                'min': min(total_tokens),
                'max': max(total_tokens)
            },
            'complexity_stats': {
                'mean': statistics.mean(complexity_scores),
                'median': statistics.median(complexity_scores),
                'stdev': statistics.stdev(complexity_scores) if len(complexity_scores) > 1 else 0,
                'violations_over_threshold': sum(1 for score in complexity_scores if score >= 5)
            },
            'analysis_timestamp': time.time(),
            'individual_results': results
        }
        
        print("📊 AGGREGATE STATISTICS")
        print("=" * 40)
        print(f"Commands analyzed: {stats['total_commands_analyzed']}")
        print(f"Mean tokens: {stats['token_stats']['mean']:.1f} ± {stats['token_stats']['stdev']:.1f}")
        print(f"Mean complexity: {stats['complexity_stats']['mean']:.1f}")
        print(f"Complexity violations: {stats['complexity_stats']['violations_over_threshold']}/{len(results)}")
        
        # Save results
        output_file = f"/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/20250829-060332-report.json"
        with open(output_file, 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"\n📁 Results saved to: {output_file}")
        
        return stats
    else:
        print("❌ NO SUCCESSFUL ANALYSES")
        return {}