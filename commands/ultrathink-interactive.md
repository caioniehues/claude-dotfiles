# ULTRATHINK Interactive - Deep Thinking with Progressive Refinement

<task>
Interactive refinement workflow integrated with ULTRATHINK deep thinking for: $ARGUMENTS
</task>

<context>
Master integration combining Interactive Refinement's one-at-a-time questioning with ULTRATHINK's deep thinking capabilities. Provides rich visual feedback, progressive confidence building, and seamless transition from understanding to execution.

**Integration Features:**
- One-at-a-time interactive questioning
- Rich visual progress indicators
- Continuous refinement cycles
- Deep thinking with pattern recognition
- Session persistence and resumability
- Adaptive complexity routing
</context>

<initialization>
## 🚀 Session Initialization

```javascript
// Load guidelines and context
const initializeSession = async () => {
  // Read CLAUDE.md files
  const globalGuidelines = await Read('~/.claude/CLAUDE.md')
  const localGuidelines = await Read('./CLAUDE.md').catch(() => null)
  
  // Load Basic Memory context
  await mcp__basic-memory__build_context("memory://technical/thinking-patterns/*")
  await mcp__basic-memory__recent_activity("--timeframe 24h")
  
  // Parse topic
  const topic = {
    raw: "$ARGUMENTS",
    domain: detectDomain("$ARGUMENTS"),
    keywords: extractKeywords("$ARGUMENTS"),
    timestamp: new Date().toISOString(),
    slug: slugify("$ARGUMENTS"),
    complexity: assessInitialComplexity("$ARGUMENTS")
  }
  
  // Create session structure
  const sessionPath = `refinement-sessions/${topic.timestamp}-${topic.slug}`
  const metadata = {
    status: "active",
    confidence: 0,
    phase: "interactive-refinement",
    iteration: 1,
    startTime: topic.timestamp,
    ultrathinkVersion: null  // Will be selected based on complexity
  }
  
  return { topic, sessionPath, metadata, guidelines: { global: globalGuidelines, local: localGuidelines } }
}

// Visual session start
console.log(`
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🎯 ULTRATHINK INTERACTIVE REFINEMENT 🎯               ║
║                                                               ║
║    Deep Thinking with Progressive Understanding               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

🚨 INITIALIZING...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📖 Global CLAUDE.md: ✓ Loaded
📖 Local CLAUDE.md: ${localGuidelines ? '✓ Loaded' : '○ Not found'}
🧠 Basic Memory: ✓ Context loaded
📊 Pattern Library: ✓ ${patternCount} patterns available
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Topic: ${topic.raw}
🏷️ Domain: ${topic.domain}
🔑 Keywords: ${topic.keywords.join(', ')}
🎚️ Initial Complexity: ${topic.complexity}/30

Let's refine your requirements through intelligent questioning...
`)
```
</initialization>

## Stage 1: Interactive Refinement (0% → 40% Confidence)

<interactive_refinement_phase>
### 🌱 Building Initial Understanding

<philosophy>
**ASK → ANALYZE → REFINE → REPEAT**

We'll start with interactive refinement to deeply understand your needs before engaging ULTRATHINK's deep analysis capabilities.
</philosophy>

<iteration_loop>
```javascript
const runInteractiveRefinement = async (context) => {
  let iteration = 1
  let confidence = 0
  const maxIterations = 10
  const targetConfidence = 40  // Handoff point to ULTRATHINK
  
  while (confidence < targetConfidence && iteration <= maxIterations) {
    console.log(getIterationHeader(iteration, confidence))
    
    // Generate adaptive questions
    const questions = generateAdaptiveQuestions(context, iteration)
    
    // Present questions one at a time
    for (let i = 0; i < questions.length; i++) {
      const answer = await presentInteractiveQuestion(
        questions[i], 
        i + 1, 
        questions.length, 
        iteration, 
        confidence
      )
      
      context.answers.push({ question: questions[i], answer, iteration })
      
      // Update confidence after each answer
      confidence = calculateConfidence(context)
      
      // Show thinking animation
      showThinkingAnimation()
      
      // Early exit if confidence reached
      if (confidence >= targetConfidence) break
    }
    
    // Analyze iteration results
    const insights = analyzeIterationResults(context, iteration)
    
    // Present continuation decision
    const shouldContinue = await presentContinuationDecision(
      iteration, 
      confidence, 
      insights.key, 
      insights.uncertainties
    )
    
    if (!shouldContinue || confidence >= targetConfidence) break
    
    iteration++
  }
  
  return { confidence, iteration, context }
}
```
</iteration_loop>

