import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

result = run({
    "error_message": "Traceback (most recent call last):\n  File \"solution.py\", line 14, in compute_total\n    total += values[i]\nIndexError: list index out of range",
    "code_context": "for i in range(len(values) + 1):\n    total += values[i]",
})

print("=== Python Error Explainer Demo ===")
print(f"Error type identified: {result['error_type']}")
print()
print("Explanation:")
print(f"  {result['explanation']}")
print()
print("General tips for reading Python errors:")
for i, tip in enumerate(result["general_tips"], start=1):
    print(f"  {i}. {tip}")
print()
print("Guiding question for the student:")
print(f"  {result['guiding_question']}")
