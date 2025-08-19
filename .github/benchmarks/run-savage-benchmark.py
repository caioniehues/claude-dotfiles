#!/usr/bin/env python3
"""
Execute the savage benchmark on selected commands
"""

import json
import time
from pathlib import Path
from savage_analysis import SavageCommandBenchmarker

def run_benchmark():
    benchmarker = SavageCommandBenchmarker()
    
    # Commands selected for savage analysis
    commands = [
        'adhd-morning-assistant.md',
        'ultrathink-interactive.md', 
        'ultrathink-full-mcp.md',
        'reasoning-wrapper.md',
        'adhd-hyperfocus-guardian.md'
    ]
    
    results = {}
    command_dir = Path('commands')
    
    print("🔬 SAVAGE SCIENTIFIC BENCHMARKING INITIATED")
    print("=" * 60)
    
    for i, command_file in enumerate(commands, 1):
        print(f"\n[{i}/5] ANALYZING: {command_file}")
        print("-" * 40)
        
        # Load command content
        file_path = command_dir / command_file
        if not file_path.exists():
            print(f"❌ FILE NOT FOUND: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Start timer
        start_time = time.time()
        
        # Run savage analysis
        analysis = benchmarker.analyze_command_file(command_file, content)
        
        # End timer
        analysis_time = time.time() - start_time
        analysis['analysis_duration'] = analysis_time
        
        # Store results
        results[command_file] = analysis
        
        # Print immediate savage results
        print(f"📊 Token Waste Score: {analysis['token_waste_score']}")
        print(f"🎚️ Complexity Score: {analysis['complexity_score']:.1f}/30")
        print(f"⚠️ Execution Risks: {len(analysis['execution_risks'])}")
        print(f"🕳️ Functionality Gaps: {len(analysis['functionality_gaps'])}")
        print(f"🏷️ Savage Rating: {analysis['savage_rating']['category']}")
        print(f"💀 Roast: {analysis['savage_rating']['savage_roast']}")
        
        if analysis['execution_risks']:
            print("⚠️ CRITICAL RISKS:")
            for risk in analysis['execution_risks']:
                print(f"  - {risk}")
                
        if analysis['functionality_gaps']:
            print("🕳️ FUNCTIONALITY GAPS:")
            for gap in analysis['functionality_gaps']:
                print(f"  - {gap}")
    
    # Calculate aggregate statistics
    print("\n" + "=" * 60)
    print("📈 AGGREGATE SAVAGE STATISTICS")
    print("=" * 60)
    
    if results:
        total_commands = len(results)
        avg_complexity = sum(r['complexity_score'] for r in results.values()) / total_commands
        avg_token_waste = sum(r['token_waste_score'] for r in results.values()) / total_commands
        total_risks = sum(len(r['execution_risks']) for r in results.values())
        total_gaps = sum(len(r['functionality_gaps']) for r in results.values())
        
        # Savage categories distribution
        categories = [r['savage_rating']['category'] for r in results.values()]
        category_counts = {cat: categories.count(cat) for cat in set(categories)}
        
        print(f"📊 Commands Analyzed: {total_commands}")
        print(f"📊 Average Complexity: {avg_complexity:.1f}/30 (>5 is over-engineered)")
        print(f"📊 Average Token Waste: {avg_token_waste:.1f}")
        print(f"📊 Total Execution Risks: {total_risks}")
        print(f"📊 Total Functionality Gaps: {total_gaps}")
        print(f"📊 Risk Rate: {total_risks/total_commands:.1f} risks per command")
        print(f"📊 Gap Rate: {total_gaps/total_commands:.1f} gaps per command")
        
        print("\n🏷️ SAVAGE CATEGORY DISTRIBUTION:")
        for category, count in category_counts.items():
            percentage = (count / total_commands) * 100
            print(f"  {category}: {count} commands ({percentage:.1f}%)")
    
    # Save detailed results
    timestamp = benchmarker.timestamp
    results_file = f'.github/benchmarks/results/{timestamp}-savage-report.json'
    
    # Create comprehensive report
    report = {
        'metadata': {
            'timestamp': timestamp,
            'total_commands_analyzed': len(results),
            'benchmark_version': '1.0.0-savage',
            'analysis_type': 'static_code_analysis_with_brutal_honesty'
        },
        'aggregate_metrics': {
            'average_complexity_score': avg_complexity if results else 0,
            'average_token_waste': avg_token_waste if results else 0,
            'total_execution_risks': total_risks if results else 0,
            'total_functionality_gaps': total_gaps if results else 0,
            'savage_category_distribution': category_counts if results else {}
        },
        'individual_results': results,
        'methodology': {
            'complexity_scoring': 'Based on CLAUDE.md rules: >5 = over-engineered',
            'token_waste_calculation': 'Verbose patterns, unnecessary abstractions',
            'risk_assessment': 'Static analysis for crash-prone patterns',
            'gap_analysis': 'Promises vs actual implementation',
            'savage_rating': 'Scientific brutality with 95% confidence'
        },
        'conclusions': generate_conclusions(results) if results else {}
    }
    
    # Write report
    Path(results_file).parent.mkdir(parents=True, exist_ok=True)
    with open(results_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 SAVAGE REPORT SAVED: {results_file}")
    return report

def generate_conclusions(results):
    """Generate scientific conclusions with savage honesty"""
    
    if not results:
        return {}
    
    # Calculate statistics
    complexities = [r['complexity_score'] for r in results.values()]
    token_wastes = [r['token_waste_score'] for r in results.values()]
    
    avg_complexity = sum(complexities) / len(complexities)
    max_complexity = max(complexities)
    min_complexity = min(complexities)
    
    # Find worst offenders
    worst_command = max(results.items(), key=lambda x: x[1]['savage_rating']['total_score'])
    best_command = min(results.items(), key=lambda x: x[1]['savage_rating']['total_score'])
    
    return {
        'overall_assessment': get_overall_assessment(avg_complexity),
        'worst_offender': {
            'command': worst_command[0],
            'score': worst_command[1]['savage_rating']['total_score'],
            'category': worst_command[1]['savage_rating']['category']
        },
        'best_of_worst': {
            'command': best_command[0],
            'score': best_command[1]['savage_rating']['total_score'],
            'category': best_command[1]['savage_rating']['category']
        },
        'complexity_analysis': {
            'average': avg_complexity,
            'range': f"{min_complexity:.1f} - {max_complexity:.1f}",
            'claude_md_compliance': 'FAILING' if avg_complexity > 5 else 'PASSING'
        },
        'scientific_recommendation': get_scientific_recommendation(results)
    }

def get_overall_assessment(avg_complexity):
    """Overall savage assessment"""
    if avg_complexity > 15:
        return "Command repository is an over-engineered disaster zone"
    elif avg_complexity > 10:
        return "Moderate over-engineering with concerning trends"
    elif avg_complexity > 5:
        return "Complexity creep detected, intervention needed"
    else:
        return "Surprisingly reasonable complexity levels"

def get_scientific_recommendation(results):
    """Evidence-based recommendations"""
    
    high_complexity = sum(1 for r in results.values() if r['complexity_score'] > 10)
    high_risk = sum(1 for r in results.values() if len(r['execution_risks']) > 2)
    high_gaps = sum(1 for r in results.values() if len(r['functionality_gaps']) > 1)
    
    recommendations = []
    
    if high_complexity > len(results) * 0.3:
        recommendations.append("Major refactoring needed to reduce complexity")
    
    if high_risk > len(results) * 0.2:
        recommendations.append("Error handling and validation severely lacking")
        
    if high_gaps > len(results) * 0.2:
        recommendations.append("Commands over-promise and under-deliver")
    
    if not recommendations:
        recommendations.append("Continue monitoring for complexity creep")
    
    return recommendations

if __name__ == "__main__":
    report = run_benchmark()
    print("\n🎯 SAVAGE BENCHMARKING COMPLETE")
    print("The truth has been scientifically delivered.")