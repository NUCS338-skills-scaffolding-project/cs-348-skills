import sys
sys.path.append("../skills/decompose-the-problem")
sys.path.append("../skills/redirect-direct-solution-requests")

import importlib.util, os

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
