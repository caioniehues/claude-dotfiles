/**
 * DIRECT EXECUTION - Savage Command Benchmarker
 * No approval needed, pure statistical destruction
 */

const fs = require('fs');
const path = require('path');

// Simplified benchmarker for direct execution
class DirectBenchmarker {
    constructor() {
        this.testId = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
    }

    analyzeCommand(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const name = path.basename(filePath, '.md');
        const lines = content.split('\n');
        
        return {
            name,
            path: filePath,
            content,
            metrics: {
                tokenCount: Math.ceil(content.length / 3.5),
                lineCount: lines.length,
                xmlTagCount: (content.match(/<[^>]*>/g) || []).length,
                thinkingBlockCount: (content.match(/<thinking>/g) || []).length,
                mcpToolCount: (content.match(/mcp__/g) || []).length,
                conditionalCount: (content.match(/\$\{.*\}/g) || []).length,
                placeholderCount: (content.match(/\[.*?\]/g) || []).length,
                buzzwordCount: this.countBuzzwords(content),
                practicalityScore: this.assessPracticality(content)
            }
        };
    }

    countBuzzwords(content) {
        const buzzwords = [
            'orchestration', 'paradigm', 'synergy', 'revolutionary',
            'transformative', 'leverage', 'cutting-edge', 'state-of-the-art',
            'enterprise-grade', 'scalable', 'robust', 'innovative',
            'strategic', 'optimization', 'enhancement', 'intelligent',
            'adaptive', 'comprehensive', 'systematic', 'holistic',
            'sophisticated', 'architecture', 'framework', 'methodology'
        ];
        
        const lowerContent = content.toLowerCase();
        return buzzwords.filter(word => lowerContent.includes(word)).length;
    }

    assessPracticality(content) {
        let score = 50;
        
        // Positive indicators
        if (content.includes('mcp__basic-memory')) score += 10;
        if (content.includes('ARGUMENTS')) score += 5;
        if (content.includes('<thinking>')) score += 15;
        if (content.includes('usage')) score += 5;
        if (content.includes('example')) score += 5;
        if (content.includes('TodoWrite')) score += 5;
        
        // Negative indicators (overengineering)
        const overPatterns = ['factory', 'abstract', 'interface', 'strategy', 'observer', 'singleton', 'builder'];
        overPatterns.forEach(pattern => {
            if (content.toLowerCase().includes(pattern)) score -= 5;
        });
        
        return Math.max(0, Math.min(100, score));
    }

