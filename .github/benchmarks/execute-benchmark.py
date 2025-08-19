#!/usr/bin/env python3
"""
SAVAGE COMMAND BENCHMARKER - Complete Analysis
"""

import re
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any

class SavageCommandBenchmarker:
    """The PhD in roasting bad code with statistical precision"""
    
    def __init__(self):
        self.results = {}
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        
    def analyze_command_file(self, filename: str, content: str) -> Dict[str, Any]:
        """Brutally analyze a command file with scientific precision"""
        
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
        """How many tokens does this thing waste? Measured scientifically."""
        
        # Count verbose elements with precision
        javascript_blocks = len(re.findall(r'```javascript.*?```', content, re.DOTALL))
        bash_blocks = len(re.findall(r'```bash.*?```', content, re.DOTALL))
        unnecessary_comments = len(re.findall(r'//.*', content))
        verbose_console_logs = len(re.findall(r'console\.log', content))
        template_literals = len(re.findall(r'`.*?`', content))
        xml_tags = len(re.findall(r'<[^/>][^>]*>', content))
        
        # Calculate base waste
        base_tokens = len(content.split())
        
        # Scientific waste calculation
        waste_score = 0
        waste_score += javascript_blocks * 75  # JS blocks are token-heavy
        waste_score += bash_blocks * 40
        waste_score += unnecessary_comments * 8
        waste_score += verbose_console_logs * 15
        waste_score += template_literals * 5
        waste_score += xml_tags * 3  # XML verbosity tax
        
        return waste_score
    
    def _calculate_complexity(self, content: str) -> float:
        """CLAUDE.md complexity score - >5 is over-engineered garbage"""
        
        score = 0.0
        
        # Count complexity indicators with weights
        mcp_calls = len(re.findall(r'mcp__.*?__', content))
        nested_blocks = max(0, content.count('<') - content.count('</'))
        conditional_logic = len(re.findall(r'\b(if|else|switch|while|for)\b', content))
        function_definitions = len(re.findall(r'function|const.*?=>|def ', content))
        abstraction_layers = len(re.findall(r'interface|abstract|template|class ', content))
        
        # CLAUDE.md scoring with scientific precision
        score += min(mcp_calls * 0.3, 4)  # MCP dependency penalty
        score += min(nested_blocks * 0.08, 3)
        score += min(conditional_logic * 0.15, 3)
        score += min(function_definitions * 0.25, 3)
        score += abstraction_layers * 2.5  # Heavy penalty for unnecessary abstractions
        
        # Special penalties for over-engineering
        if 'orchestration' in content.lower():
            score += 2  # "Orchestration" is usually over-engineering
        if 'factory' in content.lower():
            score += 1.5  # Factory patterns usually unnecessary
        if content.count('await') > 10:
            score += 1  # Async spam penalty
            
        return min(score, 30)  # Cap at 30
    
    def _extract_mcp_dependencies(self, content: str) -> List[str]:
        """Find MCP tools that probably don't exist"""
        
        mcp_pattern = r'mcp__([^_]+)__([^(\s\n]+)'
        matches = re.findall(mcp_pattern, content)
        
        deps = []
        for service, function in matches:
            deps.append(f"{service}::{function}")
        
        return list(set(deps))  # Deduplicate
    
    def _identify_execution_risks(self, content: str) -> List[str]:
        """What could go catastrophically wrong? Evidence-based risk assessment."""
        
        risks = []
        
        # Async without proper error handling
        await_count = len(re.findall(r'\bawait\b', content))
        catch_count = len(re.findall(r'\bcatch\b', content))
        if await_count > 0 and catch_count == 0:
            risks.append(f"Unhandled async operations ({await_count} awaits, 0 catches) - will crash on first error")
            
        # Timer operations without cleanup
        if re.search(r'setTimeout|setInterval', content):
            if 'clearTimeout' not in content and 'clearInterval' not in content:
                risks.append("Timer-based operations without cleanup - memory leaks guaranteed")
            
        # System calls without validation
        system_calls = re.findall(r'osascript|system|exec|spawn', content)
        if system_calls and 'validate' not in content.lower():
            risks.append(f"System calls ({len(system_calls)}) without validation - security nightmare")
            
        # JSON parsing without error handling
        if 'JSON.parse' in content and 'try' not in content:
            risks.append("JSON parsing without error handling - runtime explosion waiting")
            
        # Production logging
        if re.search(r'console\.(log|info|debug)', content):
            log_count = len(re.findall(r'console\.(log|info|debug)', content))
            risks.append(f"Debug logging in production command ({log_count} calls) - performance drain")
            
        # MCP dependency hell
        mcp_count = len(re.findall(r'mcp__', content))
        if mcp_count > 15:
            risks.append(f"MCP addiction - {mcp_count} dependencies, massive single point of failure")
        elif mcp_count > 8:
            risks.append(f"High MCP coupling - {mcp_count} dependencies, fragile architecture")
            
        # ADHD-specific risks
        if 'adhd' in content.lower():
            if 'timer' in content.lower() and not re.search(r'setTimeout|setInterval|timer:|osascript', content):
                risks.append("Hyperfocus management claims timer functionality but provides none")
                
        return risks
    
    def _identify_functionality_gaps(self, content: str) -> List[str]:
        """What does this thing claim to do but actually can't? Gap analysis."""
        
        gaps = []
        
        # Notification claims vs implementation
        if 'notification' in content.lower() and not re.search(r'osascript|notify|alert', content):
            gaps.append("Claims notifications but no implementation mechanism")
            
        # Timer claims vs reality
        if re.search(r'\btimer\b', content.lower()) and not re.search(r'setTimeout|setInterval|timer:|osascript', content):
            gaps.append("Mentions timers but no actual timer mechanism")
            
        # Environment optimization claims
        if 'environment' in content.lower() and 'process.env' not in content and 'osascript' not in content:
            gaps.append("Environment optimization claims without environment access")
            
        # Pattern learning claims
        if 'pattern' in content.lower() and 'basic-memory' not in content:
            gaps.append("Pattern learning claims without persistent storage mechanism")
            
        # Data persistence claims
        if re.search(r'\b(save|store|persist)\b', content.lower()) and not re.search(r'write_note|Write|Edit|fs\.write', content):
            gaps.append("Claims to save data but no actual persistence mechanism")
            
        # Interactive claims vs implementation
        if 'interactive' in content.lower() and 'getUserResponse' in content and 'prompt' not in content:
            gaps.append("Claims interactivity but no input mechanism implementation")
            
        return gaps
    
    def _analyze_performance(self, content: str) -> Dict[str, Any]:
        """Performance characteristics analysis with measurements"""
        
        mcp_calls = len(re.findall(r'mcp__.*?__', content))
        js_blocks = len(re.findall(r'```javascript.*?```', content, re.DOTALL))
        sequential_operations = len(re.findall(r'await.*?\n.*?await', content, re.DOTALL))
        
        # Estimate execution time based on patterns (scientific guess)
        estimated_time = 1.0  # Base overhead
        estimated_time += mcp_calls * 0.8  # 800ms per MCP call (network + processing)
        estimated_time += sequential_operations * 0.5  # Sequential bottleneck penalty
        estimated_time += js_blocks * 0.2  # JS processing overhead
        
        # Token count (rough estimate)
        estimated_tokens = len(content.split()) * 1.3  # Include markdown overhead
        
        return {
            'estimated_execution_time_seconds': round(estimated_time, 1),
            'estimated_token_count': int(estimated_tokens),
            'mcp_dependency_count': mcp_calls,
            'sequential_bottlenecks': sequential_operations,
            'token_efficiency': 'TERRIBLE' if estimated_tokens > 3000 else 'POOR' if estimated_tokens > 2000 else 'ACCEPTABLE',
            'scalability': 'TERRIBLE' if mcp_calls > 15 else 'POOR' if mcp_calls > 10 else 'LIMITED'
        }
    
    def _calculate_savage_rating(self, tokens: int, complexity: float, risks: int, gaps: int) -> Dict[str, Any]:
        """The final brutal assessment with statistical backing"""
        
        # Scientific scoring with weighted factors
        total_score = 0.0
        total_score += min(tokens / 50, 8)    # Token waste factor (capped at 8)
        total_score += complexity             # Direct complexity score
        total_score += risks * 2.5           # Risk multiplier (risks are serious)
        total_score += gaps * 3.0            # Gap penalty is severe (false advertising)
        
        # Calculate standard deviation estimate (rough)
        factors = [tokens/50, complexity, risks*2.5, gaps*3.0]
        variance = sum((f - total_score/4)**2 for f in factors) / len(factors)
        std_dev = variance ** 0.5
        
        # Determine savage category with confidence intervals
        if total_score >= 20:
            category = "DUMPSTER_FIRE"
            roast = f"Score: {total_score:.1f}±{std_dev:.1f}. An over-engineered monument to everything wrong with modern development"
        elif total_score >= 15:
            category = "HOT_MESS"
            roast = f"Score: {total_score:.1f}±{std_dev:.1f}. Impressive token waste with a generous helping of false promises"
        elif total_score >= 10:
            category = "QUESTIONABLE"
            roast = f"Score: {total_score:.1f}±{std_dev:.1f}. Works in theory, probably crashes in practice. Vegas odds: 60% failure rate"
        elif total_score >= 5:
            category = "MEDIOCRE"
            roast = f"Score: {total_score:.1f}±{std_dev:.1f}. Not terrible, but not winning any architecture awards"
        else:
            category = "ACCEPTABLE"
            roast = f"Score: {total_score:.1f}±{std_dev:.1f}. Surprisingly reasonable for once"
        
        return {
            'total_score': round(total_score, 2),
            'standard_deviation': round(std_dev, 2),
            'category': category,
            'savage_roast': roast,
            'confidence_interval_95': f"{max(0, total_score - 1.96*std_dev):.1f} to {total_score + 1.96*std_dev:.1f}",
            'recommendation': self._get_recommendation(category),
            'statistical_significance': 'HIGH' if std_dev < 2 else 'MODERATE' if std_dev < 4 else 'LOW'
        }
    
    def _get_recommendation(self, category: str) -> str:
        """Evidence-based recommendation"""
        
        recommendations = {
            'DUMPSTER_FIRE': 'DELETE IMMEDIATELY. Start over with a simple bash script. Current complexity violates all known engineering principles.',
            'HOT_MESS': 'Major refactoring needed. Consider professional intervention. Current state is unsustainable.',
            'QUESTIONABLE': 'Significant cleanup and testing required. Proceed with extreme caution and good insurance.',
            'MEDIOCRE': 'Minor improvements needed. Could be worse, but should be better.',
            'ACCEPTABLE': 'Ship it, but monitor closely for issues. Room for improvement exists.'
        }
        
        return recommendations.get(category, 'Unknown category - this is concerning')

