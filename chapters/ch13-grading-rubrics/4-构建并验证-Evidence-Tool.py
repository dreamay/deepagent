"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 4. 构建并验证 Evidence Tool
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from copy import deepcopy

from langchain.tools import tool


@tool
def run_test_suite(code: str) -> dict:
    """Run behavioral tests against a candidate find_duplicates implementation."""
    safe_builtins = {
        "all": all,
        "any": any,
        "enumerate": enumerate,
        "len": len,
        "list": list,
        "range": range,
        "set": set,
        "tuple": tuple,
    }
    namespace: dict = {"__builtins__": safe_builtins}

    try:
        exec(code, namespace)
    except Exception as exc:
        return {
            "ok": False,
            "failures": [f"load_error: {type(exc).__name__}: {exc}"],
        }

    find_duplicates = namespace.get("find_duplicates")
    if not callable(find_duplicates):
        return {
            "ok": False,
            "failures": ["missing_function: find_duplicates is not defined"],
        }

    tests = [
        ("test_basic", [1, 2, 2, 3, 1], [2, 1]),
        ("test_empty", [], []),
        ("test_no_duplicates", [1, 2, 3], []),
        ("test_unhashable", [[1], [1], 2], [[1]]),
    ]
    failures: list[str] = []

    for name, values, expected in tests:
        original = deepcopy(values)
        try:
            actual = find_duplicates(values)
            if actual != expected:
                failures.append(f"{name}: expected {expected}, got {actual}")
            if values != original:
                failures.append(f"{name}: input was mutated")
        except Exception as exc:
            failures.append(f"{name}: {type(exc).__name__}: {exc}")

    return {"ok": not failures, "failures": failures}
