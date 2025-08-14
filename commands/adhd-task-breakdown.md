# ADHD Task Breakdown

Intelligent task decomposition using the TASTE method with personalized ADHD accommodations and pattern-based time estimates.

## Core Features
- Automatic TASTE method application (20-minute chunks)
- Spiciness rating for engagement level
- Personalized time multipliers from your patterns
- 5-minute starter tasks for paralysis prevention
- Links to similar completed tasks

## Usage
```
/adhd-task-breakdown [task description]
```

## Implementation

```xml
<command>
<name>adhd-task-breakdown</name>
<description>Break down overwhelming tasks into ADHD-friendly chunks with realistic time estimates</description>
<parameter>task_description</parameter>

<initialization>
## 🎯 ADHD Task Breakdown Assistant

Analyzing your task and creating an ADHD-optimized breakdown...

**Task**: ${task_description}

Loading your patterns to create a personalized breakdown...
</initialization>

<pattern_analysis>
## Step 1: Pattern Analysis

```javascript
// Search for similar tasks in your history
const similarTasks = await mcp__basic-memory__search_notes(`task: ${task_description}`)
const taskPatterns = await mcp__basic-memory__search_notes("type:task-pattern category:${detectCategory(task_description)}")

// Calculate your personal multipliers
const timeMultiplier = calculatePersonalMultiplier(taskPatterns) || 1.5 // Default ADHD multiplier
const contextSwitchOverhead = 0.25 // 25% additional time for context switching
```

### Your Personal Patterns
- Similar tasks found: ${similarTasks.length}
- Average completion time for similar: ${avgCompletionTime}
- Your multiplier for this type: ${timeMultiplier}x
- Success rate with this approach: ${successRate}%
</pattern_analysis>

<task_assessment>
## Step 2: Task Assessment

### 🌶️ Spiciness Rating (Engagement Level)
${determineSpiciness(task_description)}

- 🌶️ **Mild** (Routine): Low engagement, high automation potential
- 🌶️🌶️ **Medium** (Familiar): Some interest, moderate challenge
- 🌶️🌶️🌶️ **Hot** (Engaging): New elements, learning opportunity
- 🌶️🌶️🌶️🌶️ **Extra Hot** (Exciting): High novelty, creative challenge
- 🌶️🌶️🌶️🌶️🌶️ **Inferno** (Hyperfocus Risk): Maximum engagement, time boundaries critical

**Your Task**: ${spiciness} - ${spicyDescription}

### ⚡ Energy Requirement
${determineEnergy(task_description)}

- 🔥 **High Energy**: Complex problem-solving, creative work, learning
- 💪 **Medium Energy**: Standard implementation, familiar patterns
- 🔋 **Low Energy**: Routine, administrative, review tasks

**Your Task**: ${energyLevel} - ${energyDescription}

### 🧠 Cognitive Load
${determineCognitiveLoad(task_description)}

- 🧠 **Heavy**: Architecture, design, complex debugging
- 🎯 **Moderate**: Implementation, testing, documentation
- 🌊 **Light**: Code reviews, updates, simple fixes

**Your Task**: ${cognitiveLoad} - ${cognitiveDescription}
</task_assessment>

<taste_breakdown>
## Step 3: TASTE Method Breakdown

**T**imed - **A**ctionable - **S**pecific - **T**iny - **E**nergizing

### 📊 Time Estimation
Base estimate: ${baseEstimate} minutes
× ADHD multiplier (${timeMultiplier}): ${baseEstimate * timeMultiplier} minutes
× Perfectionism factor (1.3): ${baseEstimate * timeMultiplier * 1.3} minutes
× Task switching (1.25): ${baseEstimate * timeMultiplier * 1.3 * 1.25} minutes
**Realistic Total**: ${realisticTotal} minutes (${formatHours(realisticTotal)})

### 🔨 Task Chunks (20-minute maximum)

${generateTasteChunks(task_description, realisticTotal)}

#### 🚀 5-Minute Starter (Beat Task Paralysis)
**Just do this**: "${generateStarter(task_description)}"
- No perfection required
- Just get something on the screen
- Momentum will build naturally

#### Chunk 1: ${chunk1.title} ⏱️ 20 minutes
**Action**: ${chunk1.action}
**Specific outcome**: ${chunk1.outcome}
**Energy level**: ${chunk1.energy}
**Done when**: ${chunk1.completion}

#### Chunk 2: ${chunk2.title} ⏱️ 20 minutes
**Action**: ${chunk2.action}
**Specific outcome**: ${chunk2.outcome}
**Energy level**: ${chunk2.energy}
**Done when**: ${chunk2.completion}

#### Chunk 3: ${chunk3.title} ⏱️ 20 minutes
**Action**: ${chunk3.action}
**Specific outcome**: ${chunk3.outcome}
**Energy level**: ${chunk3.energy}
**Done when**: ${chunk3.completion}

[Additional chunks as needed...]

#### 🎯 Integration & Polish ⏱️ 15 minutes
**Action**: Review, test, and refine
**Specific outcome**: Working solution
**Done when**: Tests pass / Requirements met
</taste_breakdown>

<environment_optimization>
## Step 4: Environment Setup for Success

Based on your patterns for ${taskCategory} tasks:

### 🎵 Optimal Environment
- **Noise Level**: ${optimalNoise}
- **Music/Focus**: ${musicRecommendation}
- **Tools Setup**: ${toolsNeeded}
- **Physical Space**: ${spaceSetup}

### 🍅 Work Session Structure
For ${spiciness} tasks, your optimal pattern:
- **Session Length**: ${sessionLength} minutes
- **Break Length**: ${breakLength} minutes
- **Max Sessions Before Long Break**: ${maxSessions}

### 🚧 Common Blockers & Solutions
Based on similar tasks:
${blockersList}

1. **${blocker1.name}**
   - Likelihood: ${blocker1.likelihood}
   - Prevention: ${blocker1.prevention}
   - If occurs: ${blocker1.solution}

2. **${blocker2.name}**
   - Likelihood: ${blocker2.likelihood}
   - Prevention: ${blocker2.prevention}
   - If occurs: ${blocker2.solution}
</environment_optimization>

<similar_patterns>
## Step 5: Learning from Similar Tasks

### 📚 Similar Completed Tasks
${similarTasksList}

#### Most Relevant: "${similarTask1.title}"
- Estimated: ${similarTask1.estimated} min
- Actual: ${similarTask1.actual} min
- Multiplier was: ${similarTask1.multiplier}x
- What worked: ${similarTask1.success}
- What didn't: ${similarTask1.failure}
- [View Pattern](obsidian://open?vault=obsidian-second-brain&file=${similarTask1.path})

### 💡 Success Patterns for This Type
Based on your history:
- Best time of day: ${bestTimeOfDay}
- Success rate morning vs afternoon: ${morningVsAfternoon}
- Average number of chunks: ${avgChunks}
- Typical total time: ${typicalTime}
</similar_patterns>

<execution_plan>
## Step 6: Execution Plan

### 📋 Task Creation
Creating task in your Life-OS system:

```markdown
---
title: ${task_description}
type: task
status: planned
spiciness: ${spiciness}
energy_required: ${energyLevel}
cognitive_load: ${cognitiveLoad}
estimated_minutes: ${realisticTotal}
adhd_multiplier: ${timeMultiplier}
chunks: ${chunkCount}
created: ${timestamp}
tags: [adhd-breakdown, ${taskCategory}]
---

