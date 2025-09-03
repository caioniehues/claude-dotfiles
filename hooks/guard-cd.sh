#!/usr/bin/env bash
# ~/.claude/hooks/guard-cd.sh (strict)
set -euo pipefail
payload="$(cat)"
tool="$(jq -r '.tool_name // ""' <<<"$payload")"
cmd="$(jq -r '.tool_input.command // ""' <<<"$payload")"

# Only inspect Bash tool calls
[[ "$tool" == "Bash" ]] || exit 0
[[ -n "$cmd" ]] || exit 0

# If any token 'cd' appears, block. (We don't try to parse shell; we disallow it.)
if grep -Eq '(^|[;&|()[:space:]])cd([[:space:]]|$)' <<<"$cmd"; then
  {
    echo "Blocked: never use plain 'cd'."
    echo "Rewrite using either:"
    echo "  ( cd \"/abs/path\" && full_command )"
    echo "  or a tool flag: git -C \"/abs/path\" … / yarn --cwd \"/abs/path\" … / make -C \"/abs/path\" …"
  } 1>&2
  exit 2
fi