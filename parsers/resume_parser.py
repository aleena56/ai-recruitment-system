import os
import json

from parsers.pdf_reader import read_pdf
from parsers.docx_reader import read_docx
from parsers.text_cleaner import clean_text
from parsers.normalizer import normalize_text
from parsers.layout_handler import handle_layout

def parse_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        raw_text = read_pdf(file_path)

    elif ext == ".docx":
        raw_text = read_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    text = handle_layout(raw_text)
    text = clean_text(text)
    text = normalize_text(text)

    return {
        "file_name": os.path.basename(file_path),
        "raw_text": raw_text,
        "clean_text": text
    }

def save_extracted_resume(parsed_data):

    os.makedirs("data/structured", exist_ok=True)

    output_file = f"data/structured/{parsed_data['file_name']}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=4)

    return output_file