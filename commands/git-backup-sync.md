# Git Backup Sync - Intelligent Repository Synchronization with Reasoning

<task>
Intelligently synchronizes git repositories with automatic backup, conflict resolution, and pattern learning for: $ARGUMENTS
</task>

<context>
This command provides intelligent git repository synchronization with built-in reasoning, automatic decision-making for complex scenarios, and integration with existing automation scripts.

Core capabilities:
- Automatic change detection and smart syncing
- Conflict resolution with reasoning
- Branch management and protection
- Stash handling for uncommitted changes
- Pattern learning from sync operations
- Integration with auto-commit.sh
- Error recovery with fallback strategies
- Multi-repository orchestration
</context>

<thinking_orchestration>
## Sync Complexity Assessment
<complexity_detection>
Evaluating sync operation complexity: "$ARGUMENTS"

Complexity factors:
- Repository state: [clean/dirty/conflicted]
- Remote divergence: [none/minor/major]
- Branch complexity: [single/multiple/protected]
- Uncommitted changes: [none/staged/unstaged/mixed]
- Conflict potential: [low/medium/high]
- Integration needs: [standalone/multi-repo/automated]
- Estimated complexity score: _____

If complexity > 3:
  INVOKE: mcp__mcp-sequentialthinking-tools__sequentialthinking_tools
  WITH: Complex sync strategy planning
If complexity <= 3:
  USE: Direct sync with reasoning blocks
</complexity_detection>

## Pre-Sync Analysis
<pre_sync_thinking>
Before synchronizing repositories:

1. Repository Assessment
   - Target: "$ARGUMENTS" or current directory
   - Current branch: [identify]
   - Working tree status: [analyze]
   - Remote status: [check divergence]
   - Last sync: [determine from logs]

2. Sync Strategy Selection
   - Full sync vs incremental: [decide based on changes]
   - Stash required: [yes/no and why]
   - Branch switching needed: [assess]
   - Conflict likelihood: [evaluate]

3. Risk Evaluation
   - Data loss potential: [assess]
   - Automation conflicts: [check auto-commit.sh]
   - Recovery options: [identify fallbacks]
   - Time constraints: [consider schedules]
</pre_sync_thinking>
</thinking_orchestration>

<repository_analysis>
## Intelligent Repository State Analysis
<state_thinking>
Analyzing repository state for optimal sync strategy:

1. Working Directory Status
   ```bash
   git status --porcelain
   ```
   - Clean: Direct sync possible
   - Uncommitted changes: Stash or commit decision
   - Conflicts: Resolution required

2. Branch Analysis
   ```bash
   git branch -vv
   git rev-parse --abbrev-ref HEAD
   ```
   - Current branch: [main/feature/etc]
   - Tracking status: [upstream configured?]
   - Protection level: [assess rules]

3. Remote Divergence Check
   ```bash
   git fetch --dry-run
   git rev-list --left-right --count HEAD...@{u}
   ```
   - Behind: Pull required
   - Ahead: Push required
   - Diverged: Merge/rebase decision

4. Automation Integration
   - Check .auto-commit.log
   - Verify cron schedules
   - Coordinate with auto-commit.sh
</state_thinking>
</repository_analysis>

<sync_strategies>
## Adaptive Sync Strategies

### Strategy 1: Simple Sync (Clean State)
<simple_sync_thinking>
When: Working directory clean, no conflicts expected

Execution:
1. Fetch latest changes
2. Fast-forward merge if possible
3. Push local commits
4. Update sync log

Reasoning: Minimal risk, maximum speed
</simple_sync_thinking>

### Strategy 2: Stash-Sync-Pop (Uncommitted Changes)
<stash_sync_thinking>
When: Uncommitted changes present, want to preserve

Execution:
1. Stash current changes with description
2. Perform sync operation
3. Pop stash and handle conflicts
4. Decide: commit or keep uncommitted

Reasoning: Preserves work-in-progress while syncing
</stash_sync_thinking>

### Strategy 3: Auto-Commit Sync (Integration Mode)
<auto_commit_sync_thinking>
When: Integrating with auto-commit.sh

Execution:
1. Check if auto-commit is running
2. Wait for completion if active
3. Add all changes
4. Create timestamped commit
5. Push with retry logic

Reasoning: Maintains automation continuity
</auto_commit_sync_thinking>

