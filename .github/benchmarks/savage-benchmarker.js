#!/usr/bin/env node

/**
 * SAVAGE COMMAND BENCHMARKER
 * PhD in Roasting Bad Code with Statistical Precision
 * 
 * Measures commands with brutal honesty backed by DATA
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class SavageCommandBenchmarker {
    constructor() {
        this.benchmarkResults = {
            timestamp: new Date().toISOString(),
            commands: [],
            statistics: {},
            savageCommentary: {},
            methodology: "Random sampling with statistical rigor and brutal honesty",
            disclaimer: "These measurements are more accurate than your last code review"
        };
        
        this.complexityRules = {
            directSolution: 1,
            newClass: 2,
            interface: 1,
            designPattern: 3,
            configFile: 2,
            mcp_integration: 2,
            thinking_blocks: 1,
            error_handling: 1
        };
    }

    /**
     * Calculate complexity score based on CLAUDE.md rules
     */
    calculateComplexityScore(commandContent) {
        let score = 1; // Base solution
        
        // Count various complexity indicators
        const indicators = {
            classes: (commandContent.match(/class\s+\w+/g) || []).length,
            interfaces: (commandContent.match(/interface\s+\w+/g) || []).length,
            patterns: (commandContent.match(/(Factory|Builder|Strategy|Observer|Singleton)/g) || []).length,
            configs: (commandContent.match(/\.yml|\.yaml|\.json|\.properties/g) || []).length,
            mcpCalls: (commandContent.match(/mcp__/g) || []).length,
            thinkingBlocks: (commandContent.match(/<\w+_thinking>/g) || []).length,
            errorHandling: (commandContent.match(/try\s*{|catch\s*\(|finally\s*{/g) || []).length
        };
        
        score += indicators.classes * this.complexityRules.newClass;
        score += indicators.interfaces * this.complexityRules.interface;
        score += indicators.patterns * this.complexityRules.designPattern;
        score += indicators.configs * this.complexityRules.configFile;
        score += indicators.mcpCalls * this.complexityRules.mcp_integration;
        score += indicators.thinkingBlocks * this.complexityRules.thinking_blocks;
        score += indicators.errorHandling * this.complexityRules.error_handling;
        
        return {
            score: score,
            breakdown: indicators,
            violatesThreshold: score >= 5
        };
    }

    /**
     * Analyze token consumption patterns
     */
    analyzeTokenConsumption(commandContent) {
        // Estimate tokens (rough approximation: 1 token ≈ 0.75 words)
        const words = commandContent.split(/\s+/).length;
        const estimatedTokens = Math.ceil(words / 0.75);
        
        // Analyze structure efficiency
        const lines = commandContent.split('\n').length;
        const codeToCommentRatio = this.calculateCodeToCommentRatio(commandContent);
        
        return {
            estimatedInputTokens: estimatedTokens,
            lines: lines,
            tokensPerLine: estimatedTokens / lines,
            codeToCommentRatio: codeToCommentRatio,
            efficiency: this.calculateTokenEfficiency(commandContent)
        };
    }

    calculateCodeToCommentRatio(content) {
        const codeLines = content.split('\n').filter(line => 
            line.trim() && !line.trim().startsWith('#') && !line.trim().startsWith('//'));
        const commentLines = content.split('\n').filter(line => 
            line.trim().startsWith('#') || line.trim().startsWith('//'));
        
        return codeLines.length / (commentLines.length || 1);
    }

    calculateTokenEfficiency(content) {
        // Measure bloat indicators
        const bloatPatterns = [
            /\b(obviously|clearly|simply|just|merely|only)\b/gi,
            /\b(very|really|quite|extremely)\b/gi,
            /\.{3,}/g, // Excessive ellipsis
            /\s{3,}/g  // Excessive whitespace
        ];
        
        let bloatScore = 0;
        bloatPatterns.forEach(pattern => {
            bloatScore += (content.match(pattern) || []).length;
        });
        
        return Math.max(0, 100 - (bloatScore * 2)); // Efficiency percentage
    }

    /**
     * Analyze maintainability metrics
     */
    analyzeMaintainability(commandContent, commandName) {
        const metrics = {
            naming: this.analyzeNaming(commandContent),
            structure: this.analyzeStructure(commandContent),
            documentation: this.analyzeDocumentation(commandContent),
            patterns: this.analyzePatterns(commandContent),
            cohesion: this.analyzeCohesion(commandContent)
        };
        
        const overallScore = Object.values(metrics).reduce((sum, m) => sum + m.score, 0) / Object.keys(metrics).length;
        
        return {
            overallScore,
            breakdown: metrics,
            maintainabilityGrade: this.getGrade(overallScore)
        };
    }

    analyzeNaming(content) {
        const variables = content.match(/\$\{(\w+)\}/g) || [];
        const badNames = variables.filter(v => v.length <= 3 || /[0-9]$/.test(v));
        const score = Math.max(0, 100 - (badNames.length / variables.length) * 100);
        
        return {
            score,
            totalVariables: variables.length,
            badNames: badNames.length,
            issues: badNames.length > 0 ? [`${badNames.length} poorly named variables`] : []
        };
    }

    analyzeStructure(content) {
        const sections = content.split(/<\/?[^>]+>/g).filter(s => s.trim());
        const avgSectionLength = sections.reduce((sum, s) => sum + s.length, 0) / sections.length;
        
        const score = avgSectionLength < 500 ? 90 : avgSectionLength < 1000 ? 70 : 40;
        
        return {
            score,
            sections: sections.length,
            avgSectionLength,
            issues: avgSectionLength > 1000 ? ['Sections too long, low cohesion'] : []
        };
    }

    analyzeDocumentation(content) {
        const hasDescription = content.includes('<description>') || content.includes('<context>');
        const hasExamples = content.includes('example') || content.includes('usage');
        const hasComments = content.includes('<!--') || content.includes('##');
        
        let score = 0;
        if (hasDescription) score += 40;
        if (hasExamples) score += 30;
        if (hasComments) score += 30;
        
        return {
            score,
            hasDescription,
            hasExamples,
            hasComments,
            issues: score < 70 ? ['Insufficient documentation'] : []
        };
    }

    analyzePatterns(content) {
        const goodPatterns = [
            /thinking.*?>/gi,
            /validation/gi,
            /error.*?handling/gi,
            /pattern.*?learning/gi
        ];
        
        const antiPatterns = [
            /TODO/gi,
            /FIXME/gi,
            /HACK/gi,
            /XXX/gi
        ];
        
        const good = goodPatterns.reduce((sum, p) => sum + (content.match(p) || []).length, 0);
        const bad = antiPatterns.reduce((sum, p) => sum + (content.match(p) || []).length, 0);
        
        const score = Math.min(100, (good * 10) - (bad * 20));
        
        return {
            score: Math.max(0, score),
            goodPatterns: good,
            antiPatterns: bad,
            issues: bad > 0 ? [`${bad} anti-patterns found`] : []
        };
    }

    analyzeCohesion(content) {
        // Measure if command has single responsibility
        const responsibilities = [
            content.includes('analysis') ? 1 : 0,
            content.includes('generation') ? 1 : 0,
            content.includes('validation') ? 1 : 0,
            content.includes('optimization') ? 1 : 0,
            content.includes('synchronization') ? 1 : 0,
            content.includes('enhancement') ? 1 : 0
        ].filter(r => r > 0).length;
        
        const score = responsibilities <= 2 ? 90 : responsibilities <= 3 ? 70 : 40;
        
        return {
            score,
            responsibilities,
            issues: responsibilities > 3 ? ['Command has too many responsibilities'] : []
        };
    }

    getGrade(score) {
        if (score >= 90) return 'A';
        if (score >= 80) return 'B';
        if (score >= 70) return 'C';
        if (score >= 60) return 'D';
        return 'F';
    }

    /**
     * Generate savage but fair commentary
     */
    generateSavageCommentary(commandName, results) {
        const complexity = results.complexity;
        const maintainability = results.maintainability;
        const tokens = results.tokenAnalysis;
        
        let commentary = [];
        
        // Complexity roasting
        if (complexity.violatesThreshold) {
            commentary.push(`🔥 COMPLEXITY VIOLATION: Score ${complexity.score}/5 exceeds threshold. ` +
                `This isn't 'intelligent design', it's architectural arrogance. Simplify immediately.`);
        } else if (complexity.score >= 4) {
            commentary.push(`⚠️ COMPLEXITY WARNING: Score ${complexity.score}/5 is dangerously close to bloat territory. ` +
                `You're one factory pattern away from enterprise horror.`);
        } else {
            commentary.push(`✅ COMPLEXITY: Score ${complexity.score}/5 - Finally, someone who understands that ` +
                `smart != complicated. Well done.`);
        }
        
        // Maintainability roasting
        if (maintainability.overallScore < 60) {
            commentary.push(`💀 MAINTAINABILITY DISASTER: Grade ${maintainability.maintainabilityGrade} ` +
                `(${maintainability.overallScore.toFixed(1)}/100). Future developers will curse your name ` +
                `and your documentation. Fix this before someone gets hurt.`);
        } else if (maintainability.overallScore < 80) {
            commentary.push(`😬 MAINTAINABILITY ISSUES: Grade ${maintainability.maintainabilityGrade} ` +
                `(${maintainability.overallScore.toFixed(1)}/100). It works, but reading it feels like ` +
                `deciphering ancient hieroglyphs.`);
        } else {
            commentary.push(`👍 MAINTAINABILITY: Grade ${maintainability.maintainabilityGrade} ` +
                `(${maintainability.overallScore.toFixed(1)}/100). Clean, readable, and doesn't make ` +
                `developers cry. Respect.`);
        }
        
        // Token efficiency roasting
        if (tokens.efficiency < 60) {
            commentary.push(`📈 TOKEN BLOAT DETECTED: ${tokens.efficiency}% efficiency. You're using more tokens ` +
                `than a JavaScript framework uses dependencies. Trim the fat.`);
        } else if (tokens.efficiency < 80) {
            commentary.push(`📊 TOKEN USAGE: ${tokens.efficiency}% efficiency. Room for improvement, but not ` +
                `terrible. Could be tighter.`);
        } else {
            commentary.push(`🎯 TOKEN EFFICIENCY: ${tokens.efficiency}% - Concise and effective. ` +
                `You understand that brevity is the soul of wit.`);
        }
        
        // Special awards
        if (complexity.score < 3 && maintainability.overallScore > 80 && tokens.efficiency > 80) {
            commentary.push(`🏆 EXCELLENCE AWARD: This command demonstrates what happens when developers ` +
                `think before they code. Simple, maintainable, efficient. Chef's kiss.`);
        }
        
        if (complexity.score >= 5 && maintainability.overallScore < 60) {
            commentary.push(`💩 WORST PRACTICES AWARD: This command is what happens when you let ` +
                `patterns and complexity run wild without adult supervision. Start over.`);
        }
        
        return commentary;
    }

    /**
     * Benchmark a single command
     */
    benchmarkCommand(commandPath) {
        const commandName = path.basename(commandPath, '.md');
        const commandContent = fs.readFileSync(commandPath, 'utf8');
        
        console.log(`🔬 Benchmarking: ${commandName}`);
        
        const results = {
            name: commandName,
            path: commandPath,
            fileSize: fs.statSync(commandPath).size,
            complexity: this.calculateComplexityScore(commandContent),
            tokenAnalysis: this.analyzeTokenConsumption(commandContent),
            maintainability: this.analyzeMaintainability(commandContent, commandName),
            timestamp: new Date().toISOString()
        };
        
        // Generate savage commentary
        const commentary = this.generateSavageCommentary(commandName, results);
        
        results.savageCommentary = commentary;
        results.overallGrade = this.calculateOverallGrade(results);
        
        console.log(`   Complexity: ${results.complexity.score}/5`);
        console.log(`   Maintainability: ${results.maintainability.maintainabilityGrade}`);
        console.log(`   Efficiency: ${results.tokenAnalysis.efficiency}%`);
        console.log(`   Overall Grade: ${results.overallGrade}`);
        
        return results;
    }

    calculateOverallGrade(results) {
        const complexityScore = Math.max(0, 100 - (results.complexity.score * 20));
        const maintainabilityScore = results.maintainability.overallScore;
        const efficiencyScore = results.tokenAnalysis.efficiency;
        
        const overall = (complexityScore + maintainabilityScore + efficiencyScore) / 3;
        return this.getGrade(overall);
    }

    /**
     * Calculate statistical analysis
     */
    calculateStatistics(results) {
        const complexityScores = results.map(r => r.complexity.score);
        const maintainabilityScores = results.map(r => r.maintainability.overallScore);
        const efficiencyScores = results.map(r => r.tokenAnalysis.efficiency);
        
        return {
            complexity: this.calculateStats(complexityScores),
            maintainability: this.calculateStats(maintainabilityScores),
            efficiency: this.calculateStats(efficiencyScores),
            sampleSize: results.length,
            violationRate: results.filter(r => r.complexity.violatesThreshold).length / results.length,
            gradeDistribution: this.calculateGradeDistribution(results)
        };
    }

    calculateStats(values) {
        const n = values.length;
        const mean = values.reduce((a, b) => a + b, 0) / n;
        const variance = values.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / n;
        const stdDev = Math.sqrt(variance);
        const sorted = [...values].sort((a, b) => a - b);
        
        return {
            mean: mean,
            median: n % 2 === 0 ? (sorted[n/2-1] + sorted[n/2]) / 2 : sorted[Math.floor(n/2)],
            stdDev: stdDev,
            min: Math.min(...values),
            max: Math.max(...values),
            confidenceInterval: {
                lower: mean - (1.96 * stdDev / Math.sqrt(n)),
                upper: mean + (1.96 * stdDev / Math.sqrt(n))
            }
        };
    }

    calculateGradeDistribution(results) {
        const grades = results.map(r => r.overallGrade);
        const distribution = {};
        ['A', 'B', 'C', 'D', 'F'].forEach(grade => {
            distribution[grade] = grades.filter(g => g === grade).length;
        });
        return distribution;
    }

    /**
     * Generate final report
     */
    generateReport(results, outputPath) {
        const statistics = this.calculateStatistics(results);
        
        const report = {
            benchmark_id: `savage-command-benchmarker-${new Date().toISOString().split('T')[0]}`,
            timestamp: new Date().toISOString(),
            benchmarker: "Dr. Savage McMetrics, PhD in Command Roasting",
            methodology: this.benchmarkResults.methodology,
            
            summary: {
                commands_analyzed: results.length,
                complexity_violations: results.filter(r => r.complexity.violatesThreshold).length,
                average_grade: this.getGrade(statistics.maintainability.mean),
                violation_rate: (statistics.violationRate * 100).toFixed(1) + '%'
            },
            
            commands: results,
            statistical_analysis: statistics,
            
            savage_summary: this.generateOverallSavageCommentary(results, statistics),
            
            recommendations: this.generateRecommendations(results, statistics),
            
            disclaimer: "These measurements are more accurate than your last performance review"
        };
        
        fs.writeFileSync(outputPath, JSON.stringify(report, null, 2));
        return report;
    }

    generateOverallSavageCommentary(results, stats) {
        const commentary = [];
        
        if (stats.violationRate > 0.4) {
            commentary.push(`🚨 COMPLEXITY EPIDEMIC: ${(stats.violationRate * 100).toFixed(1)}% of commands violate ` +
                `the sacred 5-point threshold. This isn't innovation, it's digital hoarding disorder.`);
        } else if (stats.violationRate > 0.2) {
            commentary.push(`⚠️ COMPLEXITY CONCERN: ${(stats.violationRate * 100).toFixed(1)}% violation rate suggests ` +
                `some commands are getting too clever for their own good.`);
        } else {
            commentary.push(`✅ COMPLEXITY DISCIPLINE: ${(stats.violationRate * 100).toFixed(1)}% violation rate shows ` +
                `most developers understand that simple is sustainable.`);
        }
        
        if (stats.gradeDistribution.F > 0) {
            commentary.push(`💀 FAILURE DETECTED: ${stats.gradeDistribution.F} command(s) earned the dreaded F grade. ` +
                `These need immediate intervention before they reproduce.`);
        }
        
        if (stats.gradeDistribution.A > stats.gradeDistribution.C + stats.gradeDistribution.D + stats.gradeDistribution.F) {
            commentary.push(`🏆 QUALITY CULTURE: More A grades than mediocrity. Your command ecosystem ` +
                `shows signs of actual engineering discipline.`);
        }
        
        commentary.push(`📊 STATISTICAL REALITY CHECK: Mean complexity ${stats.complexity.mean.toFixed(2)}/5, ` +
            `σ=${stats.complexity.stdDev.toFixed(2)}. If you're consistently above 3, you're not building ` +
            `commands, you're building monuments to your own cleverness.`);
        
        return commentary;
    }

    generateRecommendations(results, stats) {
        const recommendations = [];
        
        const worstOffenders = results
            .filter(r => r.complexity.violatesThreshold)
            .sort((a, b) => b.complexity.score - a.complexity.score)
            .slice(0, 3);
        
        if (worstOffenders.length > 0) {
            recommendations.push({
                priority: 'CRITICAL',
                title: 'Complexity Violations Need Immediate Refactoring',
                commands: worstOffenders.map(r => r.name),
                action: 'Apply the 3-question rule: Can I use existing? Can I simplify? Do I need abstraction NOW?'
            });
        }
        
        const lowMaintainability = results
            .filter(r => r.maintainability.overallScore < 60)
            .sort((a, b) => a.maintainability.overallScore - b.maintainability.overallScore)
            .slice(0, 3);
        
        if (lowMaintainability.length > 0) {
            recommendations.push({
                priority: 'HIGH',
                title: 'Maintainability Crisis',
                commands: lowMaintainability.map(r => r.name),
                action: 'Focus on naming, documentation, and single responsibility. Future you will thank you.'
            });
        }
        
        const inefficient = results
            .filter(r => r.tokenAnalysis.efficiency < 60)
            .sort((a, b) => a.tokenAnalysis.efficiency - b.tokenAnalysis.efficiency)
            .slice(0, 3);
        
        if (inefficient.length > 0) {
            recommendations.push({
                priority: 'MEDIUM',
                title: 'Token Efficiency Improvements',
                commands: inefficient.map(r => r.name),
                action: 'Remove bloat, eliminate redundancy, get to the point faster.'
            });
        }
        
        return recommendations;
    }
}

module.exports = SavageCommandBenchmarker;

// CLI execution
if (require.main === module) {
    const benchmarker = new SavageCommandBenchmarker();
    const commandsDir = process.argv[2] || './commands';
    const outputFile = process.argv[3] || './.github/benchmarks/results/benchmark-report.json';
    
    console.log('🔬 SAVAGE COMMAND BENCHMARKER activated');
    console.log('📊 Preparing to scientifically roast your commands...\n');
    
    // Get all command files
    const commandFiles = fs.readdirSync(commandsDir)
        .filter(file => file.endsWith('.md'))
        .map(file => path.join(commandsDir, file));
    
    console.log(`📝 Found ${commandFiles.length} commands to analyze\n`);
    
    // Benchmark each command
    const results = commandFiles.map(file => benchmarker.benchmarkCommand(file));
    
    // Generate comprehensive report
    console.log('\n📊 Generating comprehensive statistical analysis...');
    const report = benchmarker.generateReport(results, outputFile);
    
    console.log(`\n✅ Benchmark complete! Report saved to: ${outputFile}`);
    console.log(`📈 Summary: ${report.summary.commands_analyzed} commands, ` +
        `${report.summary.complexity_violations} violations, ` +
        `${report.summary.violation_rate} violation rate`);
    
    // Print savage summary
    console.log('\n🔥 SAVAGE SUMMARY:');
    report.savage_summary.forEach(comment => console.log(`   ${comment}`));
}