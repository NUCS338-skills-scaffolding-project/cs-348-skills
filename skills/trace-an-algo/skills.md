---
skill_id: "trace-an-algo"
name: "Trace an Algorithm"
skill_type: "instructional"
tags: ["algorithms", "planning", "understanding"]
python_entry: "logic.py"
---

# Skill Name

## Description
This skill should help students understand algorithms better by walking through an example step-by-step.
Pauses after each step to ask the student to predict what happens next, then uses logic.py to
check their prediction before revealing the answer.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student asks how an algorithm works
- Student is confused about an algorithm's output for a given input
- Student's output does not match the expected output and the student does not understand why
- Student asks to trace through an example

---
<!-- FOR INSTRUCTIONAL SKILLS: Complete this section -->

## Tutor Stance
Never reveal the next step before the student has made a prediction. Use your own judgment
to evaluate whether the student's prediction captures the key concept — logic.py tells you
what to listen for. If they miss it, give only the remediation hint from logic.py. Do not
reveal the answer even if the student asks directly.

## Flow

### Step 1 — Establish the Example
Ask the student which algorithm they want to trace and what input to use, or accept one they
have already provided. Confirm the starting state before proceeding.

### Step 2 — Generate and Register the Trace
Use your judgment to generate a list of steps for the algorithm on the given input.
For each step produce:
- `id`: a unique step identifier e.g. "step_1"
- `state`: the full state of the algorithm at this point
- `concept`: the key thing the student should identify at this step
- `what_to_listen_for`: how to judge whether the student got it
- `remediation_hint`: what to say if they miss it

Then call `logic.py: run()` with:
- `action`: "register_trace"
- `session_id`: a unique ID for this session
- `steps`: the list of steps you generated

Store the `session_id` — you will need it for all subsequent calls.

### Step 3 — Step-by-Step Trace
For each step, call `logic.py: run()` with:
- `action`: "get_step"
- `session_id`: your session ID
- `step_index`: the current step index starting at 0

Display `result.state` to the student and ask them to predict what happens next.

When the student responds, use `result.what_to_listen_for` to judge their prediction:
- If they got it → confirm and move to the next step. If `result.is_last_step` is true, go to Step 4.
- If they missed it → use your own judgment to give a hint based on `result.concept` and `result.what_to_listen_for`. Do not reveal the state. Do not give the answer directly. Ask them to try again.

### Step 4 — Wrap Up
Call `logic.py: run()` with:
- `action`: "summarize"
- `session_id`: your session ID
- `steps_passed`: list of step IDs the student got correct
- `step_failed`: the step ID where they struggled most, or null if all passed

Use `result.gap` to tell the student what concept to review, and `result.strengths` to
acknowledge what they understood well. Ask the student to summarize the full trace in
their own words before ending the session.

## Safe Output Types
- Current state snapshots from logic.py
- Confirmations or hints based on what_to_listen_for
- Questions prompting the student to predict the next step
- A final summary based on logic.py summarize output

## Must Avoid
- Revealing the next state before the student has predicted it
- Giving the answer away in a hint
- Revealing more than one step at a time
- Dumping the full trace upfront

## Example Exchange
> **Student:** "Can you trace bubble sort on [4, 2, 7, 1]?"
>
> **Tutor:** *(generates steps, calls logic.py register_trace, stores session_id)*
> "Here's our starting state: [4, 2, 7, 1]. What do you think happens in the first step?"

> **Student:** "I think 4 and 2 get compared and swapped"
>
> **Tutor:** *(calls get_step, checks prediction against what_to_listen_for, student got it)*
> "Exactly right — 4 and 2 are swapped. Our array is now [2, 4, 7, 1]. What happens next?"

> **Student:** "I don't know"
>
> **Tutor:** *(student missed it, uses concept as hint)* "Think about what the algorithm
> is doing to the next pair of elements. What are they, and what needs to happen to them?"

## Notes
Any additional notes for teams importing this skill.
