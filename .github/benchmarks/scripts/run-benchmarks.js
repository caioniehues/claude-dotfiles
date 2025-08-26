#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const CommandBenchmarker = require('./benchmark-framework');

// SAVAGE BENCHMARKER EXECUTION SCRIPT
async function runBenchmarks() {
    console.log("🔬 INITIALIZING SAVAGE COMMAND BENCHMARKER");
    console.log("================================================");
    
    const benchmarker = new CommandBenchmarker();
    
    // Our selected victims for scientific roasting
    const victims = [
        'adaptive-complexity-router.md',
        'adhd-context-switch.md', 
        'java-clean-code-generator.md',
        'intelligent-refactor-session.md',
        'ultrathink.md'
    ];
    
    const commandsDir = path.join(__dirname, '../../../commands');
    
    console.log("🎯 SELECTED VICTIMS FOR SCIENTIFIC ROASTING:");
    victims.forEach((victim, i) => {
        console.log(`   ${i+1}. ${victim}`);
    });
    console.log();
    
    // Benchmark each victim
    for (const victim of victims) {
        const filePath = path.join(commandsDir, victim);
        
        try {
            const content = fs.readFileSync(filePath, 'utf8');
            const name = victim.replace('.md', '');
            
            console.log(`\n🔬 ANALYZING: ${name}`);
            console.log('='.repeat(50));
            
            const results = benchmarker.benchmarkCommand(name, content);
            
            // Display immediate savage judgment
            console.log(`📊 COMPLEXITY SCORE: ${results.metrics.complexity.total}/5`);
            console.log(`💰 TOKEN ESTIMATE: ${results.metrics.tokenEstimate}`);
            console.log(`📏 VERBOSITY: ${results.metrics.readability.verbosity.toFixed(0)}`);
            console.log(`⚡ PERFORMANCE: ${results.metrics.performance}/10`);
            console.log(`🛠️ MAINTAINABILITY: ${results.metrics.maintainability.maintainabilityScore.toFixed(1)}/10`);
            console.log(`📈 OVERALL QUALITY: ${results.metrics.qualityScore.overall.toFixed(2)}/10`);
            console.log();
            console.log("🔥 SAVAGE JUDGMENT:");
            console.log(`   ${results.judgment.summary}`);
            console.log(`   📋 RECOMMENDATION: ${results.judgment.recommendation}`);
            
        } catch (error) {
            console.error(`❌ FAILED TO ANALYZE ${victim}: ${error.message}`);
        }
    }
    
    // Generate final report
    console.log('\n🏁 GENERATING FINAL SAVAGE REPORT...');
    const finalReport = benchmarker.generateReport();
    
    // Save report
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const reportPath = path.join(__dirname, '../results', `${timestamp}-savage-report.json`);
    
    fs.writeFileSync(reportPath, JSON.stringify(finalReport, null, 2));
    
    // Display summary
    console.log('\n🎭 FINAL SCIENTIFIC ROASTING SUMMARY');
    console.log('=====================================');
    console.log(`📊 COMMANDS ANALYZED: ${finalReport.summary.totalCommands}`);
    console.log(`📉 AVERAGE COMPLEXITY: ${finalReport.summary.avgComplexity.toFixed(2)}/5`);
    console.log(`🥇 BEST PERFORMER: ${finalReport.summary.bestPerformer.name} (${finalReport.summary.bestPerformer.score.toFixed(2)}/10)`);
    console.log(`🥴 WORST OFFENDER: ${finalReport.summary.worstOffender.name} (${finalReport.summary.worstOffender.score.toFixed(2)}/10)`);
    console.log(`💸 TOTAL TOKEN COST: ${finalReport.summary.totalTokens.toLocaleString()}`);
    console.log(`⏱️ ANALYSIS TIME: ${finalReport.executionTime}ms`);
    
    console.log('\n🚨 GLOBAL RECOMMENDATIONS:');
    finalReport.summary.recommendations.forEach((rec, i) => {
        console.log(`   ${i+1}. ${rec}`);
    });
    
    console.log(`\n📄 FULL REPORT SAVED: ${reportPath}`);
    console.log('\n🎯 SCIENTIFIC ROASTING COMPLETE! The data doesn\'t lie...');
    
    return finalReport;
}

// Statistical analysis functions
function calculateStatistics(values) {
    const mean = values.reduce((sum, val) => sum + val, 0) / values.length;
    const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length;
    const stdDev = Math.sqrt(variance);
    const min = Math.min(...values);
    const max = Math.max(...values);
    const median = values.sort((a, b) => a - b)[Math.floor(values.length / 2)];
    
    return { mean, stdDev, variance, min, max, median };
}

function generateConfidenceInterval(mean, stdDev, n, confidence = 0.95) {
    const tValue = 2.576; // 99% confidence for simplicity
    const margin = tValue * (stdDev / Math.sqrt(n));
    return {
        lower: mean - margin,
        upper: mean + margin,
        margin
    };
}

// Execute if run directly
if (require.main === module) {
    runBenchmarks()
        .then(() => process.exit(0))
        .catch(error => {
            console.error('💥 BENCHMARKER CRASHED:', error);
            process.exit(1);
        });
}

module.exports = { runBenchmarks };