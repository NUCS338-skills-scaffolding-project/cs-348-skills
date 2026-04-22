import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

materials = [
    {"title": "Lecture 5: SQL Joins", "type": "slides", "description": "Covers inner join, left join, right join with examples"},
    {"title": "Discussion 3 Notes", "type": "notes", "description": "Worked problems using SQL joins and aggregation"},
    {"title": "Lecture 6: Aggregation", "type": "slides", "description": "GROUP BY, HAVING, and aggregate functions"},
    {"title": "Chapter 4: Relational Algebra", "type": "reading", "description": "Deep dive into joins and relational operators"},
    {"title": "Lecture 2: ER Diagrams", "type": "slides", "description": "Entity-relationship modeling and schema design"},
]

result = run({
    "topic": "join",
    "materials": materials,
})

print("=== Course Materials Linker Demo ===")
print(f"Topic searched: 'join'")
print(f"Materials found: {result['count']}")
print()
print("Relevant materials:")
for m in result["relevant_materials"]:
    print(f"  [{m['type'].upper()}] {m['title']}")
    print(f"    -> {m['description']}")
print()
print("Suggested review order:")
for i, title in enumerate(result["suggested_order"], start=1):
    print(f"  {i}. {title}")
