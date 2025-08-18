import json
import statistics
from pathlib import Path

def analyze_commands():
    commands_dir = Path("commands")
    
    # Read sample commands
    sample_files = [
        "adaptive-complexity-router.md",
        "adhd-hyperfocus-guardian.md", 
        "java-clean-code-generator.md",
        "ultrathink.md",
        "intelligent-code-enhancer.md"
    ]
    
    results = []
    for filename in sample_files:
        filepath = commands_dir / filename
        if filepath.exists():
            content = filepath.read_text()
            
            # Calculate metrics
            lines = content.split('\n')
            line_count = len(lines)
            
            # Complexity scoring (based on CLAUDE.md)
            complexity = 1  # base
            complexity += len([l for l in lines if 'class ' in l]) * 2
            complexity += len([l for l in lines if 'interface' in l])
            complexity += len([l for l in lines if any(p in l.lower() for p in ['factory', 'pattern', 'strategy'])])
            
            # Quality metrics
            has_thinking = any('<thinking' in l for l in lines)
            has_mcp = any('mcp__' in l for l in lines)
            thinking_lines = len([l for l in lines if '<thinking' in l or '</thinking>' in l])
            thinking_overhead = (thinking_lines / line_count * 100) if line_count > 0 else 0
            
            # ADHD optimization
            adhd_score = 0
            adhd_features = ['time', 'break', 'hyperfocus', 'context switch', 'task breakdown']
            for feature in adhd_features:
                if feature in content.lower():
                    adhd_score += 1
                    
            result = {
                'name': filename,
                'line_count': line_count,
                'complexity_score': complexity,
                'thinking_overhead_pct': thinking_overhead,
                'has_thinking_blocks': has_thinking,
                'has_mcp_integration': has_mcp,
                'adhd_optimization_score': adhd_score,
                'passes_complexity_rule': complexity < 5
            }
            results.append(result)
    
    return results

# Run analysis
print("🔬 SAVAGE COMMAND BENCHMARKER")
print("=" * 50)
results = analyze_commands()

for r in results:
    print(f"\n{r['name']}:")
    print(f"  Lines: {r['line_count']}")
    print(f"  Complexity: {r['complexity_score']}/5 {'✅' if r['passes_complexity_rule'] else '❌ VIOLATION'}")
    print(f"  Thinking Overhead: {r['thinking_overhead_pct']:.1f}%")
    print(f"  ADHD Score: {r['adhd_optimization_score']}/5")
    print(f"  MCP Integration: {'✅' if r['has_mcp_integration'] else '❌'}")

# Statistical summary
complexities = [r['complexity_score'] for r in results]
overheads = [r['thinking_overhead_pct'] for r in results]
violations = len([r for r in results if not r['passes_complexity_rule']])

print(f"\n📊 SAVAGE STATISTICAL ANALYSIS:")
print(f"Sample Size: {len(results)} commands")
print(f"Complexity Violations: {violations}/{len(results)} ({violations/len(results)*100:.0f}%)")
print(f"Average Complexity: {statistics.mean(complexities):.1f}")
print(f"Average Thinking Bloat: {statistics.mean(overheads):.1f}%")
print(f"Most Bloated: {max(results, key=lambda x: x['thinking_overhead_pct'])['name']} ({max(overheads):.1f}%)")

# Save detailed results
output = {
    'timestamp': '2025-08-18T11:33:26',
    'sample_size': len(results),
    'violations': violations,
    'avg_complexity': statistics.mean(complexities),
    'avg_thinking_overhead': statistics.mean(overheads),
    'results': results
}

with open('.github/benchmarks/results/20250818-113326-report.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n✅ Full report saved to .github/benchmarks/results/20250818-113326-report.json")