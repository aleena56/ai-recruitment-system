def handle_layout(text):

    # Replace table separators
    text = text.replace("|", " ")

    # Reduce excessive spacing from column layouts
    while "    " in text:
        text = text.replace("    ", " ")

    return text