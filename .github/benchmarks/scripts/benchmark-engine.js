#!/usr/bin/env node

/**
 * SAVAGE COMMAND BENCHMARKER v1.0
 * Scientific measurement and brutal evaluation of Claude commands
 * 
 * PhD in roasting bad code with statistical rigor
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class SavageBenchmarker {
    constructor() {
        this.startTime = Date.now();
        this.commands = [];
        this.results = {
            metadata: {
                timestamp: new Date().toISOString(),
                version: "1.0.0",
                benchmarker: "SAVAGE_COMMAND_BENCHMARKER",
                totalCommands: 0
            },
            metrics: {},
            analysis: {},
            rankings: {},
            savageCommentary: {}
        };
        
        // Statistical thresholds for savage commentary
        this.thresholds = {
            excellent: { complexity: 2, tokens: 500, successRate: 0.95 },
            good: { complexity: 3, tokens: 1000, successRate: 0.85 },
            acceptable: { complexity: 4, tokens: 2000, successRate: 0.75 },
            problematic: { complexity: 5, tokens: 3000, successRate: 0.65 },
            disaster: { complexity: 6, tokens: 5000, successRate: 0.5 }
        };
    }

    async loadCommands() {
        const commandsDir = path.join(__dirname, '../../../commands');
        const files = fs.readdirSync(commandsDir).filter(f => f.endsWith('.md'));
        
        this.commands = files.map(file => ({
            name: path.basename(file, '.md'),
            path: path.join(commandsDir, file),
            content: fs.readFileSync(path.join(commandsDir, file), 'utf8')
        }));
        
        this.results.metadata.totalCommands = this.commands.length;
        console.log(`📊 Loaded ${this.commands.length} commands for SAVAGE evaluation`);
    }

    calculateComplexityScore(content) {
        // Based on CLAUDE.md complexity scoring rules
        const metrics = {
            directSolution: 1,
            newClasses: 0,
            interfaces: 0,
            designPatterns: 0,
            configFiles: 0,
            thinking_blocks: 0,
            mcp_calls: 0,
            xml_blocks: 0,
            template_sections: 0
        };

        // Count complexity indicators
        metrics.newClasses = (content.match(/class\s+\w+/g) || []).length;
        metrics.interfaces = (content.match(/interface\s+\w+/g) || []).length;
        metrics.designPatterns = (content.match(/Factory|Builder|Strategy|Observer|Singleton/gi) || []).length;
        metrics.configFiles = (content.match(/\.xml|\.yml|\.json|\.properties/g) || []).length;
        metrics.thinking_blocks = (content.match(/<thinking.*?>/g) || []).length;
        metrics.mcp_calls = (content.match(/mcp__\w+/g) || []).length;
        metrics.xml_blocks = (content.match(/<\w+>/g) || []).length;
        metrics.template_sections = (content.match(/##\s+\w+/g) || []).length;

        // Calculate score per CLAUDE.md rules
        let score = metrics.directSolution;
        score += metrics.newClasses * 2;
        score += metrics.interfaces * 1;
        score += metrics.designPatterns * 3;
        score += metrics.configFiles * 2;
        
        // Additional complexity for command-specific features
        score += Math.min(metrics.thinking_blocks * 0.5, 3); // Cap thinking complexity
        score += Math.min(metrics.mcp_calls * 0.3, 2); // Cap MCP complexity
        score += Math.min(metrics.xml_blocks * 0.1, 1); // Cap XML complexity
        score += Math.min(metrics.template_sections * 0.2, 2); // Cap template complexity

        return { score: Math.round(score * 10) / 10, breakdown: metrics };
    }

    estimateTokenConsumption(content) {
        // Rough estimation: 1 token ≈ 4 characters (GPT tokenization approximation)
        const baseTokens = Math.round(content.length / 4);
        
        // Additional tokens for processing complexity
        const thinkingBlocks = (content.match(/<thinking.*?>[\s\S]*?<\/thinking>/g) || []).length;
        const mcpCalls = (content.match(/mcp__\w+/g) || []).length;
        const xmlStructure = (content.match(/<\w+>/g) || []).length;
        
        const complexityTokens = (thinkingBlocks * 200) + (mcpCalls * 100) + (xmlStructure * 10);
        
        return {
            base: baseTokens,
            complexity: complexityTokens,
            total: baseTokens + complexityTokens,
            perExecution: Math.round((baseTokens + complexityTokens) * 1.3) // Include response generation
        };
    }

    analyzeReadability(content) {
        const lines = content.split('\n');
        const nonEmptyLines = lines.filter(line => line.trim().length > 0);
        
        // Readability metrics
        const avgLineLength = nonEmptyLines.reduce((sum, line) => sum + line.length, 0) / nonEmptyLines.length;
        const maxLineLength = Math.max(...nonEmptyLines.map(line => line.length));
        const headerCount = (content.match(/^#+\s/gm) || []).length;
        const codeBlockCount = (content.match(/```/g) || []).length / 2;
        const bulletPointCount = (content.match(/^[\s]*[-*+]/gm) || []).length;
        
        // Complexity indicators
        const nestedStructures = (content.match(/<\w+>[\s\S]*?<\/\w+>/g) || []).length;
        const conditionalBlocks = (content.match(/if\s+complexity|when\s+\w+|switch\s*\(/gi) || []).length;
        
        return {
            avgLineLength: Math.round(avgLineLength),
            maxLineLength,
            headerCount,
            codeBlockCount,
            bulletPointCount,
            nestedStructures,
            conditionalBlocks,
            readabilityScore: this.calculateReadabilityScore(avgLineLength, headerCount, nestedStructures)
        };
    }

    calculateReadabilityScore(avgLineLength, headerCount, nestedStructures) {
        let score = 100;
        
        // Penalize long lines
        if (avgLineLength > 100) score -= (avgLineLength - 100) * 0.5;
        
        // Penalize too many or too few headers
        if (headerCount < 3) score -= 20;
        if (headerCount > 15) score -= (headerCount - 15) * 2;
        
        // Penalize excessive nesting
        if (nestedStructures > 10) score -= (nestedStructures - 10) * 3;
        
        return Math.max(0, Math.round(score));
    }

    predictSuccessRate(complexity, tokens, readability) {
        // Empirical model based on command characteristics
        let successRate = 0.95; // Start optimistic
        
        // Complexity penalty
        if (complexity.score > 5) successRate -= (complexity.score - 5) * 0.05;
        if (complexity.score > 8) successRate -= 0.15; // Heavy penalty for extreme complexity
        
        // Token consumption penalty
        if (tokens.total > 2000) successRate -= (tokens.total - 2000) / 10000;
        if (tokens.total > 5000) successRate -= 0.2; // Heavy penalty for token bloat
        
        // Readability penalty
        if (readability.readabilityScore < 70) successRate -= (70 - readability.readabilityScore) / 100;
        
        // MCP dependency risk
        const mcpCalls = complexity.breakdown.mcp_calls;
        if (mcpCalls > 5) successRate -= mcpCalls * 0.02;
        
        return Math.max(0.1, Math.min(0.99, successRate));
    }

    generateSavageCommentary(name, metrics) {
        const { complexity, tokens, readability, successRate } = metrics;
        let commentary = [];
        let severity = "excellent";
        
        // Determine severity level
        if (complexity.score >= this.thresholds.disaster.complexity || 
            tokens.total >= this.thresholds.disaster.tokens ||
            successRate <= this.thresholds.disaster.successRate) {
            severity = "disaster";
        } else if (complexity.score >= this.thresholds.problematic.complexity ||
                   tokens.total >= this.thresholds.problematic.tokens ||
                   successRate <= this.thresholds.problematic.successRate) {
            severity = "problematic";
        } else if (complexity.score >= this.thresholds.acceptable.complexity ||
                   tokens.total >= this.thresholds.acceptable.tokens ||
                   successRate <= this.thresholds.acceptable.successRate) {
            severity = "acceptable";
        } else if (complexity.score >= this.thresholds.good.complexity ||
                   tokens.total >= this.thresholds.good.tokens ||
                   successRate <= this.thresholds.good.successRate) {
            severity = "good";
        }

        // Generate savage but accurate commentary
        switch (severity) {
            case "disaster":
                commentary.push(`🚨 DISASTER ALERT: ${name} has a complexity score of ${complexity.score}. That's not "sophisticated", that's a maintenance nightmare waiting to happen.`);
                if (tokens.total > 5000) {
                    commentary.push(`💸 Token consumption: ${tokens.total} tokens. At this rate, you'll bankrupt yourself before solving anything useful.`);
                }
                if (successRate < 0.6) {
                    commentary.push(`🎲 Success rate: ${(successRate * 100).toFixed(1)}%. That's not intelligent automation, that's gambling with worse odds than a slot machine.`);
                }
                break;
                
            case "problematic":
                commentary.push(`⚠️ PROBLEMATIC: ${name} shows concerning complexity (${complexity.score}/10). This is heading toward the danger zone.`);
                if (readability.readabilityScore < 60) {
                    commentary.push(`📖 Readability score: ${readability.readabilityScore}/100. If humans can't read it, how can they maintain it?`);
                }
                break;
                
            case "acceptable":
                commentary.push(`😐 ACCEPTABLE: ${name} is functional but uninspiring. Complexity: ${complexity.score}, which is acceptable but could be better.`);
                break;
                
            case "good":
                commentary.push(`✅ GOOD: ${name} demonstrates solid engineering with complexity ${complexity.score} and ${(successRate * 100).toFixed(1)}% predicted success rate.`);
                break;
                
            case "excellent":
                commentary.push(`🏆 EXCELLENT: ${name} exemplifies the simplicity principle with complexity ${complexity.score} and excellent predicted performance.`);
                break;
        }

        // Specific technical critiques
        if (complexity.breakdown.thinking_blocks > 10) {
            commentary.push(`🧠 Thinking block overload: ${complexity.breakdown.thinking_blocks} blocks. That's not deep thinking, that's paralysis by analysis.`);
        }
        
        if (complexity.breakdown.mcp_calls > 8) {
            commentary.push(`🔗 MCP dependency hell: ${complexity.breakdown.mcp_calls} calls. This command is more dependent than a helicopter parent.`);
        }
        
        if (readability.nestedStructures > 15) {
            commentary.push(`🪆 XML nesting nightmare: ${readability.nestedStructures} nested structures. This isn't configuration, it's XML archaeology.`);
        }

        return { severity, commentary };
    }

    calculateStatistics() {
        const complexities = Object.values(this.results.metrics).map(m => m.complexity.score);
        const tokens = Object.values(this.results.metrics).map(m => m.tokens.total);
        const successRates = Object.values(this.results.metrics).map(m => m.successRate);
        
        const stats = {
            complexity: this.calculateBasicStats(complexities),
            tokens: this.calculateBasicStats(tokens),
            successRate: this.calculateBasicStats(successRates)
        };
        
        // Calculate correlations
        stats.correlations = {
            complexityVsSuccess: this.calculateCorrelation(complexities, successRates),
            tokensVsSuccess: this.calculateCorrelation(tokens, successRates),
            complexityVsTokens: this.calculateCorrelation(complexities, tokens)
        };
        
        return stats;
    }

    calculateBasicStats(data) {
        const sorted = [...data].sort((a, b) => a - b);
        const mean = data.reduce((a, b) => a + b, 0) / data.length;
        const variance = data.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / data.length;
        const stdDev = Math.sqrt(variance);
        
        return {
            mean: Math.round(mean * 100) / 100,
            median: sorted[Math.floor(sorted.length / 2)],
            min: Math.min(...data),
            max: Math.max(...data),
            stdDev: Math.round(stdDev * 100) / 100,
            q1: sorted[Math.floor(sorted.length * 0.25)],
            q3: sorted[Math.floor(sorted.length * 0.75)]
        };
    }

    calculateCorrelation(x, y) {
        const n = x.length;
        const sumX = x.reduce((a, b) => a + b, 0);
        const sumY = y.reduce((a, b) => a + b, 0);
        const sumXY = x.reduce((sum, xi, i) => sum + xi * y[i], 0);
        const sumX2 = x.reduce((sum, xi) => sum + xi * xi, 0);
        const sumY2 = y.reduce((sum, yi) => sum + yi * yi, 0);
        
        const correlation = (n * sumXY - sumX * sumY) / 
            Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
        
        return Math.round(correlation * 1000) / 1000;
    }

    generateRankings() {
        const commands = Object.keys(this.results.metrics);
        
        return {
            byComplexity: commands.sort((a, b) => 
                this.results.metrics[a].complexity.score - this.results.metrics[b].complexity.score
            ),
            byTokens: commands.sort((a, b) => 
                this.results.metrics[a].tokens.total - this.results.metrics[b].tokens.total
            ),
            bySuccessRate: commands.sort((a, b) => 
                this.results.metrics[b].successRate - this.results.metrics[a].successRate
            ),
            byReadability: commands.sort((a, b) => 
                this.results.metrics[b].readability.readabilityScore - this.results.metrics[a].readability.readabilityScore
            )
        };
    }

    async benchmarkCommand(command) {
        console.log(`🔍 Analyzing ${command.name}...`);
        
        const complexity = this.calculateComplexityScore(command.content);
        const tokens = this.estimateTokenConsumption(command.content);
        const readability = this.analyzeReadability(command.content);
        const successRate = this.predictSuccessRate(complexity, tokens, readability);
        
        const metrics = { complexity, tokens, readability, successRate };
        const savage = this.generateSavageCommentary(command.name, metrics);
        
        this.results.metrics[command.name] = metrics;
        this.results.savageCommentary[command.name] = savage;
        
        return metrics;
    }

    async runBenchmarks() {
        console.log('\n🚀 Starting SAVAGE COMMAND BENCHMARKING...\n');
        
        await this.loadCommands();
        
        // Benchmark each command
        for (const command of this.commands) {
            await this.benchmarkCommand(command);
        }
        
        // Calculate statistics
        this.results.analysis = this.calculateStatistics();
        this.results.rankings = this.generateRankings();
        
        console.log('\n📊 BENCHMARKING COMPLETE\n');
    }

    generateReport() {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
        const reportPath = path.join(__dirname, '../results', `${timestamp}-savage-report.json`);
        
        // Add execution time
        this.results.metadata.executionTimeMs = Date.now() - this.startTime;
        this.results.metadata.generatedAt = new Date().toISOString();
        
        // Write detailed JSON report
        fs.writeFileSync(reportPath, JSON.stringify(this.results, null, 2));
        
        // Generate human-readable summary
        this.generateSummaryReport(timestamp);
        
        console.log(`💾 Detailed report saved: ${reportPath}`);
        return reportPath;
    }

    generateSummaryReport(timestamp) {
        const summaryPath = path.join(__dirname, '../results', `${timestamp}-summary.md`);
        const stats = this.results.analysis;
        const rankings = this.results.rankings;
        
        let summary = `# 🔬 Benchmark Report ${new Date().toLocaleDateString()}: Your commands have been scientifically roasted\n\n`;
        summary += `*Generated by SAVAGE COMMAND BENCHMARKER v1.0 - PhD in roasting bad code*\n\n`;
        
        // Executive Summary
        summary += `## 📊 Executive Summary\n\n`;
        summary += `**Total Commands Analyzed:** ${this.results.metadata.totalCommands}\n`;
        summary += `**Execution Time:** ${this.results.metadata.executionTimeMs}ms\n`;
        summary += `**Average Complexity:** ${stats.complexity.mean}/10 (σ=${stats.complexity.stdDev})\n`;
        summary += `**Average Token Consumption:** ${Math.round(stats.tokens.mean)} tokens\n`;
        summary += `**Average Success Rate:** ${(stats.successRate.mean * 100).toFixed(1)}%\n\n`;
        
        // Statistical Analysis
        summary += `## 🧮 Statistical Analysis\n\n`;
        summary += `### Complexity Distribution\n`;
        summary += `- **Range:** ${stats.complexity.min} - ${stats.complexity.max}\n`;
        summary += `- **Median:** ${stats.complexity.median}\n`;
        summary += `- **Q1-Q3:** ${stats.complexity.q1} - ${stats.complexity.q3}\n`;
        summary += `- **Standard Deviation:** ${stats.complexity.stdDev}\n\n`;
        
        summary += `### Token Consumption Analysis\n`;
        summary += `- **Range:** ${stats.tokens.min} - ${stats.tokens.max} tokens\n`;
        summary += `- **Median:** ${Math.round(stats.tokens.median)} tokens\n`;
        summary += `- **75th Percentile:** ${Math.round(stats.tokens.q3)} tokens\n\n`;
        
        summary += `### Correlations\n`;
        summary += `- **Complexity vs Success Rate:** r=${stats.correlations.complexityVsSuccess} (${this.interpretCorrelation(stats.correlations.complexityVsSuccess)})\n`;
        summary += `- **Tokens vs Success Rate:** r=${stats.correlations.tokensVsSuccess} (${this.interpretCorrelation(stats.correlations.tokensVsSuccess)})\n`;
        summary += `- **Complexity vs Tokens:** r=${stats.correlations.complexityVsTokens} (${this.interpretCorrelation(stats.correlations.complexityVsTokens)})\n\n`;
        
        // Rankings
        summary += `## 🏆 Command Rankings\n\n`;
        summary += `### 🏅 Simplicity Champions (Lowest Complexity)\n`;
        rankings.byComplexity.slice(0, 5).forEach((cmd, i) => {
            const metrics = this.results.metrics[cmd];
            summary += `${i + 1}. **${cmd}** - Complexity: ${metrics.complexity.score}/10\n`;
        });
        
        summary += `\n### 🚨 Complexity Disasters (Highest Complexity)\n`;
        rankings.byComplexity.slice(-5).reverse().forEach((cmd, i) => {
            const metrics = this.results.metrics[cmd];
            summary += `${i + 1}. **${cmd}** - Complexity: ${metrics.complexity.score}/10 ⚠️\n`;
        });
        
        summary += `\n### 💎 Efficiency Masters (Lowest Token Usage)\n`;
        rankings.byTokens.slice(0, 5).forEach((cmd, i) => {
            const metrics = this.results.metrics[cmd];
            summary += `${i + 1}. **${cmd}** - ${metrics.tokens.total} tokens\n`;
        });
        
        summary += `\n### 💸 Token Gluttons (Highest Token Usage)\n`;
        rankings.byTokens.slice(-5).reverse().forEach((cmd, i) => {
            const metrics = this.results.metrics[cmd];
            summary += `${i + 1}. **${cmd}** - ${metrics.tokens.total} tokens 💸\n`;
        });
        
        // Savage Commentary Highlights
        summary += `\n## 🔥 Savage Commentary Highlights\n\n`;
        const disasters = Object.keys(this.results.savageCommentary)
            .filter(cmd => this.results.savageCommentary[cmd].severity === 'disaster');
        const excellent = Object.keys(this.results.savageCommentary)
            .filter(cmd => this.results.savageCommentary[cmd].severity === 'excellent');
        
        if (disasters.length > 0) {
            summary += `### 🚨 Commands That Need Intervention\n`;
            disasters.forEach(cmd => {
                const commentary = this.results.savageCommentary[cmd].commentary;
                summary += `\n**${cmd}:**\n`;
                commentary.forEach(comment => summary += `- ${comment}\n`);
            });
        }
        
        if (excellent.length > 0) {
            summary += `\n### 🏆 Commands That Make Us Proud\n`;
            excellent.forEach(cmd => {
                const commentary = this.results.savageCommentary[cmd].commentary;
                summary += `\n**${cmd}:**\n`;
                commentary.forEach(comment => summary += `- ${comment}\n`);
            });
        }
        
        // Recommendations
        summary += `\n## 💡 Recommendations\n\n`;
        summary += `### Immediate Actions Required:\n`;
        if (stats.complexity.mean > 5) {
            summary += `- 🚨 **CRITICAL:** Average complexity (${stats.complexity.mean}) exceeds CLAUDE.md threshold of 5. Simplify immediately!\n`;
        }
        if (stats.tokens.mean > 3000) {
            summary += `- 💸 **EXPENSIVE:** High token consumption detected. Optimize for cost efficiency.\n`;
        }
        if (stats.successRate.mean < 0.8) {
            summary += `- 🎲 **UNRELIABLE:** Low success rate indicates commands may fail frequently.\n`;
        }
        
        summary += `\n### Strategic Improvements:\n`;
        summary += `- Focus on the ${disasters.length} disaster-level commands\n`;
        summary += `- Study the ${excellent.length} excellent commands as patterns\n`;
        summary += `- Implement complexity gates in command creation process\n`;
        summary += `- Consider breaking down commands with >5 complexity score\n\n`;
        
        summary += `---\n`;
        summary += `*Generated by SAVAGE COMMAND BENCHMARKER - Because someone needs to tell you the truth about your code.*\n`;
        
        fs.writeFileSync(summaryPath, summary);
        console.log(`📝 Summary report saved: ${summaryPath}`);
    }

    interpretCorrelation(r) {
        const abs = Math.abs(r);
        if (abs > 0.8) return 'strong correlation';
        if (abs > 0.5) return 'moderate correlation';
        if (abs > 0.3) return 'weak correlation';
        return 'negligible correlation';
    }
}

// Main execution
if (require.main === module) {
    (async () => {
        const benchmarker = new SavageBenchmarker();
        await benchmarker.runBenchmarks();
        const reportPath = benchmarker.generateReport();
        
        console.log('\n🎉 SAVAGE BENCHMARKING COMPLETE!');
        console.log(`📊 Results are in: ${reportPath}`);
        console.log('\n💡 Pro tip: Use these results to justify your refactoring budget.');
    })();
}

module.exports = SavageBenchmarker;