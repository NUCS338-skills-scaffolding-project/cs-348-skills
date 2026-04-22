import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

result = run({
    "student_message": "I've tried everything and nothing works. I keep changing the value but it still fails.",
    "recent_changes": ["changed line 12", "changed line 15", "changed line 12 again"],
})

print("=== Problem Solving Prompting Demo ===")
print(f"Frustration detected: {result['frustration_detected']}")
print(f"Signals found: {result['signals_found']}")
print()
print("Opening prompt for student:")
print(f"  \"{result['opening_prompt']}\"")
print()
print("Intervention steps:")
for i, step in enumerate(result["intervention_steps"], start=1):
    print(f"  {i}. {step}")
