---
name: code-skeletonizer
description: High-efficiency code structure analyzer. Use before reading unfamiliar large files (>200 lines) to view class, function, and method outlines with exact line numbers, achieving 80-99% token savings.
---

# Code Skeletonizer Skill

Use this skill when exploring, analyzing, or modifying existing codebases to prevent massive context bloat.

## When to Use:
- Before inspecting unfamiliar source files (`.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, `.cpp`).
- When looking for where a specific class, function, or method is implemented.
- To locate exact line numbers (`[Lxx-Lyy]`) before calling `read_file` with targeted `StartLine` and `EndLine`.

## Usage Command:
Run the skeletonizer script via PowerShell:
```powershell
python "C:\Users\Kotsuro\.gemini\config\plugins\antigravity-token-optimizer\skills\code-skeletonizer\scripts\skeletonize.py" "<absolute_path_to_file>"
```

## Workflow:
1. Run `skeletonize.py` on the target file.
2. Review the resulting outline (classes, methods, parameters, line spans).
3. Call `read_file` targeting ONLY the specific lines found (e.g. `StartLine: 87, EndLine: 108`).
4. Apply surgical edits with `edit_file`.
