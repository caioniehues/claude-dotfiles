#!/usr/bin/env node
/**
 * SAVAGE COMMAND BENCHMARKER FRAMEWORK
 * PhD in roasting bad code, Masters in evidence-based destruction
 */

const fs = require('fs');
const path = require('path');
const { execSync, spawn } = require('child_process');

class SavageCommandBenchmarker {
    constructor() {
        this.commands = [];
        this.results = {};
        this.startTime = Date.now();
        this.testId = this.generateTestId();
    }

    generateTestId() {
        const now = new Date();
        return now.toISOString().replace(/[:.]/g, '-').slice(0, -5);
    }

    /**
     * BRUTALLY HONEST ANALYSIS FRAMEWORK
     * No participation trophies here!
     */
    async analyzeCommand(commandPath) {
        console.log(`🔬 DISSECTING: ${path.basename(commandPath)}`);
        
        const command = {
            name: path.basename(commandPath, '.md'),
            path: commandPath,
            content: fs.readFileSync(commandPath, 'utf8'),
            metrics: {
                tokenCount: 0,
                complexityScore: 0,
                readabilityScore: 0,
                maintainabilityIndex: 0,
                cyclomaticComplexity: 0,
                overengineeringIndex: 0
            },
            tests: [],
            verdict: {
                score: 0,
                savage_commentary: "",
                evidence: [],
                improvement_potential: 0
            }
        };

        // Calculate raw metrics
        command.metrics = await this.calculateMetrics(command);
        
        return command;
    }

    calculateMetrics(command) {
        const content = command.content;
        const lines = content.split('\n');
        
        return {
            // Token estimation (rough GPT-4 approximation)
            tokenCount: Math.ceil(content.length / 3.5),
            
            // Lines of "code" (XML/markdown complexity)
            lineCount: lines.length,
            
            // XML/template complexity
            xmlTagCount: (content.match(/<[^>]*>/g) || []).length,
            
            // Thinking blocks (good sign)
            thinkingBlockCount: (content.match(/<thinking>/g) || []).length,
            
            // MCP tool usage
            mcpToolCount: (content.match(/mcp__/g) || []).length,
            
            // Complexity indicators
            conditionalCount: (content.match(/\$\{.*\}/g) || []).length,
            
            // Variable placeholders (potential overengineering)
            placeholderCount: (content.match(/\[.*?\]/g) || []).length,
            
            // Documentation ratio
            commentDensity: this.calculateCommentDensity(content),
            
            // Overengineering indicators
            buzzwordCount: this.countBuzzwords(content),
            
            // Practical utility score
            practicalityScore: this.assessPracticality(content)
        };
    }

    calculateCommentDensity(content) {
        const commentLines = content.split('\n').filter(line => 
            line.trim().startsWith('//') || 
            line.trim().startsWith('#') ||
            line.trim().startsWith('<!--')
        ).length;
        const totalLines = content.split('\n').length;
        return totalLines > 0 ? (commentLines / totalLines) * 100 : 0;
    }

    countBuzzwords(content) {
        const buzzwords = [
            'orchestration', 'paradigm', 'synergy', 'revolutionary',
            'transformative', 'leverage', 'cutting-edge', 'state-of-the-art',
            'enterprise-grade', 'scalable', 'robust', 'innovative',
            'strategic', 'optimization', 'enhancement', 'intelligent',
            'adaptive', 'comprehensive', 'systematic', 'holistic'
        ];
        
        const lowerContent = content.toLowerCase();
        return buzzwords.filter(word => lowerContent.includes(word)).length;
    }

    assessPracticality(content) {
        let score = 50; // Start neutral
        
        // Positive indicators
        if (content.includes('mcp__basic-memory')) score += 10;
        if (content.includes('ARGUMENTS')) score += 5;
        if (content.includes('<thinking>')) score += 15;
        if (content.includes('usage')) score += 5;
        if (content.includes('example')) score += 5;
        
        // Negative indicators (overengineering)
        const overengineeringPatterns = [
            'factory', 'abstract', 'interface', 'strategy',
            'observer', 'singleton', 'builder'
        ];
        overengineeringPatterns.forEach(pattern => {
            if (content.toLowerCase().includes(pattern)) score -= 5;
        });
        
        return Math.max(0, Math.min(100, score));
    }

