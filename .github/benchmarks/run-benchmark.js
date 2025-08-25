#!/usr/bin/env node

const { SavageCommandBenchmarker } = require('./benchmark-harness.js');
const fs = require('fs');
const path = require('path');

async function main() {
    console.log(`
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║         🔬 SAVAGE COMMAND BENCHMARKER - Scientific Roasting Session           ║
║                                                                                ║
║    "Any fool can write code that a computer can understand.                    ║
║     Good programmers write code that humans can understand." - Martin Fowler  ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
`);

    const benchmarker = new SavageCommandBenchmarker();
    
    try {
        console.log("📊 Executing comprehensive benchmark suite...\n");
        
        const results = await benchmarker.runCompleteBenchmark();
        
        // Generate timestamp for report
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-').substring(0, 19);
        const reportPath = path.join(__dirname, 'results', `${timestamp}-report.json`);
        
        // Ensure results directory exists
        const resultsDir = path.dirname(reportPath);
        if (!fs.existsSync(resultsDir)) {
            fs.mkdirSync(resultsDir, { recursive: true });
        }
        
        // Save detailed JSON report
        fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
        
        console.log(`📋 Detailed results saved to: ${reportPath}\n`);
        
        // Generate human-readable summary
        console.log("🎯 EXECUTIVE SUMMARY - THE BRUTAL TRUTH:");
        console.log("=" .repeat(80));
        
        Object.entries(results.commands).forEach(([commandName, data]) => {
            console.log(`\n📊 ${commandName.toUpperCase()}`);
            console.log("-".repeat(50));
            console.log(`📈 Token Consumption: ${data.metrics.tokenConsumption.statistics.mean.toFixed(0)} ± ${data.metrics.tokenConsumption.statistics.stdDev.toFixed(0)}`);
            console.log(`⏱️  Execution Time: ${(data.metrics.executionTime.statistics.mean / 1000).toFixed(2)}s ± ${(data.metrics.executionTime.statistics.stdDev / 1000).toFixed(2)}s`);
            console.log(`✅ Success Rate: ${data.metrics.successRate.successRate.toFixed(1)}%`);
            console.log(`🔢 Complexity Score: ${data.metrics.complexityScore.score} (${data.metrics.complexityScore.verdict})`);
            console.log(`🏆 Overall Verdict: ${data.verdict}`);
            
            if (data.savageComments.length > 0) {
                console.log("\n💀 SAVAGE BUT FAIR ASSESSMENT:");
                data.savageComments.forEach(comment => {
                    console.log(`   💣 ${comment}`);
                });
            }
        });
        
        console.log("\n" + "=".repeat(80));
        console.log("🎓 PROFESSOR'S FINAL GRADES:");
        console.log("=".repeat(80));
        
        const grades = Object.entries(results.commands).map(([name, data]) => ({
            name,
            verdict: data.verdict,
            complexity: data.metrics.complexityScore.score,
            success: data.metrics.successRate.successRate
        })).sort((a, b) => b.success - a.success);
        
        grades.forEach((cmd, index) => {
            const medal = index === 0 ? "🥇" : index === 1 ? "🥈" : index === 2 ? "🥉" : "💩";
            console.log(`${medal} ${cmd.name}: ${cmd.verdict} (Success: ${cmd.success.toFixed(1)}%, Complexity: ${cmd.complexity})`);
        });
        
        console.log(`\n📊 Report timestamp: ${timestamp}`);
        console.log(`📁 Full data: ${reportPath}`);
        console.log("\n🎯 Benchmarking complete. Science has spoken.");
        
    } catch (error) {
        console.error("💥 Benchmark failed:", error);
        process.exit(1);
    }
}

if (require.main === module) {
    main().catch(console.error);
}

module.exports = { main };