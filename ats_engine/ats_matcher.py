from utils.logger import logger

def calculate_match(resume_skills, jd_skills):
    matched = set(resume_skills).intersection(set(jd_skills))

    score = (len(matched) / len(jd_skills)) * 100

    logger.info(f"ATS Score Calculated: {score}")

    return round(score, 2)