    /**
     * STATISTICAL TORTURE CHAMBER
     * Where commands go to be exposed for what they really are
     */
    async runStatisticalTests(commands) {
        console.log(`🧪 STATISTICAL TORTURE CHAMBER ACTIVATED`);
        console.log(`📊 Preparing to destroy ${commands.length} commands with FACTS and LOGIC`);
        
        const results = {
            timestamp: new Date().toISOString(),
            testId: this.testId,
            commands: [],
            statistics: {},
            rankings: {},
            savage_summary: {}
        };

        for (const command of commands) {
            const testResults = await this.tortureCommand(command);
            results.commands.push(testResults);
        }

        results.statistics = this.calculateOverallStats(results.commands);
        results.rankings = this.rankCommands(results.commands);
        results.savage_summary = this.generateSavageAnalysis(results);

        return results;
    }

    async tortureCommand(command) {
        console.log(`🔥 TORTURING: ${command.name}`);
        
        const torture = {
            name: command.name,
            path: command.path,
            metrics: command.metrics,
            performance: {
                parseTime: 0,
                memoryUsage: 0,
                complexity_explosion_factor: 0
            },
            quality_assessment: {
                maintainability: 0,
                readability: 0,
                overengineering_level: 0,
                practical_value: 0
            },
            savage_verdict: "",
            evidence_pile: []
        };

        // Performance tests
        const parseStart = process.hrtime.bigint();
        try {
            // Simulate parsing complexity
            const lines = command.content.split('\n');
            let parseComplexity = 0;
            
            lines.forEach(line => {
                if (line.includes('<thinking>')) parseComplexity += 2;
                if (line.includes('mcp__')) parseComplexity += 3;
                if (line.includes('${')) parseComplexity += 1;
                if (line.includes('ARGUMENTS')) parseComplexity += 1;
            });
            
            // Simulate processing delay
            await new Promise(resolve => setTimeout(resolve, parseComplexity));
            
        } catch (error) {
            torture.evidence_pile.push(`PARSING FAILED: ${error.message}`);
        }
        const parseEnd = process.hrtime.bigint();
        torture.performance.parseTime = Number(parseEnd - parseStart) / 1000000; // Convert to ms

        // Quality assessments
        torture.quality_assessment = this.assessCommandQuality(command);
        
        // Generate savage verdict
        torture.savage_verdict = this.generateSavageVerdict(command, torture);
        
        return torture;
    }

    assessCommandQuality(command) {
        const metrics = command.metrics;
        
        // Maintainability (0-100)
        let maintainability = 70; // Start reasonable
        if (metrics.xmlTagCount > 100) maintainability -= 20;
        if (metrics.thinkingBlockCount > 0) maintainability += 10;
        if (metrics.commentDensity > 10) maintainability += 10;
        if (metrics.lineCount > 500) maintainability -= 15;
        
        // Readability (0-100)
        let readability = 60; // Start mediocre
        if (metrics.buzzwordCount > 10) readability -= 25;
        if (metrics.placeholderCount > 50) readability -= 15;
        if (metrics.commentDensity > 5) readability += 15;
        
        // Overengineering level (0-100, higher is worse)
        let overengineering = 0;
        overengineering += metrics.buzzwordCount * 2;
        overengineering += Math.max(0, metrics.xmlTagCount - 50) * 0.5;
        overengineering += Math.max(0, metrics.tokenCount - 2000) * 0.01;
        
        return {
            maintainability: Math.max(0, Math.min(100, maintainability)),
            readability: Math.max(0, Math.min(100, readability)),
            overengineering_level: Math.min(100, overengineering),
            practical_value: metrics.practicalityScore
        };
    }

    generateSavageVerdict(command, torture) {
        const quality = torture.quality_assessment;
        const metrics = command.metrics;
        
        let verdict = `Command "${command.name}": `;
        let savagery_level = 0;
        
        // Token bloat analysis
        if (metrics.tokenCount > 3000) {
            verdict += `This ${metrics.tokenCount}-token monster is what happens when developers confuse quantity with quality. `;
            savagery_level += 2;
        } else if (metrics.tokenCount > 1500) {
            verdict += `At ${metrics.tokenCount} tokens, this is getting into 'PhD thesis' territory. `;
            savagery_level += 1;
        }
        
        // Overengineering roast
        if (quality.overengineering_level > 60) {
            verdict += `Overengineering level: ${quality.overengineering_level.toFixed(1)}%. This isn't architecture, it's masturbation. `;
            savagery_level += 3;
        } else if (quality.overengineering_level > 30) {
            verdict += `Some overengineering detected (${quality.overengineering_level.toFixed(1)}%). `;
            savagery_level += 1;
        }
        
        // Buzzword bingo
        if (metrics.buzzwordCount > 15) {
            verdict += `${metrics.buzzwordCount} buzzwords detected. Did a consulting firm write this? `;
            savagery_level += 2;
        }
        
        // Practicality assessment
        if (quality.practical_value < 40) {
            verdict += `Practical value: ${quality.practical_value.toFixed(1)}%. This solves problems that don't exist. `;
            savagery_level += 2;
        } else if (quality.practical_value > 80) {
            verdict += `Actually practical (${quality.practical_value.toFixed(1)}%). Surprisingly competent. `;
        }
        
        // Readability roast
        if (quality.readability < 40) {
            verdict += `Readability score: ${quality.readability.toFixed(1)}%. Hieroglyphics would be clearer. `;
            savagery_level += 2;
        }
        
        // Final savage rating
        if (savagery_level >= 6) {
            verdict += "💀 VERDICT: This is a crime against software engineering.";
        } else if (savagery_level >= 4) {
            verdict += "🔥 VERDICT: Needs serious intervention.";
        } else if (savagery_level >= 2) {
            verdict += "⚠️ VERDICT: Mediocre with concerning patterns.";
        } else {
            verdict += "✅ VERDICT: Actually reasonable. Shocking.";
        }
        
        return verdict;
    }

