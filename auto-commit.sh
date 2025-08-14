#!/bin/bash

# Auto-commit script for .claude repository
# This script is designed to be run by cron

# Set up PATH to include homebrew (where git is installed)
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

# Set working directory
REPO_DIR="/Users/caio.niehues/.claude"
LOG_FILE="$REPO_DIR/.auto-commit.log"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Change to repository directory
cd "$REPO_DIR" || {
    log_message "ERROR: Failed to change to repository directory"
    exit 1
}

# Check if git is available
if ! command -v git &> /dev/null; then
    log_message "ERROR: git command not found"
    exit 1
fi

# Check if gh CLI is available and setup git auth
HAS_GH=false
if command -v gh &> /dev/null; then
    HAS_GH=true
    log_message "INFO: Using GitHub CLI for authentication"
    # Setup git to use gh for authentication
    gh auth setup-git &>/dev/null
else
    log_message "INFO: GitHub CLI not found, using git directly"
fi

# Check if there are any changes to commit
if git diff --quiet && git diff --staged --quiet; then
    # No changes to commit
    log_message "INFO: No changes to commit"
    exit 0
fi

# Add all changes
git add . 2>&1 | tee -a "$LOG_FILE"
if [ ${PIPESTATUS[0]} -ne 0 ]; then
    log_message "ERROR: Failed to add files"
    exit 1
fi

# Create commit message with timestamp
COMMIT_MSG="Sync claude configurations - $(date '+%Y-%m-%d %H:%M')"

# Commit changes
git commit -m "$COMMIT_MSG" 2>&1 | tee -a "$LOG_FILE"
if [ ${PIPESTATUS[0]} -ne 0 ]; then
    log_message "ERROR: Failed to commit changes"
    exit 1
fi

# Push to remote (git will use gh auth if available)
git push origin main 2>&1 | tee -a "$LOG_FILE"
if [ ${PIPESTATUS[0]} -ne 0 ]; then
    log_message "ERROR: Failed to push to remote"
    exit 1
fi

log_message "SUCCESS: Changes committed and pushed successfully"

# Keep log file size manageable (keep last 1000 lines)
if [ -f "$LOG_FILE" ]; then
    tail -n 1000 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
fi