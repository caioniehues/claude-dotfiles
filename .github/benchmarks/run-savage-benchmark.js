#!/usr/bin/env node

/**
 * RANDOM COMMAND SELECTOR & SAVAGE BENCHMARKER
 * Scientifically selects random commands and roasts them with statistical precision
 */

const fs = require('fs');
const path = require('path');
const SavageCommandBenchmarker = require('./command-benchmark-framework');

class RandomCommandSelector {
    constructor() {
        this.commandsDir = path.join(__dirname, '../../commands');
        this.availableCommands = [];
        this.selectedCommands = [];
    }

    loadAvailableCommands() {
        console.log('🔍 Scanning commands directory for victims...');
        
        this.availableCommands = fs.readdirSync(this.commandsDir)
            .filter(file => file.endsWith('.md'))
            .map(file => {
                const fullPath = path.join(this.commandsDir, file);
                const content = fs.readFileSync(fullPath, 'utf8');
                
                return {
                    filename: file,
                    name: path.basename(file, '.md'),
                    path: fullPath,
                    size: content.length,
                    complexity: this.estimateComplexity(content),
                    type: this.classifyCommand(content),
                    lastModified: fs.statSync(fullPath).mtime
                };
            });
        
        console.log(`📋 Found ${this.availableCommands.length} commands ready for scientific judgment`);
        return this.availableCommands;
    }

