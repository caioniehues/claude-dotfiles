# ADHD Hyperfocus Guardian

Intelligent hyperfocus management that maximizes productivity while preventing burnout through pattern-based boundaries and structured breaks.

## Core Features  
- Sets healthy time boundaries (90-120 minutes max)
- Creates comprehensive exit notes before starting
- Enforces break reminders at optimal intervals
- Captures session patterns for learning
- Prevents hyperfocus exhaustion

## Usage
```
/adhd-hyperfocus-guardian [task/project]
```

## Implementation

```xml
<command>
<name>adhd-hyperfocus-guardian</name>
<description>Manage hyperfocus sessions for maximum productivity without burnout</description>
<parameter>focus_target</parameter>

<initialization>
## 🎯 Hyperfocus Guardian Activated

Preparing a powerful but sustainable hyperfocus session...

**Focus Target**: ${focus_target}

Setting up boundaries to harness your hyperfocus safely...
</initialization>

<pattern_check>
## Step 1: Analyzing Your Hyperfocus Patterns

```javascript
// Load your hyperfocus history
const hyperfocusPatterns = await mcp__basic-memory__search_notes("hyperfocus session deep work")
const burnoutIncidents = await mcp__basic-memory__search_notes("burnout exhaustion crashed")
const optimalSessions = await mcp__basic-memory__search_notes("hyperfocus success productive flow")

// Calculate optimal parameters
const avgProductiveLength = calculateAvgLength(optimalSessions) || 90 // minutes
const maxSafeLength = calculateMaxSafe(burnoutIncidents) || 120 // minutes
const optimalBreakLength = calculateBreakNeeds(patterns) || 15 // minutes
```

### Your Hyperfocus Profile
- Average productive session: ${avgProductiveLength} minutes
- Point of diminishing returns: ${diminishingPoint} minutes
- Maximum safe duration: ${maxSafeLength} minutes
- Recovery time needed: ${recoveryTime} minutes
- Success rate with boundaries: ${successRate}%

### Recent Hyperfocus Sessions
${recentSessions.map(session => 
  `- ${session.date}: ${session.duration} min - ${session.outcome}`
).join('\n')}
</pattern_check>

<pre_hyperfocus_setup>
## Step 2: Pre-Hyperfocus Brain Dump

Before we dive deep, let's capture your current state so you can return safely:

### 🧠 Current Context Capture
```markdown
## Context Snapshot - ${timestamp}

### What I Was Doing Before
${currentContext}

### Open Loops to Remember
1. ${openLoop1}
2. ${openLoop2}
3. ${openLoop3}

### Things to NOT Forget
- ${important1}
- ${important2}

### Where to Resume After
- File: ${currentFile}
- Line/Section: ${currentLocation}
- Next action: ${nextAction}
```

### 📝 Exit Notes (Your Future Self Will Thank You)
```markdown
## Hyperfocus Exit Notes - ${focus_target}

### Starting Point
- Objective: ${objective}
- Success looks like: ${successCriteria}
- Must stop by: ${stopTime}

### If Not Finished
- Save work to: ${saveLocation}
- Key progress markers: ${progressMarkers}
- Next steps would be: ${nextSteps}

### Re-entry Instructions
- Open: ${filesToOpen}
- Read: ${contextToReview}
- Continue from: ${continuationPoint}
```

Saving context to Basic Memory...
```javascript
await mcp__basic-memory__write_note({
  title: `Hyperfocus Entry - ${focus_target} - ${timestamp}`,
  folder: "life-os/hyperfocus-sessions",
  content: contextSnapshot
})
```
</pre_hyperfocus_setup>

<hyperfocus_configuration>
## Step 3: Configuring Your Hyperfocus Session

### ⏱️ Session Parameters
Based on your patterns and current context:

**Recommended Session**: ${recommendedDuration} minutes
- Work Block: ${workBlock} minutes
- Warning at: ${warningTime} minutes
- Hard Stop: ${hardStop} minutes
- Minimum Break After: ${breakLength} minutes

### 🎯 Session Structure
```
[0-5 min] 🚀 LAUNCH PHASE
- Clear all distractions
- Set physical timer
- Start focus music
- Final bathroom/water check

[5-${warmupEnd} min] 🔥 WARMUP
- Review objectives
- Load context
- Build momentum

[${warmupEnd}-${peakEnd} min] ⚡ PEAK PERFORMANCE
- Deep focus work
- No interruptions
- Flow state

