def normalize_jd_text(text):
    replacements = {
        "yrs": "years",
        "yr": "year",
        "b.tech": "btech",
        "b.e": "be",
        "m.sc": "msc"
    }

    text = text.lower()

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text