# ${task_description}

## 🎯 TASTE Breakdown
${chunksList}

## 🚀 5-Minute Starter
"${generateStarter(task_description)}"

## ⏱️ Time Tracking
- [ ] Chunk 1: Planned 20 min | Actual: ___
- [ ] Chunk 2: Planned 20 min | Actual: ___
- [ ] Chunk 3: Planned 20 min | Actual: ___
- [ ] Integration: Planned 15 min | Actual: ___

**Total Planned**: ${realisticTotal} min
**Total Actual**: ___

## 📝 Notes
- Energy at start: ___
- Energy at end: ___
- Blockers encountered: ___
- What worked well: ___
- What to improve: ___

## 🔄 Pattern Capture
[To be filled after completion for Basic Memory]
```

### 🎬 Ready to Start?

1. **Set up environment** (2 min)
   - ${envSetup1}
   - ${envSetup2}
   - ${envSetup3}

2. **Start with 5-minute starter**
   - Set timer for 5 minutes
   - Do "${generateStarter(task_description)}"
   - No perfection, just action

3. **Continue with Chunk 1**
   - Natural momentum from starter
   - 20-minute timer set
   - Clear completion criteria

4. **Take prescribed break**
   - Stand and stretch
   - Hydrate
   - Quick win celebration

5. **Repeat for remaining chunks**
</execution_plan>

<memory_integration>
## Step 7: Pattern Capture Setup

Preparing to learn from this task:

```javascript
// Create pattern template for later capture
const patternTemplate = {
  task: "${task_description}",
  category: "${taskCategory}",
  spiciness: "${spiciness}",
  energy_required: "${energyLevel}",
  estimated_minutes: ${realisticTotal},
  multiplier_used: ${timeMultiplier},
  chunks_planned: ${chunkCount},
  breakdown_timestamp: "${timestamp}",
  actual_results: "TO_BE_FILLED"
}