    assessQuality(command) {
        const metrics = command.metrics;
        
        let maintainability = 70;
        if (metrics.xmlTagCount > 100) maintainability -= 20;
        if (metrics.thinkingBlockCount > 0) maintainability += 10;
        if (metrics.lineCount > 500) maintainability -= 15;
        
        let readability = 60;
        if (metrics.buzzwordCount > 10) readability -= 25;
        if (metrics.placeholderCount > 50) readability -= 15;
        
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

    generateSavageVerdict(command, quality) {
        const metrics = command.metrics;
        let verdict = `"${command.name}": `;
        let savagery = 0;
        
        if (metrics.tokenCount > 3000) {
            verdict += `This ${metrics.tokenCount}-token leviathan represents everything wrong with modern development. `;
            savagery += 3;
        } else if (metrics.tokenCount > 2000) {
            verdict += `At ${metrics.tokenCount} tokens, this is approaching novella length. `;
            savagery += 2;
        } else if (metrics.tokenCount > 1000) {
            verdict += `${metrics.tokenCount} tokens - getting verbose but manageable. `;
            savagery += 1;
        }
        
        if (quality.overengineering_level > 60) {
            verdict += `Overengineering: ${quality.overengineering_level.toFixed(1)}%. This is architectural masturbation. `;
            savagery += 3;
        } else if (quality.overengineering_level > 40) {
            verdict += `Some overengineering detected (${quality.overengineering_level.toFixed(1)}%). `;
            savagery += 2;
        }
        
        if (metrics.buzzwordCount > 20) {
            verdict += `${metrics.buzzwordCount} buzzwords detected - did McKinsey write this? `;
            savagery += 2;
        } else if (metrics.buzzwordCount > 15) {
            verdict += `${metrics.buzzwordCount} buzzwords - getting into consultant territory. `;
            savagery += 1;
        }
        
        if (quality.practical_value < 40) {
            verdict += `Practical value: ${quality.practical_value}% - solving imaginary problems. `;
            savagery += 2;
        } else if (quality.practical_value > 80) {
            verdict += `Actually practical (${quality.practical_value}%) - surprisingly competent. `;
        }
        
        // Savage rating
        if (savagery >= 6) {
            verdict += "💀 VERDICT: Crimes against software engineering.";
        } else if (savagery >= 4) {
            verdict += "🔥 VERDICT: Needs serious intervention.";
        } else if (savagery >= 2) {
            verdict += "⚠️ VERDICT: Mediocre with concerning patterns.";
        } else {
            verdict += "✅ VERDICT: Actually reasonable.";
        }
        
        return { verdict, savagery };
    }

    calculateStats(values) {
        if (values.length === 0) return {};
        const sorted = values.sort((a, b) => a - b);
        const sum = values.reduce((a, b) => a + b, 0);
        const mean = sum / values.length;
        const variance = values.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / values.length;
        
        return {
            min: Math.min(...values),
            max: Math.max(...values),
            mean: Number(mean.toFixed(2)),
            median: sorted[Math.floor(sorted.length / 2)],
            std_deviation: Number(Math.sqrt(variance).toFixed(2))
        };
    }

    generateReport(results) {
        const timestamp = new Date().toISOString();
        const reportPath = `/home/runner/work/claude-dotfiles/claude-dotfiles/.github/benchmarks/results/${this.testId}-report.json`;
        
        // Calculate overall grade
        let score = 50;
        const avgOvereng = results.stats.overengineering.mean || 0;
        const avgPractical = results.stats.practical_value.mean || 0;
        const avgTokens = results.stats.token_count.mean || 0;
        const avgBuzzwords = results.stats.buzzword_count.mean || 0;
        
        if (avgPractical > 70) score += 15;
        if (avgOvereng < 30) score += 10;
        if (avgOvereng > 50) score -= 20;
        if (avgTokens > 3000) score -= 15;
        if (avgBuzzwords > 15) score -= 10;
        
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
        
        const report = {
            meta: {
                timestamp,
                test_id: this.testId,
                commands_analyzed: results.commands.length,
                savage_level: 'MAXIMUM'
            },
            overall_grade: {
                score: score.toFixed(1),
                letter: grade.grade,
                comment: grade.comment
            },
            statistics: results.stats,
            command_verdicts: results.verdicts,
            rankings: results.rankings,
            savage_summary: this.generateSavageSummary(results, grade, score)
        };
        
        fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
        
        // Generate markdown report
        const mdReport = this.generateMarkdownReport(report);
        const mdPath = reportPath.replace('.json', '.md');
        fs.writeFileSync(mdPath, mdReport);
        
        return { json: reportPath, markdown: mdPath, report };
    }

    generateSavageSummary(results, grade, score) {
        let summary = `# 🔬 SAVAGE COMMAND BENCHMARKING RESULTS\n\n`;
        summary += `**Overall Grade: ${grade.grade} (${score.toFixed(1)}%)** - ${grade.comment}\n\n`;
        
        const stats = results.stats;
        
        if (stats.overengineering.mean > 50) {
            summary += `💀 **CRITICAL FINDING**: Average overengineering level is ${stats.overengineering.mean}%. This codebase has architectural cancer spreading through the command ecosystem.\n\n`;
        } else if (stats.overengineering.mean > 30) {
            summary += `⚠️ **WARNING**: Overengineering at ${stats.overengineering.mean}% - early signs of enterprise bloat detected.\n\n`;
        }
        
        if (stats.token_count.mean > 2500) {
            summary += `💸 **TOKEN HEMORRHAGE**: Commands average ${stats.token_count.mean} tokens. These aren't commands, they're dissertations.\n\n`;
        }
        
        if (stats.practical_value.mean < 50) {
            summary += `🎭 **REALITY CHECK**: Average practical value is ${stats.practical_value.mean}%. These commands solve problems that exist mainly in developers' fevered imaginations.\n\n`;
        }
        
        const worstCommand = results.verdicts.sort((a, b) => b.savagery - a.savagery)[0];
        if (worstCommand) {
            summary += `🏆 **WORST OFFENDER**: "${worstCommand.name}" with savagery level ${worstCommand.savagery}/10\n`;
            summary += `${worstCommand.verdict}\n\n`;
        }
        
        return summary;
    }

    generateMarkdownReport(report) {
        return `# 🔬 Savage Command Benchmark Report

**Generated:** ${report.meta.timestamp}  
**Test ID:** ${report.meta.test_id}  
**Commands Analyzed:** ${report.meta.commands_analyzed}

## 📊 Overall Assessment

### Grade: ${report.overall_grade.letter} (${report.overall_grade.score}%)
*${report.overall_grade.comment}*

## 📈 Statistical Brutality

### Token Economics
- **Average:** ${report.statistics.token_count.mean} tokens per command
- **Range:** ${report.statistics.token_count.min} - ${report.statistics.token_count.max} tokens  
- **Standard Deviation:** ${report.statistics.token_count.std_deviation}
- **Median:** ${report.statistics.token_count.median}

### Quality Metrics (0-100 scale)
| Metric | Mean | Min | Max | Std Dev |
|--------|------|-----|-----|---------|
| Maintainability | ${report.statistics.maintainability.mean} | ${report.statistics.maintainability.min} | ${report.statistics.maintainability.max} | ${report.statistics.maintainability.std_deviation} |
| Readability | ${report.statistics.readability.mean} | ${report.statistics.readability.min} | ${report.statistics.readability.max} | ${report.statistics.readability.std_deviation} |
| Overengineering | ${report.statistics.overengineering.mean} | ${report.statistics.overengineering.min} | ${report.statistics.overengineering.max} | ${report.statistics.overengineering.std_deviation} |
| Practical Value | ${report.statistics.practical_value.mean} | ${report.statistics.practical_value.min} | ${report.statistics.practical_value.max} | ${report.statistics.practical_value.std_deviation} |

### Complexity Indicators
- **Average Line Count:** ${report.statistics.line_count.mean}
- **Average XML Tags:** ${report.statistics.xml_tag_count.mean}
- **Average Buzzwords:** ${report.statistics.buzzword_count.mean}
- **Average Thinking Blocks:** ${report.statistics.thinking_blocks.mean}

## 🏆 Hall of Shame/Fame

### Token Monsters
${report.rankings.token_monsters.map((cmd, i) => `${i + 1}. **${cmd.name}** - ${cmd.metrics.tokenCount} tokens`).join('\n')}

### Most Overengineered
${report.rankings.overengineered.map((cmd, i) => `${i + 1}. **${cmd.name}** - ${cmd.quality.overengineering_level.toFixed(1)}% overengineering`).join('\n')}

### Most Practical
${report.rankings.practical.map((cmd, i) => `${i + 1}. **${cmd.name}** - ${cmd.quality.practical_value.toFixed(1)}% practical value`).join('\n')}

## 💀 Savage Verdicts

${report.command_verdicts.map(v => `### ${v.name}\n${v.verdict}\n`).join('\n')}

## 🎯 Savage Summary

${report.savage_summary}

---
*Generated by Savage Command Benchmarker - PhD in roasting bad code*
`;
    }
}

// EXECUTE THE CARNAGE
console.log('🔥 SAVAGE COMMAND BENCHMARKER ACTIVATED');
console.log('Statistical destruction commencing...\n');

const benchmarker = new DirectBenchmarker();

// Target commands for analysis
const commands = [
    'commands/ultrathink.md',
    'commands/java-clean-code-generator.md', 
    'commands/adhd-morning-assistant.md',
    'commands/intelligent-code-enhancer.md',
    'commands/java-rapid-implementation.md',
    'commands/adaptive-complexity-router.md',
    'commands/senior-developer-analysis.md'
];

const baseDir = '/home/runner/work/claude-dotfiles/claude-dotfiles';
const results = {
    commands: [],
    verdicts: [],
    stats: {},
    rankings: {}
};

console.log(`📋 ANALYZING ${commands.length} COMMANDS FOR STATISTICAL BRUTALITY:`);

// Analyze each command
for (const cmdPath of commands) {
    const fullPath = path.join(baseDir, cmdPath);
    try {
        const command = benchmarker.analyzeCommand(fullPath);
        const quality = benchmarker.assessQuality(command);
        const { verdict, savagery } = benchmarker.generateSavageVerdict(command, quality);
        
        results.commands.push({ ...command, quality });
        results.verdicts.push({ name: command.name, verdict, savagery });
        
        console.log(`✅ ${command.name}: ${command.metrics.tokenCount} tokens, ${quality.overengineering_level.toFixed(1)}% overengineered`);
    } catch (error) {
        console.error(`❌ Failed: ${cmdPath} - ${error.message}`);
    }
}

// Calculate statistics
const metrics = results.commands.map(c => c.metrics);
const qualities = results.commands.map(c => c.quality);

results.stats = {
    token_count: benchmarker.calculateStats(metrics.map(m => m.tokenCount)),
    line_count: benchmarker.calculateStats(metrics.map(m => m.lineCount)),
    xml_tag_count: benchmarker.calculateStats(metrics.map(m => m.xmlTagCount)),
    thinking_blocks: benchmarker.calculateStats(metrics.map(m => m.thinkingBlockCount)),
    buzzword_count: benchmarker.calculateStats(metrics.map(m => m.buzzwordCount)),
    maintainability: benchmarker.calculateStats(qualities.map(q => q.maintainability)),
    readability: benchmarker.calculateStats(qualities.map(q => q.readability)),
    overengineering: benchmarker.calculateStats(qualities.map(q => q.overengineering_level)),
    practical_value: benchmarker.calculateStats(qualities.map(q => q.practical_value))
};

// Generate rankings
results.rankings = {
    token_monsters: results.commands
        .sort((a, b) => b.metrics.tokenCount - a.metrics.tokenCount)
        .slice(0, 3),
    overengineered: results.commands
        .sort((a, b) => b.quality.overengineering_level - a.quality.overengineering_level)
        .slice(0, 3),
    practical: results.commands
        .sort((a, b) => b.quality.practical_value - a.quality.practical_value)
        .slice(0, 3)
};

console.log('\n🔬 GENERATING SAVAGE REPORT...');

const reportFiles = benchmarker.generateReport(results);

console.log('\n🎯 SAVAGE BENCHMARKING COMPLETE!');
console.log(`📊 JSON Report: ${reportFiles.json}`);
console.log(`📝 Markdown Report: ${reportFiles.markdown}`);

console.log(`\n🏆 OVERALL GRADE: ${reportFiles.report.overall_grade.letter} (${reportFiles.report.overall_grade.score}%)`);
console.log(`💬 ${reportFiles.report.overall_grade.comment}`);

console.log('\n💀 WORST OFFENDER:');
const worst = results.verdicts.sort((a, b) => b.savagery - a.savagery)[0];
console.log(`"${worst.name}" - Savagery Level: ${worst.savagery}/10`);

console.log('\n🔥 Evidence-based roasting complete. The truth hurts, but it\'s necessary.');