<interactive_question_presentation>
```javascript
const presentInteractiveQuestion = async (question, num, total, iteration, confidence) => {
  const progressBar = generateProgressBar(confidence)
  const iterationEmoji = getIterationEmoji(iteration)
  const phaseColor = getPhaseColor('refinement')
  
  console.log(`
${iterationEmoji} Interactive Refinement - Iteration ${iteration}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────┐
│     🤔 Understanding your requirements...          │
│                                                     │
│     Question ${num} of ${total}                    │
└─────────────────────────────────────────────────────┘

❓ **${question.text}**

📋 **Context**: ${question.context}
💡 **Why this matters**: ${question.rationale}
🎯 **Impact**: ${question.impact}
✨ **Default**: ${question.default || 'No default'}

${question.options ? `
Options:
${question.options.map((opt, i) => `  ${i + 1}. ${opt}`).join('\n')}
` : 'Please provide your answer:'}

[Confidence: ${progressBar} ${confidence}%]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`)
  
  // Wait for user response
  const answer = await getUserResponse()
  
  // Visual thinking indication
  console.log(`
    💭 Processing your answer...
    ${generateThinkingAnimation()}
`)
  
  return answer
}
```
</interactive_question_presentation>

<confidence_tracking>
```javascript
const calculateConfidence = (context) => {
  const factors = {
    answeredQuestions: context.answers.length * 2,
    clarityOfRequirements: context.clarity * 10,
    resolvedAmbiguities: context.resolved.length * 3,
    identifiedConstraints: context.constraints.length * 2,
    domainUnderstanding: context.domainClarity * 5,
    patternMatches: context.patterns.length * 3
  }
  
  const score = Object.values(factors).reduce((a, b) => a + b, 0)
  return Math.min(100, Math.max(0, score))
}

const generateProgressBar = (confidence) => {
  const filled = Math.round(confidence / 10)
  const empty = 10 - filled
  return '█'.repeat(filled) + '░'.repeat(empty)
}

const getIterationEmoji = (iteration) => {
  const emojis = ['🌱', '🌿', '🌳', '🌲', '🎄']
  return emojis[Math.min(iteration - 1, emojis.length - 1)]
}
```
</confidence_tracking>

<refinement_completion>
```javascript
const completeRefinementPhase = (refinementResult) => {
  console.log(`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ INTERACTIVE REFINEMENT COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Refinement Summary:
- Iterations: ${refinementResult.iteration}
- Questions Answered: ${refinementResult.context.answers.length}
- Confidence Achieved: ${refinementResult.confidence}%
- Patterns Identified: ${refinementResult.context.patterns.length}

✨ Key Understanding:
${refinementResult.context.keyInsights.map(i => `• ${i}`).join('\n')}

🎯 Ready for Deep Analysis:
Based on your requirements, selecting ULTRATHINK configuration...
`)
}
```
</refinement_completion>
</interactive_refinement_phase>

## Stage 2: ULTRATHINK Selection & Transition (40% Confidence)

<ultrathink_selection>
### 🔄 Intelligent Version Selection

