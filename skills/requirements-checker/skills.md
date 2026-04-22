---
skill_id: "requirements-checker"
name: "Requirements Checker"
skill_type: "code"
tags: ["requirements", "validation", "forbidden-modules", "academic-integrity", "code-checking"]
python_entry: "logic.py"
---

# Requirements Checker

## Description
Silently checks whether student code meets assignment requirements. Detects violations such as use of forbidden modules, modification of restricted code areas, or missing required components. Runs in the background and reports back with a precise list of which requirements were violated and where.

## Skill Type
- **Type:** code
- **Course Focus:** CS

## When to Trigger
- Before a student submits their assignment
- When an instructor wants to validate code against a rubric
- When the system needs to verify that restricted sections have not been tampered with
- On any automated code submission pipeline

---
<!-- FOR CODE SKILLS: Complete this section -->

## Inputs
The `run` function expects a dict with:
- `student_code` (str): The full source code of the student's submission
- `requirements` (list of dict): Each requirement has:
  - `type` (str): One of `"forbidden_module"`, `"restricted_section"`, or `"required_element"`
  - `value` (str): The module name, section marker, or required token to check for
  - `description` (str): Human-readable description of the requirement

## Outputs
Returns a dict with:
- `passed` (bool): True if all requirements are satisfied
- `violations` (list of dict): Each violation contains `requirement` (the original requirement dict) and `detail` (a string explaining what was found)
- `summary` (str): A plain-English summary of the results

## Usage
```python
from logic import run

result = run({
    "student_code": "import os\n\ndef solution():\n    pass\n",
    "requirements": [
        {
            "type": "forbidden_module",
            "value": "os",
            "description": "The 'os' module is not allowed in this assignment."
        }
    ]
})
print(result["summary"])
```

## Notes
- `restricted_section` checks look for markers like `# DO NOT MODIFY` or specific function names that should remain unchanged
- `required_element` checks look for the presence of a specific keyword, function call, or token in the code
- The checker does not execute student code — it performs static text analysis only
