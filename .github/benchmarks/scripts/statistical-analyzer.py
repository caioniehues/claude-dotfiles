#!/usr/bin/env python3
"""
SAVAGE STATISTICAL ANALYZER
PhD-level statistical analysis with brutal honesty about command performance.
No participation trophies here - only cold, hard data and savage truths.
"""

import json
import numpy as np
import statistics
from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime
import sys

@dataclass
class BenchmarkData:
    """Raw benchmark data - no sugar coating"""
    command: str
    scenario: str
    tokens_input: int
    tokens_output: int
    execution_time: float
    success: bool
    complexity_score: int
    errors: List[str]
    memory_usage: float

@dataclass 
class SavageStatistics:
    """Statistics that hurt but tell the truth"""
    mean: float
    median: float
    std_dev: float
    variance: float
    min_val: float
    max_val: float
    confidence_interval: tuple
    sample_size: int
    outliers: List[float]
    
    def savage_assessment(self, metric_name: str) -> str:
        """Brutal but fair statistical assessment"""
        cv = self.std_dev / self.mean if self.mean > 0 else float('inf')
        
        if cv > 1.0:
            return f"{metric_name} has a coefficient of variation of {cv:.2f}. That's not 'variable', that's gambling with worse odds than a casino."
        elif cv > 0.5:
            return f"{metric_name} varies by {cv:.2f}. Consistency isn't this command's strong suit."
        elif cv > 0.3:
            return f"{metric_name} shows {cv:.2f} variation. Decent, but not winning any precision awards."
        elif cv > 0.1:
            return f"{metric_name} varies by {cv:.2f}. Actually respectable consistency."
        else:
            return f"{metric_name} has {cv:.2f} variation. Impressively consistent - this command has its shit together."

