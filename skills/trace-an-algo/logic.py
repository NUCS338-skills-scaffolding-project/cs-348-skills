# logic.py — Trace an Algorithm skill

"""
Three modes:
  - action="register_trace": agent passes in LLM-generated steps,
    logic.py validates and stores them for the session
  - action="get_step": returns the next step for the tutor to reveal
  - action="summarize": given which steps passed and which failed,
    returns a structured gap report

Design decision: judgment is the agent's job. The agent uses LLM
judgment to generate trace steps and evaluate student predictions.
This skill holds the trace structure and manages progress through it.
"""

# Session store — holds registered traces for the current session
_SESSION = {}

REQUIRED_STEP_FIELDS = {"id", "state", "concept", "what_to_listen_for", "remediation_hint"}


def run(input):
    """
    Main entry point.

    :param input: dict with `action` and `session_id`. 
        For register_trace: also `steps`
        For get_step: also `step_index`
        For summarize: also `steps_passed` and `step_failed`
    :return: dict shaped per skills.md
    """
    action = input.get("action")
    session_id = input.get("session_id")

    if action not in ("register_trace", "get_step", "summarize"):
        return _error(action, session_id, "action must be 'register_trace', 'get_step', or 'summarize'.")

    if session_id is None:
        return _error(action, session_id, "session_id is required.")

    if action == "register_trace":
        steps = input.get("steps")

        if not isinstance(steps, list) or len(steps) == 0:
            return _error(action, session_id, "steps must be a non-empty list.")

        for i, step in enumerate(steps):
            missing = REQUIRED_STEP_FIELDS - set(step.keys())
            if missing:
                return _error(action, session_id, f"Step {i} is missing fields: {missing}")

        _SESSION[session_id] = steps

        return {
            "action": "register_trace",
            "session_id": session_id,
            "total_steps": len(steps),
            "error": None,
        }

    # get_step and summarize both need a registered trace
    steps = _SESSION.get(session_id)
    if steps is None:
        return _error(action, session_id, f"No trace registered for session_id: {session_id!r}.")

    if action == "get_step":
        step_index = input.get("step_index")

        if not isinstance(step_index, int):
            return _error(action, session_id, "step_index must be an integer.")

        if step_index >= len(steps):
            return _error(action, session_id, f"step_index {step_index} out of range. Total steps: {len(steps)}.")

        step = steps[step_index]

        return {
            "action": "get_step",
            "session_id": session_id,
            "step_number": step_index + 1,
            "total_steps": len(steps),
            "is_last_step": step_index == len(steps) - 1,
            "state": step["state"],
            "concept": step["concept"],
            "what_to_listen_for": step["what_to_listen_for"],
            "error": None,
        }

    # action == "summarize"
    steps_passed = input.get("steps_passed", [])
    step_failed = input.get("step_failed")

    if not isinstance(steps_passed, list):
        return _error(action, session_id, "steps_passed must be a list of step IDs.")

    valid_ids = {s["id"] for s in steps}

    unknown = [sid for sid in steps_passed if sid not in valid_ids]
    if unknown:
        return _error(action, session_id, f"Unknown step IDs in steps_passed: {unknown}")

    if step_failed is not None and step_failed not in valid_ids:
        return _error(action, session_id, f"Unknown step ID in step_failed: {step_failed!r}")

    strengths = [
        {"id": s["id"], "concept": s["concept"]}
        for s in steps if s["id"] in steps_passed
    ]

    if step_failed is None:
        gap = None
    else:
        failed_step = next(s for s in steps if s["id"] == step_failed)
        gap = {
            "id": failed_step["id"],
            "concept": failed_step["concept"],
            "remediation_hint": failed_step["remediation_hint"],
        }

    return {
        "action": "summarize",
        "session_id": session_id,
        "gap": gap,
        "strengths": strengths,
        "error": None,
    }


def _error(action, session_id, msg):
    return {
        "action": action,
        "session_id": session_id,
        "error": msg,
    }
