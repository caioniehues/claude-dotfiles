# CLAUDE.md - Memory-Integrated AI Assistant Configuration

## 🧠 MANDATORY: SESSION INITIALIZATION PROTOCOL

**EVERY SESSION MUST START WITH THESE STEPS:**

### 1. Load Context from Basic Memory
```bash
# ALWAYS run at session start - NO EXCEPTIONS
mcp__basic-memory__build_context "memory://life-os/*" --timeframe "7d" --depth 2
mcp__basic-memory__recent_activity --timeframe "24h"
```

### 2. Check Active Tasks & Patterns
```bash
mcp__basic-memory__search_notes "status:active OR priority:high" --entity-types "task"
mcp__basic-memory__search_notes "type:task-pattern" --after-date "7d ago"
```

### 3. Surface Relevant Insights
- Review recent daily insights for context
- Check task patterns for similar work
- Load project-specific memories

**If Basic Memory is unavailable, note it and proceed with degraded mode**

---

## 💾 CONTINUOUS MEMORY CAPTURE PROTOCOL

### ALWAYS Capture These Events:

#### Task Completion
```bash
# After EVERY task completion
mcp__basic-memory__write_note \
  --title "Task Pattern - [Task Name]" \
  --folder "life-os/task-patterns" \
  --content "[Pattern details with time, approach, blockers]"
```

#### Problem Solutions
```bash
# After solving ANY problem
mcp__basic-memory__write_note \
  --title "Solution - [Problem Description]" \
  --folder "technical/solutions" \
  --content "[Problem, approach, solution, reusable pattern]"
```

#### Daily Session End
```bash
# At the end of EVERY work session
mcp__basic-memory__write_note \
  --title "Session Insights $(date +%Y-%m-%d-%H%M)" \
  --folder "life-os/daily-insights" \
  --content "[Key accomplishments, learnings, patterns observed]"
```

#### Learning Moments
- New tool discovered → Capture usage pattern
- Error encountered → Document solution
- Workflow improved → Save optimization
- Pattern recognized → Store for reuse

---

## 🛠️ TOOL USAGE HIERARCHY

### Priority 1: Basic Memory MCP (ALWAYS FIRST)
**Before doing ANYTHING, check if memory exists:**
```bash
# Search for existing knowledge
mcp__basic-memory__search_notes "[your query]"

# Build context for complex tasks
mcp__basic-memory__build_context "memory://[relevant-path]"

# Save new insights immediately
mcp__basic-memory__write_note --folder "[appropriate-folder]"
```

### Priority 2: Life-OS Integration Tools
- **Daily Planning**: Query task patterns for time estimates
- **Task Creation**: Apply ADHD multipliers from patterns
- **Energy Matching**: Use historical energy-productivity data
- **Review Sessions**: Aggregate insights for summaries

### Priority 3: Development Tools
1. First check Basic Memory for similar code/patterns
2. Then use appropriate development tools
3. Always capture solution patterns back to memory

### Priority 4: Other MCP Tools
- Firecrawl for web research → Save findings to memory
- Sequential thinking for complex problems → Capture reasoning
- Obsidian tools for note management → Sync with Basic Memory

---

## 🔄 AUTOMATED WORKFLOWS

### Starting Any Task
1. **Search Memory First**
   ```bash
   mcp__basic-memory__search_notes "task: [description]"
   ```
2. **Load Similar Patterns**
   ```bash
   mcp__basic-memory__build_context "memory://life-os/task-patterns/*" --max-related 5
   ```
3. **Apply Learned Estimates**
   - Base time × 1.5 (ADHD factor from patterns)
   - Check energy requirements
   - Identify likely blockers

### During Task Execution
1. **Track Approach** - Note methods being used
2. **Monitor Time** - Compare to estimates
3. **Document Blockers** - As they occur
4. **Capture Insights** - Real-time learning

### Completing Any Task
1. **Document Pattern**
   ```bash
   mcp__basic-memory__write_note \
     --title "Pattern - [Task Type]" \
     --folder "life-os/task-patterns" \
     --entity-type "task-pattern"
   ```
2. **Update Estimates** - Refine multipliers
3. **Save Reusable Code/Config** - To appropriate folder
4. **Link Related Patterns** - Build knowledge graph

### Problem Solving Flow
1. **Check Existing Solutions**
   ```bash
   mcp__basic-memory__search_notes "error: [description]" 
   mcp__basic-memory__search_notes "problem: [description]"
   ```
2. **Build Problem Context**
   ```bash
   mcp__basic-memory__build_context "memory://technical/solutions/*"
   ```
3. **Apply Known Patterns** - From similar problems
4. **Document New Solution** - IMMEDIATELY after solving

---

## 📅 LIFE-OS INTEGRATION RULES

### Daily Workflow Integration

#### Morning Planning (MANDATORY)
```bash
# Load yesterday's insights and patterns
mcp__basic-memory__build_context "memory://life-os/daily-insights/*" --timeframe "1d"

# Get task recommendations based on energy
mcp__basic-memory__search_notes "energy:[current-energy] success_score:>=4"
```

#### Task Management
- **Before Creating**: Search for similar tasks
- **Time Estimates**: Apply patterns (base × 1.5 × perfectionism factor)
- **Energy Matching**: Use historical energy-success correlations
- **Spiciness Rating**: Match interest level to engagement needs

#### Evening Reflection (MANDATORY)
```bash
# Capture daily insights
mcp__basic-memory__write_note \
  --title "Daily Insights $(date +%Y-%m-%d)" \
  --folder "life-os/daily-insights" \
  --content "[accomplishments, patterns, learnings, tomorrow-focus]"
```

