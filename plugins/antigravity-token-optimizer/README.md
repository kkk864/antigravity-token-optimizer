# Antigravity Token Optimizer Plugin

Custom optimization bundle designed to reduce LLM token expenditure by up to 85% during coding and debugging workflows.

## Features:
1. **Code Skeletonizer**: AST outline extractor for source code. Parses classes, functions, and signatures without bodies, saving 80–99% tokens on file exploration.
2. **Context Economy Rules**: Enforces targeted reading (`StartLine`/`EndLine`), surgical edits, and prevents unbounded terminal log dumps.
3. **Log Truncator**: Keeps terminal command responses bounded to relevant lines.
