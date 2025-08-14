# 🤖 Claude Dotfiles

> Personal configuration repository for Claude Code - My AI pair programming setup

## 📁 Repository Structure

```
.claude/
├── 📝 CLAUDE.md           # Global coding guidelines & principles
├── ⚙️ settings.json       # Claude configuration settings
├── 🤖 agents/             # Custom AI agents for specialized tasks
├── 🎯 commands/           # Custom slash commands
├── 📋 command-templates/  # Reusable command templates
├── 📚 docs/               # Documentation & guides
├── 🏗️ projects/           # Project-specific configurations
└── 💻 ide/                # IDE integration settings
```

## 🎯 Philosophy

This repository embodies my development philosophy:

### Core Principles
- **✨ Simplicity First** - Start simple, add complexity only when necessary
- **📏 Clean Code** - Readable, maintainable, and testable
- **🧪 TDD Approach** - Red → Green → Refactor
- **🚀 Modern Java** - Leverage latest language features
- **🎨 DRY & SOLID** - Follow established design principles

### The 3-Question Rule
1. Can I use what already exists? → DO THAT
2. Can I solve this with a simple method? → DO THAT  
3. Do I really need this abstraction NOW? → PROBABLY NOT

## 🤖 Custom Agents

### Java Development Suite
- `java-clean-architect` - Clean architecture specialist
- `java-tdd-orchestrator` - TDD workflow coordinator
- `java-simplicity-guardian` - Complexity watchdog
- `java-code-reviewer` - Automated code review
- `java-api-designer` - RESTful API design expert

### Utility Agents
- `meta-agent` - Agent creation & management
- `memory-manager` - Context & memory optimization
- `greeting-fact-presenter` - Fun fact generator

## 🎮 Custom Commands

### Development Commands
- `/java-simple` - Write simple, clean Java code
- `/java-tdd` - TDD-driven implementation
- `/java-clean-implementer` - Clean code implementation
- `/refactor` - Intelligent refactoring suggestions
- `/understand` - Deep code analysis

### Utility Commands
- `/make-it-pretty` - Format & beautify code
- `/explain-like-senior` - Expert-level explanations
- `/enhancement-prompt` - Improve prompts & queries
- `/thinking-enhancer` - Enhanced reasoning mode

## 🔧 Setup & Installation

### Prerequisites
- Claude Code CLI installed
- Git configured
- GitHub account

### Clone Repository
```bash
# Backup existing .claude folder (if any)
mv ~/.claude ~/.claude.backup

# Clone this repository as your .claude folder
git clone https://github.com/caioniehues/claude-dotfiles.git ~/.claude
```

### Restore from Backup
```bash
# Pull latest changes
cd ~/.claude
git pull origin main
```

## 📊 Configuration

### Settings Overview
The `settings.json` contains:
- Model preferences
- Tool configurations
- Custom aliases
- Performance settings

### Project-Specific Settings
Each project can have custom configurations stored in `projects/` directory, automatically loaded when working in that project context.

## 🚀 Usage

### Using Custom Agents
```bash
# In Claude Code
/agent java-clean-architect "Design a payment processing system"
```

### Using Custom Commands
```bash
# Execute custom command
/java-tdd "Create a user authentication service"
```

### Updating Configurations
```bash
cd ~/.claude
git add .
git commit -m "Update configurations"
git push origin main
```

## 📝 Key Guidelines (CLAUDE.md)

### Complexity Score System
- Direct solution: 1 point
- Each new class: +2 points
- Each interface: +1 point
- Each design pattern: +3 points
- **Target: Score < 5**

### Code Standards
- Functions < 20 lines
- Max 3 parameters
- All parameters `final`
- No wildcard imports
- No null returns
- Meaningful names

## 🔄 Synchronization

### Auto-backup Script
Create a cron job for automatic backups:
```bash
# Add to crontab
0 */6 * * * cd ~/.claude && git add . && git commit -m "Auto-backup" && git push
```

### Manual Sync
```bash
# Quick sync function (add to .zshrc or .bashrc)
claude-sync() {
  cd ~/.claude
  git add .
  git commit -m "Sync claude configurations - $(date +%Y-%m-%d)"
  git push origin main
}
```

## 📈 Evolution

This configuration evolves with my development practices. Key areas of focus:
- Continuous simplification
- Performance optimization
- Tool integration
- Workflow automation

## 🤝 Contributing

This is a personal configuration repository, but feel free to:
- Fork for your own use
- Suggest improvements via issues
- Share your own agent/command ideas

## 📄 License

Personal configuration files - use at your own discretion.

---

*"Simplicity is the ultimate sophistication" - Leonardo da Vinci*

**Last Updated:** August 2025