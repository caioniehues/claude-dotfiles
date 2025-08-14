# ADHD Morning Assistant

AI-powered morning planning assistant that learns from your patterns to create realistic, ADHD-optimized daily plans.

## Core Features
- Loads 7-day pattern history from Basic Memory
- Applies personalized ADHD time multipliers
- Matches tasks to predicted energy levels
- Identifies potential blockers proactively
- Creates realistic capacity estimates

## Usage
```
/adhd-morning-assistant
```

## Implementation

```xml
<command>
<name>adhd-morning-assistant</name>
<description>Intelligent ADHD-optimized morning planning with pattern-based predictions</description>

<initialization>
## 🌅 ADHD Morning Assistant Activation

Loading your personalized patterns and preparing today's optimized plan...

### System Check
- Basic Memory: Connecting...
- Pattern Analysis: Initializing...
- Energy Prediction: Calculating...
- Task Optimization: Preparing...
</initialization>

<analysis_phase>
## Step 1: Loading Your Patterns

First, let me load your recent patterns from Basic Memory to understand your unique ADHD profile.

```javascript
// Load 7-day context
const patterns = await mcp__basic-memory__build_context("memory://life-os/*", { timeframe: "7d" })
const taskPatterns = await mcp__basic-memory__search_notes("type:task-pattern", { after_date: "7d ago" })
const energyPatterns = await mcp__basic-memory__search_notes("energy level mood productivity", { after_date: "7d ago" })
```

### Pattern Analysis Results
- Average task completion time multiplier: ${calculateMultiplier()}
- Peak productivity hours: ${identifyPeakHours()}
- Common blockers: ${identifyBlockers()}
- Success enablers: ${identifyEnablers()}
</analysis_phase>

<planning_phase>
## Step 2: Today's Personalized Plan

Based on your patterns, here's your ADHD-optimized plan for today:

### 🔋 Energy Forecast
```
Morning (9-12):   ${energyLevel.morning} - ${taskRecommendation.morning}
Afternoon (1-3):  ${energyLevel.afternoon} - ${taskRecommendation.afternoon}  
Late PM (3-5):    ${energyLevel.latePM} - ${taskRecommendation.latePM}
```

### 📊 Realistic Capacity Calculation
Based on your patterns:
- Theoretical capacity: ${theoreticalTasks} tasks
- ADHD-adjusted capacity: ${adjustedTasks} tasks
- Recommended focus: ${recommendedFocus} tasks
- Buffer for unexpected: 25% time reserved

### 🎯 Priority Stack (TASTE Method)
For each priority, I'll break it down into 20-minute chunks:

#### Priority 1: ${priority1.title}
- Spiciness: ${priority1.spiciness}
- Energy Required: ${priority1.energy}
- Realistic Time: ${priority1.baseTime} × ${personalMultiplier} = ${priority1.realTime} minutes
- TASTE Breakdown:
  1. ${priority1.chunk1} (20 min)
  2. ${priority1.chunk2} (20 min)
  3. ${priority1.chunk3} (20 min)
- Similar past task took: ${findSimilarTask()}

#### Priority 2: ${priority2.title}
[Similar breakdown...]

#### Priority 3: ${priority3.title}
[Similar breakdown...]

### ⚠️ Proactive Blocker Alerts
Based on similar days, watch for:
- ${blocker1}: Mitigation - ${mitigation1}
- ${blocker2}: Mitigation - ${mitigation2}

### 🎯 Task Paralysis Prevention
For each task, here's your 5-minute starter:
- Priority 1: "Just open ${tool} and read the first line"
- Priority 2: "Just create the file and write the title"
- Priority 3: "Just review what you did yesterday"
</planning_phase>

<execution_setup>
## Step 3: Setting Up Your Day

### 🧠 Hyperfocus Windows
Based on your patterns, optimal deep work windows:
- Window 1: ${hyperfocusWindow1} (90 minutes max)
- Window 2: ${hyperfocusWindow2} (90 minutes max)
- Set timers to prevent burnout

### 🔄 Context Switching Plan
Batching similar tasks to reduce switching costs:
- Communication block: ${commBlock}
- Coding block: ${codeBlock}
- Admin block: ${adminBlock}

### 💊 Medication Optimization
- If taking medication, optimal timing for tasks: ${medTiming}
- Peak effectiveness window: ${peakMedWindow}

### 🎵 Environment Setup
Your most productive environment based on patterns:
- Noise level: ${optimalNoise}
- Tool setup: ${toolSetup}
- Physical needs: ${physicalNeeds}
</execution_setup>

<obsidian_integration>
## Step 4: Creating Your Daily Note

Now I'll create today's daily note with all this information:

```markdown
---
date: ${today}
type: adhd-daily-note
energy_morning: predicted_${energyLevel.morning}
energy_afternoon: predicted_${energyLevel.afternoon}
adhd_multiplier: ${personalMultiplier}
realistic_capacity: ${adjustedTasks}
---

# 📅 Daily Note - ${today}

## 🌅 ADHD Morning Plan (AI-Generated)

