SKILL_SYNONYMS = {
    "python": ["py", "python programming"],
    "sql": ["mysql", "postgresql", "sql server"],
    "power bi": ["powerbi"],
    "machine learning": ["ml", "predictive modeling"]
}

ROLE_VARIATIONS = {
    "data analyst": [
        "junior data analyst",
        "business analyst",
        "reporting analyst"
    ],
    "python developer": [
        "backend developer",
        "software engineer python"
    ]
}

def detect_skill_synonyms(text):
    detected = set()

    for standard, synonyms in SKILL_SYNONYMS.items():
        if standard in text:
            detected.add(standard)

        for synonym in synonyms:
            if synonym in text:
                detected.add(standard)

    return list(detected)

def detect_role_variations(text):
    detected = []

    for standard, variations in ROLE_VARIATIONS.items():
        if standard in text:
            detected.append(standard)

        for role in variations:
            if role in text:
                detected.append(standard)

    return list(set(detected))