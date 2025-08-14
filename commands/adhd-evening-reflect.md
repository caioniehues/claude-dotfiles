# ADHD Evening Reflection

Intelligent evening reflection that captures patterns, updates predictions, and prepares tomorrow's plan based on today's reality.

## Core Features
- Automatic pattern extraction from daily activities
- Time multiplier refinement based on actual vs estimated
- Energy correlation analysis
- Blocker and solution documentation
- Tomorrow's plan generation

## Usage
```
/adhd-evening-reflect
```

## Implementation

```xml
<command>
<name>adhd-evening-reflect</name>
<description>Evening reflection with pattern capture and intelligent planning for tomorrow</description>

<initialization>
## 🌙 ADHD Evening Reflection

Time to capture today's learnings and prepare for tomorrow's success...

Loading today's data and patterns...
</initialization>

<daily_data_load>
## Step 1: Loading Today's Data

```javascript
// Load morning predictions
const morningPredictions = await mcp__basic-memory__search_notes(`Morning Predictions - ${today}`)
const dailyNote = await Read(`🧠 Life-OS/📅 Daily/${year}/${today}.md`)

// Extract actual results
const actualData = {
  tasksCompleted: extractCompleted(dailyNote),
  tasksPlanned: morningPredictions.plannedTasks,
  energyActual: {
    morning: prompt("Actual morning energy (1-10):"),
    afternoon: prompt("Actual afternoon energy (1-10):"),
    evening: prompt("Actual evening energy (1-10):")
  },
  energyPredicted: morningPredictions.energyPredictions,
  timeEstimates: extractTimeEstimates(dailyNote),
  contextSwitches: await mcp__basic-memory__search_notes(`context-switch date:${today}`)
}
```

### 📊 Today's Overview
- **Tasks Completed**: ${actualData.tasksCompleted.length} / ${actualData.tasksPlanned}
- **Completion Rate**: ${completionRate}%
- **Energy Accuracy**: ${energyAccuracy}%
- **Time Estimate Accuracy**: ${timeAccuracy}%
- **Context Switches**: ${actualData.contextSwitches.length}
</daily_data_load>

<task_pattern_analysis>
## Step 2: Task Pattern Analysis

### ⏱️ Time Estimation Patterns
Analyzing your estimates vs reality:

| Task | Estimated | Actual | Multiplier | Learning |
|------|-----------|--------|------------|----------|
${tasks.map(task => 
  `| ${task.name} | ${task.estimated} | ${task.actual} | ${task.multiplier}x | ${task.learning} |`
).join('\n')}

### 🎯 Your Personal Multipliers (Updated)
Based on today's data:
- **Coding Tasks**: ${codingMultiplier}x (was ${oldCodingMultiplier}x)
- **Documentation**: ${docMultiplier}x (was ${oldDocMultiplier}x)
- **Meetings**: ${meetingMultiplier}x (was ${oldMeetingMultiplier}x)
- **Admin Work**: ${adminMultiplier}x (was ${oldAdminMultiplier}x)
- **Creative Work**: ${creativeMultiplier}x (was ${oldCreativeMultiplier}x)

### 💡 Key Insights
- Most underestimated: ${mostUnderestimated}
- Most overestimated: ${mostOverestimated}
- Sweet spot tasks: ${sweetSpotTasks}
</task_pattern_analysis>

<energy_pattern_analysis>
## Step 3: Energy Pattern Analysis

### 🔋 Energy Predictions vs Reality

```
Morning:   Predicted ${predictedMorning} → Actual ${actualMorning} ${morningDelta}
Afternoon: Predicted ${predictedAfternoon} → Actual ${actualAfternoon} ${afternoonDelta}
Evening:   Predicted ${predictedEvening} → Actual ${actualEvening} ${eveningDelta}
```

### 📈 Energy-Productivity Correlation
Based on today:
- High energy tasks completed: ${highEnergyCompletion}%
- Low energy tasks completed: ${lowEnergyCompletion}%
- Mismatched tasks (wrong energy): ${mismatchedTasks}

### 🎯 Energy Optimization Insights
- **Best productivity**: ${bestProductivityTime} with ${bestProductivityEnergy} energy
- **Worst productivity**: ${worstProductivityTime} with ${worstProductivityEnergy} energy
- **Surprise finding**: ${surpriseEnergyFinding}
</energy_pattern_analysis>

<blocker_solution_capture>
## Step 4: Blockers & Solutions

### 🚧 Today's Blockers
What got in your way?

1. **Blocker**: ${blocker1}
   - **Impact**: ${blocker1Impact} minutes lost
   - **Solution Used**: ${blocker1Solution}
   - **Effectiveness**: ${blocker1Effectiveness}
   - **Future Prevention**: ${blocker1Prevention}

2. **Blocker**: ${blocker2}
   - **Impact**: ${blocker2Impact} minutes lost
   - **Solution Used**: ${blocker2Solution}
   - **Effectiveness**: ${blocker2Effectiveness}
   - **Future Prevention**: ${blocker2Prevention}

### ✅ What Worked Well
Success patterns to repeat:

1. **Success**: ${success1}
   - **Why it worked**: ${success1Why}
   - **Conditions**: ${success1Conditions}
   - **Reproducible?**: ${success1Reproducible}

2. **Success**: ${success2}
   - **Why it worked**: ${success2Why}
   - **Conditions**: ${success2Conditions}
   - **Reproducible?**: ${success2Reproducible}

### 💡 Task Paralysis Incidents
Did you experience task paralysis today?
${paralysisIncidents}

What helped you start:
${paralysisBreakers}
</blocker_solution_capture>

<adhd_symptom_tracking>
## Step 5: ADHD Symptom Tracking

### 🧠 Today's ADHD Experience
Rate today's symptoms (1-10, 10 being most challenging):

- **Time Blindness**: ${timeBlindness}/10
- **Task Paralysis**: ${taskParalysis}/10
- **Hyperfocus Episodes**: ${hyperfocusCount} (${hyperfocusDuration} total minutes)
- **Distractibility**: ${distractibility}/10
- **Impulsivity**: ${impulsivity}/10
- **Working Memory Issues**: ${workingMemory}/10

### 💊 Medication Effectiveness (if applicable)
- **Timing**: ${medTiming}
- **Effectiveness**: ${medEffectiveness}/10
- **Peak Window**: ${peakWindow}
- **Correlation with productivity**: ${medProductivityCorrelation}

### 🌟 ADHD Wins Today
Celebrating ADHD strengths:
- **Creative Solutions**: ${creativeSolutions}
- **Hyperfocus Achievements**: ${hyperfocusAchievements}
- **Pattern Recognition**: ${patternWins}
- **Crisis Performance**: ${crisisPerformance}
</adhd_symptom_tracking>

<pattern_capture_to_memory>
## Step 6: Saving Today's Patterns

```javascript
// Compile today's patterns
const dailyPatterns = {
  date: "${today}",
  metrics: {
    completion_rate: ${completionRate},
    time_accuracy: ${timeAccuracy},
    energy_accuracy: ${energyAccuracy},
    context_switches: ${contextSwitchCount}
  },
  multipliers: {
    coding: ${codingMultiplier},
    documentation: ${docMultiplier},
    meetings: ${meetingMultiplier},
    admin: ${adminMultiplier},
    creative: ${creativeMultiplier}
  },
  energy_patterns: {
    morning: { predicted: ${predictedMorning}, actual: ${actualMorning} },
    afternoon: { predicted: ${predictedAfternoon}, actual: ${actualAfternoon} },
    evening: { predicted: ${predictedEvening}, actual: ${actualEvening} }
  },
  blockers: blockersList,
  successes: successesList,
  adhd_symptoms: symptomData,
  key_learnings: [
    "${learning1}",
    "${learning2}",
    "${learning3}"
  ]
}

