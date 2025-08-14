#!/bin/bash

# Fix all agent files by adding the location field
AGENTS_DIR="/Users/caio.niehues/.claude/agents"
LOCATION="/Users/caio.niehues/.claude/commands"

for agent_file in "$AGENTS_DIR"/*.md; do
    if [ -f "$agent_file" ]; then
        # Check if location field already exists
        if ! grep -q "^location:" "$agent_file"; then
            echo "Fixing: $(basename "$agent_file")"
            # Add location field before the closing ---
            sed -i '' '/^---$/,/^---$/{
                /^---$/{
                    N
                    s/\(tools:.*\)\n---/\1\nlocation: '"$(echo $LOCATION | sed 's/\//\\\//g')"'\n---/
                }
            }' "$agent_file"
        else
            echo "Already fixed: $(basename "$agent_file")"
        fi
    fi
done

echo "All agent files have been processed!"