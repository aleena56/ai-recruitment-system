from utils.logger import logger

def screen_candidate(ats_score):
    if ats_score >= 70:
        result = "Shortlisted"
    elif ats_score >= 50:
        result = "Review Manually"
    else:
        result = "Rejected"

    logger.info(f"Screening Result: {result}")

    return result