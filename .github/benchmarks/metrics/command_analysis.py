#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific analysis of Claude command effectiveness
"""
import re
import json
import time
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from statistics import mean, stdev

@dataclass
class ComplexityMetrics:
    """Complexity scoring based on CLAUDE.md rules"""
    thinking_blocks: int = 0
    mcp_integrations: int = 0
    conditional_logic: int = 0
    abstraction_layers: int = 0
    configuration_options: int = 0
    total_lines: int = 0
    
    @property
    def complexity_score(self) -> float:
        """Calculate complexity score per CLAUDE.md (must be < 5)"""
        score = 0
        score += self.thinking_blocks * 0.5  # Thinking is good
        score += self.mcp_integrations * 1.0  # Integration complexity  
        score += self.conditional_logic * 0.3
        score += self.abstraction_layers * 2.0  # Heavy penalty per CLAUDE.md
        score += self.configuration_options * 1.5
        score += (self.total_lines / 100) * 0.5  # Size penalty
        return score

@dataclass
class PerformanceMetrics:
    """Performance measurements for command execution"""
    token_consumption: int = 0
    execution_time: float = 0.0
    success_rate: float = 0.0
    error_count: int = 0
    memory_usage: int = 0

@dataclass
class CommandAnalysis:
    """Complete command analysis"""
    name: str
    file_path: str
    complexity: ComplexityMetrics
    performance: PerformanceMetrics
    maintainability_score: float = 0.0
    pattern_compliance: float = 0.0
    savage_rating: str = ""

class CommandAnalyzer:
    """The SAVAGE COMMAND BENCHMARKER itself"""
    
    def __init__(self):
        self.claude_md_rules = self._load_claude_rules()
        
    def _load_claude_rules(self) -> Dict:
        """Load CLAUDE.md complexity rules"""
        return {
            "max_complexity": 5,
            "abstraction_penalty": 2,
            "interface_penalty": 1, 
            "pattern_penalty": 3,
            "config_penalty": 2
        }
    
    def analyze_command(self, file_path: Path) -> CommandAnalysis:
        """Analyze a single command file with scientific rigor"""
        content = file_path.read_text()
        
        # Complexity analysis
        complexity = self._analyze_complexity(content)
        
        # Performance simulation (since we can't execute in isolation)
        performance = self._simulate_performance(content, complexity)
        
        # Pattern compliance check
        compliance = self._check_pattern_compliance(content)
        
        # Maintainability assessment  
        maintainability = self._assess_maintainability(content, complexity)
        
        # Generate savage but fair rating
        savage_rating = self._generate_savage_rating(complexity, performance, compliance)
        
        return CommandAnalysis(
            name=file_path.stem,
            file_path=str(file_path),
            complexity=complexity,
            performance=performance,
            maintainability_score=maintainability,
            pattern_compliance=compliance,
            savage_rating=savage_rating
        )
    
    def _analyze_complexity(self, content: str) -> ComplexityMetrics:
        """Calculate complexity metrics per CLAUDE.md standards"""
        
        # Count thinking blocks
        thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content, re.IGNORECASE))
        
        # Count MCP integrations
        mcp_integrations = len(re.findall(r'mcp__[^_]+__\w+', content))
        
        # Count conditional logic
        conditional_logic = len(re.findall(r'\bif\b|\bswitch\b|\b\?\s*:', content, re.IGNORECASE))
        
        # Count abstraction layers (interfaces, abstract classes)
        abstraction_layers = len(re.findall(r'interface\s+\w+|abstract\s+class|extends\s+\w+', content, re.IGNORECASE))
        
        # Count configuration options
        config_options = len(re.findall(r'config[uration]*[:=]|settings[:=]|options[:=]', content, re.IGNORECASE))
        
        # Total lines
        total_lines = len(content.splitlines())
        
        return ComplexityMetrics(
            thinking_blocks=thinking_blocks,
            mcp_integrations=mcp_integrations, 
            conditional_logic=conditional_logic,
            abstraction_layers=abstraction_layers,
            configuration_options=config_options,
            total_lines=total_lines
        )
    
    def _simulate_performance(self, content: str, complexity: ComplexityMetrics) -> PerformanceMetrics:
        """Simulate performance based on content analysis"""
        
        # Token estimation based on content size and complexity
        base_tokens = len(content.split()) * 1.3  # Rough token estimation
        complexity_multiplier = 1 + (complexity.complexity_score / 10)
        estimated_tokens = int(base_tokens * complexity_multiplier)
        
        # Execution time estimation
        base_time = len(content) / 1000 * 2  # 2 seconds per 1000 chars
        complexity_time_penalty = complexity.complexity_score * 5
        estimated_time = base_time + complexity_time_penalty
        
        # Success rate estimation (inverse of complexity)
        success_rate = max(0.1, 1.0 - (complexity.complexity_score / 10))
        
        # Error estimation
        error_count = max(0, int(complexity.complexity_score - 3))
        
        return PerformanceMetrics(
            token_consumption=estimated_tokens,
            execution_time=estimated_time,
            success_rate=success_rate,
            error_count=error_count,
            memory_usage=estimated_tokens * 4  # Rough memory estimation
        )
    
    def _check_pattern_compliance(self, content: str) -> float:
        """Check compliance with CLAUDE.md patterns"""
        score = 1.0
        
        # Required elements
        required_patterns = [
            r'<task>',
            r'<context>',
            r'<thinking',
            r'\$ARGUMENTS'
        ]
        
        for pattern in required_patterns:
            if not re.search(pattern, content, re.IGNORECASE):
                score -= 0.2
        
        # Bonus for good patterns
        if re.search(r'complexity.*assessment', content, re.IGNORECASE):
            score += 0.1
            
        if re.search(r'mcp__.*sequentialthinking', content, re.IGNORECASE):
            score += 0.1
            
        return max(0.0, min(1.0, score))
    
    def _assess_maintainability(self, content: str, complexity: ComplexityMetrics) -> float:
        """Assess maintainability based on CLAUDE.md principles"""
        
        # Start with base maintainability
        maintainability = 1.0
        
        # Penalize complexity
        if complexity.complexity_score > 5:
            maintainability -= (complexity.complexity_score - 5) * 0.2
        
        # Penalize size
        if complexity.total_lines > 500:
            maintainability -= (complexity.total_lines - 500) / 1000
            
        # Reward structure
        if re.search(r'## .+\n<[^>]*thinking[^>]*>', content):
            maintainability += 0.1  # Good thinking structure
            
        # Penalize anti-patterns from CLAUDE.md
        anti_patterns = [
            r'Factory.*Factory',  # Factory madness
            r'interface.*\{\s*\}',  # Empty interfaces
            r'abstract.*abstract',  # Over-abstraction
        ]
        
        for pattern in anti_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                maintainability -= 0.3
                
        return max(0.0, min(1.0, maintainability))
    
    def _generate_savage_rating(self, complexity: ComplexityMetrics, 
                              performance: PerformanceMetrics, 
                              compliance: float) -> str:
        """Generate savage but accurate rating"""
        
        score = complexity.complexity_score
        
        if score > 8:
            return f"🔥 COMPLEXITY DISASTER: Score {score:.1f}/5. This isn't 'intelligent automation', it's a Rube Goldberg machine with delusions of grandeur."
        elif score > 6:
            return f"⚠️ OVER-ENGINEERED: Score {score:.1f}/5. You've violated the Prime Directive: SIMPLICITY FIRST. This needs an intervention."
        elif score > 5:
            return f"🚨 CLAUDE.MD VIOLATION: Score {score:.1f}/5. The rules exist for a reason. This complexity score must be < 5."
        elif score > 3:
            return f"📊 ACCEPTABLE: Score {score:.1f}/5. Not terrible, but room for simplification exists."
        elif score > 1:
            return f"✅ GOOD: Score {score:.1f}/5. Reasonable complexity, follows principles."
        else:
            return f"🎯 EXCELLENT: Score {score:.1f}/5. This is how you do it - simple, effective, maintainable."

def main():
    """Run the savage benchmarking"""
    analyzer = CommandAnalyzer()
    commands_dir = Path("commands")
    
    if not commands_dir.exists():
        print("Commands directory not found. Are you in the right location?")
        return
    
    results = []
    
    for cmd_file in commands_dir.glob("*.md"):
        if cmd_file.name.startswith('.'):
            continue
            
        analysis = analyzer.analyze_command(cmd_file)
        results.append(analysis)
        
        print(f"\n📊 ANALYZING: {cmd_file.name}")
        print(f"Complexity Score: {analysis.complexity.complexity_score:.1f}/5")
        print(f"Pattern Compliance: {analysis.pattern_compliance:.1%}")
        print(f"Maintainability: {analysis.maintainability_score:.1%}")
        print(f"Savage Rating: {analysis.savage_rating}")
    
    # Generate final report
    generate_report(results)

def generate_report(analyses: List[CommandAnalysis]):
    """Generate the final savage report"""
    
    report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_commands": len(analyses),
        "summary_statistics": {
            "avg_complexity": mean([a.complexity.complexity_score for a in analyses]),
            "complexity_std_dev": stdev([a.complexity.complexity_score for a in analyses]) if len(analyses) > 1 else 0,
            "claude_md_violations": len([a for a in analyses if a.complexity.complexity_score > 5]),
            "avg_compliance": mean([a.pattern_compliance for a in analyses]),
            "avg_maintainability": mean([a.maintainability_score for a in analyses])
        },
        "command_details": [
            {
                "name": a.name,
                "complexity_score": round(a.complexity.complexity_score, 2),
                "claude_md_compliant": a.complexity.complexity_score < 5,
                "pattern_compliance": round(a.pattern_compliance, 2),
                "maintainability": round(a.maintainability_score, 2),
                "savage_rating": a.savage_rating,
                "thinking_blocks": a.complexity.thinking_blocks,
                "mcp_integrations": a.complexity.mcp_integrations,
                "total_lines": a.complexity.total_lines
            }
            for a in analyses
        ]
    }
    
    # Save detailed JSON report
    report_path = Path(".github/benchmarks/results/20250820-203522-report.json")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 SAVAGE BENCHMARK REPORT GENERATED: {report_path}")

if __name__ == "__main__":
    main()