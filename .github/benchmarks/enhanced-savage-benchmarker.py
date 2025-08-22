#!/usr/bin/env python3
"""
ENHANCED SAVAGE COMMAND BENCHMARKER v2.0
PhD-level statistical analysis with brutal but fair judgment
"""

import json
import time
import statistics
import re
import hashlib
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Tuple
import math

@dataclass
class EnhancedMetrics:
    """Comprehensive command analysis metrics"""
    name: str
    file_size_bytes: int
    line_count: int
    word_count: int
    token_estimate: int
    complexity_score: int
    mcp_dependencies: List[str]
    mcp_dependency_count: int
    xml_blocks: int
    thinking_blocks: int
    code_blocks: int
    template_quality: int
    reusability_score: int
    estimated_response_time: float
    performance_tier: str
    failure_modes: List[str]
    composition_compatibility: List[str]
    maintenance_burden: str
    innovation_score: int

@dataclass
class StatisticalAnalysis:
    """Rigorous statistical measurements"""
    mean: float
    median: float
    std_deviation: float
    variance: float
    confidence_interval_95: Tuple[float, float]
    sample_size: int
    coefficient_of_variation: float
    outliers: List[float]
    distribution_shape: str

@dataclass 
class BenchmarkEvidence:
    """Hard evidence supporting all claims"""
    content_hash: str
    creation_timestamp: str
    sample_content: List[str]
    complexity_breakdown: Dict[str, int]
    dependency_analysis: Dict[str, Any]
    performance_measurements: Dict[str, float]
    failure_simulation_results: List[str]
    comparison_baseline: Dict[str, float]

@dataclass
class SavageVerdict:
    """Data-backed brutal assessment"""
    final_score: float
    grade: str
    strengths: List[str]
    weaknesses: List[str]
    brutal_commentary: str
    improvement_recommendations: List[str]
    comparable_commands: List[str]
    roi_assessment: str

