import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

result = run({
    "question": "How do I write a BFS to find the shortest path in my graph?",
})

print("=== Code Helper Demo ===")
print(f"Concept found: {result['concept_found']}")
print(f"Matched concept: {result['matched_concept']}")
print()
print("Plain-English explanation (no code):")
print(f"  {result['plain_english']}")
print()
print("Guiding questions for the student:")
for i, q in enumerate(result["key_questions"], start=1):
    print(f"  {i}. {q}")
print()
print("First hint:")
print(f"  {result['first_hint']}")
