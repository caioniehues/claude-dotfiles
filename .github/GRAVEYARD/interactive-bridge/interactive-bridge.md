# Interactive Bridge Component

<component>
Bridge between Interactive Refinement and ULTRATHINK systems for seamless question conversion and state management
</component>

## Core Functions

### Question Conversion

<question_converter>
```javascript
/**
 * Converts ULTRATHINK batch questions to interactive one-at-a-time format
 */
const convertToInteractiveQuestions = (ultrathinkQuestions, context) => {
  return ultrathinkQuestions.map((question, index) => {
    return {
      id: generateQuestionId(context.phase, context.iteration, index),
      text: question.text || question,
      context: enrichQuestionContext(question, context),
      rationale: question.rationale || generateRationale(question, context),
      impact: question.impact || assessImpact(question, context),
      default: question.default || suggestDefault(question, context),
      options: question.options || null,
      metadata: {
        source: 'ultrathink',
        phase: context.phase,
        iteration: context.iteration,
        priority: question.priority || calculatePriority(question, context),
        category: question.category || categorizeQuestion(question)
      }
    }
  })
}

/**
 * Enriches question with contextual information
 */
const enrichQuestionContext = (question, context) => {
  const relevantHistory = context.answers
    .filter(a => isRelated(a.question, question))
    .slice(-3)  // Last 3 related answers
  
  const patterns = context.patterns
    .filter(p => p.applicable(question))
    .map(p => p.name)
  
  return {
    description: `Based on your previous answers about ${summarizeContext(relevantHistory)}`,
    relatedPatterns: patterns.length > 0 ? `Similar to patterns: ${patterns.join(', ')}` : null,
    dependencies: question.dependencies || [],
    previousAnswers: relevantHistory.map(h => ({ q: h.question.text, a: h.answer }))
  }
}
```
</question_converter>

### Visual Enhancement

<visual_enhancer>
```javascript
/**
 * Applies Interactive Refinement visual styling to ULTRATHINK outputs
 */
const applyVisualEnhancements = (content, phase, confidence) => {
  const phaseEmoji = getPhaseEmoji(phase)
  const progressBar = generateProgressBar(confidence)
  const phaseColor = getPhaseColor(phase)
  
  return `
${phaseEmoji} ${phase.toUpperCase()} Phase
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${content}

[Progress: ${progressBar} ${confidence}%]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`
}

/**
 * Phase-specific emoji mapping
 */
const getPhaseEmoji = (phase) => {
  const emojiMap = {
    'refinement': '🌱',
    'research': '🌳',
    'planning': '🌲',
    'execution': '🎄',
    'validation': '✅'
  }
  return emojiMap[phase.toLowerCase()] || '🔄'
}

/**
 * Generates visual progress bar
 */
const generateProgressBar = (percentage) => {
  const filled = Math.round(percentage / 10)
  const empty = 10 - filled
  return '█'.repeat(filled) + '░'.repeat(empty)
}

/**
 * Creates animated thinking indicator
 */
const createThinkingAnimation = () => {
  const frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
  let currentFrame = 0
  
  return {
    next: () => frames[currentFrame++ % frames.length],
    full: () => frames.join(' → '),
    reset: () => currentFrame = 0
  }
}
```
</visual_enhancer>

### State Synchronization