class EnhancedSavageBenchmarker:
    """Scientific command torture testing with PhD-level statistical rigor"""
    
    def __init__(self):
        self.commands_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/commands")
        self.results_dir = Path("/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results")
        self.baseline_metrics = self._establish_baseline()
        self.selected_commands = [
            "reasoning-wrapper",
            "adhd-context-switch", 
            "ultrathink-full-mcp",
            "ultrathink-hybrid-mcp",
            "java-clean-code-generator"
        ]
        
    def _establish_baseline(self) -> Dict[str, float]:
        """Establish baseline metrics for comparison"""
        return {
            "acceptable_complexity": 5.0,
            "target_response_time": 4.0,
            "minimum_reusability": 6.0,
            "acceptable_token_count": 3000,
            "target_success_rate": 0.85,
            "maximum_dependencies": 3
        }
    
    def analyze_command_deeply(self, command_file: Path) -> EnhancedMetrics:
        """Perform comprehensive deep analysis of command"""
        content = command_file.read_text()
        
        # Basic metrics
        file_size = command_file.stat().st_size
        lines = content.splitlines()
        words = content.split()
        
        # Advanced analysis
        complexity = self._calculate_advanced_complexity(content)
        mcp_deps = self._extract_mcp_dependencies(content)
        xml_blocks = len(re.findall(r'<[^/>][^>]*>', content))
        thinking_blocks = len(re.findall(r'<thinking>', content, re.IGNORECASE))
        code_blocks = len(re.findall(r'```', content))
        
        # Quality assessments
        template_quality = self._assess_template_quality(content)
        reusability = self._calculate_reusability(content)
        response_time = self._estimate_response_time(content, len(mcp_deps), complexity)
        perf_tier = self._classify_performance_tier(response_time, complexity)
        
        # Risk analysis
        failure_modes = self._identify_failure_modes(content, complexity, len(mcp_deps))
        composition = self._analyze_composition_patterns(content)
        maintenance = self._assess_maintenance_burden(content, complexity)
        innovation = self._score_innovation(content)
        
        return EnhancedMetrics(
            name=command_file.stem,
            file_size_bytes=file_size,
            line_count=len(lines),
            word_count=len(words),
            token_estimate=len(words) * 1.3,  # Conservative estimate
            complexity_score=complexity,
            mcp_dependencies=mcp_deps,
            mcp_dependency_count=len(mcp_deps),
            xml_blocks=xml_blocks,
            thinking_blocks=thinking_blocks,
            code_blocks=code_blocks,
            template_quality=template_quality,
            reusability_score=reusability,
            estimated_response_time=response_time,
            performance_tier=perf_tier,
            failure_modes=failure_modes,
            composition_compatibility=composition,
            maintenance_burden=maintenance,
            innovation_score=innovation
        )
    
    def _calculate_advanced_complexity(self, content: str) -> int:
        """Advanced complexity scoring based on CLAUDE.md rules"""
        score = 1  # Base solution
        
        # Structural complexity
        score += len(re.findall(r'class\s+\w+', content, re.IGNORECASE)) * 2
        score += len(re.findall(r'interface\s+\w+', content, re.IGNORECASE)) * 1
        score += len(re.findall(r'abstract\s+class', content, re.IGNORECASE)) * 2
        
        # Design pattern complexity
        patterns = ['factory', 'builder', 'strategy', 'observer', 'singleton', 'adapter']
        for pattern in patterns:
            score += len(re.findall(pattern, content, re.IGNORECASE)) * 3
        
        # Configuration complexity
        score += len(re.findall(r'\.(xml|yml|yaml|properties)', content)) * 2
        
        # MCP complexity
        score += len(re.findall(r'mcp__[^_]+__[^\s\(]+', content)) * 1
        
        # Nested thinking complexity
        nested_thinking = len(re.findall(r'<thinking>.*?<thinking>', content, re.DOTALL))
        score += nested_thinking * 2
        
        # Sequential thinking penalty
        if 'sequentialthinking' in content.lower():
            score += 5
        
        # XML structure complexity
        xml_depth = self._calculate_xml_nesting_depth(content)
        score += max(0, xml_depth - 2)  # Penalty for deep nesting
        
        return min(score, 15)  # Cap at 15
    
    def _calculate_xml_nesting_depth(self, content: str) -> int:
        """Calculate maximum XML nesting depth"""
        max_depth = 0
        current_depth = 0
        
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('<') and not line.startswith('</') and not line.endswith('/>'):
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif line.startswith('</'):
                current_depth = max(0, current_depth - 1)
                
        return max_depth
    
    def _extract_mcp_dependencies(self, content: str) -> List[str]:
        """Extract and categorize MCP dependencies"""
        pattern = r'mcp__([^_\s]+)__([^\s\(]+)'
        matches = re.findall(pattern, content)
        return [f"{provider}__{tool}" for provider, tool in matches]
    
    def _assess_template_quality(self, content: str) -> int:
        """Assess quality of template structure (1-10)"""
        score = 5  # Baseline
        
        # Positive indicators
        if '$ARGUMENTS' in content or '${' in content:
            score += 2  # Parameterized
        if '<task>' in content and '<context>' in content:
            score += 1  # Well structured
        if 'example' in content.lower():
            score += 1  # Has examples
        if len(re.findall(r'###?\s+', content)) >= 5:
            score += 1  # Good section organization
            
        # Negative indicators
        if len(content.split()) > 6000:
            score -= 2  # Too bloated
        if content.count('hardcoded') > 0:
            score -= 1  # Hardcoded values
        if len(re.findall(r'TODO|FIXME|XXX', content, re.IGNORECASE)) > 0:
            score -= 1  # Incomplete
            
        return max(1, min(10, score))
    
    def _calculate_reusability(self, content: str) -> int:
        """Calculate reusability score (1-10)"""
        score = 5  # Baseline
        
        # Parameterization
        if '$ARGUMENTS' in content:
            score += 2
        if '${' in content:
            score += 1
            
        # Structure quality
        if '<task>' in content:
            score += 1
        if len(re.findall(r'<[^>]+>', content)) > 8:
            score += 1  # Good XML structure
            
        # Composition friendly
        if 'template' in content.lower():
            score += 1
        if 'example' in content.lower():
            score += 1
            
        # Negative factors
        if 'ultrathink-full' in content.lower():
            score -= 2  # Too heavyweight
        if len(content.split()) > 5000:
            score -= 1  # Too complex
        if 'hardcoded' in content.lower():
            score -= 2  # Not flexible
            
        return max(1, min(10, score))
    
    def _estimate_response_time(self, content: str, mcp_count: int, complexity: int) -> float:
        """Estimate realistic response time in seconds"""
        base_time = 1.5  # Base processing time
        
        # Content processing time
        token_count = len(content.split()) * 1.3
        base_time += token_count / 2000  # 2000 tokens per second baseline
        
        # Complexity penalty
        base_time += complexity * 0.4
        
        # MCP call overhead
        base_time += mcp_count * 1.2  # Each MCP call adds latency
        
        # Thinking overhead
        thinking_count = len(re.findall(r'<thinking>', content, re.IGNORECASE))
        base_time += thinking_count * 0.3
        
        # Sequential thinking major penalty
        if 'sequentialthinking' in content.lower():
            base_time += 8.0  # Major latency increase
            
        # XML processing overhead
        xml_count = len(re.findall(r'<[^>]+>', content))
        base_time += xml_count * 0.01
        
        return round(base_time, 2)
    
    def _classify_performance_tier(self, response_time: float, complexity: int) -> str:
        """Classify command into performance tier"""
        if response_time <= 2.0 and complexity <= 3:
            return "FAST_SIMPLE"
        elif response_time <= 4.0 and complexity <= 5:
            return "MEDIUM_BALANCED"
        elif response_time <= 8.0 and complexity <= 8:
            return "SLOW_COMPLEX"
        else:
            return "HEAVYWEIGHT_BEAST"
    
    def _identify_failure_modes(self, content: str, complexity: int, mcp_count: int) -> List[str]:
        """Identify potential failure modes"""
        failures = []
        
        # Complexity failures
        if complexity > 10:
            failures.append("COMPLEXITY_OVERFLOW: Users will get lost in abstraction layers")
        elif complexity > 7:
            failures.append("COMPLEXITY_WARNING: Approaching cognitive overload threshold")
            
        # Dependency failures
        if mcp_count > 5:
            failures.append("DEPENDENCY_HELL: High failure probability from external services")
        elif mcp_count > 3:
            failures.append("DEPENDENCY_RISK: Multiple points of failure")
            
        # Token failures
        token_count = len(content.split()) * 1.3
        if token_count > 5000:
            failures.append("TOKEN_BOMB: May exceed context limits")
        elif token_count > 4000:
            failures.append("TOKEN_HEAVY: Approaching practical limits")
            
        # Performance failures
        if 'sequentialthinking' in content.lower():
            failures.append("TIMEOUT_RISK: Sequential thinking may cause timeouts")
            
        # Maintenance failures
        if len(content.splitlines()) > 1000:
            failures.append("MAINTENANCE_NIGHTMARE: Command too large for effective debugging")
            
        # Usability failures
        if '$ARGUMENTS' not in content and '${' not in content:
            failures.append("REUSABILITY_ZERO: Hardcoded command with no flexibility")
            
        return failures
    
    def _analyze_composition_patterns(self, content: str) -> List[str]:
        """Analyze what this command composes well with"""
        patterns = []
        
        content_lower = content.lower()
        
        if 'java' in content_lower:
            patterns.append("java-ecosystem")
        if 'test' in content_lower or 'tdd' in content_lower:
            patterns.append("testing-workflow")
        if 'mcp__basic-memory' in content:
            patterns.append("memory-persistent")
        if 'thinking' in content_lower:
            patterns.append("reasoning-enhanced")
        if 'agent' in content_lower:
            patterns.append("agent-orchestration")
        if 'adhd' in content_lower:
            patterns.append("adhd-optimized")
        if 'ultrathink' in content_lower:
            patterns.append("deep-analysis")
        if 'refactor' in content_lower:
            patterns.append("code-improvement")
        if 'sequential' in content_lower:
            patterns.append("complex-reasoning")
        if 'wrapper' in content_lower:
            patterns.append("meta-command")
            
        return patterns
    
    def _assess_maintenance_burden(self, content: str, complexity: int) -> str:
        """Assess maintenance difficulty"""
        lines = len(content.splitlines())
        
        if complexity <= 3 and lines <= 200:
            return "LOW"
        elif complexity <= 5 and lines <= 500:
            return "MEDIUM"
        elif complexity <= 8 and lines <= 1000:
            return "HIGH"
        else:
            return "NIGHTMARE"
    
    def _score_innovation(self, content: str) -> int:
        """Score innovation/novelty (1-10)"""
        score = 5  # Baseline
        
        # Innovation indicators
        if 'sequentialthinking' in content.lower():
            score += 2  # Advanced reasoning
        if 'meta' in content.lower() or 'wrapper' in content.lower():
            score += 1  # Meta-programming
        if 'orchestration' in content.lower():
            score += 1  # System integration
        if 'adaptive' in content.lower():
            score += 1  # Adaptive behavior
        if 'pattern' in content.lower() and 'learning' in content.lower():
            score += 2  # Learning systems
            
        # Subtract for common patterns
        if 'simple' in content.lower():
            score -= 1  # Basic approach
        if 'standard' in content.lower():
            score -= 1  # Standard solution
            
        return max(1, min(10, score))
    
    def perform_statistical_analysis(self, metrics_list: List[EnhancedMetrics], metric_name: str) -> StatisticalAnalysis:
        """Perform rigorous statistical analysis on any metric"""
        values = [getattr(m, metric_name) for m in metrics_list if hasattr(m, metric_name)]
        
        if not values:
            return StatisticalAnalysis(0, 0, 0, 0, (0, 0), 0, 0, [], "INSUFFICIENT_DATA")
        
        # Basic statistics
        mean_val = statistics.mean(values)
        median_val = statistics.median(values)
        
        if len(values) > 1:
            std_dev = statistics.stdev(values)
            variance = statistics.variance(values)
        else:
            std_dev = 0
            variance = 0
        
        # Confidence interval (95%)
        if len(values) > 1 and std_dev > 0:
            margin = 1.96 * (std_dev / math.sqrt(len(values)))
            ci = (mean_val - margin, mean_val + margin)
        else:
            ci = (mean_val, mean_val)
        
        # Coefficient of variation
        cv = (std_dev / mean_val) if mean_val != 0 else 0
        
        # Outlier detection (simple IQR method)
        if len(values) >= 4:
            q1 = statistics.quantiles(values, n=4)[0]
            q3 = statistics.quantiles(values, n=4)[2]
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = [v for v in values if v < lower_bound or v > upper_bound]
        else:
            outliers = []
        
        # Distribution shape assessment
        if cv < 0.1:
            dist_shape = "HIGHLY_CONSISTENT"
        elif cv < 0.3:
            dist_shape = "CONSISTENT"
        elif cv < 0.5:
            dist_shape = "MODERATE_VARIATION"
        else:
            dist_shape = "HIGH_VARIATION"
        
        return StatisticalAnalysis(
            mean=round(mean_val, 3),
            median=round(median_val, 3),
            std_deviation=round(std_dev, 3),
            variance=round(variance, 3),
            confidence_interval_95=ci,
            sample_size=len(values),
            coefficient_of_variation=round(cv, 3),
            outliers=outliers,
            distribution_shape=dist_shape
        )
    
    def collect_evidence(self, command_file: Path, metrics: EnhancedMetrics) -> BenchmarkEvidence:
        """Collect hard evidence for all claims"""
        content = command_file.read_text()
        
        # Content hash for integrity
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        
        # Creation timestamp
        creation_time = datetime.fromtimestamp(command_file.stat().st_mtime).isoformat()
        
        # Sample content (first and last few lines)
        lines = content.splitlines()
        sample_content = lines[:3] + ["..."] + lines[-3:] if len(lines) > 6 else lines
        
        # Complexity breakdown
        complexity_breakdown = {
            "xml_blocks": metrics.xml_blocks,
            "thinking_blocks": metrics.thinking_blocks,
            "code_blocks": metrics.code_blocks,
            "mcp_dependencies": metrics.mcp_dependency_count,
            "total_score": metrics.complexity_score
        }
        
        # Dependency analysis
        dependency_analysis = {
            "mcp_tools": metrics.mcp_dependencies,
            "dependency_types": list(set([dep.split('__')[0] for dep in metrics.mcp_dependencies])),
            "external_dependency_count": len(set([dep.split('__')[0] for dep in metrics.mcp_dependencies]))
        }
        
        # Performance measurements
        performance_measurements = {
            "estimated_response_time": metrics.estimated_response_time,
            "token_efficiency": metrics.reusability_score / max(metrics.token_estimate / 1000, 1),
            "complexity_per_line": metrics.complexity_score / max(metrics.line_count, 1),
            "features_per_kb": len(metrics.composition_compatibility) / max(metrics.file_size_bytes / 1024, 1)
        }
        
        # Failure simulation
        failure_simulation = []
        for failure in metrics.failure_modes:
            probability = self._estimate_failure_probability(failure, metrics)
            failure_simulation.append(f"{failure}: {probability:.1%} probability")
        
        # Baseline comparison
        baseline_comparison = {
            "complexity_vs_baseline": metrics.complexity_score / self.baseline_metrics["acceptable_complexity"],
            "response_time_vs_baseline": metrics.estimated_response_time / self.baseline_metrics["target_response_time"],
            "reusability_vs_baseline": metrics.reusability_score / self.baseline_metrics["minimum_reusability"],
            "tokens_vs_baseline": metrics.token_estimate / self.baseline_metrics["acceptable_token_count"]
        }
        
        return BenchmarkEvidence(
            content_hash=content_hash,
            creation_timestamp=creation_time,
            sample_content=sample_content,
            complexity_breakdown=complexity_breakdown,
            dependency_analysis=dependency_analysis,
            performance_measurements=performance_measurements,
            failure_simulation_results=failure_simulation,
            comparison_baseline=baseline_comparison
        )
    
    def _estimate_failure_probability(self, failure_mode: str, metrics: EnhancedMetrics) -> float:
        """Estimate probability of specific failure mode"""
        if "COMPLEXITY_OVERFLOW" in failure_mode:
            return min(0.8, (metrics.complexity_score - 10) * 0.1)
        elif "DEPENDENCY_HELL" in failure_mode:
            return min(0.7, metrics.mcp_dependency_count * 0.1)
        elif "TOKEN_BOMB" in failure_mode:
            return min(0.6, (metrics.token_estimate - 5000) / 10000)
        elif "TIMEOUT_RISK" in failure_mode:
            return min(0.5, (metrics.estimated_response_time - 10) * 0.05)
        elif "MAINTENANCE_NIGHTMARE" in failure_mode:
            return min(0.4, (metrics.line_count - 1000) / 2000)
        else:
            return 0.1  # Default low probability
    
    def generate_savage_verdict(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence, 
                              stats: Dict[str, StatisticalAnalysis]) -> SavageVerdict:
        """Generate brutal but data-backed verdict"""
        
        # Calculate final score (0-100)
        final_score = self._calculate_final_score(metrics, evidence)
        
        # Assign grade
        grade = self._assign_grade(final_score)
        
        # Identify strengths and weaknesses
        strengths = self._identify_strengths(metrics, evidence)
        weaknesses = self._identify_weaknesses(metrics, evidence)
        
        # Generate brutal commentary
        commentary = self._generate_brutal_commentary(metrics, evidence, final_score)
        
        # Generate improvements
        improvements = self._generate_improvement_recommendations(metrics, evidence)
        
        # Find comparable commands
        comparable = self._find_comparable_commands(metrics)
        
        # ROI assessment
        roi = self._assess_roi(metrics, evidence)
        
        return SavageVerdict(
            final_score=final_score,
            grade=grade,
            strengths=strengths,
            weaknesses=weaknesses,
            brutal_commentary=commentary,
            improvement_recommendations=improvements,
            comparable_commands=comparable,
            roi_assessment=roi
        )
    
    def _calculate_final_score(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence) -> float:
        """Calculate scientific final score (0-100)"""
        score = 50  # Baseline
        
        # Performance factors (30 points)
        response_score = max(0, 15 - (metrics.estimated_response_time - 2) * 2)
        score += response_score
        
        token_efficiency = evidence.performance_measurements["token_efficiency"]
        efficiency_score = min(15, token_efficiency * 3)
        score += efficiency_score
        
        # Quality factors (40 points)
        reusability_score = min(20, metrics.reusability_score * 2)
        score += reusability_score
        
        complexity_score = max(0, 10 - (metrics.complexity_score - 5) * 2) if metrics.complexity_score > 5 else 10
        score += complexity_score
        
        template_score = min(10, metrics.template_quality)
        score += template_score
        
        # Innovation/Value factors (30 points)
        innovation_score = min(15, metrics.innovation_score * 1.5)
        score += innovation_score
        
        composition_score = min(10, len(metrics.composition_compatibility) * 2)
        score += composition_score
        
        failure_penalty = len(metrics.failure_modes) * 3
        score -= failure_penalty
        
        dependency_penalty = max(0, (metrics.mcp_dependency_count - 3) * 2)
        score -= dependency_penalty
        
        return max(0, min(100, round(score, 1)))
    
    def _assign_grade(self, score: float) -> str:
        """Assign letter grade based on score"""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    def _identify_strengths(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence) -> List[str]:
        """Identify command strengths"""
        strengths = []
        
        if metrics.complexity_score <= 5:
            strengths.append(f"Low complexity ({metrics.complexity_score}/15) follows CLAUDE.md principles")
        
        if metrics.estimated_response_time <= 3:
            strengths.append(f"Fast response time ({metrics.estimated_response_time}s)")
        
        if metrics.reusability_score >= 7:
            strengths.append(f"High reusability score ({metrics.reusability_score}/10)")
        
        if metrics.mcp_dependency_count == 0:
            strengths.append("Zero external dependencies - bulletproof reliability")
        
        if metrics.template_quality >= 8:
            strengths.append(f"Excellent template structure ({metrics.template_quality}/10)")
        
        if metrics.innovation_score >= 7:
            strengths.append(f"High innovation value ({metrics.innovation_score}/10)")
        
        if len(metrics.failure_modes) == 0:
            strengths.append("No identified failure modes - robust design")
        
        return strengths or ["Functional - meets basic requirements"]
    
    def _identify_weaknesses(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence) -> List[str]:
        """Identify command weaknesses"""
        weaknesses = []
        
        if metrics.complexity_score > 8:
            weaknesses.append(f"Excessive complexity ({metrics.complexity_score}/15) violates simplicity principles")
        
        if metrics.estimated_response_time > 8:
            weaknesses.append(f"Slow response time ({metrics.estimated_response_time}s) - users will suffer")
        
        if metrics.reusability_score <= 4:
            weaknesses.append(f"Poor reusability ({metrics.reusability_score}/10) - one-trick pony")
        
        if metrics.mcp_dependency_count > 5:
            weaknesses.append(f"Dependency hell ({metrics.mcp_dependency_count} MCP tools) - fragile")
        
        if len(metrics.failure_modes) > 2:
            weaknesses.append(f"Multiple failure modes ({len(metrics.failure_modes)}) - unreliable")
        
        if metrics.maintenance_burden == "NIGHTMARE":
            weaknesses.append("Maintenance nightmare - will cause developer tears")
        
        if metrics.token_estimate > 5000:
            weaknesses.append(f"Token bloat ({metrics.token_estimate:,}) - inefficient")
        
        return weaknesses or ["Room for improvement in all areas"]
    
    def _generate_brutal_commentary(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence, score: float) -> str:
        """Generate brutally honest commentary"""
        
        if score >= 85:
            return f"🏆 {metrics.name} scores {score}/100 - Actually competent! Complexity {metrics.complexity_score}, response {metrics.estimated_response_time}s. Rare to see engineering principles properly applied."
        
        elif score >= 70:
            return f"👍 {metrics.name} scores {score}/100 - Adequate performance. Not embarrassing, which is surprisingly good for developer work."
        
        elif score >= 55:
            return f"😐 {metrics.name} scores {score}/100 - Mediocre but functional. The 'participation trophy' of commands."
        
        elif score >= 40:
            return f"⚠️ {metrics.name} scores {score}/100 - Below average. Like a car that starts most of the time."
        
        else:
            brutal_issues = []
            
            if metrics.complexity_score > 10:
                brutal_issues.append(f"complexity {metrics.complexity_score}/15 (architectural masturbation)")
            
            if metrics.estimated_response_time > 10:
                brutal_issues.append(f"{metrics.estimated_response_time}s response time (users will age visibly)")
            
            if metrics.mcp_dependency_count > 5:
                brutal_issues.append(f"{metrics.mcp_dependency_count} dependencies (single point of failure festival)")
            
            if len(metrics.failure_modes) > 3:
                brutal_issues.append(f"{len(metrics.failure_modes)} failure modes (Murphy's Law playground)")
            
            issues_text = ", ".join(brutal_issues) if brutal_issues else "fundamental incompetence"
            
            return f"💀 {metrics.name} scores {score}/100 - Systematic failure with {issues_text}. Recommend complete refactoring or ritual burning."
    
    def _generate_improvement_recommendations(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence) -> List[str]:
        """Generate actionable improvement recommendations"""
        improvements = []
        
        if metrics.complexity_score > 8:
            improvements.append(f"CRITICAL: Reduce complexity from {metrics.complexity_score} to <5 by eliminating unnecessary abstractions")
        
        if metrics.estimated_response_time > 8:
            improvements.append(f"PERFORMANCE: Optimize response time from {metrics.estimated_response_time}s to <4s")
        
        if metrics.mcp_dependency_count > 3:
            improvements.append(f"RELIABILITY: Reduce MCP dependencies from {metrics.mcp_dependency_count} to ≤3")
        
        if metrics.reusability_score < 6:
            improvements.append(f"REUSABILITY: Improve score from {metrics.reusability_score} to ≥6 by adding parameterization")
        
        if metrics.token_estimate > 4000:
            improvements.append(f"EFFICIENCY: Reduce token usage from {metrics.token_estimate:,} to <4000")
        
        if len(metrics.failure_modes) > 1:
            improvements.append(f"ROBUSTNESS: Address {len(metrics.failure_modes)} failure modes for better reliability")
        
        if metrics.template_quality < 6:
            improvements.append(f"STRUCTURE: Improve template quality from {metrics.template_quality} to ≥7")
        
        return improvements or ["Continue monitoring - no critical issues detected"]
    
    def _find_comparable_commands(self, metrics: EnhancedMetrics) -> List[str]:
        """Find commands with similar characteristics"""
        # This would typically search through all commands, but for now return logical comparisons
        comparable = []
        
        if metrics.performance_tier == "HEAVYWEIGHT_BEAST":
            comparable.extend(["ultrathink-full-mcp", "sequential-thinking-orchestrator"])
        elif metrics.performance_tier == "FAST_SIMPLE":
            comparable.extend(["simple-utilities", "basic-templates"])
        elif "java" in metrics.name:
            comparable.extend(["java-clean-code-generator", "java-tdd", "java-rapid-implementation"])
        elif "adhd" in metrics.name:
            comparable.extend(["adhd-morning-assistant", "adhd-task-breakdown"])
        elif "ultrathink" in metrics.name:
            comparable.extend(["reasoning-wrapper", "thinking-enhancer"])
        
        return comparable[:3]  # Return top 3
    
    def _assess_roi(self, metrics: EnhancedMetrics, evidence: BenchmarkEvidence) -> str:
        """Assess return on investment"""
        value_score = metrics.reusability_score + metrics.innovation_score + len(metrics.composition_compatibility)
        cost_score = metrics.complexity_score + (metrics.estimated_response_time / 2) + len(metrics.failure_modes)
        
        roi_ratio = value_score / max(cost_score, 1)
        
        if roi_ratio > 2.0:
            return f"EXCELLENT ROI ({roi_ratio:.1f}x) - High value, reasonable cost"
        elif roi_ratio > 1.5:
            return f"GOOD ROI ({roi_ratio:.1f}x) - Positive value proposition"
        elif roi_ratio > 1.0:
            return f"MARGINAL ROI ({roi_ratio:.1f}x) - Barely worth the effort"
        else:
            return f"NEGATIVE ROI ({roi_ratio:.1f}x) - Costs exceed benefits"
    
    def execute_comprehensive_benchmark(self) -> Dict[str, Any]:
        """Execute the full savage benchmark suite"""
        print("🔥 ENHANCED SAVAGE BENCHMARKER v2.0 ACTIVATED")
        print("=" * 70)
        print("PhD-level statistical analysis with brutal honesty")
        print()
        
        results = []
        all_metrics = []
        
        # Process each selected command
        for cmd_name in self.selected_commands:
            cmd_file = self.commands_dir / f"{cmd_name}.md"
            
            if not cmd_file.exists():
                print(f"❌ {cmd_name}.md not found - skipping")
                continue
            
            print(f"🔬 ANALYZING: {cmd_name}")
            
            # Deep analysis
            metrics = self.analyze_command_deeply(cmd_file)
            evidence = self.collect_evidence(cmd_file, metrics)
            
            all_metrics.append(metrics)
            
            # Generate verdict
            verdict = self.generate_savage_verdict(metrics, evidence, {})
            
            result = {
                "command": cmd_name,
                "metrics": asdict(metrics),
                "evidence": asdict(evidence),
                "verdict": asdict(verdict)
            }
            
            results.append(result)
            
            print(f"   📊 Score: {verdict.final_score}/100 (Grade: {verdict.grade})")
            print(f"   🎯 {verdict.brutal_commentary}")
            print()
        
        # Statistical analysis across all commands
        statistical_analyses = {}
        metrics_to_analyze = [
            'complexity_score', 'estimated_response_time', 'reusability_score', 
            'token_estimate', 'mcp_dependency_count', 'innovation_score'
        ]
        
        for metric in metrics_to_analyze:
            statistical_analyses[metric] = asdict(self.perform_statistical_analysis(all_metrics, metric))
        
        # Generate final report
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Calculate aggregate statistics
        all_scores = [r["verdict"]["final_score"] for r in results]
        avg_score = statistics.mean(all_scores) if all_scores else 0
        score_std = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
        
        # Overall assessment
        if avg_score >= 80:
            overall_assessment = "🏆 SURPRISINGLY COMPETENT: Commands show proper engineering"
        elif avg_score >= 70:
            overall_assessment = "👍 ADEQUATE: Not embarrassing, which is good"
        elif avg_score >= 60:
            overall_assessment = "😐 MEDIOCRE: Functional but uninspiring"
        elif avg_score >= 40:
            overall_assessment = "⚠️ PROBLEMATIC: Significant issues detected"
        else:
            overall_assessment = "💀 CATASTROPHIC: Fundamental problems require intervention"
        
        report = {
            "benchmark_metadata": {
                "timestamp": timestamp,
                "version": "2.0-savage-phd",
                "commands_analyzed": len(results),
                "analysis_depth": "COMPREHENSIVE"
            },
            "executive_summary": {
                "average_score": round(avg_score, 1),
                "score_standard_deviation": round(score_std, 2),
                "score_range": [min(all_scores), max(all_scores)] if all_scores else [0, 0],
                "overall_assessment": overall_assessment
            },
            "statistical_analysis": statistical_analyses,
            "command_results": results,
            "rankings": sorted(results, key=lambda x: x["verdict"]["final_score"], reverse=True),
            "key_findings": self._generate_key_findings(results, statistical_analyses),
            "strategic_recommendations": self._generate_strategic_recommendations(results)
        }
        
        return report
    
    def _generate_key_findings(self, results: List[Dict], stats: Dict[str, Any]) -> List[str]:
        """Generate key insights from analysis"""
        findings = []
        
        # Complexity analysis
        complexity_stats = stats.get("complexity_score", {})
        avg_complexity = complexity_stats.get("mean", 0)
        
        if avg_complexity > 8:
            findings.append(f"🚨 EXCESSIVE COMPLEXITY: Average {avg_complexity:.1f}/15 exceeds recommended threshold")
        elif avg_complexity > 5:
            findings.append(f"⚠️ COMPLEXITY WARNING: Average {avg_complexity:.1f}/15 approaching limits")
        else:
            findings.append(f"✅ COMPLEXITY GOOD: Average {avg_complexity:.1f}/15 within acceptable range")
        
        # Performance analysis
        time_stats = stats.get("estimated_response_time", {})
        avg_time = time_stats.get("mean", 0)
        
        if avg_time > 8:
            findings.append(f"🐌 PERFORMANCE POOR: Average {avg_time:.1f}s response time")
        elif avg_time > 4:
            findings.append(f"⏱️ PERFORMANCE SLOW: Average {avg_time:.1f}s response time")
        else:
            findings.append(f"⚡ PERFORMANCE GOOD: Average {avg_time:.1f}s response time")
        
        # Dependency analysis
        dep_stats = stats.get("mcp_dependency_count", {})
        avg_deps = dep_stats.get("mean", 0)
        
        if avg_deps > 5:
            findings.append(f"🕸️ DEPENDENCY HELL: Average {avg_deps:.1f} MCP dependencies")
        elif avg_deps > 3:
            findings.append(f"🔗 DEPENDENCY RISK: Average {avg_deps:.1f} MCP dependencies")
        else:
            findings.append(f"🛡️ DEPENDENCY SAFE: Average {avg_deps:.1f} MCP dependencies")
        
        # Innovation analysis
        innovation_stats = stats.get("innovation_score", {})
        avg_innovation = innovation_stats.get("mean", 0)
        
        if avg_innovation >= 7:
            findings.append(f"🚀 HIGH INNOVATION: Average {avg_innovation:.1f}/10 innovation score")
        elif avg_innovation >= 5:
            findings.append(f"💡 MODERATE INNOVATION: Average {avg_innovation:.1f}/10 innovation score")
        else:
            findings.append(f"📋 LOW INNOVATION: Average {avg_innovation:.1f}/10 innovation score")
        
        return findings
    
    def _generate_strategic_recommendations(self, results: List[Dict]) -> List[str]:
        """Generate high-level strategic recommendations"""
        recommendations = []
        
        # Analyze distribution of issues
        high_complexity_count = sum(1 for r in results if r["metrics"]["complexity_score"] > 8)
        slow_commands_count = sum(1 for r in results if r["metrics"]["estimated_response_time"] > 8)
        low_reusability_count = sum(1 for r in results if r["metrics"]["reusability_score"] < 5)
        high_dependency_count = sum(1 for r in results if r["metrics"]["mcp_dependency_count"] > 5)
        
        if high_complexity_count > 0:
            recommendations.append(f"🎯 SIMPLIFICATION PRIORITY: {high_complexity_count} commands need complexity reduction")
        
        if slow_commands_count > 0:
            recommendations.append(f"⚡ PERFORMANCE OPTIMIZATION: {slow_commands_count} commands need speed improvements")
        
        if low_reusability_count > 0:
            recommendations.append(f"🔄 REUSABILITY ENHANCEMENT: {low_reusability_count} commands need better parameterization")
        
        if high_dependency_count > 0:
            recommendations.append(f"🛡️ DEPENDENCY REDUCTION: {high_dependency_count} commands are too fragile")
        
        # Strategic insights
        total_commands = len(results)
        if total_commands > 0:
            success_rate = sum(1 for r in results if r["verdict"]["final_score"] >= 70) / total_commands
            
            if success_rate < 0.5:
                recommendations.append("🚨 SYSTEMATIC OVERHAUL: <50% commands meet quality standards - fundamental review needed")
            elif success_rate < 0.8:
                recommendations.append("📈 QUALITY IMPROVEMENT: Focus on bringing underperforming commands up to standard")
            else:
                recommendations.append("✅ QUALITY MAINTENANCE: Most commands are adequate - focus on optimization")
        
        return recommendations

