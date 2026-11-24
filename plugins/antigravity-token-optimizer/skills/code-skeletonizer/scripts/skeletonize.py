#!/usr/bin/env python3
"""
Code Skeletonizer: Extracts class and function signatures with line ranges
from source files, stripping bodies to minimize token usage by up to 85%.
Supports Python, JavaScript, TypeScript, and general languages.
"""

import ast
import os
import re
import sys

def skeletonize_python(content: str, filename: str) -> str:
    try:
        tree = ast.parse(content, filename=filename)
    except Exception as e:
        return f"// Failed to parse AST: {e}\n" + skeletonize_generic(content)

    lines = content.splitlines()
    out = []

    def get_docstring(node):
        if (node.body and isinstance(node.body[0], ast.Expr) and
                isinstance(node.body[0].value, ast.Constant) and
                isinstance(node.body[0].value.value, str)):
            doc = node.body[0].value.value.strip().splitlines()[0]
            return f' """{doc}"""'
        return ""

    class Visitor(ast.NodeVisitor):
        def __init__(self):
            self.indent = 0

        def visit_ClassDef(self, node):
            prefix = "  " * self.indent
            doc = get_docstring(node)
            bases = ", ".join(ast.unparse(b) for b in node.bases)
            base_str = f"({bases})" if bases else ""
            end_line = getattr(node, "end_lineno", node.lineno)
            out.append(f"{prefix}[L{node.lineno}-L{end_line}] class {node.name}{base_str}:{doc}")
            self.indent += 1
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    self.visit(item)
                elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                    target = ast.unparse(item.target)
                    annotation = ast.unparse(item.annotation)
                    out.append(f"{'  ' * self.indent}[L{item.lineno}] {target}: {annotation}")
            self.indent -= 1

        def visit_FunctionDef(self, node):
            self._visit_func(node, is_async=False)

        def visit_AsyncFunctionDef(self, node):
            self._visit_func(node, is_async=True)

        def _visit_func(self, node, is_async=False):
            prefix = "  " * self.indent
            async_pfx = "async " if is_async else ""
            doc = get_docstring(node)
            
            # Format arguments
            args_list = []
            for a in node.args.args:
                arg_str = a.arg
                if a.annotation:
                    arg_str += f": {ast.unparse(a.annotation)}"
                args_list.append(arg_str)
            if node.args.vararg:
                args_list.append(f"*{node.args.vararg.arg}")
            if node.args.kwarg:
                args_list.append(f"**{node.args.kwarg.arg}")
            
            ret = f" -> {ast.unparse(node.returns)}" if node.returns else ""
            sig = f"{prefix}[L{node.lineno}-L{getattr(node, 'end_lineno', node.lineno)}] {async_pfx}def {node.name}({', '.join(args_list)}){ret}:{doc} ..."
            out.append(sig)

    Visitor().visit(tree)
    return "\n".join(out) if out else "// No classes or functions detected"

def skeletonize_generic(content: str) -> str:
    lines = content.splitlines()
    out = []
    # Match functions, classes, methods in JS, TS, Go, Rust, Java
    pattern = re.compile(
        r'^\s*(export\s+)?(default\s+)?(async\s+)?(function|class|interface|type|const|let|var|def|fn|pub fn|func)\b'
    )
    for idx, line in enumerate(lines, 1):
        if pattern.search(line):
            out.append(f"[L{idx}] {line.strip()}")
    return "\n".join(out[:150]) if out else "// Generic outline empty"

def main():
    if len(sys.argv) < 2:
        print("Usage: skeletonize.py <path_to_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    ext = os.path.splitext(filepath)[1].lower()
    total_lines = len(content.splitlines())
    
    print(f"=== SKELETON: {os.path.basename(filepath)} ({total_lines} lines) ===")
    if ext == ".py":
        skeleton = skeletonize_python(content, filepath)
    else:
        skeleton = skeletonize_generic(content)
    
    skel_lines = len(skeleton.splitlines())
    savings = round((1 - skel_lines / max(1, total_lines)) * 100)
    print(skeleton)
    print(f"\n--- [Token Savings: ~{savings}% | Showing {skel_lines} lines instead of {total_lines}] ---")

if __name__ == "__main__":
    main()
