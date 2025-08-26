#!/usr/bin/env node

/**
 * SAVAGE COMMAND BENCHMARKER
 * Scientific measurement and brutal judgment framework
 */

class CommandBenchmarker {
    constructor() {
        this.startTime = Date.now();
        this.results = {
            timestamp: new Date().toISOString(),
            benchmarks: {},
            metadata: {
                testRunner: "SAVAGE_BENCHMARKER_v1.0",
                environment: process.env,
                nodeVersion: process.version,
                platform: process.platform
            }
        };
    }

    // Measure complexity score based on CLAUDE.md rules
    calculateComplexityScore(commandContent) {
        let score = 1; // Base solution
        
        // Count complexity indicators
        const classCount = (commandContent.match(/class\s+\w+/g) || []).length;
        const interfaceCount = (commandContent.match(/interface\s+\w+/g) || []).length;
        const patternMatches = this.countDesignPatterns(commandContent);
        const configCount = (commandContent.match(/\.json|\.yaml|\.xml|config/g) || []).length;
        const mcpInvocations = (commandContent.match(/mcp__/g) || []).length;
        
        score += classCount * 2;
        score += interfaceCount * 1;
        score += patternMatches * 3;
        score += configCount * 2;
        score += mcpInvocations * 0.5; // Mild penalty for MCP usage
        
        return {
            total: score,
            breakdown: {
                base: 1,
                classes: classCount * 2,
                interfaces: interfaceCount * 1,
                patterns: patternMatches * 3,
                configs: configCount * 2,
                mcpCalls: mcpInvocations * 0.5
            }
        };
    }

    countDesignPatterns(content) {
        const patterns = [
            'Factory', 'Builder', 'Singleton', 'Observer', 'Strategy',
            'Command', 'Adapter', 'Decorator', 'Facade', 'Proxy'
        ];
        
        return patterns.reduce((count, pattern) => {
            const regex = new RegExp(pattern, 'gi');
            return count + (content.match(regex) || []).length;
        }, 0);
    }

    // Token estimation (rough approximation)
    estimateTokens(text) {
        // Rough estimation: ~4 characters per token
        return Math.ceil(text.length / 4);
    }

    // Readability analysis
    analyzeReadability(content) {
        const lines = content.split('\n');
        const totalLines = lines.length;
        const nonEmptyLines = lines.filter(line => line.trim().length > 0).length;
        const avgLineLength = lines.reduce((sum, line) => sum + line.length, 0) / totalLines;
        
        // Count thinking blocks
        const thinkingBlocks = (content.match(/<thinking>/g) || []).length;
        const xmlBlocks = (content.match(/<\w+>/g) || []).length;
        
        return {
            totalLines,
            nonEmptyLines,
            avgLineLength,
            thinkingBlocks,
            xmlBlocks,
            verbosity: avgLineLength * nonEmptyLines, // Verbosity metric
            thinkingRatio: thinkingBlocks / (nonEmptyLines / 100) // Thinking blocks per 100 lines
        };
    }