### Strategy 4: Conflict Resolution Sync
<conflict_sync_thinking>
When: Merge conflicts detected or expected

Execution:
1. Attempt automatic resolution
2. If fails, analyze conflict patterns
3. Apply learned resolutions
4. Manual intervention if needed
5. Document resolution pattern

Reasoning: Minimizes manual intervention over time
</conflict_sync_thinking>

### Strategy 5: Multi-Repository Orchestration
<multi_repo_thinking>
When: Multiple repositories need syncing

Execution:
1. Analyze dependencies between repos
2. Determine sync order
3. Parallel where possible
4. Sequential where required
5. Aggregate results

Reasoning: Efficient multi-repo management
</multi_repo_thinking>
</sync_strategies>

<commit_message_generation>
## Intelligent Commit Message Creation
<message_thinking>
Generating context-aware commit messages:

1. Change Analysis
   - Files modified: [count and categorize]
   - Change scope: [feature/fix/docs/refactor]
   - Impact assessment: [breaking/minor/patch]

2. Message Structure Selection
   ```
   Type: [feat|fix|docs|style|refactor|test|chore]
   Scope: [affected area]
   Description: [what and why]
   ```

3. Auto-Generated vs Custom
   - Simple changes: Auto-generate
   - Complex changes: Prompt for input
   - Pattern-based: Use learned templates

4. Integration Markers
   - Add automation flags
   - Include sync metadata
   - Reference related commits
</message_thinking>
</commit_message_generation>

<error_recovery>
## Intelligent Error Recovery
<recovery_thinking>
Handling sync failures gracefully:

1. Network Failures
   - Retry with exponential backoff
   - Cache operations for later
   - Switch to offline mode

2. Merge Conflicts
   - Attempt auto-resolution
   - Create conflict branch
   - Notify for manual review

3. Authentication Issues
   - Check credential helpers
   - Refresh tokens if needed
   - Fallback to manual auth

4. Disk Space Issues
   - Clean unnecessary files
   - Prune git objects
   - Alert if critical

5. Corruption Detection
   - Verify repository integrity
   - Attempt repair
   - Backup before proceeding
</recovery_thinking>
</error_recovery>

<pattern_learning>
## Sync Pattern Learning
<learning_thinking>
Learning from sync operations:

1. Success Patterns
   - Optimal sync times
   - Successful merge strategies
   - Effective commit grouping

2. Conflict Patterns
   - Common conflict files
   - Resolution strategies that work
   - Prevention opportunities

3. Performance Patterns
   - Peak sync times to avoid
   - Batch size optimizations
   - Network quality patterns

4. User Patterns
   - Commit message preferences
   - Branch naming conventions
   - Workflow preferences

Store patterns in Basic Memory:
```bash
mcp__basic-memory__write_note \
  --title "Git Sync Pattern - $(date +%Y-%m-%d)" \
  --folder "technical/git-patterns" \
  --content "[Pattern details, success metrics, optimizations]"
```
</learning_thinking>
</pattern_learning>

<automation_integration>
## Integration with auto-commit.sh
<integration_thinking>
Coordinating with existing automation:

1. Script Detection
   ```bash
   if [ -f "$HOME/.claude/auto-commit.sh" ]; then
     AUTOMATION_ACTIVE=true
   fi
   ```

2. Schedule Awareness
   - Parse cron schedules
   - Avoid conflicts
   - Complement automation

3. Log Coordination
   - Read .auto-commit.log
   - Append sync operations
   - Maintain log rotation

4. Handoff Logic
   - Let auto-commit handle routine
   - Take over for complex scenarios
   - Document handoff points
</integration_thinking>
</automation_integration>

<monitoring_dashboard>
## Sync Operation Monitoring
<monitoring_thinking>
Real-time sync status and metrics:

```
SYNC STATUS
├── Repository: [path]
├── Branch: [current]
├── State: [syncing/idle/error]
├── Last Sync: [timestamp]
├── Changes: [ahead/behind counts]
└── Conflicts: [count if any]

SYNC METRICS
├── Success Rate: [percentage]
├── Avg Sync Time: [seconds]
├── Conflicts Resolved: [auto/manual]
├── Patterns Learned: [count]
└── Error Recovery: [success rate]

AUTOMATION STATUS
├── Auto-commit: [active/idle]
├── Next Schedule: [time]
├── Integration Mode: [enabled/disabled]
└── Log Size: [lines/size]
```
</monitoring_thinking>
</monitoring_dashboard>