<state_synchronizer>
```javascript
/**
 * Synchronizes confidence between Interactive Refinement and ULTRATHINK
 */
const syncConfidence = (refinementConfidence, ultrathinkPhase) => {
  const phaseMapping = {
    'research': { min: 40, max: 85, weight: 0.45 },
    'planning': { min: 60, max: 90, weight: 0.30 },
    'execution': { min: 80, max: 95, weight: 0.25 }
  }
  
  const phase = phaseMapping[ultrathinkPhase]
  if (!phase) return refinementConfidence
  
  // Map refinement confidence to ULTRATHINK phase range
  const phaseProgress = (refinementConfidence - phase.min) / (phase.max - phase.min)
  const adjustedConfidence = phase.min + (phaseProgress * (phase.max - phase.min))
  
  return Math.round(adjustedConfidence)
}

/**
 * Merges context from both systems
 */
const mergeContexts = (refinementContext, ultrathinkContext) => {
  return {
    // From refinement
    initialUnderstanding: refinementContext.keyInsights,
    userPreferences: refinementContext.preferences,
    clarifiedRequirements: refinementContext.requirements,
    
    // From ULTRATHINK
    patterns: ultrathinkContext.patterns || [],
    researchFindings: ultrathinkContext.research || {},
    technicalAnalysis: ultrathinkContext.analysis || {},
    
    // Merged
    answers: [...refinementContext.answers, ...(ultrathinkContext.answers || [])],
    constraints: mergeConstraints(refinementContext.constraints, ultrathinkContext.constraints),
    decisions: mergeDecisions(refinementContext.decisions, ultrathinkContext.decisions),
    
    // Metadata
    totalQuestions: refinementContext.questions + (ultrathinkContext.questions || 0),
    totalIterations: refinementContext.iterations + (ultrathinkContext.iterations || 0),
    sessionId: refinementContext.sessionId,
    timestamp: new Date().toISOString()
  }
}

/**
 * Maintains session continuity across phases
 */
const maintainSessionContinuity = (session, phaseTransition) => {
  const transition = {
    from: phaseTransition.from,
    to: phaseTransition.to,
    timestamp: new Date().toISOString(),
    confidence: phaseTransition.confidence,
    context: phaseTransition.context
  }
  
  session.transitions.push(transition)
  session.currentPhase = phaseTransition.to
  session.lastUpdate = transition.timestamp
  
  // Persist session state
  saveSessionState(session)
  
  return session
}
```
</state_synchronizer>

### Question Flow Management

<question_flow>
```javascript
/**
 * Manages question flow between systems
 */
class InteractiveQuestionFlow {
  constructor(context) {
    this.context = context
    this.questionQueue = []
    this.answeredQuestions = []
    this.currentQuestion = null
    this.confidence = 0
  }
  
  /**
   * Adds questions to the queue
   */
  addQuestions(questions, source = 'unknown') {
    const interactive = convertToInteractiveQuestions(questions, this.context)
    interactive.forEach(q => {
      q.source = source
      this.questionQueue.push(q)
    })
  }
  
  /**
   * Gets next question with visual presentation
   */
  async getNextQuestion() {
    if (this.questionQueue.length === 0) return null
    
    this.currentQuestion = this.questionQueue.shift()
    
    // Apply visual enhancements
    const enhanced = this.enhanceQuestionPresentation(this.currentQuestion)
    
    return enhanced
  }
  
  /**
   * Enhances question with rich visual context
   */
  enhanceQuestionPresentation(question) {
    const questionNumber = this.answeredQuestions.length + 1
    const totalQuestions = this.answeredQuestions.length + this.questionQueue.length + 1
    const progressBar = generateProgressBar(this.confidence)
    
    return `
┌─────────────────────────────────────────────────────┐
│     🤔 ${this.context.phase} Analysis              │
│                                                     │
│     Question ${questionNumber} of ${totalQuestions} │
└─────────────────────────────────────────────────────┘

❓ **${question.text}**

${question.context.description ? `📋 **Context**: ${question.context.description}` : ''}
${question.rationale ? `💡 **Why this matters**: ${question.rationale}` : ''}
${question.impact ? `🎯 **Impact**: ${question.impact}` : ''}
${question.default ? `✨ **Suggestion**: ${question.default}` : ''}

${question.options ? `
Options:
${question.options.map((opt, i) => `  ${i + 1}. ${opt}`).join('\n')}
` : 'Your answer:'}