```javascript
const selectUltrathinkVersion = (context) => {
  const complexity = calculateComplexity(context)
  const needsPersistence = context.patterns.length > 0 || context.requiresLearning
  const needsResearch = context.externalResearch || context.unknownDomain
  const isOffline = checkOfflineMode()
  
  let selectedVersion
  let rationale
  
  if (isOffline) {
    selectedVersion = 'pure-xml'
    rationale = 'Offline mode - using self-contained version'
  } else if (complexity > 15) {
    selectedVersion = 'full-mcp'
    rationale = 'High complexity - sequential thinking needed'
  } else if (needsPersistence || needsResearch) {
    selectedVersion = 'hybrid-mcp'
    rationale = 'Pattern learning and research capabilities needed'
  } else {
    selectedVersion = 'pure-xml'
    rationale = 'Optimizing for speed with adequate capability'
  }
  
  console.log(`
┌─────────────────────────────────────────────────────┐
│     🧠 ULTRATHINK Configuration Selected            │
│                                                     │
│     Version: ${selectedVersion.toUpperCase()}      │
│     Rationale: ${rationale}                        │
│     Complexity Score: ${complexity}/30              │
└─────────────────────────────────────────────────────┘

Transitioning to deep thinking mode...
`)
  
  return selectedVersion
}
```
</ultrathink_selection>

## Stage 3: ULTRATHINK Research Phase (40% → 85% Confidence)

<ultrathink_research>
### 🌳 Deep Analysis with Visual Feedback

```javascript
const runUltrathinkResearch = async (context, version) => {
  const startConfidence = 40
  const targetConfidence = 85
  let currentConfidence = startConfidence
  
  console.log(`
═══════════════════════════════════════════════════════════
🌳 ULTRATHINK RESEARCH PHASE
═══════════════════════════════════════════════════════════

Starting deep analysis with ${version} implementation...
`)
  
  // Execute appropriate ULTRATHINK version with interactive mode
  const command = `/user:ultrathink-${version} --interactive --context ${JSON.stringify(context)}`
  
  // Research loop with interactive questions
  while (currentConfidence < targetConfidence) {
    // Generate research questions based on ULTRATHINK analysis
    const researchQuestions = generateResearchQuestions(context, currentConfidence)
    
    // Present questions interactively
    for (const question of researchQuestions) {
      const answer = await presentInteractiveQuestion(
        question,
        researchQuestions.indexOf(question) + 1,
        researchQuestions.length,
        'Research',
        currentConfidence
      )
      
      context.researchAnswers.push({ question, answer })
      
      // Update confidence
      currentConfidence = updateResearchConfidence(context, startConfidence, targetConfidence)
      
      // Visual progress update
      showPhaseProgress('Research', currentConfidence, targetConfidence)
      
      if (currentConfidence >= targetConfidence) break
    }
    
    // Check if additional research needed
    if (currentConfidence < targetConfidence) {
      const needsMore = await confirmAdditionalResearch(currentConfidence, targetConfidence)
      if (!needsMore) break
    }
  }
  
  return { confidence: currentConfidence, context }
}
```
</ultrathink_research>

## Stage 4: ULTRATHINK Planning Phase (60% → 90% Confidence)

<ultrathink_planning>
### 🌲 Solution Design with Refinement

```javascript
const runUltrathinkPlanning = async (context) => {
  const startConfidence = 60
  const targetConfidence = 90
  let currentConfidence = startConfidence
  
  console.log(`
═══════════════════════════════════════════════════════════
🌲 ULTRATHINK PLANNING PHASE
═══════════════════════════════════════════════════════════

Designing solution with interactive refinement...
`)
  
  // Planning with interactive optimization
  while (currentConfidence < targetConfidence) {
    // Generate planning questions
    const planningQuestions = generatePlanningQuestions(context, currentConfidence)
    
    // Interactive planning refinement
    for (const question of planningQuestions) {
      const answer = await presentInteractiveQuestion(
        question,
        planningQuestions.indexOf(question) + 1,
        planningQuestions.length,
        'Planning',
        currentConfidence
      )
      
      context.planningDecisions.push({ question, answer })
      currentConfidence = updatePlanningConfidence(context, startConfidence, targetConfidence)
      
      showPhaseProgress('Planning', currentConfidence, targetConfidence)
      
      if (currentConfidence >= targetConfidence) break
    }
  }
  
  // Generate task breakdown
  const tasks = generateTaskBreakdown(context)
  displayInteractiveTasks(tasks)
  
  return { confidence: currentConfidence, tasks, context }
}
```
</ultrathink_planning>

