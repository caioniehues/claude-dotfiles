#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER
Scientific analysis with brutal honesty
"""

import json
import statistics

# Load the metrics data
metrics = {
  "adhd-context-switch": {
    "lines": 399,
    "characters": 9885,
    "estimated_tokens": 2471,
    "complexity_score": 4,
    "xml_tags": 28,
    "thinking_blocks": 0,
    "mcp_integrations": 4,
    "avg_line_length": 24.77,
    "file_size_kb": 9.65
  },
  "generate-thinking-command": {
    "lines": 137,
    "characters": 3803,
    "estimated_tokens": 950,
    "complexity_score": 3,
    "xml_tags": 26,
    "thinking_blocks": 9,
    "mcp_integrations": 1,
    "avg_line_length": 27.76,
    "file_size_kb": 3.71
  },
  "adhd-evening-reflect": {
    "lines": 438,
    "characters": 12536,
    "estimated_tokens": 3134,
    "complexity_score": 4,
    "xml_tags": 28,
    "thinking_blocks": 0,
    "mcp_integrations": 3,
    "avg_line_length": 28.62,
    "file_size_kb": 12.24
  },
  "intelligent-refactor-session": {
    "lines": 534,
    "characters": 16531,
    "estimated_tokens": 4132,
    "complexity_score": 10,
    "xml_tags": 68,
    "thinking_blocks": 62,
    "mcp_integrations": 1,
    "avg_line_length": 30.96,
    "file_size_kb": 16.14
  },
  "reasoning-wrapper": {
    "lines": 415,
    "characters": 10162,
    "estimated_tokens": 2540,
    "complexity_score": 7,
    "xml_tags": 67,
    "thinking_blocks": 35,
    "mcp_integrations": 2,
    "avg_line_length": 24.49,
    "file_size_kb": 9.92
  }
}

def analyze_violations():
    print("=== SAVAGE ANALYSIS: CLAUDE.MD VIOLATIONS ===")
    print()

    claude_md_max_complexity = 5
    violations = []

    for cmd, data in metrics.items():
        print(f"Command: {cmd}")
        print(f"  Complexity Score: {data['complexity_score']}/10")
        
        if data["complexity_score"] >= claude_md_max_complexity:
            violation_severity = data["complexity_score"] - claude_md_max_complexity + 1
            violations.append({
                "command": cmd,
                "violation": "complexity_exceeded",
                "severity": violation_severity,
                "actual": data["complexity_score"],
                "allowed": claude_md_max_complexity
            })
            print(f"  ❌ VIOLATION: Complexity {data['complexity_score']} >= {claude_md_max_complexity}")
            print(f"  🔥 SEVERITY: {violation_severity}/5 (BRUTAL)")
        else:
            print(f"  ✅ COMPLIANT: Under complexity limit")
        
        # Token consumption analysis
        if data["estimated_tokens"] > 3000:
            print(f"  ⚠️  TOKEN HOG: {data['estimated_tokens']} tokens (expensive!)")
        elif data["estimated_tokens"] > 2000:
            print(f"  ⚠️  TOKEN HEAVY: {data['estimated_tokens']} tokens")
        else:
            print(f"  ✅ TOKEN EFFICIENT: {data['estimated_tokens']} tokens")
        
        # Thinking block analysis
        thinking_ratio = data["thinking_blocks"] / data["lines"] * 100
        print(f"  Thinking blocks: {data['thinking_blocks']} ({thinking_ratio:.1f}% of lines)")
        
        print()
    
    return violations

def statistical_analysis():
    complexity_scores = [data["complexity_score"] for data in metrics.values()]
    token_counts = [data["estimated_tokens"] for data in metrics.values()]
    
    print("=== STATISTICAL BRUTALITY ===")
    print(f"Complexity Score Stats:")
    print(f"  Mean: {statistics.mean(complexity_scores):.2f}")
    print(f"  Median: {statistics.median(complexity_scores):.2f}")
    print(f"  Std Dev: {statistics.stdev(complexity_scores):.2f}")
    print(f"  Max: {max(complexity_scores)} (Worst offender)")
    print(f"  Min: {min(complexity_scores)} (Least bad)")
    print()

    print(f"Token Consumption Stats:")
    print(f"  Mean: {statistics.mean(token_counts):.0f} tokens")
    print(f"  Median: {statistics.median(token_counts):.0f} tokens")
    total_cost = sum(token_counts) * 0.000003
    print(f"  Total: {sum(token_counts)} tokens (Cost: ~${total_cost:.3f})")
    print()

def efficiency_rankings():
    efficiency_scores = {}
    for cmd, data in metrics.items():
        # Simple efficiency: functionality per token
        functionality_score = data["mcp_integrations"] + (data["thinking_blocks"] / 10) + (10 - data["complexity_score"])
        efficiency = functionality_score / data["estimated_tokens"] * 1000
        efficiency_scores[cmd] = efficiency

    print("=== EFFICIENCY RANKINGS (Higher = Better) ===")
    sorted_efficiency = sorted(efficiency_scores.items(), key=lambda x: x[1], reverse=True)
    for i, (cmd, score) in enumerate(sorted_efficiency):
        print(f"{i+1}. {cmd}: {score:.2f} efficiency points")
    print()
    return efficiency_scores

if __name__ == "__main__":
    violations = analyze_violations()
    statistical_analysis()
    efficiency_scores = efficiency_rankings()
    
    print("=== VIOLATIONS SUMMARY ===")
    print(f"Total violations: {len(violations)}")
    for v in violations:
        print(f"  - {v['command']}: {v['violation']} (severity {v['severity']}/5)")