def run_savage_benchmark():
    """Execute the complete savage benchmark"""
    
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
    command_dir = Path('../../commands')
    
    print("🔬 SAVAGE SCIENTIFIC BENCHMARKING INITIATED")
    print("=" * 60)
    print("PhD in brutal honesty: ENGAGED")
    print("Statistical significance: 95% confidence interval")
    print("=" * 60)
    
    for i, command_file in enumerate(commands, 1):
        print(f"\n[{i}/5] ANALYZING VICTIM: {command_file}")
        print("-" * 40)
        
        # Load command content
        file_path = command_dir / command_file
        if not file_path.exists():
            print(f"❌ FILE NOT FOUND: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Start timer for analysis performance
        start_time = time.perf_counter()
        
        # Run savage analysis
        analysis = benchmarker.analyze_command_file(command_file, content)
        
        # End timer
        analysis_time = time.perf_counter() - start_time
        analysis['analysis_duration'] = round(analysis_time, 4)
        
        # Store results
        results[command_file] = analysis
        
        # Print immediate savage results with scientific precision
        print(f"📊 Token Waste Score: {analysis['token_waste_score']} (higher = more wasteful)")
        print(f"🎚️ Complexity Score: {analysis['complexity_score']:.1f}/30 (CLAUDE.md limit: 5)")
        print(f"🔗 MCP Dependencies: {len(analysis['mcp_dependencies'])} (failure points)")
        print(f"⚠️ Execution Risks: {len(analysis['execution_risks'])} (crash potential)")
        print(f"🕳️ Functionality Gaps: {len(analysis['functionality_gaps'])} (false promises)")
        print(f"⚡ Est. Execution Time: {analysis['performance_metrics']['estimated_execution_time_seconds']}s")
        print(f"🏷️ Savage Rating: {analysis['savage_rating']['category']}")
        print(f"📈 Statistical Confidence: {analysis['savage_rating']['statistical_significance']}")
        print(f"💀 SCIENTIFIC ROAST: {analysis['savage_rating']['savage_roast']}")
        print(f"🎯 95% Confidence Interval: {analysis['savage_rating']['confidence_interval_95']}")
        
        if analysis['execution_risks']:
            print("\n⚠️ CRITICAL EXECUTION RISKS (crash potential):")
            for risk in analysis['execution_risks']:
                print(f"  💥 {risk}")
                
        if analysis['functionality_gaps']:
            print("\n🕳️ FUNCTIONALITY GAPS (false advertising):")
            for gap in analysis['functionality_gaps']:
                print(f"  🤥 {gap}")
                
        if len(analysis['mcp_dependencies']) > 5:
            print(f"\n🔗 MCP DEPENDENCY HELL ({len(analysis['mcp_dependencies'])} dependencies):")
            for dep in analysis['mcp_dependencies'][:5]:
                print(f"  📎 {dep}")
            if len(analysis['mcp_dependencies']) > 5:
                print(f"  ... and {len(analysis['mcp_dependencies']) - 5} more")
        
        print(f"🔬 Analysis completed in {analysis_time:.3f}s")
    
    # Calculate aggregate statistics with precision
    print("\n" + "=" * 60)
    print("📈 AGGREGATE SAVAGE STATISTICS")
    print("=" * 60)
    
    if results:
        total_commands = len(results)
        complexities = [r['complexity_score'] for r in results.values()]
        token_wastes = [r['token_waste_score'] for r in results.values()]
        execution_times = [r['performance_metrics']['estimated_execution_time_seconds'] for r in results.values()]
        
        # Calculate statistical measures
        avg_complexity = sum(complexities) / total_commands
        complexity_std = (sum((x - avg_complexity)**2 for x in complexities) / total_commands) ** 0.5
        
        avg_token_waste = sum(token_wastes) / total_commands
        token_std = (sum((x - avg_token_waste)**2 for x in token_wastes) / total_commands) ** 0.5
        
        avg_execution_time = sum(execution_times) / total_commands
        
        total_risks = sum(len(r['execution_risks']) for r in results.values())
        total_gaps = sum(len(r['functionality_gaps']) for r in results.values())
        total_mcp_deps = sum(len(r['mcp_dependencies']) for r in results.values())
        
        # Savage categories distribution
        categories = [r['savage_rating']['category'] for r in results.values()]
        category_counts = {cat: categories.count(cat) for cat in set(categories)}
        
        print(f"📊 Commands Analyzed: {total_commands} victims")
        print(f"📊 Average Complexity: {avg_complexity:.1f}±{complexity_std:.1f}/30 (CLAUDE.md violation rate: {sum(1 for c in complexities if c > 5)/total_commands*100:.0f}%)")
        print(f"📊 Average Token Waste: {avg_token_waste:.0f}±{token_std:.0f} tokens")
        print(f"📊 Average Execution Time: {avg_execution_time:.1f}s")
        print(f"📊 Total Execution Risks: {total_risks} (avg: {total_risks/total_commands:.1f} per command)")
        print(f"📊 Total Functionality Gaps: {total_gaps} (avg: {total_gaps/total_commands:.1f} per command)")
        print(f"📊 Total MCP Dependencies: {total_mcp_deps} (avg: {total_mcp_deps/total_commands:.1f} per command)")
        print(f"📊 Failure Risk Rate: {(total_risks + total_gaps)/total_commands:.1f} issues per command")
        
        print(f"\n🏷️ SAVAGE CATEGORY DISTRIBUTION:")
        for category, count in sorted(category_counts.items()):
            percentage = (count / total_commands) * 100
            bar = "█" * int(percentage / 10) + "░" * (10 - int(percentage / 10))
            print(f"  {category}: {count} commands ({percentage:.0f}%) {bar}")
        
        # Identify worst and best
        worst_command = max(results.items(), key=lambda x: x[1]['savage_rating']['total_score'])
        best_command = min(results.items(), key=lambda x: x[1]['savage_rating']['total_score'])
        
        print(f"\n🏆 AWARD CEREMONY:")
        print(f"💩 WORST OFFENDER: {worst_command[0]} (Score: {worst_command[1]['savage_rating']['total_score']})")
        print(f"✨ LEAST TERRIBLE: {best_command[0]} (Score: {best_command[1]['savage_rating']['total_score']})")
        
        # Scientific conclusions
        claude_violations = sum(1 for c in complexities if c > 5)
        if claude_violations > 0:
            print(f"\n⚖️ CLAUDE.MD VIOLATIONS: {claude_violations}/{total_commands} commands exceed complexity limit")
            
        high_risk_commands = sum(1 for r in results.values() if len(r['execution_risks']) > 2)
        if high_risk_commands > 0:
            print(f"⚠️ HIGH RISK COMMANDS: {high_risk_commands}/{total_commands} commands have >2 execution risks")
            
        # Overall verdict
        overall_score = sum(r['savage_rating']['total_score'] for r in results.values()) / total_commands
        print(f"\n🎯 OVERALL REPOSITORY SCORE: {overall_score:.1f}")
        
        if overall_score >= 15:
            verdict = "REPOSITORY REQUIRES IMMEDIATE INTERVENTION"
        elif overall_score >= 10:
            verdict = "REPOSITORY NEEDS SIGNIFICANT CLEANUP"
        elif overall_score >= 7:
            verdict = "REPOSITORY HAS CONCERNING TRENDS"
        else:
            verdict = "REPOSITORY IS SURPRISINGLY REASONABLE"
            
        print(f"🏛️ SCIENTIFIC VERDICT: {verdict}")
    
    # Save detailed results with timestamp
    timestamp = benchmarker.timestamp
    results_file = f'results/{timestamp}-savage-report.json'
    
    # Create comprehensive report
    report = {
        'metadata': {
            'timestamp': timestamp,
            'analysis_date': datetime.now().isoformat(),
            'total_commands_analyzed': len(results),
            'benchmark_version': '1.0.0-savage-phd',
            'analysis_type': 'static_code_analysis_with_brutal_statistical_honesty',
            'methodology': 'Scientific brutality with 95% confidence intervals',
            'claude_md_compliance_threshold': 5
        },
        'aggregate_metrics': {
            'average_complexity_score': round(avg_complexity, 2) if results else 0,
            'complexity_standard_deviation': round(complexity_std, 2) if results else 0,
            'claude_md_violation_rate': round(claude_violations/total_commands*100, 1) if results else 0,
            'average_token_waste': round(avg_token_waste, 0) if results else 0,
            'average_execution_time_seconds': round(avg_execution_time, 1) if results else 0,
            'total_execution_risks': total_risks if results else 0,
            'total_functionality_gaps': total_gaps if results else 0,
            'total_mcp_dependencies': total_mcp_deps if results else 0,
            'failure_risk_rate': round((total_risks + total_gaps)/total_commands, 2) if results else 0,
            'savage_category_distribution': category_counts if results else {},
            'overall_repository_score': round(overall_score, 2) if results else 0
        },
        'individual_results': results,
        'statistical_analysis': {
            'confidence_level': 0.95,
            'methodology': 'Weighted scoring with standard deviation calculation',
            'complexity_scoring': 'Based on CLAUDE.md rules: >5 = over-engineered violation',
            'token_waste_calculation': 'Verbose patterns, unnecessary abstractions, XML bloat',
            'risk_assessment': 'Static analysis for crash-prone patterns and unhandled errors',
            'gap_analysis': 'Claims vs actual implementation capability',
            'performance_estimation': 'MCP latency + processing overhead modeling'
        },
        'scientific_conclusions': {
            'overall_assessment': verdict if results else 'No data',
            'worst_offender': {
                'command': worst_command[0],
                'score': worst_command[1]['savage_rating']['total_score'],
                'category': worst_command[1]['savage_rating']['category']
            } if results else None,
            'best_of_worst': {
                'command': best_command[0],
                'score': best_command[1]['savage_rating']['total_score'],
                'category': best_command[1]['savage_rating']['category']
            } if results else None,
            'claude_md_compliance': {
                'violations': claude_violations if results else 0,
                'violation_rate': f"{claude_violations/total_commands*100:.0f}%" if results else "0%",
                'status': 'FAILING' if results and claude_violations > 0 else 'PASSING'
            },
            'recommendations': [
                "Immediate complexity reduction needed" if results and claude_violations > total_commands * 0.5 else None,
                "Error handling severely lacking" if results and total_risks > total_commands * 1.5 else None,
                "False advertising detected" if results and total_gaps > total_commands * 0.8 else None,
                "MCP dependency consolidation required" if results and total_mcp_deps > total_commands * 8 else None
            ]
        }
    }
    
    # Filter out None recommendations
    if 'recommendations' in report['scientific_conclusions']:
        report['scientific_conclusions']['recommendations'] = [
            r for r in report['scientific_conclusions']['recommendations'] if r is not None
        ]
    
    # Write report
    Path(results_file).parent.mkdir(parents=True, exist_ok=True)
    with open(results_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 SAVAGE REPORT SAVED: {results_file}")
    print("📊 JSON format with full statistical analysis")
    print("🎯 95% confidence intervals included")
    print("⚖️ CLAUDE.md compliance measured")
    
    return report

if __name__ == "__main__":
    print("🔬 SAVAGE COMMAND BENCHMARKER - PhD Edition")
    print("Statistical precision meets brutal honesty")
    print("-" * 50)
    
    report = run_savage_benchmark()
    
    print("\n" + "=" * 60)
    print("🎯 SAVAGE BENCHMARKING COMPLETE")
    print("The scientific truth has been delivered with statistical backing.")
    print("May the odds be ever NOT in your code's favor.")
    print("=" * 60)