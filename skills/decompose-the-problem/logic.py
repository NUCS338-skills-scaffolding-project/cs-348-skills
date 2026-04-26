def run(input):
    """
    Detects which sub-problem the student is stuck on and returns a targeted guiding question.

    :param input: dict with key "message" (str) — the student's message
    :return: dict with key "prompt" (str) — the tutor's guiding question
    """
    message = input.get("message", "").lower()

    overwhelm_phrases = [
        "don't know where to start", "no idea where", "overwhelmed",
        "too much", "what do i do", "where do i start", "what should i do first",
        "i'm lost", "i'm confused", "don't know what to do"
    ]
    sorting_phrases = [
        "sort", "order the array", "in place", "ascending", "swap",
        "no .sort", "without sort", "can't use sort"
    ]
    mean_phrases = ["mean", "average", "floor", "floor division", "rounded down"]
    median_phrases = ["median", "middle", "even array", "even length", "two middle"]
    mode_phrases = ["mode", "most common", "most frequent", "tie", "lowest value"]

    if any(phrase in message for phrase in overwhelm_phrases):
        return {
            "prompt": (
                "It sounds like the function has a lot of moving parts. "
                "Let's slow down — what are the two main things the function "
                "is supposed to produce when it finishes running?"
            )
        }

    if any(phrase in message for phrase in sorting_phrases):
        return {
            "prompt": (
                "Sorting without built-ins is a great place to focus. "
                "Think about how you would sort a hand of playing cards by hand — "
                "what's the very first comparison you would make?"
            )
        }

    if any(phrase in message for phrase in mean_phrases):
        return {
            "prompt": (
                "If someone read you five numbers out loud and asked for the average, "
                "what two things would you need to keep track of as you listened? "
                "And once you have those, how do you get the final answer?"
            )
        }

    if any(phrase in message for phrase in median_phrases):
        return {
            "prompt": (
                "If you had a sorted list of five numbers, how would you find the middle one? "
                "Now what changes if the list has six numbers instead — "
                "how would you pick which value counts as the median?"
            )
        }

    if any(phrase in message for phrase in mode_phrases):
        return {
            "prompt": (
                "If you were going through a list and counting how many times each number appeared, "
                "what would you write down to keep track? "
                "And if two numbers appeared the same number of times, how would you decide which one to return?"
            )
        }

    return {
        "prompt": (
            "Which part of the function feels most separate from the rest — "
            "sorting, or one of the three statistics? "
            "Let's start with whichever one feels clearest to you."
        )
    }
