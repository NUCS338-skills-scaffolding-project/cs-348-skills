# logic.py — Compare Algorithms and Stragegies

"""
Three modes:
  - action="register_strategies": agent passes in LLM-generated strategies
    along with assignment context and learning goals, logic.py validates
    and stores them for the session
  - action="get_strategy": returns the next strategy for the tutor to discuss
  - action="summarize": given which strategies were understood and which
    were not, returns a structured gap report tied to learning goals

Design decision: judgment is the agent's job. The agent uses LLM judgment
to generate strategies informed by the assignment and learning goals, and
to evaluate student understanding during discussion. This skill holds the
strategy structure and manages progress through it.
"""

# Session store — holds registered strategies for the current session
_SESSION = {}

REQUIRED_STRATEGY_FIELDS = {
    "id",
    "name",
    "description",
    "tradeoffs",
    "what_to_listen_for",
    "discussion_prompt",
}


def run(input):
    """
    Main entry point.

    :param input: dict with `action` and `session_id`.
        For register_strategies: also `assignment`, `learning_goals`,
            `inferred`, and `strategies`
        For get_strategy: also `strategy_index`
        For summarize: also `strategies_understood` and `strategies_missed`
    :return: dict shaped per skills.md
    """
    action = input.get("action")
    session_id = input.get("session_id")

    if action not in ("register_strategies", "get_strategy", "summarize"):
        return _error(
            action, session_id,
            "action must be 'register_strategies', 'get_strategy', or 'summarize'."
        )

    if session_id is None:
        return _error(action, session_id, "session_id is required.")

    if action == "register_strategies":
        assignment = input.get("assignment")
        learning_goals = input.get("learning_goals")
        inferred = input.get("inferred", False)
        strategies = input.get("strategies")

        if not assignment:
            return _error(action, session_id, "assignment is required.")

        if not isinstance(learning_goals, list) or len(learning_goals) == 0:
            return _error(action, session_id, "learning_goals must be a non-empty list.")

        if not isinstance(strategies, list) or len(strategies) == 0:
            return _error(action, session_id, "strategies must be a non-empty list.")

        for i, strategy in enumerate(strategies):
            missing = REQUIRED_STRATEGY_FIELDS - set(strategy.keys())
            if missing:
                return _error(
                    action, session_id,
                    f"Strategy {i} is missing fields: {missing}"
                )

        _SESSION[session_id] = {
            "assignment": assignment,
            "learning_goals": learning_goals,
            "inferred": inferred,
            "strategies": strategies,
        }

        return {
            "action": "register_strategies",
            "session_id": session_id,
            "total_strategies": len(strategies),
            "learning_goals": learning_goals,
            "inferred": inferred,
            "error": None,
        }

    # get_strategy and summarize both need a registered session
    session = _SESSION.get(session_id)
    if session is None:
        return _error(
            action, session_id,
            f"No strategies registered for session_id: {session_id!r}."
        )

    strategies = session["strategies"]

    if action == "get_strategy":
        strategy_index = input.get("strategy_index")

        if not isinstance(strategy_index, int):
            return _error(action, session_id, "strategy_index must be an integer.")

        if strategy_index >= len(strategies):
            return _error(
                action, session_id,
                f"strategy_index {strategy_index} out of range. Total strategies: {len(strategies)}."
            )

        strategy = strategies[strategy_index]

        return {
            "action": "get_strategy",
            "session_id": session_id,
            "strategy_number": strategy_index + 1,
            "total_strategies": len(strategies),
            "is_last_strategy": strategy_index == len(strategies) - 1,
            "name": strategy["name"],
            "description": strategy["description"],
            "discussion_prompt": strategy["discussion_prompt"],
            "what_to_listen_for": strategy["what_to_listen_for"],
            "error": None,
        }

    # action == "summarize"
    strategies_understood = input.get("strategies_understood", [])
    strategies_missed = input.get("strategies_missed", [])

    if not isinstance(strategies_understood, list):
        return _error(action, session_id, "strategies_understood must be a list of strategy IDs.")

    if not isinstance(strategies_missed, list):
        return _error(action, session_id, "strategies_missed must be a list of strategy IDs.")

    valid_ids = {s["id"] for s in strategies}

    unknown_understood = [sid for sid in strategies_understood if sid not in valid_ids]
    if unknown_understood:
        return _error(
            action, session_id,
            f"Unknown strategy IDs in strategies_understood: {unknown_understood}"
        )

    unknown_missed = [sid for sid in strategies_missed if sid not in valid_ids]
    if unknown_missed:
        return _error(
            action, session_id,
            f"Unknown strategy IDs in strategies_missed: {unknown_missed}"
        )

    understood = [
        {"id": s["id"], "name": s["name"]}
        for s in strategies if s["id"] in strategies_understood
    ]

    gaps = [
        {
            "id": s["id"],
            "name": s["name"],
            "tradeoffs": s["tradeoffs"],
        }
        for s in strategies if s["id"] in strategies_missed
    ]

    # Check which learning goals were covered based on understood strategies
    learning_goals = session["learning_goals"]
    inferred = session["inferred"]

    return {
        "action": "summarize",
        "session_id": session_id,
        "understood": understood,
        "gaps": gaps,
        "learning_goals": learning_goals,
        "inferred": inferred,
        "goals_caveat": (
            "Learning goals were inferred from the assignment — gaps may reflect "
            "inaccurate goals rather than student misunderstanding."
            if inferred else None
        ),
        "error": None,
    }


def _error(action, session_id, msg):
    return {
        "action": action,
        "session_id": session_id,
        "error": msg,
    }

