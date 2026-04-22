ERROR_EXPLANATIONS = {
    "NameError": (
        "Python tried to use a variable or function name that hasn't been defined yet. "
        "Check that you created the variable before using it, and that it's in the same scope."
    ),
    "TypeError": (
        "An operation was applied to the wrong type of value — for example, adding a string to an integer. "
        "Check what types your variables actually hold at that point."
    ),
    "IndexError": (
        "You tried to access a list position that doesn't exist. "
        "Check the length of your list and the index you're using."
    ),
    "KeyError": (
        "You tried to look up a key in a dictionary that doesn't exist. "
        "Check whether the key is actually in the dictionary before accessing it."
    ),
    "AttributeError": (
        "You called a method or accessed a property that doesn't exist on that object. "
        "Check the type of the object and the correct method names for it."
    ),
    "SyntaxError": (
        "Python couldn't parse your code because of a grammatical mistake. "
        "Look at the line number in the error — check for missing colons, brackets, or mismatched quotes."
    ),
    "IndentationError": (
        "Your code has inconsistent indentation. "
        "Make sure each block is indented consistently (all spaces or all tabs, not mixed)."
    ),
    "ValueError": (
        "A function received an argument of the right type but an inappropriate value. "
        "Check what value you are passing and what range or format the function expects."
    ),
    "ZeroDivisionError": (
        "Your code attempted to divide by zero. "
        "Check the denominator before performing division."
    ),
    "ImportError": (
        "Python could not find the module you tried to import. "
        "Check that the module name is spelled correctly and that it is installed."
    ),
}

GENERAL_TIPS = [
    "Always read the last line of a traceback first — that is the actual error.",
    "The line number in the traceback tells you where Python noticed the problem, which may differ from where the bug actually is.",
    "The error type (e.g., NameError, TypeError) tells you the category of the problem — use it to narrow your search.",
    "If the traceback is long, find YOUR code in it (not library code) and start there.",
]


def run(input):
    """
    Explains a Python error message and provides general tips for reading errors.
    :param input: dict with keys:
        - "error_message" (str): the full error text or traceback
        - "code_context" (str, optional): relevant lines of student code
    :return: dict with "error_type", "explanation", "general_tips", and "guiding_question"
    """
    error_message = input.get("error_message", "")
    error_type = "Unknown"

    for known_type in ERROR_EXPLANATIONS:
        if known_type in error_message:
            error_type = known_type
            break

    explanation = ERROR_EXPLANATIONS.get(
        error_type,
        "This error type is not in the common list. Read the message carefully — it usually describes the problem directly.",
    )

    guiding_question = (
        f"Now that you know what a {error_type} means, look at the line number in your error. "
        "What do you think your code is doing at that point that might cause this?"
    )

    return {
        "error_type": error_type,
        "explanation": explanation,
        "general_tips": GENERAL_TIPS,
        "guiding_question": guiding_question,
    }