[${peakEnd}-${cooldownStart} min] 📈 SUSTAINED FOCUS
- Maintaining productivity
- Watch for fatigue signs

[${cooldownStart}-${sessionEnd} min] 🎯 WRAP-UP
- Start consolidating
- Document progress
- Prepare stopping point

[${sessionEnd}+ min] 🛑 MANDATORY STOP
- Save all work
- Write exit notes
- Begin break
```

### 🚨 Boundary Enforcement
Setting up protection mechanisms:

1. **Timer Setup**
   - Primary: ${primaryTimer} (phone/device)
   - Backup: ${backupTimer} (physical/alternate)
   - Nuclear: ${nuclearOption} (someone to call you)

2. **Break Enforcement**
   ```javascript
   // Automated reminder schedule
   scheduleReminder(${warningTime}, "10 minutes until break - start wrapping up")
   scheduleReminder(${hardStop}, "STOP NOW - Hyperfocus boundary reached")
   scheduleReminder(${hardStop + 5}, "Seriously, stop. Future you needs this break")
   ```

3. **Environmental Boundaries**
   - Close all unrelated tabs/apps
   - Phone in another room or airplane mode
   - Status indicator: "In Deep Work until ${endTime}"
   - Bathroom/snacks prepared
</hyperfocus_configuration>

<hyperfocus_launch>
## Step 4: Launching Hyperfocus Mode

### 🚀 Pre-Flight Checklist
- [ ] Context saved to Basic Memory
- [ ] Exit notes written
- [ ] Timer set for ${recommendedDuration} minutes
- [ ] Backup timer configured
- [ ] Water bottle filled
- [ ] Snacks available
- [ ] Bathroom visited
- [ ] Phone away/silenced
- [ ] Notifications disabled
- [ ] Focus music ready
- [ ] Standing desk adjusted
- [ ] "Do Not Disturb" active

### 🎵 Environment Optimization
Your optimal hyperfocus environment:
- **Sound**: ${soundEnvironment}
- **Tools**: ${toolSetup}
- **Physical**: ${physicalSetup}

### 🧠 Mental Preparation
Quick focus primer:
1. Take 3 deep breaths
2. Visualize your end goal
3. Commit to the boundaries
4. Trust the process

### ⚡ Ignition Sequence
```bash
# Start focus session
echo "Hyperfocus session starting: ${focus_target}"
echo "Duration: ${recommendedDuration} minutes"
echo "Hard stop at: ${stopTime}"

# Set system DND
osascript -e 'tell application "System Events" to set do not disturb to true'

# Start timer
open "timer://${recommendedDuration}m"

# Launch focus music (if configured)
open "https://brain.fm/focus"

# Create session log
echo "Session started: $(date)" >> hyperfocus.log
```

## 🎯 YOU ARE NOW IN HYPERFOCUS MODE

**Remember**:
- Quality over quantity
- Boundaries ensure sustainability
- Breaks multiply productivity
- Your future self will thank you

**When timer goes off**:
- STOP even if mid-sentence
- Save your work
- Take the full break
- Run `/adhd-hyperfocus-complete` to capture patterns
</hyperfocus_launch>

<break_protocol>
## Step 5: Break Protocol (Activates at Timer)

### 🛑 Mandatory Stop Sequence
When your timer goes off:

1. **Immediate Actions** (2 minutes)
   - Save all work (Cmd+S everywhere)
   - Write one sentence about where you are
   - Close laptop/step away from desk

2. **Physical Reset** (5 minutes)
   - Stand and stretch
   - Walk to another room
   - Hydrate (full glass of water)
   - Look at something distant (20-20-20 rule)

3. **Mental Reset** (5-8 minutes)
   - No screens
   - No thinking about the task
   - Light movement or breathing
   - Celebrate what you accomplished

### 📊 Quick Capture (Before You Forget)
```markdown
## Hyperfocus Session Complete

### Session Stats
- Duration: ${actualDuration} minutes
- Planned: ${recommendedDuration} minutes
- Productivity: [1-10] ___
- Energy Before: [1-10] ___
- Energy After: [1-10] ___

### Accomplishments
- ${accomplishment1}
- ${accomplishment2}
- ${accomplishment3}

### State at Stop
- Natural stopping point? Y/N
- Could continue? Y/N
- Need longer break? Y/N

