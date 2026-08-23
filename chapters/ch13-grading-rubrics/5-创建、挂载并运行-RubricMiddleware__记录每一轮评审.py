"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 5. 创建、挂载并运行 RubricMiddleware / 记录每一轮评审
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.middleware.rubric import RubricEvaluation


evaluations: list[RubricEvaluation] = []
evaluations_by_run: dict[str, list[RubricEvaluation]] = {}


def record_evaluation(evaluation: RubricEvaluation) -> None:
    run_id = evaluation["grading_run_id"]
    evaluations.append(evaluation)
    evaluations_by_run.setdefault(run_id, []).append(evaluation)
    print(
        f"run {run_id[:8]} iteration {evaluation['iteration']}: "
        f"{evaluation['result']} — {evaluation['explanation']}"
    )
    for criterion in evaluation["criteria"]:
        if not criterion["passed"]:
            print(f"  gap: {criterion['name']} — {criterion.get('gap', '')}")
