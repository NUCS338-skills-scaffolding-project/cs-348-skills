def _check_forbidden_module(code, requirement):
    module = requirement["value"]
    violations = []
    for i, line in enumerate(code.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith(f"import {module}") or stripped.startswith(f"from {module}"):
            violations.append({
                "requirement": requirement,
                "detail": f"Forbidden module '{module}' imported on line {i}: {line.strip()}",
            })
    return violations


def _check_restricted_section(code, requirement):
    marker = requirement["value"]
    violations = []
    lines = code.splitlines()
    for i, line in enumerate(lines, start=1):
        if marker in line:
            violations.append({
                "requirement": requirement,
                "detail": f"Restricted section marker '{marker}' found on line {i} — this area must not be modified.",
            })
    return violations


def _check_required_element(code, requirement):
    token = requirement["value"]
    if token not in code:
        return [{
            "requirement": requirement,
            "detail": f"Required element '{token}' was not found anywhere in the submission.",
        }]
    return []


def run(input):
    """
    Checks student code against a list of assignment requirements.
    :param input: dict with keys:
        - "student_code" (str): the full source of the student's submission
        - "requirements" (list of dict): each has "type", "value", "description"
    :return: dict with "passed" bool, "violations" list, and "summary" str
    """
    code = input.get("student_code", "")
    requirements = input.get("requirements", [])

    violations = []
    for req in requirements:
        req_type = req.get("type")
        if req_type == "forbidden_module":
            violations.extend(_check_forbidden_module(code, req))
        elif req_type == "restricted_section":
            violations.extend(_check_restricted_section(code, req))
        elif req_type == "required_element":
            violations.extend(_check_required_element(code, req))

    passed = len(violations) == 0

    if passed:
        summary = "All requirements passed. No violations detected."
    else:
        lines = [f"Found {len(violations)} violation(s):"]
        for v in violations:
            lines.append(f"  - [{v['requirement']['description']}] {v['detail']}")
        summary = "\n".join(lines)

    return {
        "passed": passed,
        "violations": violations,
        "summary": summary,
    }
