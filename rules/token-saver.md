# Token Saver & High-Productivity Rules

Minimize token burn per task while maximizing speed and accuracy:

1. **Batch Tool Calls:** Issue independent `read_file`, `edit_file`, and search calls in parallel within one turn. Fewer round-trips save entire context re-sends.
2. **Locate Before Reading:** Use `rg -n` / `Select-String` to find exact lines first. Read only target ranges (50–150 lines) via `StartLine`/`EndLine`. Avoid full reads on files >250 lines unless refactoring the whole file, and never re-read unchanged files.
3. **Offload Broad Research:** Delegate multi-file codebase surveys to the `research` subagent so exploration logs don't bloat the main context.
4. **Surgical Edits:** Use `edit_file` for targeted changes instead of full-file `write_file` rewrites.
5. **Lean Command Output:** Run tests/builds with compact flags (`-q`, `--tb=short`, `--oneline`) and cap output (`Select-Object -First/-Last 25`, `head`/`tail`). On failure, extract only the failing error/trace—never dump full logs.
6. **Concise Responses & Hygiene:** No preambles or repeating unchanged code; give diffs, line links, and verified results. Put temp scripts/dumps in `scratch/`. Suggest `/compact` on long sessions (>25 turns).
