def run(input):
    """
    Detects lack of edge case consideration and prompts the student
    to think about boundary conditions.
    """
    message = input.get("message", "").lower()

    confident_phrases = [
        "it works", "works fine", "i think it's correct",
        "passes tests", "should be right"
    ]

    confusion_phrases = [
        "why is this failing", "not working sometimes",
        "random error", "fails on some inputs"
    ]

    if any(p in message for p in confident_phrases):
        return {
            "prompt": (
                "Nice — you've tested the normal case. "
                "What happens if your input is empty or much smaller than expected?"
            )
        }

    if any(p in message for p in confusion_phrases):
        return {
            "prompt": (
                "Interesting — bugs like that often come from edge cases. "
                "Have you tried inputs like empty data, duplicates, or extreme values?"
            )
        }

    return {
        "prompt": (
            "Before assuming it works, what are some unusual or boundary inputs "
            "you haven't tested yet?"
        )
    }