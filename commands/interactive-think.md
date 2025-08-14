# Interactive Thinking - Progressive Refinement

**Intelligent one-at-a-time questioning with visual progress for complex problems**

## Usage
```bash
/user:interactive-think "your complex question or problem"
```

## How It Works

### 🌱 Phase 1: Understanding (Target: 40% confidence)
Ask clarifying questions one at a time to build understanding:

**Question Format:**
```
❓ [Question] 
📋 Context: [Why this question matters]
💡 Impact: [How this affects the solution]
[Options if applicable]

Progress: ██████░░░░ 60%
```

**Stop when:**
- 40% confidence reached OR
- User indicates readiness to proceed

### 🌳 Phase 2: Deep Analysis (Target: 85% confidence)  
Research and analyze with continued interactive refinement:
- Use gathered context for targeted analysis
- Ask research questions as needed
- Build comprehensive understanding

### 🎯 Phase 3: Solution Design (Target: 95% confidence)
Present solution with quality gates:
- Break down implementation steps
- Confirm approach before execution
- Offer refinement opportunities

## Key Features

### ✨ Progressive Confidence
- Visual progress bars
- Clear confidence targets per phase
- Adaptive questioning based on current understanding

### 🤔 Smart Questioning
- One question at a time (no cognitive overload)
- Rich context for each question  
- Options provided when helpful
- Skip questions when confidence target reached

### 🔄 Quality Gates
```
⚖️ QUALITY GATE CHECK
Task: [Current step]
Status: ✅ PASSED / ⚠️ NEEDS REVIEW
Continue? (yes/refine/abort)
```

### 📊 Session Tracking
Save patterns to Basic Memory:
```bash
mcp__basic-memory__write_note \
  --title "Interactive Session - [topic]" \
  --folder "technical/interactive-sessions" \
  --content "[session results and patterns]"
```

## When to Use

**Perfect for:**
- Architecture decisions
- Complex problem analysis
- Requirements gathering
- Multi-step implementations
- Learning new domains

**Skip for:**
- Simple questions
- Quick fixes
- Well-understood problems

## Implementation Notes

**Following CLAUDE.md:**
- Complexity score: 3 (simple, focused)
- No over-engineering
- Uses existing tools (Basic Memory, visual formatting)
- Practical, not theatrical

**Visual Elements:**
- Progress bars: `██████░░░░ 60%`
- Phase emojis: 🌱→🌳→🎯
- Status indicators: ✅⚠️❓
- Simple ASCII boxes for questions

## Example Flow

```
🌱 Interactive Thinking - Understanding Phase
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────┐
│  🤔 Building understanding...              │
│  Question 1 of 3                           │
└─────────────────────────────────────────────┘

❓ What's the primary constraint you're working within?
📋 Context: Understanding limitations shapes the entire solution approach
💡 Impact: Determines feasibility and implementation strategy

Progress: ███░░░░░░░ 30%
```

This captures the valuable interactive features while eliminating the bloat - exactly what CLAUDE.md principles demand!