## Stage 5: ULTRATHINK Execution Phase (80% → 95% Confidence)

<ultrathink_execution>
### 🎄 Implementation with Progress Tracking

```javascript
const runUltrathinkExecution = async (context, tasks) => {
  const startConfidence = 80
  const targetConfidence = 95
  let currentConfidence = startConfidence
  
  console.log(`
═══════════════════════════════════════════════════════════
🎄 ULTRATHINK EXECUTION PHASE
═══════════════════════════════════════════════════════════

Executing solution with quality gates...
`)
  
  // Execute tasks with visual progress
  for (const task of tasks) {
    console.log(`
┌─────────────────────────────────────────────────────┐
│  Executing: ${task.name}                           │
│  Progress: ${generateTaskProgress(task)}           │
└─────────────────────────────────────────────────────┘
`)
    
    // Execute task
    const result = await executeTask(task, context)
    
    // Quality gate check
    const qualityCheck = await presentQualityGate(task, result, currentConfidence)
    
    if (!qualityCheck.passed) {
      const refine = await requestRefinement(task, qualityCheck.issues)
      if (refine) {
        // Re-execute with refinements
        continue
      }
    }
    
    currentConfidence = updateExecutionConfidence(context, startConfidence, targetConfidence)
    showPhaseProgress('Execution', currentConfidence, targetConfidence)
  }
  
  return { confidence: currentConfidence, results: context.executionResults }
}
```
</ultrathink_execution>

## Final Output Generation

<final_output>
### 🎉 Complete Solution Delivery

```javascript
const generateFinalOutput = (session) => {
  const successArt = `
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║            🎉 ULTRATHINK INTERACTIVE COMPLETE! 🎉            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
`
  
  console.log(successArt)
  
  return `
# 🎯 Solution: ${session.topic.raw}

## 📊 Journey Dashboard
┌─────────────────────────────────────────────────────┐
│ 🌱 Refinement:  ${generateProgressBar(40)} 40%     │
│ 🌳 Research:    ${generateProgressBar(85)} 85%     │
│ 🌲 Planning:    ${generateProgressBar(90)} 90%     │
│ 🎄 Execution:   ${generateProgressBar(95)} 95%     │
│                                                     │
│ Total Questions: ${session.totalQuestions}         │
│ Patterns Used:   ${session.patternsUsed}           │
│ Time Elapsed:    ${session.duration}               │
└─────────────────────────────────────────────────────┘

## 🌱 Interactive Refinement Phase
- Iterations: ${session.refinement.iterations}
- Key Understanding: ${session.refinement.keyInsights}
- Confidence Achieved: 40%

## 🌳 ULTRATHINK Research Phase
- Version Used: ${session.ultrathinkVersion}
- Patterns Identified: ${session.research.patterns}
- External Research: ${session.research.externalSources}
- Confidence Achieved: 85%

## 🌲 ULTRATHINK Planning Phase
- Tasks Created: ${session.planning.taskCount}
- Optimizations: ${session.planning.optimizations}
- Parallel Execution: ${session.planning.parallelTasks}
- Confidence Achieved: 90%

## 🎄 ULTRATHINK Execution Phase
- Tasks Completed: ${session.execution.completed}/${session.execution.total}
- Quality Gates Passed: ✅
- Patterns Captured: ${session.execution.patternsCaptured}
- Final Confidence: 95%

## 📋 Complete Solution

${session.solution.summary}

### Implementation Details
${session.solution.implementation}

### Key Decisions
${session.solution.decisions.map(d => `- ${d}`).join('\n')}

