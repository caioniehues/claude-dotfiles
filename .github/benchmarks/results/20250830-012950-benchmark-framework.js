/**
 * SAVAGE COMMAND BENCHMARKER - Scientific Measurement Framework
 * PhD-level statistical analysis of command effectiveness
 */

const SELECTED_COMMANDS = [
  'ultrathink.md',
  'java-rapid-implementation.md', 
  'adhd-morning-assistant.md',
  'analyze-project-architecture.md'
];

const BENCHMARK_METRICS = {
  // Objective measurements
  tokenConsumption: {
    input: 'measured',
    output: 'measured', 
    total: 'calculated'
  },
  executionTime: {
    startTime: 'timestamp',
    endTime: 'timestamp',
    duration: 'calculated',
    variance: 'statistical'
  },
  successRate: {
    definition: 'task_completed_as_intended',
    threshold: 0.8, // 80% success minimum
    failures: 'categorized'
  },
  complexityScore: {
    calculation: 'based_on_CLAUDE_md_rules',
    threshold: 5, // Must be < 5 per rules
    violations: 'counted'
  },
  composition: {
    chainability: 'tested',
    compatibility: 'matrix_analysis',
    conflicts: 'identified'
  }
};

const EVIDENCE_COLLECTION = {
  samplesPerCommand: 5,
  scenarios: [
    'simple_task',
    'moderate_complexity', 
    'edge_case',
    'error_condition',
    'integration_test'
  ],
  documentation: {
    screenshots: 'equivalent_outputs',
    errorLogs: 'full_traces',
    userExperience: 'subjective_scoring'
  }
};

const STATISTICAL_ANALYSIS = {
  descriptive: {
    mean: 'calculated',
    median: 'calculated', 
    stdDev: 'calculated',
    variance: 'calculated'
  },
  inferential: {
    confidenceInterval: 0.95,
    significanceLevel: 0.05,
    outlierDetection: 'modified_zscore'
  },
  comparative: {
    baseline: 'manual_execution',
    peerComparison: 'other_commands',
    benchmarkStandards: 'industry_norms'
  }
};

// SAVAGE JUDGMENT FRAMEWORK
const JUDGMENT_CRITERIA = {
  effectiveness: {
    excellent: '>90% success rate, σ<10%',
    good: '>80% success rate, σ<20%', 
    mediocre: '>60% success rate, σ<30%',
    garbage: '<60% success rate OR σ>30%'
  },
  efficiency: {
    tokenCostBenefit: 'time_saved / tokens_consumed',
    executionOverhead: 'vs_manual_baseline',
    memoryFootprint: 'resource_consumption'
  },
  reliability: {
    consistency: 'performance_variance',
    errorRate: 'failure_frequency', 
    recovery: 'error_handling_quality'
  }
};

module.exports = {
  SELECTED_COMMANDS,
  BENCHMARK_METRICS,
  EVIDENCE_COLLECTION,
  STATISTICAL_ANALYSIS,
  JUDGMENT_CRITERIA
};