// Save to Basic Memory
await mcp__basic-memory__write_note({
  title: `Daily Patterns - ${today}`,
  folder: "life-os/daily-patterns",
  content: JSON.stringify(dailyPatterns),
  tags: ["daily-pattern", "adhd", "reflection"]
})

// Update running averages
await updatePersonalMetrics(dailyPatterns)
```

### ✅ Patterns Captured
- Time multipliers updated
- Energy patterns recorded
- Blocker solutions saved
- Success factors documented
- ADHD symptoms tracked
</pattern_capture_to_memory>

<tomorrow_planning>
## Step 7: Tomorrow's Intelligent Plan

Based on today's patterns and tomorrow's calendar:

### 📅 Tomorrow Preview
- **Day**: ${tomorrowDay}
- **Scheduled Meetings**: ${meetingCount}
- **Available Deep Work Time**: ${deepWorkTime} hours
- **Predicted Energy Pattern**: ${predictedPattern}

### 🎯 Recommended Task Load
Based on your recent capacity:
- **Realistic Task Count**: ${realisticTasks} (not ${theoreticalTasks})
- **High Energy Slots**: ${highEnergySlots}
- **Low Energy Buffers**: ${lowEnergyBuffers}

### 📋 Tomorrow's Priorities (AI Suggested)
Based on today's progress and patterns:

1. **Priority 1**: ${suggestedPriority1}
   - Why: ${priority1Reason}
   - When: ${priority1Time} (${priority1Energy} energy)
   - Estimated time: ${priority1Estimate}

2. **Priority 2**: ${suggestedPriority2}
   - Why: ${priority2Reason}
   - When: ${priority2Time} (${priority2Energy} energy)
   - Estimated time: ${priority2Estimate}

3. **Priority 3**: ${suggestedPriority3}
   - Why: ${priority3Reason}
   - When: ${priority3Time} (${priority3Energy} energy)
   - Estimated time: ${priority3Estimate}

### ⚠️ Proactive Warnings
Based on patterns, watch for:
- ${warning1}
- ${warning2}
- ${warning3}

### 💪 Success Enablers
Set these up tonight:
- ${enabler1}
- ${enabler2}
- ${enabler3}
</tomorrow_planning>

<daily_note_update>
## Step 8: Updating Daily Note

Completing today's daily note with reflection:

```markdown
## 🌙 Evening Reflection - ${timestamp}

