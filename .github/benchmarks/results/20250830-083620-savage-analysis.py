#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific analysis with brutal honesty
"""
import json
import re
import time
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class CommandMetrics:
    name: str
    lines: int
    thinking_blocks: int
    mcp_calls: int
    complexity_score: int
    token_estimate: int
    cognitive_load: int
    maintainability: float
    savage_rating: str

def analyze_command(file_path: str) -> CommandMetrics:
    """Brutally analyze a command file with scientific precision"""
    content = Path(file_path).read_text()
    name = Path(file_path).stem
    
    # Basic metrics
    lines = len(content.splitlines())
    
    # Thinking block analysis - SAVAGE METRIC
    thinking_blocks = len(re.findall(r'<[^>]*thinking[^>]*>', content))
    
    # MCP integration count
    mcp_calls = len(re.findall(r'mcp__', content))
    
    # CLAUDE.md Complexity Score Calculation
    complexity_score = calculate_savage_complexity(content)
    
    # Token estimation (brutal approximation)
    token_estimate = len(content.split()) * 1.3  # Conservative estimate
    
    # Cognitive load metric (how much brain damage reading this causes)
    cognitive_load = calculate_cognitive_damage(content)
    
    # Maintainability score (0-1, where 1 = actually maintainable)
    maintainability = calculate_maintainability(content, thinking_blocks, lines)
    
    # Savage rating based on all metrics
    savage_rating = generate_savage_rating(complexity_score, cognitive_load, maintainability)
    
    return CommandMetrics(
        name=name,
        lines=lines,
        thinking_blocks=thinking_blocks,
        mcp_calls=mcp_calls,
        complexity_score=complexity_score,
        token_estimate=int(token_estimate),
        cognitive_load=cognitive_load,
        maintainability=maintainability,
        savage_rating=savage_rating
    )

def calculate_savage_complexity(content: str) -> int:
    """Calculate complexity using CLAUDE.md rules with SAVAGE precision"""
    score = 1  # Direct solution baseline
    
    # Count abstractions that violate CLAUDE.md principles
    abstractions = len(re.findall(r'interface|abstract|factory|builder|strategy|decorator', content, re.I))
    score += abstractions * 3  # Each pattern = +3 (CLAUDE.md violation)
    
    # Nested thinking blocks (meta-complexity)
    nested_thinking = len(re.findall(r'<[^>]*thinking[^>]*>.*?<[^>]*thinking[^>]*>', content, re.DOTALL))
    score += nested_thinking * 2
    
    # Configuration complexity
    config_sections = len(re.findall(r'configuration|settings|options', content, re.I))
    score += config_sections * 2
    
    # Template complexity
    template_count = len(re.findall(r'template|wrapper|enhancement', content, re.I))
    score += template_count
    
    return score

def calculate_cognitive_damage(content: str) -> int:
    """How much brain damage does reading this cause? (1-10 scale)"""
    damage = 1
    
    # Deeply nested XML-like structures
    max_nesting = find_max_xml_nesting(content)
    damage += min(max_nesting, 5)
    
    # Excessive meta-language
    meta_words = len(re.findall(r'meta-|orchestration|enhancement|wrapper|thinking|reasoning', content, re.I))
    damage += min(meta_words // 10, 3)
    
    # Redundant repetition
    lines = content.splitlines()
    unique_lines = set(line.strip() for line in lines if line.strip())
    repetition_factor = len(lines) / len(unique_lines) if unique_lines else 1
    damage += min(int(repetition_factor), 2)
    
    return min(damage, 10)

def find_max_xml_nesting(content: str) -> int:
    """Find maximum XML nesting depth"""
    max_depth = 0
    current_depth = 0
    
    for match in re.finditer(r'<(/?)([^>]+)>', content):
        if match.group(1) == '/':  # Closing tag
            current_depth = max(0, current_depth - 1)
        else:  # Opening tag
            current_depth += 1
            max_depth = max(max_depth, current_depth)
    
    return max_depth

def calculate_maintainability(content: str, thinking_blocks: int, lines: int) -> float:
    """Maintainability score (0-1, brutal honesty)"""
    score = 1.0
    
    # Penalty for excessive length
    if lines > 500:
        score -= 0.3
    elif lines > 300:
        score -= 0.2
    
    # Penalty for thinking block madness
    thinking_ratio = thinking_blocks / lines if lines > 0 else 0
    if thinking_ratio > 0.1:  # More than 10% thinking blocks
        score -= 0.4
    
    # Penalty for XML soup
    xml_tags = len(re.findall(r'<[^>]+>', content))
    xml_ratio = xml_tags / lines if lines > 0 else 0
    if xml_ratio > 0.2:  # More than 20% XML tags
        score -= 0.3
    
    # Penalty for excessive meta-language
    meta_density = len(re.findall(r'orchestration|enhancement|wrapper|meta', content, re.I)) / lines if lines > 0 else 0
    if meta_density > 0.05:
        score -= 0.2
    
    return max(0.0, score)

def generate_savage_rating(complexity: int, cognitive_load: int, maintainability: float) -> str:
    """Generate brutally honest ratings"""
    if complexity >= 10:
        return "ARCHITECTURAL DISASTER - Violates every CLAUDE.md principle"
    elif complexity >= 7:
        return "OVER-ENGINEERED NIGHTMARE - More abstractions than a philosophy PhD"
    elif complexity >= 5:
        return "COMPLEXITY VIOLATION - Breaks CLAUDE.md threshold"
    elif cognitive_load >= 8:
        return "BRAIN MELTER - Causes immediate headaches"
    elif maintainability < 0.3:
        return "UNMAINTAINABLE MESS - Future developers will curse your name"
    elif maintainability < 0.5:
        return "QUESTIONABLE DESIGN - Maintenance will be painful"
    elif maintainability < 0.7:
        return "ACCEPTABLE BUT BLOATED - Could be simplified"
    else:
        return "ACTUALLY REASONABLE - Rare find in this codebase"

def main():
    """Execute the SAVAGE BENCHMARKING"""
    commands = [
        "reasoning-wrapper.md",
        "git-backup-sync.md", 
        "ultrathink.md",
        "context-enhanced-executor.md",
        "intelligent-refactor-session.md"
    ]
    
    results = []
    base_path = "/home/runner/work/claude-dotfiles/claude-dotfiles/commands"
    
    for cmd in commands:
        file_path = f"{base_path}/{cmd}"
        metrics = analyze_command(file_path)
        results.append(metrics)
        print(f"Analyzed {cmd}: Complexity={metrics.complexity_score}, Savage='{metrics.savage_rating}'")
    
    # Calculate statistics
    complexity_scores = [r.complexity_score for r in results]
    avg_complexity = sum(complexity_scores) / len(complexity_scores)
    max_complexity = max(complexity_scores)
    min_complexity = min(complexity_scores)
    
    # Generate savage commentary
    savage_stats = {
        "average_complexity": avg_complexity,
        "max_complexity": max_complexity,
        "violations": sum(1 for score in complexity_scores if score >= 5),
        "total_analyzed": len(results),
        "disaster_rate": sum(1 for score in complexity_scores if score >= 10) / len(results) * 100
    }
    
    return results, savage_stats

if __name__ == "__main__":
    results, stats = main()
    print(f"\nSAVAGE STATISTICS:")
    print(f"Average Complexity: {stats['average_complexity']:.1f}")
    print(f"CLAUDE.md Violations: {stats['violations']}/{stats['total_analyzed']}")
    print(f"Disaster Rate: {stats['disaster_rate']:.1f}%")