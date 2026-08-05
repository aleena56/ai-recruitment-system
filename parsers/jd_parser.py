import json
import os

from parsers.jd_cleaner import clean_jd_text
from parsers.jd_normalizer import normalize_jd_text
from parsers.synonym_detector import (
    detect_skill_synonyms,
    detect_role_variations
)
from parsers.jd_extractor import (
    extract_required_skills,
    extract_experience,
    extract_education
)

def parse_job_description(jd_text):
    cleaned = clean_jd_text(jd_text)
    normalized = normalize_jd_text(cleaned)

    skills = extract_required_skills(normalized)
    synonym_skills = detect_skill_synonyms(normalized)

    all_skills = list(set(skills + synonym_skills))

    roles = detect_role_variations(normalized)
    experience = extract_experience(normalized)
    education = extract_education(normalized)

    return {
        "job_title": roles[0] if roles else "unknown",
        "required_skills": all_skills,
        "experience_requirements": experience,
        "education_preferences": education,
        "normalized_text": normalized
    }

def save_jd_profile(profile, file_name):
    os.makedirs("data/jd_structured", exist_ok=True)

    output_file = f"data/jd_structured/{file_name}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)

    return output_file