// Save to Basic Memory for comparison
await mcp__basic-memory__write_note({
  title: `Task Breakdown - ${task_description} - ${timestamp}`,
  folder: "life-os/task-breakdowns",
  content: JSON.stringify(patternTemplate)
})
```

After completion, I'll help you capture:
- Actual time per chunk
- Which estimates were accurate
- Energy levels throughout
- Blockers encountered
- Success factors
- Refined multiplier for next time
</memory_integration>

<final_summary>
## ✅ Your Task is Ready!

### 🎯 Quick Reference
**Task**: ${task_description}
**Realistic Time**: ${formatHours(realisticTotal)}
**Chunks**: ${chunkCount} × 20 minutes
**Spiciness**: ${spiciness}
**Energy Needed**: ${energyLevel}

### 🚀 First Action (Do Now!)
> "${generateStarter(task_description)}"

Set a 5-minute timer and just start. Perfection not required!

### 💡 Key Success Factors
1. **Start imperfectly** - The 5-minute starter breaks paralysis
2. **Honor the chunks** - 20 minutes max, then break
3. **Track reality** - Note actual times for better future estimates
4. **Celebrate progress** - Each chunk is a win

### 🔄 Related Commands
- `/adhd-hyperfocus-guardian` - For deep work sessions
- `/adhd-context-switch` - If you need to switch tasks
- `/adhd-evening-reflect` - Capture patterns after completion

**Remember**: This breakdown is based on YOUR patterns, not generic advice. The more you use it, the smarter it gets!

Type `/adhd-paralysis-break` if you get stuck!
</final_summary>

</command>
```

## Key Features

1. **TASTE Method Implementation**
   - Every task broken into 20-minute maximum chunks
   - Clear, actionable, specific outcomes
   - Energy-matched to your patterns

2. **Spiciness Rating System**
   - 🌶️ to 🌶️🌶️🌶️🌶️🌶️ scale
   - Helps match tasks to current mood
   - Prevents boredom and overwhelm

3. **Realistic Time Estimation**
   - Your personal multiplier (not generic)
   - Accounts for perfectionism
   - Includes task-switching overhead

4. **Task Paralysis Prevention**
   - 5-minute starter for every task
   - "Just do this" instruction
   - Momentum-building approach

5. **Pattern Learning**
   - Compares to similar past tasks
   - Refines estimates over time
   - Captures success factors

## Integration
- Works with Basic Memory for pattern storage
- Creates tasks in Life-OS structure
- Links to similar completed tasks
- Feeds data to morning assistant