def main():
    """Execute the enhanced savage benchmark"""
    benchmarker = EnhancedSavageBenchmarker()
    
    # Execute comprehensive analysis
    report = benchmarker.execute_comprehensive_benchmark()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_file = benchmarker.results_dir / f"{timestamp}-savage-benchmark-report.json"
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("=" * 70)
    print("🎯 FINAL SCIENTIFIC VERDICT")
    print("=" * 70)
    print(f"📊 Average Score: {report['executive_summary']['average_score']}/100")
    print(f"📈 Score Range: {report['executive_summary']['score_range']}")
    print(f"🎓 Assessment: {report['executive_summary']['overall_assessment']}")
    print()
    
    print("🏆 COMMAND RANKINGS:")
    for i, result in enumerate(report['rankings']):
        score = result['verdict']['final_score']
        grade = result['verdict']['grade']
        name = result['command']
        print(f"{i+1}. {name} - {score}/100 (Grade: {grade})")
    
    print()
    print("🔍 KEY FINDINGS:")
    for finding in report['key_findings']:
        print(f"   {finding}")
    
    print()
    print("🎯 STRATEGIC RECOMMENDATIONS:")
    for rec in report['strategic_recommendations']:
        print(f"   {rec}")
    
    print()
    print(f"📄 Full report: {report_file}")
    
    return report

if __name__ == "__main__":
    main()