    calculateOverallStats(commandResults) {
        if (commandResults.length === 0) return {};
        
        const metrics = commandResults.map(cmd => cmd.metrics);
        const qualities = commandResults.map(cmd => cmd.quality_assessment);
        
        const stats = {
            token_count: this.calculateStats(metrics.map(m => m.tokenCount)),
            line_count: this.calculateStats(metrics.map(m => m.lineCount)),
            xml_tag_count: this.calculateStats(metrics.map(m => m.xmlTagCount)),
            thinking_blocks: this.calculateStats(metrics.map(m => m.thinkingBlockCount)),
            buzzword_count: this.calculateStats(metrics.map(m => m.buzzwordCount)),
            maintainability: this.calculateStats(qualities.map(q => q.maintainability)),
            readability: this.calculateStats(qualities.map(q => q.readability)),
            overengineering: this.calculateStats(qualities.map(q => q.overengineering_level)),
            practical_value: this.calculateStats(qualities.map(q => q.practical_value))
        };
        
        return stats;
    }

    calculateStats(values) {
        const sorted = values.sort((a, b) => a - b);
        const sum = values.reduce((a, b) => a + b, 0);
        const mean = sum / values.length;
        const variance = values.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / values.length;
        
        return {
            min: Math.min(...values),
            max: Math.max(...values),
            mean: Number(mean.toFixed(2)),
            median: sorted[Math.floor(sorted.length / 2)],
            std_deviation: Number(Math.sqrt(variance).toFixed(2)),
            coefficient_of_variation: Number((Math.sqrt(variance) / mean * 100).toFixed(2))
        };
    }

    rankCommands(commandResults) {
        const rankings = {
            most_overengineered: commandResults
                .sort((a, b) => b.quality_assessment.overengineering_level - a.quality_assessment.overengineering_level)
                .slice(0, 3),
            most_practical: commandResults
                .sort((a, b) => b.quality_assessment.practical_value - a.quality_assessment.practical_value)
                .slice(0, 3),
            token_monsters: commandResults
                .sort((a, b) => b.metrics.tokenCount - a.metrics.tokenCount)
                .slice(0, 3),
            most_readable: commandResults
                .sort((a, b) => b.quality_assessment.readability - a.quality_assessment.readability)
                .slice(0, 3),
            buzzword_champions: commandResults
                .sort((a, b) => b.metrics.buzzwordCount - a.metrics.buzzwordCount)
                .slice(0, 3)
        };
        
        return rankings;
    }

