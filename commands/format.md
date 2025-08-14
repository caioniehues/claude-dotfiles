# Format - Simple Code Formatting

<task>
Format code using appropriate tool: $ARGUMENTS
</task>

## Process
1. Detect file type
2. Run appropriate formatter:
   - JavaScript/TypeScript: `prettier`
   - Python: `black` or `autopep8`
   - Java: `google-java-format`
   - Rust: `rustfmt`
   - Go: `gofmt`

Use existing tools, don't reinvent formatting.