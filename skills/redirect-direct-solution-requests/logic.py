def run(input):
    """
    Detects direct solution request phrases and returns a warm Socratic redirect.

    :param input: dict with key "message" (str) — the student's message
    :return: dict with key "prompt" (str) — the tutor's redirecting question
    """
    message = input.get("message", "").lower()

    sorting_phrases = [
        "sort", "order the array", "swap", "bubble", "ascending",
        "without .sort", "without sort", "in place"
    ]
    mean_phrases = ["mean", "average", "floor division", "rounded down"]
    median_phrases = ["median", "middle value", "even array", "two middle"]
    mode_phrases = ["mode", "most common", "most frequent", "lowest mode"]
    give_up_phrases = [
        "give up", "just finish", "finish it for me", "do it for me",
        "write it for me", "complete it", "just complete"
    ]

    if any(phrase in message for phrase in sorting_phrases):
        return {
            "prompt": (
                "Sorting by hand is actually pretty intuitive — "
                "if you had a pile of numbered cards and had to put them in order, "
                "what would you do first?"
            )
        }

    if any(phrase in message for phrase in mean_phrases):
        return {
            "prompt": (
                "If a friend read you a list of numbers and asked for the average, "
                "what two things would you scribble down as you listened? "
                "How do those two things combine into the final answer?"
            )
        }

    if any(phrase in message for phrase in median_phrases):
        return {
            "prompt": (
                "Imagine laying out a sorted row of five poker chips and finding the middle one — "
                "how do you know which chip that is? "
                "What would you do differently if there were six chips instead of five?"
            )
        }

    if any(phrase in message for phrase in mode_phrases):
        return {
            "prompt": (
                "Say you were tallying votes and two candidates tied — "
                "how would you decide which one wins in this function's rules? "
                "What does the spec say to do in that case?"
            )
        }

    if any(phrase in message for phrase in give_up_phrases):
        return {
            "prompt": (
                "Totally fair to feel stuck — this function has a lot of pieces. "
                "What's the last part you felt confident about? "
                "Let's pick it back up from there."
            )
        }

    # Generic redirect: student asked for code/answer without specifying a topic
    return {
        "prompt": (
            "Working through it together is more useful than just seeing the answer. "
            "Which part of the function were you trying to tackle — "
            "the sorting, or one of the three statistics?"
        )
    }
