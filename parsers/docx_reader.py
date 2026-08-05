from docx import Document

def read_docx(file_path):
    text = ""

    doc = Document(file_path)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text