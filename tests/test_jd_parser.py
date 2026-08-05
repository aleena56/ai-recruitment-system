from parsers.jd_parser import parse_job_description

def test_jd_parsing():
    sample_jd = """
    Hiring Data Analyst with Python, SQL, and Excel skills.
    Candidates should have 1-3 years of experience.
    BTech or MSc preferred.
    """

    result = parse_job_description(sample_jd)

    assert "python" in result["required_skills"]
    assert result["experience_requirements"]["minimum_years"] == 1
    assert "BTECH" in result["education_preferences"]