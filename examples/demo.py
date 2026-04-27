import sys
import importlib.util
import os

def load_skill(skill_path):
    spec = importlib.util.spec_from_file_location("logic", skill_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
decompose = load_skill(os.path.join(root, "skills", "decompose-the-problem", "logic.py"))
redirect  = load_skill(os.path.join(root, "skills", "redirect-direct-solution-requests", "logic.py"))

# ── decompose-the-problem ──────────────────────────────────────────────
print("=== decompose-the-problem ===\n")

decompose_cases = [
    "I don't know where to start with this function at all.",
    "I kind of get the stats part but I don't know how to sort without .sort().",
    "I'm stuck on the median — I'm not sure what to do for even-length arrays.",
]

for msg in decompose_cases:
    result = decompose.run({"message": msg})
    print(f"Student: {msg}")
    print(f"Tutor:   {result['prompt']}\n")

# ── redirect-direct-solution-requests ─────────────────────────────────
print("=== redirect-direct-solution-requests ===\n")

redirect_cases = [
    "Can you just write the sort for me? I don't get it.",
    "Just tell me how to compute the mode, what's the answer?",
    "I give up, can you just finish the whole function?",
]

for msg in redirect_cases:
    result = redirect.run({"message": msg})
    print(f"Student: {msg}")
    print(f"Tutor:   {result['prompt']}\n")

# ── explain-edge-cases ────────────────────────────────────────────────
edge = load_skill(os.path.join(root, "skills", "explain-edge-cases", "logic.py"))

print("=== explain-edge-cases ===\n")

cases = [
    "My code works fine for most inputs.",
    "It fails sometimes but I don't know why.",
]

for msg in cases:
    result = edge.run({"message": msg})
    print(f"Student: {msg}")
    print(f"Tutor:   {result['prompt']}\n")

compare = load_skill(os.path.join(root, "skills", "compare-algorithm-strategies", "logic.py"))
trace = load_skill(os.path.join(root, "skills", "trace-an-algo", "logic.py"))

# ── compare-algorithm-strategies ───────────────────────────────────────
print("=== compare-algorithm-strategies ===\n")

# Test the registration action
register_result = compare.run({
    "action": "register_strategies",
    "session_id": "test-compare-1",
    "assignment": "Find a path from robot start to goal in a grid using search",
    "learning_goals": ["search strategy tradeoffs", "DFS vs BFS exploration", "frontier management"],
    "inferred": True,
    "strategies": [
        {
            "id": "strategy_1",
            "name": "Depth-First Search (DFS)",
            "description": "Use a stack to explore as deep as possible before backtracking",
            "discussion_prompt": "If you keep going in one direction until you hit a dead end, then back up and try another way, what data structure helps you remember where to backtrack?",
            "tradeoffs": "O(V+E) time, O(h) space where h is depth; can use less space but explores less efficiently",
            "what_to_listen_for": "They mention a stack, Last-In-First-Out, or going deep before exploring other branches"
        },
        {
            "id": "strategy_2",
            "name": "Breadth-First Search (BFS)",
            "description": "Use a queue to explore all neighbors at current distance before going deeper",
            "discussion_prompt": "What if instead of going deep, you explored all cells 1 step away, then all cells 2 steps away, and so on?",
            "tradeoffs": "O(V+E) time, O(w) space where w is width; explores more systematically but uses more memory",
            "what_to_listen_for": "They mention a queue, FIFO, or exploring level-by-level"
        }
    ]
})

print(f"Registered {register_result['total_strategies']} strategies")
print(f"Learning goals: {register_result['learning_goals']}\n")

# Get first strategy
strategy_result = compare.run({
    "action": "get_strategy",
    "session_id": "test-compare-1",
    "strategy_index": 0
})

print(f"Strategy {strategy_result['strategy_number']}/{strategy_result['total_strategies']}: {strategy_result['name']}")
print(f"Prompt: {strategy_result['discussion_prompt']}\n")

# ── trace-an-algo ─────────────────────────────────────────────────────
print("=== trace-an-algo ===\n")

# Test the registration action
register_trace_result = trace.run({
    "action": "register_trace",
    "session_id": "test-trace-1",
    "steps": [
        {
            "id": "step_1",
            "state": "Grid with robot at [1,1], goal at [3,3], frontier = {(1,1)}",
            "concept": "Start search at the robot's position",
            "what_to_listen_for": "They mention starting at the robot location [1,1]",
            "remediation_hint": "The search always begins from where the robot is located"
        },
        {
            "id": "step_2",
            "state": "Explore neighbors of [1,1]: right=[1,2], down=[2,1], left=[1,0], up=[0,1]",
            "concept": "Expand node by checking all 4 valid neighbors in search order",
            "what_to_listen_for": "They mention checking right, down, left, up in that order",
            "remediation_hint": "Remember the specific order: right [y,x+1], down [y+1,x], left [y,x-1], up [y-1,x]"
        },
        {
            "id": "step_3",
            "state": "Mark explored cells with 4, keep frontier updated",
            "concept": "Track which cells you've already visited to avoid revisiting",
            "what_to_listen_for": "They mention marking visited cells or checking if a cell was already explored",
            "remediation_hint": "Use the map itself or a visited set to remember which cells you've seen"
        }
    ]
})

print(f"Registered trace with {register_trace_result['total_steps']} steps\n")

# Get first step
step_result = trace.run({
    "action": "get_step",
    "session_id": "test-trace-1",
    "step_index": 0
})

print(f"Step {step_result['step_number']}/{step_result['total_steps']}: {step_result['state']}")
print(f"Concept to understand: {step_result['concept']}")
print(f"Listen for: {step_result['what_to_listen_for']}\n")