[Confidence: ${progressBar} ${this.confidence}%]
`
  }
  
  /**
   * Records answer and updates confidence
   */
  recordAnswer(answer) {
    this.answeredQuestions.push({
      question: this.currentQuestion,
      answer: answer,
      timestamp: new Date().toISOString()
    })
    
    this.updateConfidence()
    this.currentQuestion = null
  }
  
  /**
   * Updates confidence based on answers
   */
  updateConfidence() {
    const factors = {
      questionsAnswered: this.answeredQuestions.length * 2,
      clarityScore: this.calculateClarityScore() * 10,
      consistencyScore: this.calculateConsistencyScore() * 5
    }
    
    this.confidence = Math.min(100, Object.values(factors).reduce((a, b) => a + b, 0))
  }
  
  /**
   * Calculates answer clarity score
   */
  calculateClarityScore() {
    const recentAnswers = this.answeredQuestions.slice(-5)
    const clarityIndicators = ['yes', 'no', 'specific', 'clear', 'defined']
    
    let score = 0
    recentAnswers.forEach(qa => {
      if (clarityIndicators.some(indicator => 
        qa.answer.toLowerCase().includes(indicator))) {
        score += 0.2
      }
    })
    
    return Math.min(1, score)
  }
  
  /**
   * Calculates answer consistency score
   */
  calculateConsistencyScore() {
    // Check for contradictions in answers
    const contradictions = this.findContradictions()
    return Math.max(0, 1 - (contradictions.length * 0.2))
  }
  
  /**
   * Finds contradictions in answers
   */
  findContradictions() {
    const contradictions = []
    
    // Simple contradiction detection
    this.answeredQuestions.forEach((qa1, i) => {
      this.answeredQuestions.slice(i + 1).forEach(qa2 => {
        if (this.areContradictory(qa1, qa2)) {
          contradictions.push({ qa1, qa2 })
        }
      })
    })
    
    return contradictions
  }
  
  /**
   * Checks if two answers are contradictory
   */
  areContradictory(qa1, qa2) {
    // Simplified contradiction detection
    if (qa1.question.category === qa2.question.category) {
      if ((qa1.answer === 'yes' && qa2.answer === 'no') ||
          (qa1.answer === 'no' && qa2.answer === 'yes')) {
        return true
      }
    }
    return false
  }
}
```
</question_flow>

### Progress Visualization

<progress_visualization>
```javascript
/**
 * Creates comprehensive progress visualization
 */
const createProgressVisualization = (session) => {
  const phases = ['refinement', 'research', 'planning', 'execution']
  const currentPhaseIndex = phases.indexOf(session.currentPhase)
  
  const visualization = phases.map((phase, index) => {
    const phaseData = session.phases[phase] || {}
    const isComplete = index < currentPhaseIndex
    const isCurrent = index === currentPhaseIndex
    const emoji = getPhaseEmoji(phase)
    const confidence = phaseData.confidence || 0
    
    let status
    if (isComplete) status = '✅ Complete'
    else if (isCurrent) status = '🔄 In Progress'
    else status = '⏳ Pending'
    
    return `${emoji} ${phase.charAt(0).toUpperCase() + phase.slice(1)}: ${generateProgressBar(confidence)} ${confidence}% ${status}`
  }).join('\n')
  
  return `
📊 Overall Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
${visualization}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ Time Elapsed: ${calculateElapsedTime(session.startTime)}
❓ Total Questions: ${session.totalQuestions}
🎯 Current Confidence: ${session.currentConfidence}%
`
}

/**
 * Creates phase transition animation
 */
const createPhaseTransitionAnimation = (fromPhase, toPhase) => {
  const fromEmoji = getPhaseEmoji(fromPhase)
  const toEmoji = getPhaseEmoji(toPhase)
  
  return `
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 PHASE TRANSITION
                 
         ${fromEmoji} ${fromPhase.toUpperCase()}
                      ↓
         ${toEmoji} ${toPhase.toUpperCase()}
         
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`
}
```
</progress_visualization>

### Pattern Integration