### ADHD Optimizations (FROM PATTERNS)
- **Time Blindness**: Always use 1.5x multiplier minimum
- **Task Breakdown**: Max 20-minute chunks (TASTE method)
- **Energy Matching**: High-energy tasks in morning
- **Context Switching**: Add 25% overhead between different types
- **Hyperfocus Risk**: Set timers for breaks

### Weekly Reviews
```bash
# Aggregate week's patterns
mcp__basic-memory__recent_activity --timeframe "7d" --type "task-pattern,daily-insight"

# Identify improvement areas
mcp__basic-memory__search_notes "blocker:* OR challenge:*" --after-date "7d ago"
```

---

## 📊 PATTERN RECOGNITION & APPLICATION

### What to Track in Every Pattern
```yaml
pattern:
  name: "Descriptive Pattern Name"
  category: "coding|planning|debugging|writing|research"
  triggers: "What initiates this pattern"
  approach: "Step-by-step method"
  time_actual: "How long it really took"
  time_estimated: "Original estimate"
  energy_required: "high|medium|low"
  success_factors: "What made it work"
  blockers: "What got in the way"
  reusable: true
  adhd_factors:
    - time_multiplier: 1.5
    - break_needed_after: 20
    - hyperfocus_risk: "high|medium|low"
```

### Pattern Application Rules
1. **Similar Task Found** → Apply time multiplier
2. **Same Category** → Use energy requirements
3. **Previous Blocker** → Proactive mitigation
4. **Success Pattern** → Replicate environment

---

## ⚡ QUICK COMMAND REFERENCE

### Essential Basic Memory Commands
```bash
# Start of session
mcp__basic-memory__build_context "memory://life-os/*" --timeframe "7d"

# Search for anything
mcp__basic-memory__search_notes "[query]"

# Save insight
mcp__basic-memory__write_note --title "[Title]" --folder "[folder]"

# Recent activity
mcp__basic-memory__recent_activity --timeframe "24h"

# Get current project info
mcp__basic-memory__get_current_project
```

### Life-OS Specific
```bash
# Morning planning context
basic-memory tool build-context "memory://life-os/daily-insights/*" --timeframe "7d"

# Task pattern search
basic-memory tool search-notes "category:[category] energy:[level]"

# Save daily insights
basic-memory tool write-note --folder "life-os/daily-insights" --title "Daily $(date +%Y-%m-%d)"
```

### Workflow Shortcuts
```bash
# Find similar work
alias find-similar='mcp__basic-memory__search_notes'

# Save pattern quickly  
alias save-pattern='mcp__basic-memory__write_note --folder "life-os/task-patterns"'

# Morning routine
alias morning-context='mcp__basic-memory__build_context "memory://life-os/*" --timeframe "7d"'
```

---

## 🚨 CRITICAL RULES - NEVER VIOLATE

1. **ALWAYS start sessions with memory context** - No exceptions
2. **ALWAYS capture patterns after tasks** - Even small ones
3. **ALWAYS check memory before starting new work** - Avoid repetition
4. **ALWAYS save solutions immediately** - Don't lose insights
5. **ALWAYS apply ADHD time multipliers** - From learned patterns
6. **ALWAYS match task energy to time of day** - Use historical data
7. **ALWAYS document blockers as they occur** - For pattern recognition

---

## 🔔 MEMORY TRIGGERS - AUTOMATIC CAPTURE POINTS

### Immediate Capture Triggers
- ✅ Task completed → Pattern documentation
- 🐛 Bug fixed → Solution pattern
- 💡 Insight gained → Knowledge note
- 🚧 Blocker hit → Challenge documentation
- 🎯 Goal achieved → Success pattern
- 📚 Concept learned → Learning note
- 🔧 Tool configured → Setup pattern
- 📈 Process improved → Optimization note

### Session Boundaries
- **Session Start**: Load context, check recent
- **Mid-Session**: Capture insights as they occur
- **Session End**: Summarize and save session insights
- **Context Switch**: Save state before switching

---

## 🎯 SUCCESS METRICS - TRACK THESE

### Daily Minimums
- [ ] Context loaded at session start
- [ ] 3+ insights captured
- [ ] 1+ pattern documented
- [ ] Evening reflection saved

### Weekly Goals
- [ ] 20+ insights captured
- [ ] 5+ reusable patterns documented
- [ ] Time estimates within 20% accuracy
- [ ] Energy matching success >70%

### Monthly Improvements
- [ ] Pattern library growing
- [ ] Time estimation improving
- [ ] Blocker prediction accuracy increasing
- [ ] Productivity metrics trending up

---

## 🔧 DEGRADED MODE OPERATIONS

If Basic Memory is unavailable:
1. Note the limitation at session start
2. Create local markdown notes in Obsidian
3. Queue captures for later sync
4. Rely on Obsidian search instead
5. Sync when Basic Memory returns

---

## 📝 METADATA STANDARDS

Every memory note should include:
```yaml
---
type: [insight|pattern|solution|daily|weekly]
category: [work|personal|learning|life-os]
energy: [high|medium|low]
timestamp: YYYY-MM-DD HH:MM
project: [current-project]
tags: [relevant, tags]
success_score: [1-5]
reusable: [true|false]
---
```

---

## 🚀 CONTINUOUS IMPROVEMENT

### Weekly Memory Review
1. Review captured patterns
2. Identify most reused
3. Refine time multipliers
4. Update energy correlations
5. Adjust capture triggers

### Pattern Evolution
- Patterns should evolve with use
- Update success factors regularly
- Refine blockers and mitigations
- Improve reusability

---

*Remember: Every interaction makes me smarter through Basic Memory. The more you capture, the better I become at helping you!*

---

**Basic Memory Project**: obsidian | **Life-OS Integration**: Active | **Last Updated**: 2025-01-14