    generateSavageAnalysis(results) {
        const stats = results.statistics;
        const commands = results.commands;
        
        let analysis = "# 🔥 SAVAGE COMMAND ANALYSIS REPORT\n\n";
        
        // Overall ecosystem health
        analysis += "## Ecosystem Health Assessment\n\n";
        
        const avgOverengineering = stats.overengineering?.mean || 0;
        if (avgOverengineering > 50) {
            analysis += `💀 **CRITICAL**: Average overengineering level is ${avgOverengineering.toFixed(1)}%. This codebase has architectural cancer.\n\n`;
        } else if (avgOverengineering > 30) {
            analysis += `⚠️ **WARNING**: Average overengineering level is ${avgOverengineering.toFixed(1)}%. Showing early symptoms of enterprise bloat.\n\n`;
        } else {
            analysis += `✅ **HEALTHY**: Average overengineering level is ${avgOverengineering.toFixed(1)}%. Surprisingly restrained.\n\n`;
        }
        
        // Token analysis
        const avgTokens = stats.token_count?.mean || 0;
        analysis += `📊 **Token Economy**: Average command consumes ${avgTokens.toFixed(0)} tokens. `;
        if (avgTokens > 2500) {
            analysis += "These commands are eating tokens like a glutton at a buffet.\n\n";
        } else if (avgTokens > 1500) {
            analysis += "Moderate token consumption, but watch for bloat.\n\n";
        } else {
            analysis += "Reasonable token efficiency.\n\n";
        }
        
        // Practical value assessment
        const avgPractical = stats.practical_value?.mean || 0;
        analysis += `🎯 **Practical Value**: Average practical value is ${avgPractical.toFixed(1)}%. `;
        if (avgPractical < 50) {
            analysis += "These commands solve problems that exist mainly in the developer's imagination.\n\n";
        } else if (avgPractical > 75) {
            analysis += "Actually addresses real problems. Impressive.\n\n";
        } else {
            analysis += "Mixed bag of utility.\n\n";
        }
        
        return {
            summary: analysis,
            overall_grade: this.calculateOverallGrade(stats),
            improvement_recommendations: this.generateImprovementPlan(results)
        };
    }

    calculateOverallGrade(stats) {
        let score = 50; // Start with C
        
        // Positive factors
        if ((stats.practical_value?.mean || 0) > 70) score += 15;
        if ((stats.readability?.mean || 0) > 70) score += 15;
        if ((stats.overengineering?.mean || 0) < 30) score += 10;
        if ((stats.thinking_blocks?.mean || 0) > 5) score += 10;
        
        // Negative factors
        if ((stats.overengineering?.mean || 0) > 50) score -= 20;
        if ((stats.token_count?.mean || 0) > 3000) score -= 15;
        if ((stats.buzzword_count?.mean || 0) > 15) score -= 10;
        
        score = Math.max(0, Math.min(100, score));
        
        const grades = [
            { min: 90, grade: 'A+', comment: 'Unicorn-level quality' },
            { min: 80, grade: 'A', comment: 'Excellent work' },
            { min: 70, grade: 'B', comment: 'Good with minor issues' },
            { min: 60, grade: 'C', comment: 'Average, needs improvement' },
            { min: 50, grade: 'D', comment: 'Below average, concerning' },
            { min: 0, grade: 'F', comment: 'Architectural disaster' }
        ];
        
        const grade = grades.find(g => score >= g.min);
        return { score: score.toFixed(1), letter: grade.grade, comment: grade.comment };
    }

    generateImprovementPlan(results) {
        const recommendations = [];
        const stats = results.statistics;
        
        if ((stats.overengineering?.mean || 0) > 40) {
            recommendations.push({
                priority: 'HIGH',
                issue: 'Overengineering Epidemic',
                solution: 'Apply YAGNI principle ruthlessly. Remove unnecessary abstractions.',
                impact: 'Improved maintainability and reduced complexity'
            });
        }
        
        if ((stats.token_count?.mean || 0) > 2000) {
            recommendations.push({
                priority: 'MEDIUM',
                issue: 'Token Bloat',
                solution: 'Refactor verbose commands. Use more concise patterns.',
                impact: 'Reduced API costs and faster processing'
            });
        }
        
        if ((stats.practical_value?.mean || 0) < 60) {
            recommendations.push({
                priority: 'HIGH',
                issue: 'Low Practical Value',
                solution: 'Focus on solving real user problems. Remove theoretical features.',
                impact: 'Increased user adoption and satisfaction'
            });
        }
        
        if ((stats.readability?.mean || 0) < 60) {
            recommendations.push({
                priority: 'MEDIUM',
                issue: 'Poor Readability',
                solution: 'Simplify language. Reduce buzzwords. Add clear examples.',
                impact: 'Easier maintenance and onboarding'
            });
        }
        
        return recommendations;
    }

    async generateReport(results) {
        const reportPath = `/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/${this.testId}-report.json`;
        
        const report = {
            meta: {
                timestamp: new Date().toISOString(),
                test_id: this.testId,
                benchmarker_version: '1.0.0',
                savage_level: 'MAXIMUM',
                commands_analyzed: results.commands.length
            },
            executive_summary: {
                overall_grade: results.savage_summary.overall_grade,
                key_findings: this.extractKeyFindings(results),
                immediate_actions: results.savage_summary.improvement_recommendations.filter(r => r.priority === 'HIGH')
            },
            detailed_analysis: {
                command_results: results.commands,
                statistical_analysis: results.statistics,
                rankings: results.rankings
            },
            savage_commentary: results.savage_summary.summary,
            improvement_roadmap: results.savage_summary.improvement_recommendations
        };
        
        // Write comprehensive JSON report
        fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
        
        // Generate human-readable report
        const humanReport = this.generateHumanReadableReport(report);
        const humanReportPath = reportPath.replace('.json', '.md');
        fs.writeFileSync(humanReportPath, humanReport);
        
        return { jsonReport: reportPath, humanReport: humanReportPath };
    }