<pattern_integration>
```javascript
/**
 * Integrates pattern recognition between systems
 */
const integratePatterns = async (context) => {
  // Search for relevant patterns in Basic Memory
  const patterns = await mcp__basic-memory__search_notes(
    `type:pattern ${context.keywords.join(' OR ')}`
  )
  
  // Match patterns to current context
  const applicablePatterns = patterns.filter(pattern => {
    return calculatePatternRelevance(pattern, context) > 0.7
  })
  
  // Enrich questions with pattern insights
  context.patterns = applicablePatterns.map(pattern => ({
    name: pattern.title,
    description: pattern.content,
    confidence: pattern.metadata?.confidence || 0.8,
    applicable: (question) => isPatternApplicable(pattern, question, context)
  }))
  
  return context
}

/**
 * Calculates pattern relevance score
 */
const calculatePatternRelevance = (pattern, context) => {
  let score = 0
  
  // Keyword matching
  const patternKeywords = extractKeywords(pattern.content)
  const contextKeywords = context.keywords
  const keywordOverlap = calculateOverlap(patternKeywords, contextKeywords)
  score += keywordOverlap * 0.4
  
  // Domain matching
  if (pattern.metadata?.domain === context.domain) {
    score += 0.3
  }
  
  // Complexity matching
  const complexityDiff = Math.abs(
    (pattern.metadata?.complexity || 10) - context.complexity
  )
  score += (1 - complexityDiff / 30) * 0.3
  
  return score
}
```
</pattern_integration>

## Utility Functions

<utilities>
```javascript
/**
 * Generates unique question ID
 */
const generateQuestionId = (phase, iteration, index) => {
  return `${phase}-iter${iteration}-q${index}`
}

/**
 * Calculates question priority
 */
const calculatePriority = (question, context) => {
  let priority = 5  // Default medium
  
  if (question.text.includes('critical') || question.text.includes('must')) {
    priority = 10
  } else if (question.text.includes('optional') || question.text.includes('nice to have')) {
    priority = 3
  }
  
  // Adjust based on phase
  if (context.phase === 'execution') {
    priority += 2
  }
  
  return priority
}

/**
 * Categorizes question type
 */
const categorizeQuestion = (question) => {
  const text = question.text?.toLowerCase() || question.toLowerCase()
  
  if (text.includes('requirement') || text.includes('need')) {
    return 'requirement'
  } else if (text.includes('constraint') || text.includes('limit')) {
    return 'constraint'
  } else if (text.includes('preference') || text.includes('prefer')) {
    return 'preference'
  } else if (text.includes('technical') || text.includes('implementation')) {
    return 'technical'
  } else if (text.includes('risk') || text.includes('concern')) {
    return 'risk'
  }
  
  return 'general'
}

/**
 * Calculates elapsed time
 */
const calculateElapsedTime = (startTime) => {
  const elapsed = Date.now() - new Date(startTime).getTime()
  const minutes = Math.floor(elapsed / 60000)
  const seconds = Math.floor((elapsed % 60000) / 1000)
  
  return `${minutes}m ${seconds}s`
}

/**
 * Merges constraints from different sources
 */
const mergeConstraints = (constraints1, constraints2) => {
  const merged = [...(constraints1 || [])]
  
  (constraints2 || []).forEach(c2 => {
    if (!merged.some(c1 => c1.type === c2.type && c1.value === c2.value)) {
      merged.push(c2)
    }
  })
  
  return merged
}

/**
 * Merges decisions ensuring no conflicts
 */
const mergeDecisions = (decisions1, decisions2) => {
  const merged = [...(decisions1 || [])]
  
  (decisions2 || []).forEach(d2 => {
    const existing = merged.find(d1 => d1.category === d2.category)
    if (existing) {
      // Keep the more recent or higher confidence decision
      if (d2.confidence > existing.confidence) {
        merged[merged.indexOf(existing)] = d2
      }
    } else {
      merged.push(d2)
    }
  })
  
  return merged
}
```
</utilities>

## Export Interface

<exports>
```javascript
// Main exports for use by other commands
module.exports = {
  // Question conversion
  convertToInteractiveQuestions,
  enrichQuestionContext,
  
  // Visual enhancement
  applyVisualEnhancements,
  getPhaseEmoji,
  generateProgressBar,
  createThinkingAnimation,
  
  // State synchronization
  syncConfidence,
  mergeContexts,
  maintainSessionContinuity,
  
  // Question flow
  InteractiveQuestionFlow,
  
  // Progress visualization
  createProgressVisualization,
  createPhaseTransitionAnimation,
  
  // Pattern integration
  integratePatterns,
  calculatePatternRelevance,
  
  // Utilities
  generateQuestionId,
  calculatePriority,
  categorizeQuestion,
  calculateElapsedTime,
  mergeConstraints,
  mergeDecisions
}
```
</exports>