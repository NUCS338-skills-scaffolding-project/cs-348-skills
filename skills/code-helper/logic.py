CONCEPT_GUIDES = {
    "bfs": {
        "plain_english": (
            "BFS (Breadth-First Search) explores a graph level by level. "
            "Starting from one node, it visits all immediate neighbors first, "
            "then their neighbors, and so on. It uses a queue to keep track of which node to visit next."
        ),
        "key_questions": [
            "What data structure lets you process items in the order they were added?",
            "How will you keep track of nodes you've already visited?",
            "What should happen when you reach a node that has no unvisited neighbors?",
        ],
        "first_hint": "Think about what you add to your queue at the very start, before any iteration begins.",
    },
    "dfs": {
        "plain_english": (
            "DFS (Depth-First Search) explores as far as possible along one path before backtracking. "
            "It uses a stack (or recursion) to remember where to go back when a path ends."
        ),
        "key_questions": [
            "What data structure naturally supports backtracking?",
            "How is the order you process nodes different from BFS?",
            "What is your base case if you implement this recursively?",
        ],
        "first_hint": "Think about what it means to 'go as deep as possible' before moving to a sibling node.",
    },
    "hash table": {
        "plain_english": (
            "A hash table stores key-value pairs. It uses a hash function to convert a key into an index, "
            "then stores the value at that index. This gives very fast average-case lookups."
        ),
        "key_questions": [
            "What happens if two different keys hash to the same index?",
            "Why do lookups in a hash table tend to be faster than in a list?",
            "What kinds of keys can be hashed, and what kinds cannot?",
        ],
        "first_hint": "Think about what makes a good hash function — what properties should it have?",
    },
    "recursion": {
        "plain_english": (
            "Recursion is when a function calls itself to solve a smaller version of the same problem. "
            "Every recursive function needs a base case (the simplest version it can solve directly) "
            "and a recursive case (where it breaks the problem down and calls itself)."
        ),
        "key_questions": [
            "What is the smallest version of this problem that you can solve directly?",
            "How does calling the function on a smaller input get you closer to that base case?",
            "What do you do with the result that the recursive call returns?",
        ],
        "first_hint": "Start by writing the base case first — what input makes the problem trivially easy to solve?",
    },
}


def run(input):
    """
    Returns a Socratic guide for a conceptual coding question without producing any code.
    :param input: dict with keys:
        - "question" (str): the student's conceptual question
        - "topic" (str, optional): explicit topic if known (e.g., "bfs", "recursion")
    :return: dict with "concept_found" bool, "plain_english", "key_questions", and "first_hint"
    """
    question = input.get("question", "").lower()
    topic_key = input.get("topic", "").lower()

    guide = None
    matched_concept = None

    if topic_key in CONCEPT_GUIDES:
        guide = CONCEPT_GUIDES[topic_key]
        matched_concept = topic_key
    else:
        for concept, content in CONCEPT_GUIDES.items():
            if concept in question:
                guide = content
                matched_concept = concept
                break

    if guide:
        return {
            "concept_found": True,
            "matched_concept": matched_concept,
            "plain_english": guide["plain_english"],
            "key_questions": guide["key_questions"],
            "first_hint": guide["first_hint"],
        }

    return {
        "concept_found": False,
        "matched_concept": None,
        "plain_english": "I don't have a built-in guide for that concept yet.",
        "key_questions": [
            "Can you describe in your own words what you think this concept does?",
            "What part of it is most confusing to you right now?",
        ],
        "first_hint": "Let's start from what you already know and build from there.",
    }