    // Performance prediction (static analysis)
    predictPerformance(content) {
        const nestedLoops = (content.match(/for.*for|while.*while/g) || []).length;
        const recursiveCalls = (content.match(/function.*\1\(/g) || []).length;
        const asyncOperations = (content.match(/await|async|Promise/g) || []).length;
        
        let performanceScore = 10; // Start with perfect score
        performanceScore -= nestedLoops * 3; // Heavy penalty for nested loops
        performanceScore -= recursiveCalls * 2; // Penalty for recursion
        performanceScore += asyncOperations * 0.5; // Slight bonus for async
        
        return Math.max(0, performanceScore);
    }

    // Analyze maintainability
    analyzeMaintainability(content) {
        const functionCount = (content.match(/function|=>/g) || []).length;
        const longLines = content.split('\n').filter(line => line.length > 120).length;
        const comments = (content.match(/\/\/|\/\*|\#/g) || []).length;
        const magicNumbers = (content.match(/\b\d{2,}\b/g) || []).length;
        
        return {
            functionCount,
            longLines,
            comments,
            magicNumbers,
            maintainabilityScore: Math.max(0, 10 - longLines * 0.5 - magicNumbers * 0.2)
        };
    }

    // Main benchmark function
    benchmarkCommand(name, content) {
        console.log(`🔬 BENCHMARKING: ${name}`);
        
        const complexity = this.calculateComplexityScore(content);
        const readability = this.analyzeReadability(content);
        const performance = this.predictPerformance(content);
        const maintainability = this.analyzeMaintainability(content);
        const tokenEstimate = this.estimateTokens(content);
        
        // Calculate overall quality score
        const qualityScore = this.calculateQualityScore({
            complexity: complexity.total,
            readability: readability.verbosity,
            performance,
            maintainability: maintainability.maintainabilityScore
        });
        
        const results = {
            name,
            timestamp: new Date().toISOString(),
            metrics: {
                complexity,
                readability,
                performance,
                maintainability,
                tokenEstimate,
                qualityScore
            },
            judgment: this.generateSavageJudgment(name, {
                complexity: complexity.total,
                readability: readability.verbosity,
                performance,
                maintainability: maintainability.maintainabilityScore,
                tokens: tokenEstimate
            })
        };
        
        this.results.benchmarks[name] = results;
        return results;
    }

    calculateQualityScore(metrics) {
        // Lower is better for complexity and readability verbosity
        // Higher is better for performance and maintainability
        const complexityScore = Math.max(0, 10 - metrics.complexity);
        const readabilityScore = Math.max(0, 10 - (metrics.readability / 1000));
        const performanceScore = metrics.performance;
        const maintainabilityScore = metrics.maintainability;
        
        return {
            complexity: complexityScore,
            readability: readabilityScore,
            performance: performanceScore,
            maintainability: maintainabilityScore,
            overall: (complexityScore + readabilityScore + performanceScore + maintainabilityScore) / 4
        };
    }

    generateSavageJudgment(name, metrics) {
        const judgments = [];
        
        // Complexity judgment
        if (metrics.complexity > 10) {
            judgments.push(`🚨 COMPLEXITY VIOLATION: Score ${metrics.complexity}/5 - This isn't "intelligent", it's architectural masturbation!`);
        } else if (metrics.complexity > 5) {
            judgments.push(`⚠️ COMPLEXITY WARNING: Score ${metrics.complexity}/5 - Dangerously close to over-engineering territory.`);
        } else {
            judgments.push(`✅ COMPLEXITY: Score ${metrics.complexity}/5 - Finally, someone who understands simplicity!`);
        }
        
        // Token efficiency judgment
        if (metrics.tokens > 2000) {
            judgments.push(`💸 TOKEN WASTE: ${metrics.tokens} tokens - This command burns more tokens than a crypto mining rig!`);
        } else if (metrics.tokens > 1000) {
            judgments.push(`💰 TOKEN COST: ${metrics.tokens} tokens - Expensive but maybe worth it.`);
        } else {
            judgments.push(`💚 TOKEN EFFICIENT: ${metrics.tokens} tokens - Respectable token economy.`);
        }
        
        // Performance judgment
        if (metrics.performance < 3) {
            judgments.push(`🐌 PERFORMANCE DISASTER: ${metrics.performance}/10 - Slower than government bureaucracy!`);
        } else if (metrics.performance < 6) {
            judgments.push(`⏳ PERFORMANCE CONCERNS: ${metrics.performance}/10 - Room for improvement.`);
        } else {
            judgments.push(`⚡ PERFORMANCE: ${metrics.performance}/10 - Acceptable speed.`);
        }
        
        // Readability judgment
        if (metrics.readability > 5000) {
            judgments.push(`📚 VERBOSITY OVERLOAD: This reads like a PhD thesis, not a command!`);
        } else if (metrics.readability > 2000) {
            judgments.push(`📖 VERBOSE: Could use some editing for clarity.`);
        } else {
            judgments.push(`📝 READABLE: Appropriately concise.`);
        }
        
        return {
            summary: judgments[0], // Most critical judgment first
            details: judgments,
            recommendation: this.generateRecommendation(metrics)
        };
    }

    generateRecommendation(metrics) {
        if (metrics.complexity > 10) {
            return "URGENT: Refactor to reduce complexity below 5. Consider the 3-question rule.";
        }
        if (metrics.tokens > 2000) {
            return "Optimize for token efficiency. Remove unnecessary verbosity.";
        }
        if (metrics.performance < 5) {
            return "Performance optimization needed. Review algorithmic complexity.";
        }
        return "Command meets basic quality standards. Consider minor optimizations.";
    }

    // Generate final report
    generateReport() {
        const report = {
            ...this.results,
            summary: {
                totalCommands: Object.keys(this.results.benchmarks).length,
                avgComplexity: this.calculateAverageComplexity(),
                worstOffender: this.findWorstOffender(),
                bestPerformer: this.findBestPerformer(),
                totalTokens: this.calculateTotalTokens(),
                recommendations: this.generateGlobalRecommendations()
            },
            executionTime: Date.now() - this.startTime
        };
        
        return report;
    }

    calculateAverageComplexity() {
        const complexities = Object.values(this.results.benchmarks)
            .map(b => b.metrics.complexity.total);
        return complexities.reduce((sum, c) => sum + c, 0) / complexities.length;
    }

    findWorstOffender() {
        return Object.entries(this.results.benchmarks)
            .reduce((worst, [name, benchmark]) => {
                const score = benchmark.metrics.qualityScore.overall;
                return score < worst.score ? { name, score } : worst;
            }, { name: null, score: Infinity });
    }

    findBestPerformer() {
        return Object.entries(this.results.benchmarks)
            .reduce((best, [name, benchmark]) => {
                const score = benchmark.metrics.qualityScore.overall;
                return score > best.score ? { name, score } : best;
            }, { name: null, score: -Infinity });
    }

    calculateTotalTokens() {
        return Object.values(this.results.benchmarks)
            .reduce((total, b) => total + b.metrics.tokenEstimate, 0);
    }

    generateGlobalRecommendations() {
        const recommendations = [];
        const avgComplexity = this.calculateAverageComplexity();
        const totalTokens = this.calculateTotalTokens();
        
        if (avgComplexity > 7) {
            recommendations.push("CRITICAL: Average complexity too high. Implement simplicity enforcement.");
        }
        
        if (totalTokens > 10000) {
            recommendations.push("WARNING: Token consumption excessive. Review command necessity.");
        }
        
        recommendations.push("Consider consolidating commands with similar functionality.");
        recommendations.push("Implement automated complexity monitoring in CI/CD.");
        
        return recommendations;
    }
}

module.exports = CommandBenchmarker;

// If run directly
if (require.main === module) {
    console.log("🔬 SAVAGE COMMAND BENCHMARKER - Ready for Scientific Brutality!");
}