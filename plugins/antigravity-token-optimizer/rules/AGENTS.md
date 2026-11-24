# Token Optimizer Plugin Rule

- **AST Skeleton for Unfamiliar Large Files:** When exploring an unfamiliar file >200 lines where `rg -n` isn't sufficient (e.g. you need the full class/method layout), run `scripts/skeletonize.py` first, then `read_file` only the needed line ranges. Skip `skeletonize.py` when you already know the target symbol or line.
