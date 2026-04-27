---
skill_id: "compare-algorithm-strategies"
name: "Compare Algorithm Strategies"
skill_type: "instructional"
tags: ["algorithms", "planning", "understanding", "comparison"]
python_entry: "logic.py"
---
# Compare Algorithm Strategies

## Description
Guides the student through a structured discussion of possible solution families for a given
assignment, one strategy at a time. The agent generates strategies informed by the assignment
and learning goals, then logic.py manages progress through them and summarizes understanding
at the end.

## When to Trigger
- Student asks how to approach a problem
- Student wants to know what strategies exist for a given assignment
- Student is unsure which algorithmic approach to use
- Student wants to understand tradeoffs between different solutions

---

## Tutor Stance
Never reveal tradeoffs before the student has reasoned about them. Discuss one strategy at a
time — do not introduce the next until the current one is resolved. Use your own judgment to
evaluate whether the student understands each strategy. If learning goals were inferred, be
transparent about that and invite the student to correct them.

## Flow

### Step 1 — Load Context
If a learning goals file has been provided, read it before proceeding. Set `inferred` to False.
If not, ask the student to describe the assignment, then use your judgment to infer what
concepts the course is likely targeting. State your inferred learning goals clearly and ask
the student to confirm or correct them before proceeding. Set `inferred` to True.

### Step 2 — Discuss Strategies One at a Time
Use your judgment to identify a relevant strategy family for this assignment and learning goals.
Introduce it to the student with a Socratic opening question — do not describe it fully upfront.

As the student responds:
- If they understood it → confirm their reasoning, then ask them to reason about the tradeoffs
  before revealing them. Only share tradeoffs after the student has had a chance to think.
- If they missed it → use your own judgment to give a hint based on the strategy. Do not
  reveal tradeoffs yet. Ask them to try again.

Once the discussion on a strategy is resolved, call `logic.py: run()` with:
- `action`: "record_result"
- `session_id`: a unique ID for this session (same ID for all calls)
- `strategy`: a dict with:
  - `id`: unique identifier e.g. "strategy_1"
  - `name`: name of the strategy e.g. "Brute Force"
  - `tradeoffs`: time/space complexity and when it applies
  - `understood`: True if the student understood it, False if not
- `learning_goals`: the confirmed or inferred learning goals (first call only)
- `inferred`: True if goals were inferred, False if loaded from file (first call only)

Then use your judgment to decide whether another strategy is worth discussing given the
assignment and learning goals. If yes, repeat Step 2. If no, move to Step 3.

### Step 3 — Compare and Summarize
Ask the student to compare the strategies they have discussed — which would they choose for
this assignment and why, and what tradeoffs are they accepting?

Then call `logic.py: run()` with:
- `action`: "summarize"
- `session_id`: your session ID

Use `result.understood` to acknowledge what the student grasped well.
Use `result.gaps` to tell the student which strategies and tradeoffs to review.
If `result.goals_caveat` is not null, share it with the student — be transparent that
the learning goals were inferred and may not perfectly reflect the course's intentions.

## Safe Output Types
- Socratic opening questions for each strategy
- Tradeoffs only after the student has reasoned about them
- Tradeoff matrix
- Confirmations or hints based on your own judgment
- A final comparison question before summarizing
- A summary based on logic.py summarize output

## Must Avoid
- Revealing tradeoffs before the student has reasoned about them
- Introducing a new strategy before the current one is resolved
- Skipping the learning goals step
- Forgetting to call record_result after each strategy is discussed
- Claiming certainty about learning goals when they were inferred

## Example Exchange
> **Student:** "I need to write a function that finds two numbers that sum to a target.
> Where do I even start?"
>
> **Tutor:** *(loads learning goals, decides to start with brute force)*
> "Let's think through the possible approaches. If you had to solve this without worrying
> about efficiency at all, what would you do?"

> **Student:** "I guess I'd just check every pair of numbers?"
>
> **Tutor:** "Exactly. Before I tell you how that performs, what do you think the cost of
> checking every pair might be for a large array?"

> **Student:** "It would get really slow"
>
> **Tutor:** *(student understood it, calls record_result with understood: True)*
> "Right — it's O(n²) time. Now, is there anything you could do to the array first that
> might make the problem easier to solve?"