### 📊 Day Stats
- Tasks Completed: ${tasksCompleted} / ${tasksPlanned}
- Focus Time: ${focusTime} hours
- Context Switches: ${contextSwitches}
- Energy Average: ${avgEnergy}/10

### 💡 Key Learnings
1. ${learning1}
2. ${learning2}
3. ${learning3}

### 🎯 Multiplier Updates
- New coding multiplier: ${codingMultiplier}x
- New doc multiplier: ${docMultiplier}x
- New meeting multiplier: ${meetingMultiplier}x

### 🚀 Tomorrow's Focus
1. ${tomorrowFocus1}
2. ${tomorrowFocus2}
3. ${tomorrowFocus3}

### 💭 Gratitude
${gratitude}

### 🧠 ADHD Notes
- What helped today: ${whatHelped}
- What to adjust: ${whatToAdjust}
- Energy pattern noticed: ${energyPattern}

---
*Reflection captured to Basic Memory for continuous learning*
```

Saving updates to daily note...
</daily_note_update>

<weekly_trend_analysis>
## Step 9: Weekly Trend Analysis

### 📈 This Week So Far
Looking at the bigger picture:

| Day | Completion | Energy Accuracy | Time Accuracy | Pattern |
|-----|------------|-----------------|---------------|---------|
${weekData.map(day => 
  `| ${day.name} | ${day.completion}% | ${day.energyAcc}% | ${day.timeAcc}% | ${day.pattern} |`
).join('\n')}

### 🎯 Weekly Improvements
- Time estimation: ${weekTimeImprovement}% better
- Energy prediction: ${weekEnergyImprovement}% better
- Task completion: ${weekCompletionImprovement}% better

### 🔄 Emerging Patterns
Based on this week's data:
- ${emergingPattern1}
- ${emergingPattern2}
- ${emergingPattern3}
</weekly_trend_analysis>

<final_summary>
## ✅ Evening Reflection Complete!

### 🏆 Today's Summary
- **Overall Performance**: ${overallScore}/10
- **ADHD Management**: ${adhdScore}/10
- **Pattern Learning**: ${learningScore}/10
- **Tomorrow Prepared**: ✓

### 📊 Your Progress
**Accuracy Improvements**:
- Time estimates: ${timeAccuracyTrend} 📈
- Energy predictions: ${energyAccuracyTrend} 📈
- Task completion: ${completionTrend} 📈

**Personal Records**:
- Best completion rate: ${bestCompletion}% on ${bestDay}
- Most accurate estimates: ${bestAccuracy}% on ${bestAccuracyDay}
- Longest streak: ${longestStreak} days

### 🎯 Tomorrow's Game Plan
1. **First Task**: ${firstTask} (5-min starter ready)
2. **Peak Hours**: ${peakHours} for deep work
3. **Energy Dips**: ${energyDips} for admin/easy tasks
4. **Hard Stop**: ${hardStop} for end of day

### 💤 Wind-Down Recommendations
Based on tomorrow's needs:
- Suggested bedtime: ${suggestedBedtime}
- Prep tonight: ${prepTonight}
- Morning routine: Start at ${morningStart}

### 🤖 AI Learning Activated
Today's patterns will improve:
- Tomorrow's time estimates
- Energy predictions
- Task recommendations
- Blocker warnings

### 🔄 Related Commands
- `/adhd-morning-assistant` - Ready for tomorrow morning
- `/adhd-weekly-review` - Run on Friday/Sunday
- `/adhd-pattern-insights` - See your trends

**Great job completing today's reflection! Your system is ${learningRate}% smarter than yesterday.**

Sweet dreams and see you tomorrow! 🌙
</final_summary>

</command>
```

## Key Features

1. **Comprehensive Pattern Capture**
   - Time estimation accuracy tracking
   - Energy prediction validation
   - Blocker documentation
   - Success factor identification

2. **Intelligent Learning**
   - Multiplier refinement
   - Pattern recognition
   - Trend analysis
   - Predictive improvements

3. **ADHD-Specific Tracking**
   - Symptom monitoring
   - Medication effectiveness
   - Strategy success rates
   - Strength celebration

4. **Tomorrow Preparation**
   - AI-generated priorities
   - Energy-based scheduling
   - Proactive warnings
   - Success enabler setup

5. **Continuous Improvement**
   - Weekly trend analysis
   - Progress visualization
   - Personal records
   - System optimization

## Benefits
- Continuous learning from daily patterns
- Improved predictions over time
- Reduced planning time
- Better self-awareness
- Celebrated ADHD strengths