import re

def clean_jd_text(text):
    text = text.replace("\t", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s\.\,\-\:\n]", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()