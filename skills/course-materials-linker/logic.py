def run(input):
    """
    Aggregates and links course materials relevant to an assignment or concept.
    :param input: dict with keys:
        - "topic" (str): the assignment name or concept to search for
        - "materials" (list of dict): each has "title", "type", and "description"
    :return: dict with "relevant_materials" list and "suggested_order" list
    """
    topic = input.get("topic", "").lower()
    materials = input.get("materials", [])

    relevant = []
    for material in materials:
        title = material.get("title", "").lower()
        description = material.get("description", "").lower()
        if topic in title or topic in description:
            relevant.append(material)

    suggested_order = sorted(
        relevant,
        key=lambda m: {"slides": 0, "notes": 1, "reading": 2, "supplementary": 3}.get(
            m.get("type", "supplementary"), 3
        ),
    )

    return {
        "relevant_materials": relevant,
        "suggested_order": [m["title"] for m in suggested_order],
        "count": len(relevant),
    }