### For Next Session
- Continue from: ___
- Time needed: ___
- Energy required: ___
```
</break_protocol>

<pattern_capture>
## Step 6: Pattern Capture (Post-Session)

### 📈 Session Analytics
Automatically captured for learning:

```javascript
const sessionData = {
  task: "${focus_target}",
  date: "${sessionDate}",
  planned_duration: ${recommendedDuration},
  actual_duration: ${actualDuration},
  productivity_score: ${productivityScore},
  energy_before: ${energyBefore},
  energy_after: ${energyAfter},
  completed_objectives: ${completedObjectives},
  boundary_respected: ${boundaryRespected},
  break_taken: ${breakTaken},
  recovery_time: ${recoveryTime},
  would_repeat: ${wouldRepeat}
}

// Save to Basic Memory
await mcp__basic-memory__write_note({
  title: `Hyperfocus Pattern - ${focus_target} - ${timestamp}`,
  folder: "life-os/hyperfocus-patterns",
  content: JSON.stringify(sessionData),
  tags: ["hyperfocus", "deep-work", "pattern"]
})

// Update your optimal parameters
if (sessionData.productivity_score >= 8) {
  updateOptimalDuration(sessionData.actual_duration)
}
if (sessionData.energy_after < 3) {
  reduceFutureDuration(10) // Shorten by 10 minutes
}
```

### 🔄 Pattern Insights
Based on this session:
- Optimal duration trending: ${durationTrend}
- Best time of day: ${bestTimePattern}
- Recovery need: ${recoveryPattern}
- Productivity correlation: ${productivityCorrelation}
</pattern_capture>

<next_session_planning>
## Step 7: Planning Next Hyperfocus

### 📅 Next Session Recommendations
Based on today's session:

- **Minimum Rest Before Next**: ${minimumRest} hours
- **Optimal Next Session Time**: ${optimalNextTime}
- **Recommended Duration**: ${nextDuration} minutes
- **Energy Investment**: ${energyInvestment}

### 🔄 Continuation Planning
If task not complete:
```markdown
## Next Hyperfocus Session Plan

### Resume Point
- File: ${resumeFile}
- Section: ${resumeSection}
- Context: ${contextNeeded}

### Objectives
1. ${nextObjective1}
2. ${nextObjective2}
3. ${nextObjective3}

### Time Estimate
- Remaining work: ${remainingEstimate} minutes
- Sessions needed: ${sessionsNeeded}
- Target completion: ${targetCompletion}
```

### 💡 Optimization Suggestions
Based on your patterns:
${optimizationSuggestions}
</next_session_planning>

<final_guidance>
## ✅ Hyperfocus Guardian Complete

### 🏆 Session Summary
- **Focus**: ${focus_target}
- **Duration**: ${actualDuration} minutes
- **Productivity**: ${productivityScore}/10
- **Boundaries**: ${boundaryStatus}
- **Pattern Captured**: ✓

### 💪 Hyperfocus Mastery Progress
- Sessions with boundaries: ${boundedSessions}
- Average productivity: ${avgProductivity}
- Burnout incidents: ${burnoutCount} (decreasing!)
- Optimal duration found: ${currentOptimal} minutes

### 🎯 Key Takeaways
1. **Boundaries Enable Sustainability** - Short breaks multiply long-term output
2. **Exit Notes Save Context** - Your future self always knows where to resume
3. **Patterns Improve Predictions** - Each session makes the next one better
4. **Quality Over Quantity** - 90 focused minutes > 180 exhausted minutes

### 🔄 Related Commands
- `/adhd-context-switch` - If you need to change tasks
- `/adhd-evening-reflect` - Capture daily patterns
- `/adhd-task-breakdown` - For next task planning

**Remember**: Hyperfocus is your superpower, but like any superpower, it needs responsible use. The Guardian ensures you can hyperfocus every day, not just on good days!

See you next session! 🚀
</final_guidance>

</command>
```

## Key Features

1. **Pattern-Based Boundaries**
   - Learns your optimal session length
   - Adjusts based on success/burnout history
   - Personalizes break requirements

2. **Context Preservation**
   - Complete brain dump before starting
   - Exit notes for seamless resume
   - State capture to Basic Memory

3. **Boundary Enforcement**
   - Multiple timer systems
   - Progressive warnings
   - Mandatory stop protocols

4. **Session Analytics**
   - Productivity scoring
   - Energy tracking
   - Pattern recognition
   - Optimization suggestions

5. **Burnout Prevention**
   - Maximum duration limits
   - Required break enforcement
   - Recovery time calculation
   - Next session planning

## Benefits
- Sustainable daily hyperfocus
- Eliminated burnout cycles
- Improved session quality
- Better work-life balance
- Continuous optimization