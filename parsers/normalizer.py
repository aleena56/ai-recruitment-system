SECTION_HEADINGS = [
    "education",
    "experience",
    "skills",
    "projects",
    "certifications",
    "summary"
]

def normalize_text(text):

    bullets = ["•", "●", "▪", "■", "►"]

    for bullet in bullets:
        text = text.replace(bullet, "- ")

    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.lower() in SECTION_HEADINGS:
            line = line.upper()

        lines.append(line)

    return "\n".join(lines)