### 🔋 Energy Forecast
- Morning: ${energyLevel.morning} → Focus on: ${taskRecommendation.morning}
- Afternoon: ${energyLevel.afternoon} → Focus on: ${taskRecommendation.afternoon}
- Evening: ${energyLevel.latePM} → Focus on: ${taskRecommendation.latePM}

### 🎯 Today's Priorities (TASTE Breakdown)
1. ${priority1.full}
2. ${priority2.full}
3. ${priority3.full}

### ⚡ Hyperfocus Sessions
- [ ] Session 1: ${hyperfocusWindow1} - ${hyperfocusTask1}
- [ ] Session 2: ${hyperfocusWindow2} - ${hyperfocusTask2}

### 🚧 Blocker Watch List
${blockerWatchList}

### 📝 Quick Capture
[Space for thoughts throughout the day]

### 🔄 Context Switches Log
[Track switches and state]

## 🌙 Evening Reflection (To Complete Later)
- Actual energy levels: Morning [ ] Afternoon [ ] Evening [ ]
- Tasks completed vs planned: [ ] / ${adjustedTasks}
- Patterns noticed: 
- Tomorrow's focus:
```
</obsidian_integration>

<memory_capture>
## Step 5: Preparing Pattern Capture

Setting up automatic pattern capture for today:

```javascript
// Create pattern capture template
const patternTemplate = {
  date: today,
  predictedCapacity: adjustedTasks,
  energyPredictions: energyLevels,
  multiplierUsed: personalMultiplier,
  actualResults: "TO_BE_FILLED",
  patterns: []
}

// Save to Basic Memory for evening comparison
await mcp__basic-memory__write_note({
  title: `Morning Predictions - ${today}`,
  folder: "life-os/daily-predictions",
  content: JSON.stringify(patternTemplate)
})
```

### Pattern Tracking Activated For:
- Time estimation accuracy
- Energy prediction accuracy
- Blocker predictions
- Task completion rate
- Hyperfocus session effectiveness
</memory_capture>

<final_output>
## ✅ Your ADHD-Optimized Day is Ready!

### 🎯 Quick Summary
- **Realistic Capacity**: ${adjustedTasks} tasks (not ${theoreticalTasks}!)
- **Peak Hours**: ${peakHours}
- **Danger Zone**: ${dangerZone} (schedule breaks/easy tasks)
- **Must-Do #1**: ${mustDo1} (just start with 5 minutes)

### 🚀 First Action (Do This Now)
${firstAction}
- Set a 5-minute timer
- Just begin, imperfectly
- Momentum will build

### 📊 Success Metrics for Today
- ✅ Complete ${adjustedTasks} tasks = Success
- ✅ Take breaks every 90 minutes = Health
- ✅ Capture patterns = Learning
- ✅ Energy match tasks = Optimization

### 🤖 AI Assistant Ready
I'll check in throughout the day to:
- Remind you of breaks
- Help with task paralysis
- Capture patterns
- Adjust plans as needed

**Remember**: Your ADHD brain is wired for innovation and creative problem-solving. Today's plan works WITH your wiring, not against it.

Type `/adhd-task-breakdown [task]` anytime you feel stuck!
Type `/adhd-context-switch` when changing focus!
Type `/adhd-evening-reflect` at day's end!

Let's make today productive AND sustainable! 🚀
</final_output>

<tools>
- mcp__basic-memory__build_context
- mcp__basic-memory__search_notes
- mcp__basic-memory__write_note
- Read
- Write
- Edit
</tools>

<pattern_library>
## Pattern Recognition Rules

### Time Multiplier Calculation
- Base: 1.5x for ADHD
- +0.2x for each context switch
- +0.3x for low energy state
- +0.4x for "boring" tasks
- -0.2x for high interest tasks
- Personal adjustment from historical data

### Energy Prediction Model
- Morning energy based on sleep + yesterday's end
- Afternoon dip typically 2-3pm
- Late afternoon recovery if morning was protected
- Evening energy correlates with day's success

### Task-Energy Matching
- High Energy + High Complexity = Optimal
- Low Energy + Low Complexity = Sustainable
- Mismatch = Higher failure rate

### Blocker Patterns
- Monday: Motivation issues
- Post-meeting: Context switching cost
- Pre-lunch: Hunger distraction
- Late afternoon: Fatigue
- Unplanned interruptions: 25% time loss
</pattern_library>

</command>
```

## Benefits
1. **Personalized Predictions**: Uses YOUR patterns, not generic advice
2. **Realistic Planning**: Accounts for ADHD time blindness
3. **Energy Optimization**: Matches tasks to energy levels
4. **Proactive Support**: Warns about likely blockers
5. **Pattern Learning**: Gets smarter every day

## Integration Points
- Basic Memory for pattern storage
- Obsidian for daily note creation
- Morning Planning Dashboard enhancement
- Evening reflection companion

## Success Metrics
- Time estimation accuracy > 75%
- Task completion rate > 80%
- Energy prediction accuracy > 70%
- Reduced morning planning time < 5 minutes