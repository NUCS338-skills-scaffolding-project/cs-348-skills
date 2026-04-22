import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import run

instructions = """
Assignment 3: Graph Traversal
Implement BFS and DFS on an adjacency list representation of a directed graph.
Your program should find shortest paths using BFS and detect cycles using DFS.
Handle disconnected graphs and return results for all connected components.
"""

starter_code = """
def build_graph(edges):
    pass

def bfs(graph, start):
    pass

def dfs(graph, start, visited=None):
    pass

def find_shortest_path(graph, source, target):
    pass

def detect_cycle(graph):
    pass
"""

result = run({
    "instructions": instructions,
    "starter_code": starter_code,
})

print("=== Code Planner Demo ===")
print(f"Function stubs found: {result['function_stubs']}")
print(f"Assignment prompt word count: {result['instruction_word_count']}")
print()
print("Planning questions to work through:")
for i, q in enumerate(result["planning_questions"], start=1):
    print(f"  {i}. {q}")
