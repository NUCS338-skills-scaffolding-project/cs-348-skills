import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

student_code = """
import os
import json

# DO NOT MODIFY — grader helper
def load_test_cases():
    return json.load(open("tests.json"))

def solution(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result
"""

requirements = [
    {
        "type": "forbidden_module",
        "value": "os",
        "description": "The 'os' module is not allowed in this assignment.",
    },
    {
        "type": "restricted_section",
        "value": "DO NOT MODIFY",
        "description": "The grader helper section must not be touched.",
    },
    {
        "type": "required_element",
        "value": "def solution",
        "description": "A function named 'solution' must be present.",
    },
    {
        "type": "required_element",
        "value": "def missing_function",
        "description": "A function named 'missing_function' must be present.",
    },
]

result = run({
    "student_code": student_code,
    "requirements": requirements,
})

print("=== Requirements Checker Demo ===")
print(f"Passed: {result['passed']}")
print()
print("Summary:")
print(result["summary"])
print()
if result["violations"]:
    print(f"Total violations: {len(result['violations'])}")
