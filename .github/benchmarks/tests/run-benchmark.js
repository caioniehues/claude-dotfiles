#!/usr/bin/env node
/**
 * EXECUTION CHAMBER for Command Benchmarking
 * Where commands meet their statistical doom
 */

const SavageCommandBenchmarker = require('./benchmark-framework.js');
const path = require('path');

async function main() {
    console.log('🔥 ENTERING THE STATISTICAL TORTURE CHAMBER');
    console.log('Preparing to expose command quality with BRUTAL HONESTY');
    console.log('');

    const benchmarker = new SavageCommandBenchmarker();
    
    // Representative commands for comprehensive analysis
    const targetCommands = [
        'commands/ultrathink.md',
        'commands/java-clean-code-generator.md', 
        'commands/adhd-morning-assistant.md',
        'commands/intelligent-code-enhancer.md',
        'commands/java-rapid-implementation.md',
        'commands/adaptive-complexity-router.md',
        'commands/senior-developer-analysis.md'
    ];

    const commandPaths = targetCommands.map(cmd => 
        path.join('/home/runner/work/claude-dotfiles/claude-dotfiles', cmd)
    );

    console.log(`📋 SELECTED VICTIMS: ${commandPaths.length} commands`);
    commandPaths.forEach(cmd => console.log(`  - ${path.basename(cmd)}`));
    console.log('');

    // Phase 1: Analysis
    console.log('🔬 PHASE 1: DISSECTION BEGINS');
    const analyzedCommands = [];
    
    for (const commandPath of commandPaths) {
        try {
            const command = await benchmarker.analyzeCommand(commandPath);
            analyzedCommands.push(command);
            console.log(`✅ Analyzed: ${command.name} (${command.metrics.tokenCount} tokens, ${command.metrics.buzzwordCount} buzzwords)`);
        } catch (error) {
            console.error(`❌ Failed to analyze ${path.basename(commandPath)}: ${error.message}`);
        }
    }

    console.log('');
    console.log(`🧪 PHASE 2: STATISTICAL TORTURE (${analyzedCommands.length} victims prepared)`);
    
    // Phase 2: Statistical Analysis
    const results = await benchmarker.runStatisticalTests(analyzedCommands);
    
    console.log('');
    console.log('📊 PHASE 3: EVIDENCE COMPILATION');
    
    // Phase 3: Report Generation
    const reportFiles = await benchmarker.generateReport(results);
    
    console.log('');
    console.log('🎯 SAVAGE BENCHMARKING COMPLETE!');
    console.log('');
    console.log('📄 REPORTS GENERATED:');
    console.log(`  📊 JSON Report: ${reportFiles.jsonReport}`);
    console.log(`  📝 Human Report: ${reportFiles.humanReport}`);
    console.log('');
    
    // Preview of savage findings
    console.log('🔥 PREVIEW OF SAVAGE FINDINGS:');
    console.log('');
    console.log(`Overall Grade: ${results.savage_summary.overall_grade.letter} (${results.savage_summary.overall_grade.score}%)`);
    console.log(`Comment: ${results.savage_summary.overall_grade.comment}`);
    console.log('');
    
    if (results.savage_summary.improvement_recommendations.length > 0) {
        console.log('🚨 HIGH PRIORITY ISSUES:');
        results.savage_summary.improvement_recommendations
            .filter(rec => rec.priority === 'HIGH')
            .forEach(rec => {
                console.log(`  - ${rec.issue}: ${rec.solution}`);
            });
        console.log('');
    }
    
    // Most savage verdict preview
    const mostSavage = results.commands
        .sort((a, b) => b.quality_assessment.overengineering_level - a.quality_assessment.overengineering_level)[0];
    
    if (mostSavage) {
        console.log('💀 MOST SAVAGE VERDICT:');
        console.log(`"${mostSavage.name}": ${mostSavage.savage_verdict}`);
        console.log('');
    }
    
    console.log('Evidence-based roasting complete. Check the reports for full statistical destruction.');
}

main().catch(console.error);