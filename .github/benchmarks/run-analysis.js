const fs = require('fs');
const path = require('path');

// Simplified benchmarking analysis
function analyzeCommand(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const name = path.basename(filePath, '.md');
    
    // Calculate metrics
    const lines = content.split('\n').length;
    const thinkingBlocks = (content.match(/<thinking>/g) || []).length;
    const mcpCalls = (content.match(/mcp__/g) || []).length;
    const variables = (content.match(/\$\{[^}]+\}/g) || []).length;
    const complexExpressions = (content.match(/\$\{[^}]*[^}]*\}/g) || []).length;
    
    // Complexity score (1-10, <5 is passing)
    const complexityScore = Math.min(10, Math.max(1, Math.round(
        lines * 0.01 + 
        thinkingBlocks * 0.5 + 
        mcpCalls * 0.3 + 
        variables * 0.1 +
        complexExpressions * 0.2
    )));
    
    // Token estimate (rough)
    const estimatedTokens = Math.ceil(content.length / 4);
    
    // Effectiveness score
    let effectiveness = 0;
    if (content.includes('<thinking>')) effectiveness += 25;
    if (content.includes('complexity_detection')) effectiveness += 20;
    if (content.includes('mcp__')) effectiveness += 15;
    if (content.includes('## Usage') || content.includes('Examples')) effectiveness += 15;
    if (content.includes('error') || content.includes('Error')) effectiveness += 10;
    if (thinkingBlocks >= 3) effectiveness += 10;
    if ((content.match(/```/g) || []).length >= 4) effectiveness += 5;
    
    // Risk factors
    const risks = [];
    if (complexityScore >= 5) {
        risks.push('CRITICAL: Complexity violation');
    }
    if (!content.includes('<thinking>')) {
        risks.push('HIGH: No thinking architecture');
    }
    if (lines > 500) {
        risks.push('MEDIUM: Command bloat');
    }
    
    return {
        name,
        lines,
        complexityScore,
        effectiveness,
        estimatedTokens,
        thinkingBlocks,
        mcpCalls,
        risks,
        passesComplexityRule: complexityScore < 5,
        isEffective: effectiveness >= 50
    };
}

// Analyze our 5 commands
const commands = [
    '../../commands/adhd-evening-reflect.md',
    '../../commands/git-backup-sync.md', 
    '../../commands/context-enhanced-executor.md',
    '../../commands/generate-thinking-command.md',
    '../../commands/safe-code-beautifier.md'
];

const results = [];
commands.forEach(cmd => {
    try {
        const analysis = analyzeCommand(cmd);
        results.push(analysis);
        console.log(`✅ Analyzed: ${analysis.name}`);
    } catch (err) {
        console.log(`❌ Failed: ${cmd} - ${err.message}`);
    }
});

console.log('\n📊 BENCHMARK RESULTS:\n');
console.log(JSON.stringify(results, null, 2));