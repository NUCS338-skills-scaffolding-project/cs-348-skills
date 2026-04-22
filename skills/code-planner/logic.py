def run(input):
    """
    Analyzes assignment instructions and skeleton code to produce a planning guide.
    :param input: dict with keys:
        - "instructions" (str): the assignment prompt text
        - "starter_code" (str): the skeleton or starter code provided
    :return: dict with "function_stubs" list and "planning_questions" list
    """
    instructions = input.get("instructions", "")
    starter_code = input.get("starter_code", "")

    stubs = []
    for line in starter_code.splitlines():
        stripped = line.strip()
        if stripped.startswith("def "):
            func_name = stripped.split("(")[0].replace("def ", "")
            stubs.append(func_name)

    planning_questions = [
        f"What should `{stub}` receive as input and what should it return?" for stub in stubs
    ]
    planning_questions += [
        "What is the first thing your program needs to do before anything else?",
        "Are there any edge cases in the instructions you should handle?",
        "How do the functions depend on each other — what order should they be called?",
    ]

    return {
        "function_stubs": stubs,
        "planning_questions": planning_questions,
        "instruction_word_count": len(instructions.split()),
    }
