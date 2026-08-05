import re

KNOWN_SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "aws",
    "git"
]

KNOWN_DEGREES = [
    "bsc",
    "btech",
    "be",
    "msc",
    "mca",
    "mba"
]

def extract_required_skills(text):
    skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            skills.append(skill)

    return list(set(skills))

def extract_experience(text):
    pattern = r"(\d+)\s*[-to]*\s*(\d+)?\s*years"
    match = re.search(pattern, text)

    if match:
        minimum = int(match.group(1))
        maximum = match.group(2)

        return {
            "minimum_years": minimum,
            "maximum_years": int(maximum) if maximum else minimum
        }

    return {
        "minimum_years": 0,
        "maximum_years": 0
    }

def extract_education(text):
    degrees = []

    for degree in KNOWN_DEGREES:
        if degree in text:
            degrees.append(degree.upper())

    return list(set(degrees))