class SavageBenchmarkAnalyzer:
    """The PhD roaster of command performance"""
    
    def __init__(self):
        self.brutality_level = "MAXIMUM"
        self.confidence_level = 0.95
        
    def analyze_command_performance(self, data: List[BenchmarkData]) -> Dict[str, Any]:
        """Comprehensive statistical analysis with savage commentary"""
        
        if len(data) < 5:
            return {
                "error": f"Only {len(data)} samples? That's not statistics, that's anecdotal evidence. Come back with proper sample sizes."
            }
            
        # Extract metrics
        token_totals = [d.tokens_input + d.tokens_output for d in data]
        execution_times = [d.execution_time for d in data]
        success_rate = sum(1 for d in data if d.success) / len(data)
        complexity_scores = [d.complexity_score for d in data]
        error_counts = [len(d.errors) for d in data]
        
        # Calculate savage statistics
        token_stats = self._calculate_savage_stats(token_totals)
        time_stats = self._calculate_savage_stats(execution_times)
        complexity_stats = self._calculate_savage_stats(complexity_scores)
        error_stats = self._calculate_savage_stats(error_counts)
        
        # Token efficiency analysis
        successful_data = [d for d in data if d.success]
        if successful_data:
            successful_tokens = [d.tokens_input + d.tokens_output for d in successful_data]
            efficiency_stats = self._calculate_savage_stats(successful_tokens)
        else:
            efficiency_stats = None
            
        # The brutal truth calculation
        bullshit_factor = self._calculate_bullshit_factor(data)
        reality_gap = self._calculate_reality_gap(data)
        
        return {
            "command": data[0].command,
            "sample_size": len(data),
            "performance_metrics": {
                "token_consumption": {
                    "statistics": token_stats.__dict__,
                    "savage_assessment": token_stats.savage_assessment("Token consumption"),
                    "efficiency_per_success": efficiency_stats.__dict__ if efficiency_stats else "No successful runs to analyze"
                },
                "execution_time": {
                    "statistics": time_stats.__dict__,
                    "savage_assessment": time_stats.savage_assessment("Execution time")
                },
                "success_rate": {
                    "percentage": success_rate * 100,
                    "fraction": f"{sum(1 for d in data if d.success)}/{len(data)}",
                    "savage_assessment": self._assess_success_rate(success_rate)
                },
                "complexity_handling": {
                    "statistics": complexity_stats.__dict__,
                    "savage_assessment": complexity_stats.savage_assessment("Complexity scoring")
                },
                "error_frequency": {
                    "statistics": error_stats.__dict__,
                    "savage_assessment": error_stats.savage_assessment("Error frequency")
                }
            },
            "savage_insights": {
                "bullshit_factor": {
                    "score": bullshit_factor,
                    "interpretation": self._interpret_bullshit_factor(bullshit_factor)
                },
                "reality_gap": {
                    "score": reality_gap,
                    "interpretation": self._interpret_reality_gap(reality_gap)
                },
                "vegas_comparison": self._vegas_odds_comparison(success_rate),
                "brutal_summary": self._generate_brutal_summary(data, success_rate, bullshit_factor)
            }
        }
    
    def _calculate_savage_stats(self, values: List[float]) -> SavageStatistics:
        """Calculate statistics that don't lie"""
        if not values:
            return SavageStatistics(0, 0, 0, 0, 0, 0, (0, 0), 0, [])
            
        mean_val = statistics.mean(values)
        median_val = statistics.median(values)
        std_dev = statistics.stdev(values) if len(values) > 1 else 0
        variance = statistics.variance(values) if len(values) > 1 else 0
        
        # Confidence interval
        if len(values) > 1:
            margin = 1.96 * (std_dev / np.sqrt(len(values)))  # 95% CI
            ci = (mean_val - margin, mean_val + margin)
        else:
            ci = (mean_val, mean_val)
            
        # Outlier detection (IQR method)
        q1 = np.percentile(values, 25)
        q3 = np.percentile(values, 75)
        iqr = q3 - q1
        outliers = [v for v in values if v < q1 - 1.5*iqr or v > q3 + 1.5*iqr]
        
        return SavageStatistics(
            mean=mean_val,
            median=median_val,
            std_dev=std_dev,
            variance=variance,
            min_val=min(values),
            max_val=max(values),
            confidence_interval=ci,
            sample_size=len(values),
            outliers=outliers
        )
    
    def _assess_success_rate(self, rate: float) -> str:
        """Brutal assessment of success rate"""
        percentage = rate * 100
        
        if percentage >= 95:
            return f"{percentage:.1f}% success rate. Actually impressive - this command delivers."
        elif percentage >= 85:
            return f"{percentage:.1f}% success rate. Decent reliability, room for improvement."
        elif percentage >= 70:
            return f"{percentage:.1f}% success rate. Would you board a plane with these odds?"
        elif percentage >= 50:
            return f"{percentage:.1f}% success rate. Coin flip reliability. Literally."
        elif percentage >= 25:
            return f"{percentage:.1f}% success rate. Russian roulette has better odds."
        else:
            return f"{percentage:.1f}% success rate. This command is broken. Full stop."
    
    def _calculate_bullshit_factor(self, data: List[BenchmarkData]) -> float:
        """Measures unnecessary complexity vs actual utility"""
        total_complexity = sum(d.complexity_score for d in data)
        successful_utility = sum(1 for d in data if d.success)
        
        if successful_utility == 0:
            return float('inf')  # Infinite bullshit
            
        return total_complexity / successful_utility
    
    def _interpret_bullshit_factor(self, factor: float) -> str:
        """Savage interpretation of bullshit factor"""
        if factor == float('inf'):
            return "Infinite bullshit detected. All complexity, zero utility."
        elif factor > 10:
            return f"Bullshit factor: {factor:.1f}. This is complexity theater, not engineering."
        elif factor > 5:
            return f"Bullshit factor: {factor:.1f}. Over-engineered for what it delivers."
        elif factor > 3:
            return f"Bullshit factor: {factor:.1f}. Some unnecessary complexity detected."
        elif factor > 1:
            return f"Bullshit factor: {factor:.1f}. Reasonable complexity for utility provided."
        else:
            return f"Bullshit factor: {factor:.1f}. Surprisingly lean and effective."
    
    def _calculate_reality_gap(self, data: List[BenchmarkData]) -> float:
        """Measures gap between promise and delivery"""
        # This would need more context about what each command promises
        # For now, using success rate as a proxy
        success_rate = sum(1 for d in data if d.success) / len(data)
        return 1.0 - success_rate
    
    def _interpret_reality_gap(self, gap: float) -> str:
        """Interpret the reality gap"""
        percentage = gap * 100
        if percentage < 5:
            return f"Reality gap: {percentage:.1f}%. Promises mostly match delivery."
        elif percentage < 15:
            return f"Reality gap: {percentage:.1f}%. Minor overpromising detected."
        elif percentage < 30:
            return f"Reality gap: {percentage:.1f}%. Significant gap between hype and reality."
        elif percentage < 50:
            return f"Reality gap: {percentage:.1f}%. More promise than delivery."
        else:
            return f"Reality gap: {percentage:.1f}%. This command writes checks its ass can't cash."
    
    def _vegas_odds_comparison(self, success_rate: float) -> str:
        """Compare to Vegas gambling odds"""
        percentage = success_rate * 100
        
        if percentage > 95:
            return "Better odds than the house edge. Actually reliable."
        elif percentage > 85:
            return "Better than most slot machines. Not bad."
        elif percentage > 70:
            return "Worse than blackjack basic strategy. Concerning."
        elif percentage > 50:
            return "Coin flip territory. Might as well gamble."
        elif percentage > 30:
            return "Worse than roulette. At least roulette pays well."
        else:
            return "Lottery ticket odds. But lottery tickets are cheaper."
    
    def _generate_brutal_summary(self, data: List[BenchmarkData], success_rate: float, bullshit_factor: float) -> str:
        """The final brutal verdict"""
        command = data[0].command
        
        if success_rate < 0.5:
            verdict = "BROKEN"
        elif bullshit_factor > 5:
            verdict = "OVER-ENGINEERED"
        elif success_rate > 0.9 and bullshit_factor < 2:
            verdict = "ACTUALLY GOOD"
        else:
            verdict = "MEDIOCRE"
            
        return f"Command '{command}' receives verdict: {verdict}. " + \
               f"Success rate of {success_rate*100:.1f}% with bullshit factor {bullshit_factor:.1f}. " + \
               "The numbers don't lie, even when feelings get hurt."

def main():
    """Main analysis entry point"""
    analyzer = SavageBenchmarkAnalyzer()
    print("🔬 SAVAGE STATISTICAL ANALYZER - PhD in Roasting Commands")
    print("Preparing to deliver brutal truths backed by mathematics...")

if __name__ == "__main__":
    main()