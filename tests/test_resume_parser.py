from parsers.resume_parser import parse_resume, save_extracted_resume

def test_pdf_resume():
    result = parse_resume("data/raw/sample_resume.pdf")
    assert "clean_text" in result
    assert len(result["clean_text"]) > 0

def test_docx_resume():
    result = parse_resume("data/raw/sample_resume.docx")
    assert "clean_text" in result
    assert len(result["clean_text"]) > 0

def test_save_resume():
    sample = {
        "file_name": "test_resume",
        "raw_text": "Sample text",
        "clean_text": "Sample text"
    }

    output = save_extracted_resume(sample)
    assert output.endswith(".json")