### Quality Metrics
${session.solution.metrics}

## 🚀 Next Steps
${session.nextSteps.map((step, i) => `${i + 1}. ${step}`).join('\n')}

## 📚 Captured Patterns
${session.patterns.map(p => `- **${p.name}**: ${p.description}`).join('\n')}

---
✨ *Solution refined through ${session.totalIterations} iterations of interactive deep thinking*
🧠 *Patterns saved to Basic Memory for future use*
`
}
```
</final_output>

## Helper Functions

<helper_functions>
```javascript
// Visual progress for phases
const showPhaseProgress = (phase, current, target) => {
  const percentage = Math.round((current / target) * 100)
  const progressBar = generateProgressBar(percentage)
  
  console.log(`
${phase} Progress: ${progressBar} ${current}% / ${target}%
`)
}

// Thinking animation
const generateThinkingAnimation = () => {
  const frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
  return frames.join(' → ')
}

// Quality gate presentation
const presentQualityGate = async (task, result, confidence) => {
  console.log(`
┌─────────────────────────────────────────────────────┐
│            ⚖️ QUALITY GATE CHECK                    │
├─────────────────────────────────────────────────────┤
│ Task: ${task.name}                                 │
│ Status: ${result.success ? '✅ PASSED' : '⚠️ NEEDS REVIEW'} │
│ Confidence: ${confidence}%                         │
└─────────────────────────────────────────────────────┘

${result.details}

Continue? (yes/refine/abort): `)
  
  return await getUserResponse()
}

// Session persistence
const saveSession = (session) => {
  const sessionData = {
    ...session,
    savedAt: new Date().toISOString()
  }
  
  // Save to Basic Memory
  mcp__basic-memory__write_note({
    title: `Interactive Session - ${session.topic.slug}`,
    folder: 'technical/interactive-sessions',
    content: JSON.stringify(sessionData)
  })
  
  return sessionData
}
```
</helper_functions>

## Usage Examples

### Example 1: Complex Architecture Decision
```bash
/user:ultrathink-interactive "design microservices architecture for e-commerce platform"
# Starts with refinement, progressively builds understanding, executes with full depth
```

### Example 2: Technical Problem Solving
```bash
/user:ultrathink-interactive "optimize database performance for high-traffic application"
# Interactive questions lead to targeted solution with pattern learning
```

### Example 3: Process Improvement
```bash
/user:ultrathink-interactive "improve code review process for distributed team"
# Refinement captures team dynamics, ULTRATHINK provides systematic approach
```

## Configuration Options

```javascript
const config = {
  // Refinement settings
  refinement: {
    targetConfidence: 40,
    maxIterations: 10,
    questionStyle: 'detailed'
  },
  
  // ULTRATHINK settings
  ultrathink: {
    autoSelectVersion: true,
    preferredVersion: null,  // or 'pure-xml', 'hybrid-mcp', 'full-mcp'
    interactiveMode: true
  },
  
  // Visual settings
  visual: {
    useEmojis: true,
    progressBars: true,
    animations: true
  },
  
  // Persistence
  persistence: {
    saveSession: true,
    capturePatterns: true,
    trackMetrics: true
  }
}
```

## Benefits of Integration

1. **Progressive Understanding**: Start simple, build complexity gradually
2. **Rich Visual Feedback**: See progress throughout entire journey
3. **One-at-a-Time Questions**: Prevent cognitive overload
4. **Deep Analysis**: Full ULTRATHINK capability when needed
5. **Pattern Learning**: Continuous improvement across sessions
6. **Resumable Sessions**: Can pause and continue later
7. **Adaptive Complexity**: Automatically selects appropriate depth

## Success Metrics

- Questions presented individually with context ✅
- Visual progress throughout all phases ✅
- Seamless transition between systems ✅
- Pattern learning integrated ✅
- Session persistence enabled ✅
- Confidence progression: 0% → 40% → 85% → 90% → 95% ✅