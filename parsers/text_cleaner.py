import re

def clean_text(text):

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted symbols
    text = re.sub(r"[^\w\s\.\,\-\:\n]", " ", text)

    # Remove repeated new lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()