    extractKeyFindings(results) {
        const findings = [];
        const stats = results.statistics;
        
        if ((stats.overengineering?.mean || 0) > 50) {
            findings.push(`🚨 CRITICAL: ${(stats.overengineering.mean).toFixed(1)}% average overengineering level`);
        }
        
        if ((stats.token_count?.max || 0) > 4000) {
            findings.push(`💸 Token monster detected: ${stats.token_count.max} tokens in single command`);
        }
        
        if ((stats.practical_value?.mean || 0) < 50) {
            findings.push(`🎭 Low practical value: ${(stats.practical_value.mean).toFixed(1)}% average utility`);
        }
        
        const topBuzzword = results.rankings.buzzword_champions[0];
        if (topBuzzword && topBuzzword.metrics.buzzwordCount > 20) {
            findings.push(`📢 Buzzword champion: "${topBuzzword.name}" with ${topBuzzword.metrics.buzzwordCount} buzzwords`);
        }
        
        return findings;
    }

    generateHumanReadableReport(report) {
        return `# 🔬 Savage Command Benchmark Report
**Generated:** ${new Date().toISOString()}  
**Test ID:** ${report.meta.test_id}

## 📊 Executive Summary

### Overall Grade: ${report.executive_summary.overall_grade.letter} (${report.executive_summary.overall_grade.score}%)
*${report.executive_summary.overall_grade.comment}*

### 🚨 Key Findings
${report.executive_summary.key_findings.map(f => `- ${f}`).join('\n')}

### 🔥 Immediate Actions Required
${report.executive_summary.immediate_actions.map(a => 
`- **${a.priority}**: ${a.issue} → ${a.solution}`
).join('\n')}

## 📈 Statistical Analysis

### Token Economy
- **Average**: ${report.detailed_analysis.statistical_analysis.token_count?.mean || 0} tokens
- **Range**: ${report.detailed_analysis.statistical_analysis.token_count?.min || 0} - ${report.detailed_analysis.statistical_analysis.token_count?.max || 0}
- **Standard Deviation**: ${report.detailed_analysis.statistical_analysis.token_count?.std_deviation || 0}

### Quality Metrics
- **Maintainability**: ${report.detailed_analysis.statistical_analysis.maintainability?.mean || 0}/100
- **Readability**: ${report.detailed_analysis.statistical_analysis.readability?.mean || 0}/100  
- **Overengineering Level**: ${report.detailed_analysis.statistical_analysis.overengineering?.mean || 0}/100
- **Practical Value**: ${report.detailed_analysis.statistical_analysis.practical_value?.mean || 0}/100

## 🏆 Rankings

### Most Overengineered
${report.detailed_analysis.rankings.most_overengineered?.map((cmd, i) => 
`${i + 1}. **${cmd.name}** (${cmd.quality_assessment.overengineering_level.toFixed(1)}%)`
).join('\n') || 'None'}

### Token Monsters
${report.detailed_analysis.rankings.token_monsters?.map((cmd, i) => 
`${i + 1}. **${cmd.name}** (${cmd.metrics.tokenCount} tokens)`
).join('\n') || 'None'}

### Most Practical
${report.detailed_analysis.rankings.most_practical?.map((cmd, i) => 
`${i + 1}. **${cmd.name}** (${cmd.quality_assessment.practical_value.toFixed(1)}% practical value)`
).join('\n') || 'None'}

## 💬 Savage Commentary

${report.savage_commentary}

## 🛠 Improvement Roadmap

${report.improvement_roadmap.map(rec => 
`### ${rec.priority} Priority: ${rec.issue}
**Solution**: ${rec.solution}  
**Impact**: ${rec.impact}`
).join('\n\n')}

---
*Report generated by Savage Command Benchmarker v${report.meta.benchmarker_version}*
*Savage Level: ${report.meta.savage_level}*
`;
    }
}

// Export for use
module.exports = SavageCommandBenchmarker;

// CLI usage
if (require.main === module) {
    console.log('🔬 SAVAGE COMMAND BENCHMARKER ACTIVATED');
    console.log('PhD in roasting bad code, Masters in evidence-based destruction');
    console.log('');
    console.log('Usage: node benchmark-framework.js [command-paths...]');
}