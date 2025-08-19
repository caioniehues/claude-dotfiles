#!/bin/bash

# SAVAGE COMMAND BENCHMARKER Runner
# Because your commands need a reality check

echo "🚀 Starting SAVAGE COMMAND BENCHMARKING..."
echo "📅 Date: $(date)"
echo "🧠 Benchmarker: SAVAGE_COMMAND_BENCHMARKER v1.0"
echo ""

# Create timestamp for results
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
RESULTS_DIR="../results"
mkdir -p "$RESULTS_DIR"

# Run the Node.js benchmarker
echo "📊 Analyzing commands with scientific rigor..."
node benchmark-engine.js > "$RESULTS_DIR/${TIMESTAMP}-execution.log" 2>&1

# Check if successful
if [ $? -eq 0 ]; then
    echo "✅ Benchmarking completed successfully!"
    echo "📁 Results saved in: $RESULTS_DIR"
    echo ""
    echo "📊 Summary of generated files:"
    ls -la "$RESULTS_DIR"/${TIMESTAMP}* 2>/dev/null || echo "No timestamped files found"
    echo ""
    echo "🔍 Latest summary:"
    find "$RESULTS_DIR" -name "*summary.md" -exec tail -10 {} \;
else
    echo "❌ Benchmarking failed! Check logs:"
    cat "$RESULTS_DIR/${TIMESTAMP}-execution.log"
fi

echo ""
echo "🎉 SAVAGE BENCHMARKING SESSION COMPLETE!"
echo "💡 Use these results to justify your refactoring decisions."