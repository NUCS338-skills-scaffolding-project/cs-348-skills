FRUSTRATION_SIGNALS = [
    "i've tried everything",
    "nothing works",
    "i don't know",
    "i give up",
    "i keep changing",
    "i just changed",
    "random",
    "i don't understand",
    "it still fails",
    "why isn't this working",
    "i hate this",
]


def run(input):
    """
    Detects signs of frustration or trial-and-error behavior and returns
    a structured intervention guide.
    :param input: dict with keys:
        - "student_message" (str): the student's latest message
        - "recent_changes" (list of str, optional): recent code changes the student made
    :return: dict with "frustration_detected" bool, "intervention_steps" list, and "opening_prompt" str
    """
    message = input.get("student_message", "").lower()
    recent_changes = input.get("recent_changes", [])

    signals_found = [s for s in FRUSTRATION_SIGNALS if s in message]
    frustration_detected = len(signals_found) > 0 or len(recent_changes) >= 3

    intervention_steps = [
        "Acknowledge the student's frustration without judgment.",
        "Ask the student to stop changing code and describe in plain English what the code is supposed to do.",
        "Ask: 'What does your code currently do?' and 'What did you expect it to do?'",
        "Help the student identify the smallest piece of code that behaves incorrectly.",
        "Suggest one concrete debugging step: add a print statement, trace through manually, or check one assumption.",
    ]

    opening_prompt = (
        "I hear you — that kind of loop is really frustrating. "
        "Let's take a step back from the code. Without looking at it, "
        "can you tell me in plain English what this part of your program is supposed to do?"
    )

    return {
        "frustration_detected": frustration_detected,
        "signals_found": signals_found,
        "intervention_steps": intervention_steps,
        "opening_prompt": opening_prompt,
    }
