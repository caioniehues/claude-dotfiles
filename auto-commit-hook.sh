# #!/bin/bash

# # Auto-commit hook script for Claude Code
# # This script is triggered by the Stop hook when a Claude session ends

# # Set up PATH to include homebrew (where git is installed)
# export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

# # Set working directory
# REPO_DIR="/Users/caio.niehues/.claude"
# LOG_FILE="$REPO_DIR/.auto-commit.log"

# # Function to log messages
# log_message() {
#     echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
# }

# # Change to repository directory
# cd "$REPO_DIR" || {
#     log_message "ERROR: Failed to change to repository directory"
#     exit 0  # Exit with 0 to not block Claude from stopping
# }

# # Check if git is available
# if ! command -v git &> /dev/null; then
#     log_message "ERROR: git command not found"
#     exit 0  # Exit with 0 to not block Claude from stopping
# fi

# # Check if gh CLI is available and setup git auth
# HAS_GH=false
# if command -v gh &> /dev/null; then
#     HAS_GH=true
#     log_message "INFO: Using GitHub CLI for authentication"
#     # Setup git to use gh for authentication
#     gh auth setup-git &>/dev/null
# else
#     log_message "INFO: GitHub CLI not found, using git directly"
# fi

# # Fetch latest changes from remote
# git fetch origin main &>/dev/null

# # Check if there are any changes to commit (both unstaged and staged)
# if git diff --quiet && git diff --staged --quiet; then
#     # No local changes to commit
#     log_message "INFO: No changes to commit"
    
#     # Check if we're behind the remote
#     if git status | grep -q "Your branch is behind"; then
#         log_message "INFO: Local branch is behind remote, pulling changes"
#         git pull origin main --rebase &>/dev/null
#         if [ $? -eq 0 ]; then
#             log_message "SUCCESS: Pulled remote changes successfully"
#         else
#             log_message "WARNING: Failed to pull remote changes"
#         fi
#     fi
#     exit 0
# fi

# # Add all changes
# git add . 2>&1 | tee -a "$LOG_FILE" &>/dev/null
# if [ ${PIPESTATUS[0]} -ne 0 ]; then
#     log_message "ERROR: Failed to add files"
#     exit 0  # Exit with 0 to not block Claude from stopping
# fi

# # Create commit message with timestamp
# COMMIT_MSG="Sync claude configurations - $(date '+%Y-%m-%d %H:%M')"

# # Commit changes
# git commit -m "$COMMIT_MSG" 2>&1 | tee -a "$LOG_FILE" &>/dev/null
# if [ ${PIPESTATUS[0]} -ne 0 ]; then
#     log_message "ERROR: Failed to commit changes"
#     exit 0  # Exit with 0 to not block Claude from stopping
# fi

# log_message "SUCCESS: Changes committed locally"

# # Try to pull and rebase before pushing
# git pull origin main --rebase 2>&1 | tee -a "$LOG_FILE" &>/dev/null
# if [ ${PIPESTATUS[0]} -ne 0 ]; then
#     log_message "WARNING: Rebase failed, attempting merge"
    
#     # Abort the rebase
#     git rebase --abort &>/dev/null
    
#     # Try a regular pull with merge
#     git pull origin main --no-rebase 2>&1 | tee -a "$LOG_FILE" &>/dev/null
#     if [ ${PIPESTATUS[0]} -ne 0 ]; then
#         log_message "ERROR: Failed to sync with remote, changes saved locally"
#         exit 0  # Exit with 0 to not block Claude from stopping
#     fi
# fi

# # Push to remote (git will use gh auth if available)
# git push origin main 2>&1 | tee -a "$LOG_FILE" &>/dev/null
# if [ ${PIPESTATUS[0]} -ne 0 ]; then
#     log_message "ERROR: Failed to push to remote, changes saved locally"
#     exit 0  # Exit with 0 to not block Claude from stopping
# fi

# log_message "SUCCESS: Changes pushed to remote successfully"

# # Keep log file size manageable (keep last 1000 lines)
# if [ -f "$LOG_FILE" ]; then
#     tail -n 1000 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
# fi

# # Exit successfully
# exit 0