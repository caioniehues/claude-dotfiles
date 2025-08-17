#!/usr/bin/env python3
"""
Execute the savage benchmark on selected commands
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from pathlib import Path
import json
from datetime import datetime

# Import our savage benchmarker
exec(open('.github/benchmarks/results/20250817-220239-benchmark-framework.py').read())

def load_command_files():
    """Load the selected command files for benchmarking"""
    commands_dir = Path("commands")
    selected_commands = [
        "adhd-context-switch.md",
        "ultrathink.md", 
        "adhd-evening-reflect.md",
        "intelligent-code-enhancer.md",
        "adaptive-complexity-router.md"
    ]
    
    commands = []
    for cmd_file in selected_commands:
        file_path = commands_dir / cmd_file
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                commands.append((cmd_file.replace('.md', ''), content))
        else:
            print(f"⚠️ Command file not found: {cmd_file}")
    
    return commands

def main():
    print("\n🔬 SAVAGE COMMAND BENCHMARKER - PhD in Roasting Bad Code")
    print("=" * 80)
    print("MISSION: Scientifically measure and brutally judge commands")
    print("METHOD: Evidence-based statistical analysis with savage commentary")
    print("=" * 80)
    
    # Initialize benchmarker
    benchmarker = SavageBenchmarker()
    
    # Load commands
    commands = load_command_files()
    print(f"\n📋 LOADED {len(commands)} COMMANDS FOR SCIENTIFIC DESTRUCTION")
    for name, _ in commands:
        print(f"  • {name}")
    
    # Run benchmark suite
    results = benchmarker.run_benchmark_suite(commands)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    results_file = f".github/benchmarks/results/{timestamp}-savage-benchmark-report.json"
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 RESULTS SAVED TO: {results_file}")
    
    # Generate summary report
    print("\n" + "=" * 80)
    print("🏆 SAVAGE BENCHMARK RESULTS SUMMARY")
    print("=" * 80)
    
    stats = results["statistical_summary"]
    print(f"📊 STATISTICAL ANALYSIS:")
    print(f"   Mean Score: {stats['mean_score']:.2f}/10")
    print(f"   Std Dev: {stats['std_dev']:.2f}")
    print(f"   Score Range: {stats['min_score']:.1f} - {stats['max_score']:.1f}")
    print(f"   Total Commands: {results['benchmark_metadata']['total_commands']}")
    print(f"   Execution Time: {results['benchmark_metadata']['execution_time']:.2f}s")
    
    print(f"\n🏆 HALL OF FAME (Score ≥ 8.0):")
    for name in results["hall_of_fame"]:
        score = results["individual_results"][name]["overall_score"]
        print(f"   • {name}: {score}/10 ⭐")
    
    print(f"\n💩 HALL OF SHAME (Score < 4.0):")
    for name in results["hall_of_shame"]:
        score = results["individual_results"][name]["overall_score"]
        print(f"   • {name}: {score}/10 💩")
    
    print(f"\n📈 COMMAND RANKING:")
    for i, (name, result) in enumerate(results["ranking"], 1):
        score = result["overall_score"]
        complexity = result["complexity_analysis"]["complexity_score"]
        failures = result["failure_analysis"]["failure_count"]
        print(f"   {i}. {name}: {score}/10 (Complexity: {complexity}/5, Failures: {failures})")
    
    print(f"\n🔥 SAVAGE COMMENTARY HIGHLIGHTS:")
    for name, result in results["individual_results"].items():
        print(f"\n{name}:")
        print(f"   {result['savage_commentary']}")
    
    print("\n" + "=" * 80)
    print("🎯 CONCLUSION: The numbers don't lie. Some commands are statistical disasters.")
    print("=" * 80)
    
    return results_file

if __name__ == "__main__":
    results_file = main()
    print(f"\nDetailed report available at: {results_file}")