<execution_flow>
## Main Execution Flow
<flow_thinking>
Step-by-step sync execution:

1. **Initialize**
   - Load configuration
   - Check Basic Memory for patterns
   - Assess complexity

2. **Analyze**
   - Repository state
   - Remote status
   - Automation status

3. **Strategize**
   - Select sync strategy
   - Prepare operations
   - Set up recovery

4. **Execute**
   - Perform sync operations
   - Handle errors
   - Apply patterns

5. **Finalize**
   - Update logs
   - Save patterns
   - Clean up

6. **Learn**
   - Capture insights
   - Update patterns
   - Optimize for next time
</flow_thinking>
</execution_flow>

<usage_examples>
## Usage Examples

### Basic Repository Sync
```bash
/user:git-backup-sync
# Syncs current repository with smart decisions
```

### Specific Repository
```bash
/user:git-backup-sync /Users/caio.niehues/.claude
# Syncs specified repository
```

### Force Strategy
```bash
/user:git-backup-sync --strategy auto-commit
# Uses auto-commit integration strategy
```

### Multi-Repository Sync
```bash
/user:git-backup-sync --repos ".claude,obsidian-vault,projects/*"
# Syncs multiple repositories
```

### Conflict Resolution Mode
```bash
/user:git-backup-sync --resolve-conflicts
# Focuses on resolving existing conflicts
```

### Schedule Integration
```bash
/user:git-backup-sync --schedule "*/5 * * * *"
# Sets up scheduled sync with cron
```

### Dry Run Mode
```bash
/user:git-backup-sync --dry-run
# Shows what would be done without executing
```
</usage_examples>

<configuration>
## Configuration Options
<config_thinking>
Configurable sync parameters:

```yaml
git_backup_sync:
  complexity_threshold: 3
  auto_commit_integration: true
  
  strategies:
    default: smart
    conflict_resolution: auto_first
    stash_uncommitted: true
    
  commit:
    auto_message: true
    template: "Sync: {branch} - {timestamp}"
    include_stats: true
    
  patterns:
    learning_enabled: true
    memory_integration: true
    pattern_cache: ~/.claude/git-patterns
    
  automation:
    respect_cron: true
    log_file: .auto-commit.log
    max_log_size: 1000
    
  monitoring:
    show_dashboard: true
    metrics_tracking: true
    alert_on_conflicts: true
```
</config_thinking>
</configuration>

<integration_notes>
## Integration with Other Commands

Works seamlessly with:
- `/user:reasoning-wrapper` - Adds additional reasoning layers
- `/user:adaptive-complexity-router` - Routes complex scenarios
- `auto-commit.sh` - Coordinates with existing automation
- Basic Memory - Stores and retrieves sync patterns

Can be enhanced:
```bash
/user:reasoning-wrapper /user:git-backup-sync
# Adds extra reasoning layer to sync operations
```

Chain with other operations:
```bash
/user:git-backup-sync && /user:intelligent-code-enhancer
# Sync then enhance code
```
</integration_notes>

<best_practices>
## Best Practices
<practices_thinking>
Recommended sync practices:

1. **Regular Syncing**
   - Set up scheduled syncs
   - Don't let changes accumulate
   - Sync before major changes

2. **Commit Hygiene**
   - Meaningful commit messages
   - Logical change grouping
   - Regular small commits

3. **Branch Management**
   - Keep main branch clean
   - Use feature branches
   - Regular branch cleanup

4. **Automation Balance**
   - Let automation handle routine
   - Manual review for complex
   - Monitor automation logs

5. **Pattern Learning**
   - Review learned patterns
   - Adjust strategies based on patterns
   - Share patterns across repositories
</practices_thinking>
</best_practices>

<completion_check>
## Sync Completion Verification
<verification_thinking>
Ensuring successful sync:

1. **State Verification**
   ```bash
   git status
   git log --oneline -5
   git rev-list --left-right --count HEAD...@{u}
   ```

2. **Success Criteria**
   - Working directory clean or as expected
   - Local and remote in sync
   - No unresolved conflicts
   - Automation still functioning

3. **Pattern Capture**
   - Document what worked
   - Note any issues
   - Save to Basic Memory
   - Update configuration
</verification_thinking>
</completion_check>