#!/usr/bin/env node

/**
 * SAVAGE COMMAND BENCHMARKER - Scientific Analysis Framework
 * PhD-level roasting with statistical rigor
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class CommandBenchmarker {
    constructor() {
        this.results = [];
        this.benchmarkStartTime = new Date();
        this.testIterations = 5;
        this.complexityScoreWeights = {
            lines: 0.1,
            thinking_blocks: 2.0,
            mcp_calls: 1.5,
            nested_complexity: 3.0,
            variables: 0.2
        };
    }

    /**
     * Calculate complexity score based on CLAUDE.md rules
     * Returns score 1-10, where >5 is failing complexity
     */
    calculateComplexityScore(commandContent) {
        const lines = commandContent.split('\n').length;
        const thinkingBlocks = (commandContent.match(/<thinking>/g) || []).length;
        const mcpCalls = (commandContent.match(/mcp__/g) || []).length;
        const nestedComplexity = this.calculateNestingDepth(commandContent);
        const variables = (commandContent.match(/\$\{[^}]+\}/g) || []).length;

        const score = 
            lines * this.complexityScoreWeights.lines +
            thinkingBlocks * this.complexityScoreWeights.thinking_blocks +
            mcpCalls * this.complexityScoreWeights.mcp_calls +
            nestedComplexity * this.complexityScoreWeights.nested_complexity +
            variables * this.complexityScoreWeights.variables;

        return Math.min(10, Math.max(1, Math.round(score / 100)));
    }

    calculateNestingDepth(content) {
        const lines = content.split('\n');
        let maxDepth = 0;
        let currentDepth = 0;

        for (const line of lines) {
            const opens = (line.match(/[<{(]/g) || []).length;
            const closes = (line.match(/[>})]/g) || []).length;
            currentDepth += opens - closes;
            maxDepth = Math.max(maxDepth, currentDepth);
        }

        return maxDepth;
    }

    /**
     * Estimate token consumption for a command
     * Based on content length and complexity
     */
    estimateTokenConsumption(commandContent) {
        // Rough estimation: 4 characters per token
        const inputTokens = Math.ceil(commandContent.length / 4);
        
        // Complex commands generate more output
        const complexityMultiplier = this.calculateComplexityScore(commandContent) / 5;
        const outputTokens = Math.round(inputTokens * complexityMultiplier);
        
        return {
            input: inputTokens,
            output: outputTokens,
            total: inputTokens + outputTokens
        };
    }

    /**
     * Analyze command effectiveness based on structure
     */
    analyzeCommandEffectiveness(commandPath, commandContent) {
        const metrics = {
            hasThinking: commandContent.includes('<thinking>'),
            hasComplexityDetection: commandContent.includes('complexity_detection'),
            hasMCPIntegration: commandContent.includes('mcp__'),
            hasExamples: commandContent.includes('## Usage') || commandContent.includes('Examples'),
            hasErrorHandling: commandContent.includes('error') || commandContent.includes('Error'),
            linesOfCode: commandContent.split('\n').length,
            thinkingBlockCount: (commandContent.match(/<thinking>/g) || []).length,
            exampleCount: (commandContent.match(/```/g) || []).length / 2, // Pairs
        };

        // Calculate effectiveness score (0-100)
        let effectivenessScore = 0;
        if (metrics.hasThinking) effectivenessScore += 25;
        if (metrics.hasComplexityDetection) effectivenessScore += 20;
        if (metrics.hasMCPIntegration) effectivenessScore += 15;
        if (metrics.hasExamples) effectivenessScore += 15;
        if (metrics.hasErrorHandling) effectivenessScore += 10;
        if (metrics.thinkingBlockCount >= 3) effectivenessScore += 10;
        if (metrics.exampleCount >= 2) effectivenessScore += 5;

        return {
            ...metrics,
            effectivenessScore: Math.min(100, effectivenessScore)
        };
    }

    /**
     * Perform statistical analysis on command
     */
    benchmarkCommand(commandPath) {
        const commandName = path.basename(commandPath, '.md');
        const commandContent = fs.readFileSync(commandPath, 'utf-8');
        
        console.log(`🔬 Analyzing ${commandName}...`);
        
        const startTime = process.hrtime.bigint();
        
        // Core metrics
        const complexityScore = this.calculateComplexityScore(commandContent);
        const tokenEstimate = this.estimateTokenConsumption(commandContent);
        const effectiveness = this.analyzeCommandEffectiveness(commandPath, commandContent);
        
        const endTime = process.hrtime.bigint();
        const analysisTimeMs = Number(endTime - startTime) / 1000000;
        
        // Generate savage commentary based on scores
        const commentary = this.generateSavageCommentary(commandName, {
            complexity: complexityScore,
            effectiveness: effectiveness.effectivenessScore,
            tokens: tokenEstimate.total,
            lines: effectiveness.linesOfCode
        });

        const result = {
            commandName,
            commandPath,
            timestamp: new Date().toISOString(),
            metrics: {
                complexityScore,
                tokenEstimate,
                effectiveness,
                analysisTimeMs,
                fileSizeBytes: commandContent.length,
                maintainabilityIndex: this.calculateMaintainabilityIndex(effectiveness, complexityScore)
            },
            commentary,
            riskFactors: this.identifyRiskFactors(commandContent, effectiveness, complexityScore),
            recommendations: this.generateRecommendations(effectiveness, complexityScore)
        };

        this.results.push(result);
        return result;
    }

    calculateMaintainabilityIndex(effectiveness, complexity) {
        // Higher effectiveness = better, lower complexity = better
        // Scale: 0-100, where 100 is perfectly maintainable
        const effectivenessWeight = 0.7;
        const complexityWeight = 0.3;
        
        const complexityPenalty = (complexity - 1) / 9 * 100; // Convert 1-10 to 0-100 penalty
        
        return Math.max(0, Math.round(
            effectiveness.effectivenessScore * effectivenessWeight - 
            complexityPenalty * complexityWeight
        ));
    }

    identifyRiskFactors(content, effectiveness, complexity) {
        const risks = [];
        
        if (complexity >= 5) {
            risks.push({
                type: 'CRITICAL',
                factor: 'Complexity Violation',
                description: `Complexity score ${complexity}/10 violates CLAUDE.md rule (must be <5)`,
                impact: 'High maintenance burden, difficult debugging'
            });
        }
        
        if (!effectiveness.hasThinking) {
            risks.push({
                type: 'HIGH',
                factor: 'Missing Thinking Architecture',
                description: 'No <thinking> blocks detected',
                impact: 'Poor decision-making, unpredictable behavior'
            });
        }
        
        if (!effectiveness.hasComplexityDetection) {
            risks.push({
                type: 'MEDIUM',
                factor: 'No Complexity Detection',
                description: 'Missing automated complexity routing',
                impact: 'Cannot scale to complex scenarios'
            });
        }
        
        if (effectiveness.linesOfCode > 500) {
            risks.push({
                type: 'MEDIUM',
                factor: 'Command Bloat',
                description: `${effectiveness.linesOfCode} lines exceeds maintainable size`,
                impact: 'Cognitive overload, hard to understand'
            });
        }
        
        if (effectiveness.exampleCount < 2) {
            risks.push({
                type: 'LOW',
                factor: 'Poor Documentation',
                description: 'Insufficient usage examples',
                impact: 'User confusion, adoption barriers'
            });
        }
        
        return risks;
    }

    generateRecommendations(effectiveness, complexity) {
        const recommendations = [];
        
        if (complexity >= 5) {
            recommendations.push({
                priority: 'CRITICAL',
                action: 'Simplify Command Architecture',
                details: 'Break into smaller commands or add complexity routing'
            });
        }
        
        if (!effectiveness.hasThinking) {
            recommendations.push({
                priority: 'HIGH',
                action: 'Add Thinking Blocks',
                details: 'Implement <thinking> sections for decision transparency'
            });
        }
        
        if (!effectiveness.hasMCPIntegration && complexity > 3) {
            recommendations.push({
                priority: 'MEDIUM',
                action: 'Add MCP Integration',
                details: 'Connect to appropriate MCP tools for enhanced capabilities'
            });
        }
        
        if (effectiveness.effectivenessScore < 50) {
            recommendations.push({
                priority: 'HIGH',
                action: 'Complete Command Restructure',
                details: 'Command fails basic effectiveness standards'
            });
        }
        
        return recommendations;
    }

    generateSavageCommentary(commandName, scores) {
        const { complexity, effectiveness, tokens, lines } = scores;
        
        let commentary = [`🔥 SCIENTIFIC ROAST OF ${commandName.toUpperCase()}`];
        
        // Complexity roasting
        if (complexity >= 5) {
            commentary.push(`❌ COMPLEXITY FAILURE: ${complexity}/10 - That's not "intelligent", that's technical debt with delusions of grandeur.`);
        } else if (complexity <= 2) {
            commentary.push(`✅ COMPLEXITY: ${complexity}/10 - Finally, someone who read the simplicity memo.`);
        } else {
            commentary.push(`⚠️ COMPLEXITY: ${complexity}/10 - Borderline acceptable, like a C+ student.`);
        }
        
        // Effectiveness roasting
        if (effectiveness < 30) {
            commentary.push(`💀 EFFECTIVENESS: ${effectiveness}% - This command has the effectiveness of a chocolate teapot.`);
        } else if (effectiveness < 50) {
            commentary.push(`🤡 EFFECTIVENESS: ${effectiveness}% - Mediocre performance. Even my grandmother's COBOL is more effective.`);
        } else if (effectiveness < 70) {
            commentary.push(`😐 EFFECTIVENESS: ${effectiveness}% - Average. Like vanilla ice cream - functional but forgettable.`);
        } else {
            commentary.push(`🎯 EFFECTIVENESS: ${effectiveness}% - Actually competent. Shocked.`);
        }
        
        // Token efficiency roasting
        const tokensPerLine = Math.round(tokens / lines);
        if (tokensPerLine > 50) {
            commentary.push(`💸 TOKEN EFFICIENCY: ${tokensPerLine} tokens/line - Are you mining Bitcoin or writing commands?`);
        } else if (tokensPerLine < 10) {
            commentary.push(`📈 TOKEN EFFICIENCY: ${tokensPerLine} tokens/line - Surprisingly efficient. Did you accidentally follow best practices?`);
        }
        
        // Size roasting
        if (lines > 400) {
            commentary.push(`📚 SIZE: ${lines} lines - This isn't a command, it's a novella. War and Peace had fewer plot twists.`);
        } else if (lines < 50) {
            commentary.push(`🤏 SIZE: ${lines} lines - Concise. Someone actually understood the assignment.`);
        }
        
        return commentary;
    }

    /**
     * Generate comprehensive statistical report
     */
    generateReport() {
        console.log('\n📊 GENERATING STATISTICAL ANALYSIS...\n');
        
        const totalCommands = this.results.length;
        const complexityScores = this.results.map(r => r.metrics.complexityScore);
        const effectivenessScores = this.results.map(r => r.metrics.effectiveness.effectivenessScore);
        const tokenTotals = this.results.map(r => r.metrics.tokenEstimate.total);
        const maintainabilityIndices = this.results.map(r => r.metrics.maintainabilityIndex);
        
        // Statistical calculations
        const stats = {
            complexity: this.calculateStats(complexityScores),
            effectiveness: this.calculateStats(effectivenessScores),
            tokens: this.calculateStats(tokenTotals),
            maintainability: this.calculateStats(maintainabilityIndices)
        };
        
        // Generate rankings
        const rankings = this.generateRankings();
        
        // Count failures
        const complexityFailures = this.results.filter(r => r.metrics.complexityScore >= 5).length;
        const effectivenessFailures = this.results.filter(r => r.metrics.effectiveness.effectivenessScore < 50).length;
        
        const report = {
            benchmarkMetadata: {
                timestamp: this.benchmarkStartTime.toISOString(),
                totalCommands: totalCommands,
                analysisVersion: '1.0.0',
                criteriaUsed: 'CLAUDE.md compliance + statistical analysis'
            },
            executiveSummary: {
                overallHealthScore: this.calculateOverallHealth(),
                complexityFailureRate: Math.round(complexityFailures / totalCommands * 100),
                effectivenessFailureRate: Math.round(effectivenessFailures / totalCommands * 100),
                averageTokenCost: Math.round(stats.tokens.mean),
                worstOffender: rankings.worst.commandName,
                topPerformer: rankings.best.commandName
            },
            statisticalAnalysis: stats,
            commandRankings: rankings,
            riskAssessment: this.generateRiskAssessment(),
            savageCommentary: this.generateExecutiveSavageCommentary(stats, complexityFailures, effectivenessFailures),
            detailedResults: this.results,
            recommendations: this.generateGlobalRecommendations(stats, complexityFailures, effectivenessFailures)
        };
        
        return report;
    }

    calculateStats(values) {
        const sorted = values.slice().sort((a, b) => a - b);
        const sum = values.reduce((a, b) => a + b, 0);
        const mean = sum / values.length;
        const variance = values.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / values.length;
        const stdDev = Math.sqrt(variance);
        
        return {
            mean: Math.round(mean * 100) / 100,
            median: sorted[Math.floor(sorted.length / 2)],
            min: Math.min(...values),
            max: Math.max(...values),
            stdDev: Math.round(stdDev * 100) / 100,
            values: values
        };
    }

    generateRankings() {
        const ranked = this.results
            .map(r => ({
                commandName: r.commandName,
                overallScore: r.metrics.maintainabilityIndex,
                complexity: r.metrics.complexityScore,
                effectiveness: r.metrics.effectiveness.effectivenessScore
            }))
            .sort((a, b) => b.overallScore - a.overallScore);
        
        return {
            best: ranked[0],
            worst: ranked[ranked.length - 1],
            rankings: ranked
        };
    }

    calculateOverallHealth() {
        const avgMaintainability = this.results.reduce((sum, r) => sum + r.metrics.maintainabilityIndex, 0) / this.results.length;
        return Math.round(avgMaintainability);
    }

    generateRiskAssessment() {
        const allRisks = this.results.flatMap(r => r.riskFactors);
        const riskCounts = {
            CRITICAL: allRisks.filter(r => r.type === 'CRITICAL').length,
            HIGH: allRisks.filter(r => r.type === 'HIGH').length,
            MEDIUM: allRisks.filter(r => r.type === 'MEDIUM').length,
            LOW: allRisks.filter(r => r.type === 'LOW').length
        };
        
        return {
            riskCounts,
            totalRisks: allRisks.length,
            riskDensity: Math.round(allRisks.length / this.results.length * 100) / 100,
            criticalCommandsCount: this.results.filter(r => r.riskFactors.some(rf => rf.type === 'CRITICAL')).length
        };
    }

    generateExecutiveSavageCommentary(stats, complexityFailures, effectivenessFailures) {
        const commentary = ['🎯 EXECUTIVE SAVAGE SUMMARY'];
        
        if (complexityFailures > 0) {
            commentary.push(`💥 ${complexityFailures} commands violate the sacred complexity rule. That's like having ${complexityFailures} broken legs in a dance competition.`);
        }
        
        if (effectivenessFailures > 0) {
            commentary.push(`🤮 ${effectivenessFailures} commands fail basic effectiveness. I've seen more productivity from a broken calculator.`);
        }
        
        if (stats.complexity.mean >= 4) {
            commentary.push(`📈 Average complexity: ${stats.complexity.mean}/10. We're approaching "PhD thesis" levels of unnecessary sophistication.`);
        }
        
        if (stats.tokens.mean > 2000) {
            commentary.push(`💸 Average token consumption: ${Math.round(stats.tokens.mean)}. These commands burn tokens like a Tesla burns rubber.`);
        }
        
        commentary.push(`📊 Statistical confidence: High. Sample size: ${this.results.length}. Margin of error: Your ego.`);
        
        return commentary;
    }

    generateGlobalRecommendations(stats, complexityFailures, effectivenessFailures) {
        const recommendations = [];
        
        if (complexityFailures > 0) {
            recommendations.push({
                priority: 'CRITICAL',
                scope: 'SYSTEM-WIDE',
                action: 'Complexity Audit and Refactoring',
                details: `${complexityFailures} commands need immediate simplification`
            });
        }
        
        if (effectivenessFailures > 0) {
            recommendations.push({
                priority: 'HIGH',
                scope: 'ARCHITECTURE',
                action: 'Command Effectiveness Overhaul',
                details: `${effectivenessFailures} commands need complete restructuring`
            });
        }
        
        if (stats.complexity.mean > 3.5) {
            recommendations.push({
                priority: 'MEDIUM',
                scope: 'DESIGN',
                action: 'Implement Complexity Budget System',
                details: 'Enforce complexity limits during development'
            });
        }
        
        return recommendations;
    }
}

module.exports = CommandBenchmarker;

// CLI execution
if (require.main === module) {
    const benchmarker = new CommandBenchmarker();
    
    // Add command paths here for testing
    const commandPaths = process.argv.slice(2);
    
    if (commandPaths.length === 0) {
        console.log('Usage: node benchmark-framework.js <command1.md> <command2.md> ...');
        process.exit(1);
    }
    
    commandPaths.forEach(path => {
        if (fs.existsSync(path)) {
            benchmarker.benchmarkCommand(path);
        } else {
            console.error(`❌ Command not found: ${path}`);
        }
    });
    
    const report = benchmarker.generateReport();
    console.log('\n' + JSON.stringify(report, null, 2));
}