    estimateComplexity(content) {
        let score = 0;
        const indicators = [
            { pattern: /mcp__/g, weight: 2 },
            { pattern: /<thinking>/g, weight: 3 },
            { pattern: /orchestration/gi, weight: 4 },
            { pattern: /sequential/gi, weight: 3 },
            { pattern: /complexity/gi, weight: 2 },
            { pattern: /###/g, weight: 1 },
            { pattern: /```/g, weight: 1 }
        ];
        
        indicators.forEach(({ pattern, weight }) => {
            const matches = (content.match(pattern) || []).length;
            score += matches * weight;
        });
        
        return Math.min(score, 20);
    }

    classifyCommand(content) {
        if (content.includes('java') || content.includes('Java')) return 'java';
        if (content.includes('adhd') || content.includes('ADHD')) return 'adhd';
        if (content.includes('think') || content.includes('analysis')) return 'thinking';
        if (content.includes('git') || content.includes('backup')) return 'utility';
        if (content.includes('refactor') || content.includes('enhance')) return 'code-enhancement';
        return 'general';
    }

    selectRandomCommands(count = 5, criteria = {}) {
        console.log(`🎯 Selecting ${count} random commands for scientific torture...`);
        
        let candidates = [...this.availableCommands];
        
        // Apply criteria filters
        if (criteria.minComplexity) {
            candidates = candidates.filter(cmd => cmd.complexity >= criteria.minComplexity);
        }
        if (criteria.maxComplexity) {
            candidates = candidates.filter(cmd => cmd.complexity <= criteria.maxComplexity);
        }
        if (criteria.type) {
            candidates = candidates.filter(cmd => cmd.type === criteria.type);
        }
        if (criteria.minSize) {
            candidates = candidates.filter(cmd => cmd.size >= criteria.minSize);
        }
        if (criteria.maxSize) {
            candidates = candidates.filter(cmd => cmd.size <= criteria.maxSize);
        }

        console.log(`📊 ${candidates.length} commands match criteria`);
        
        // Randomly select commands
        const selected = [];
        while (selected.length < count && candidates.length > 0) {
            const randomIndex = Math.floor(Math.random() * candidates.length);
            selected.push(candidates.splice(randomIndex, 1)[0]);
        }
        
        this.selectedCommands = selected;
        
        console.log('🎲 RANDOMLY SELECTED VICTIMS FOR SCIENTIFIC JUDGMENT:');
        selected.forEach((cmd, index) => {
            console.log(`   ${index + 1}. ${cmd.name} (${cmd.type}, complexity: ${cmd.complexity}, size: ${cmd.size})`);
        });
        
        return selected;
    }

    async runSavageBenchmarks() {
        console.log('\n🔬 INITIATING SAVAGE SCIENTIFIC ANALYSIS');
        console.log('========================================');
        
        // Create enhanced benchmarker with selected commands
        const benchmarker = new EnhancedSavageBenchmarker(this.selectedCommands);
        
        const reportPath = await benchmarker.runBenchmarks();
        
        console.log('\n💀 SAVAGE ANALYSIS COMPLETE');
        console.log(`📊 Results written to: ${reportPath}`);
        
        return reportPath;
    }

    generateSelectionReport() {
        const timestamp = new Date().toISOString().slice(0, 19).replace(/[:.]/g, '-');
        const reportPath = path.join(__dirname, `results/${timestamp}-selection-report.json`);
        
        const report = {
            timestamp: new Date().toISOString(),
            totalAvailable: this.availableCommands.length,
            selectedCount: this.selectedCommands.length,
            selectionCriteria: 'Random with statistical distribution',
            selectedCommands: this.selectedCommands.map(cmd => ({
                name: cmd.name,
                type: cmd.type,
                complexity: cmd.complexity,
                size: cmd.size,
                lastModified: cmd.lastModified
            })),
            distributionAnalysis: this.analyzeDistribution()
        };
        
        fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
        console.log(`📋 Selection report saved: ${reportPath}`);
        
        return reportPath;
    }

    analyzeDistribution() {
        const typeDistribution = {};
        const complexityRanges = { low: 0, medium: 0, high: 0 };
        const sizeRanges = { small: 0, medium: 0, large: 0 };
        
        this.selectedCommands.forEach(cmd => {
            // Type distribution
            typeDistribution[cmd.type] = (typeDistribution[cmd.type] || 0) + 1;
            
            // Complexity distribution
            if (cmd.complexity <= 5) complexityRanges.low++;
            else if (cmd.complexity <= 10) complexityRanges.medium++;
            else complexityRanges.high++;
            
            // Size distribution
            if (cmd.size <= 5000) sizeRanges.small++;
            else if (cmd.size <= 15000) sizeRanges.medium++;
            else sizeRanges.large++;
        });
        
        return {
            byType: typeDistribution,
            byComplexity: complexityRanges,
            bySize: sizeRanges
        };
    }
}

class EnhancedSavageBenchmarker extends SavageCommandBenchmarker {
    constructor(selectedCommands) {
        super();
        this.selectedCommands = selectedCommands;
        
        // Enhanced test cases with more variety
        this.enhancedTestCases = [
            {
                type: 'simple-task',
                input: 'Create a hello world function',
                expectedPatterns: ['function', 'hello', 'world'],
                complexity: 1
            },
            {
                type: 'medium-complexity',
                input: 'Design a REST API for user management with authentication',
                expectedPatterns: ['REST', 'API', 'user', 'authentication'],
                complexity: 5
            },
            {
                type: 'high-complexity',
                input: 'Architect a distributed microservices system with event sourcing and CQRS',
                expectedPatterns: ['microservices', 'event sourcing', 'CQRS', 'distributed'],
                complexity: 10
            },
            {
                type: 'edge-case',
                input: '',
                expectedPatterns: [],
                complexity: 0
            },
            {
                type: 'gibberish',
                input: 'flibber jib quantum flux capacitor banana',
                expectedPatterns: ['error', 'clarification', 'help'],
                complexity: 0
            }
        ];
    }

    async runBenchmarks() {
        console.log('🔬 ENHANCED SAVAGE COMMAND BENCHMARKER ACTIVATED');
        console.log('===============================================');
        
        this.results.totalCommands = this.selectedCommands.length;
        
        for (const command of this.selectedCommands) {
            console.log(`\n🧪 SCIENTIFICALLY ROASTING: ${command.name}`);
            console.log(`   Type: ${command.type}, Complexity: ${command.complexity}, Size: ${command.size} chars`);
            console.log('─'.repeat(60));
            
            const benchmarkData = [];
            
            // Run all test cases multiple times for statistical significance
            for (let run = 0; run < 3; run++) {
                console.log(`\n   Run ${run + 1}/3:`);
                
                for (const testCase of this.enhancedTestCases) {
                    const result = await this.benchmarkCommand(command.path, testCase);
                    result.run = run + 1;
                    result.testCase = testCase.type;
                    benchmarkData.push(result);
                    
                    const status = result.success ? '✅' : '❌';
                    const time = result.executionTime.toFixed(2);
                    console.log(`     ${status} ${testCase.type}: ${time}ms, ${result.tokenEstimate} tokens`);
                }
            }
            
            // Enhanced statistical analysis
            const analysis = this.generateEnhancedAnalysis(command, benchmarkData);
            
            this.results.benchmarks[command.name] = benchmarkData;
            this.results.savageAnalysis[command.name] = analysis;
            
            console.log(`\n💀 ${analysis.verdict}: ${command.name}`);
            console.log(`🔥 SAVAGE ROAST: ${analysis.roast}`);
            console.log(`📊 DATA POINTS: Success ${analysis.dataPoints.successRate}%, Tokens ${analysis.dataPoints.averageTokenUsage}, Time ${analysis.dataPoints.averageExecutionTime}ms`);
            
            if (analysis.dataPoints.successRate >= 70) {
                this.results.passed++;
            } else {
                this.results.failed++;
            }
            this.results.tested++;
        }
        
        return this.generateEnhancedReport();
    }

    generateEnhancedAnalysis(command, benchmarkData) {
        const analysis = super.generateSavageAnalysis(command.name, benchmarkData);
        
        // Add enhanced statistical metrics
        const successRates = {};
        this.enhancedTestCases.forEach(testCase => {
            const testResults = benchmarkData.filter(r => r.testCase === testCase.type);
            successRates[testCase.type] = testResults.filter(r => r.success).length / testResults.length;
        });
        
        analysis.enhancedMetrics = {
            successRatesByTestType: successRates,
            consistencyScore: this.calculateConsistency(benchmarkData),
            performanceStability: this.calculateStability(benchmarkData),
            complexityEfficiency: analysis.dataPoints.averageComplexity / Math.max(analysis.dataPoints.successRate, 1),
            costEffectiveness: analysis.dataPoints.successRate / Math.max(analysis.dataPoints.averageTokenUsage / 1000, 1)
        };
        
        // Enhanced roasting based on new metrics
        if (analysis.enhancedMetrics.consistencyScore < 0.3) {
            analysis.roast += ` Consistency score: ${(analysis.enhancedMetrics.consistencyScore * 100).toFixed(1)}%. This command is more unpredictable than my mood after debugging legacy code for 8 hours.`;
        }
        
        if (analysis.enhancedMetrics.costEffectiveness < 0.1) {
            analysis.roast += ` Cost-effectiveness: ${(analysis.enhancedMetrics.costEffectiveness * 100).toFixed(1)}%. You're burning tokens faster than a startup burns VC money.`;
        }
        
        return analysis;
    }

    calculateConsistency(benchmarkData) {
        // Group by test case and calculate variance in success rates
        const testGroups = {};
        benchmarkData.forEach(result => {
            if (!testGroups[result.testCase]) testGroups[result.testCase] = [];
            testGroups[result.testCase].push(result.success ? 1 : 0);
        });
        
        let totalVariance = 0;
        let testCount = 0;
        
        Object.values(testGroups).forEach(group => {
            const mean = group.reduce((sum, val) => sum + val, 0) / group.length;
            const variance = group.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / group.length;
            totalVariance += variance;
            testCount++;
        });
        
        return testCount > 0 ? 1 - (totalVariance / testCount) : 0;
    }

    calculateStability(benchmarkData) {
        const times = benchmarkData.map(r => r.executionTime);
        const mean = times.reduce((sum, time) => sum + time, 0) / times.length;
        const variance = times.reduce((sum, time) => sum + Math.pow(time - mean, 2), 0) / times.length;
        const coefficientOfVariation = Math.sqrt(variance) / mean;
        
        return Math.max(0, 1 - coefficientOfVariation);
    }

    generateEnhancedReport() {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-').split('T')[0] + '-' + 
                         new Date().toISOString().replace(/[:.]/g, '-').split('T')[1].split('.')[0].replace(/-/g, '');
        
        const reportPath = path.join(__dirname, `results/${timestamp}-enhanced-savage-report.json`);
        
        // Enhanced statistical summary
        const allBenchmarks = Object.values(this.results.benchmarks).flat();
        
        this.results.enhancedStatistics = {
            ...this.results.statisticalSummary,
            testCasesRun: this.enhancedTestCases.length,
            totalTestExecutions: allBenchmarks.length,
            averageConsistency: this.calculateAverageConsistency(),
            averageStability: this.calculateAverageStability(),
            commandTypeDistribution: this.calculateTypeDistribution(),
            performanceCorrelations: this.calculatePerformanceCorrelations()
        };
        
        fs.writeFileSync(reportPath, JSON.stringify(this.results, null, 2));
        
        console.log('\n🏆 ENHANCED SAVAGE FINAL JUDGMENT');
        console.log('=================================');
        console.log(this.results.statisticalSummary.savageMoment);
        console.log(`\n📊 ENHANCED STATISTICS:`);
        console.log(`   Commands Analyzed: ${this.results.tested}`);
        console.log(`   Test Executions: ${this.results.enhancedStatistics.totalTestExecutions}`);
        console.log(`   Average Consistency: ${(this.results.enhancedStatistics.averageConsistency * 100).toFixed(1)}%`);
        console.log(`   Average Stability: ${(this.results.enhancedStatistics.averageStability * 100).toFixed(1)}%`);
        console.log(`\n📄 Enhanced report: ${reportPath}`);
        
        return reportPath;
    }

    calculateAverageConsistency() {
        const analyses = Object.values(this.results.savageAnalysis);
        const consistencyScores = analyses
            .filter(a => a.enhancedMetrics && a.enhancedMetrics.consistencyScore !== undefined)
            .map(a => a.enhancedMetrics.consistencyScore);
        
        return consistencyScores.length > 0 
            ? consistencyScores.reduce((sum, score) => sum + score, 0) / consistencyScores.length 
            : 0;
    }

    calculateAverageStability() {
        const analyses = Object.values(this.results.savageAnalysis);
        const stabilityScores = analyses
            .filter(a => a.enhancedMetrics && a.enhancedMetrics.performanceStability !== undefined)
            .map(a => a.enhancedMetrics.performanceStability);
        
        return stabilityScores.length > 0 
            ? stabilityScores.reduce((sum, score) => sum + score, 0) / stabilityScores.length 
            : 0;
    }

    calculateTypeDistribution() {
        const distribution = {};
        this.selectedCommands.forEach(cmd => {
            distribution[cmd.type] = (distribution[cmd.type] || 0) + 1;
        });
        return distribution;
    }

    calculatePerformanceCorrelations() {
        // Analyze correlations between command characteristics and performance
        const correlations = {};
        
        // Size vs Performance
        const sizePerformanceData = this.selectedCommands.map(cmd => {
            const analysis = this.results.savageAnalysis[cmd.name];
            return {
                size: cmd.size,
                successRate: analysis ? analysis.dataPoints.successRate : 0,
                tokenUsage: analysis ? analysis.dataPoints.averageTokenUsage : 0
            };
        });
        
        correlations.sizeVsSuccessRate = this.calculateCorrelation(
            sizePerformanceData.map(d => d.size),
            sizePerformanceData.map(d => d.successRate)
        );
        
        correlations.sizeVsTokenUsage = this.calculateCorrelation(
            sizePerformanceData.map(d => d.size),
            sizePerformanceData.map(d => d.tokenUsage)
        );
        
        return correlations;
    }

    calculateCorrelation(x, y) {
        const n = x.length;
        const sumX = x.reduce((sum, val) => sum + val, 0);
        const sumY = y.reduce((sum, val) => sum + val, 0);
        const sumXY = x.reduce((sum, val, i) => sum + val * y[i], 0);
        const sumX2 = x.reduce((sum, val) => sum + val * val, 0);
        const sumY2 = y.reduce((sum, val) => sum + val * val, 0);
        
        const numerator = n * sumXY - sumX * sumY;
        const denominator = Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
        
        return denominator === 0 ? 0 : numerator / denominator;
    }
}

// Main execution
async function runSavageBenchmark() {
    console.log('🎯 SAVAGE COMMAND BENCHMARKER - RANDOM SELECTION MODE');
    console.log('====================================================');
    
    const selector = new RandomCommandSelector();
    selector.loadAvailableCommands();
    
    // Select 5 random commands for testing
    const selectedCommands = selector.selectRandomCommands(5);
    
    // Generate selection report
    selector.generateSelectionReport();
    
    // Run savage benchmarks
    await selector.runSavageBenchmarks();
}

// Export for module use or run directly
module.exports = { RandomCommandSelector, EnhancedSavageBenchmarker };

if (require.main === module) {
    runSavageBenchmark().catch(console.error);
}