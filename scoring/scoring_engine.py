from utils.logger import logger

def calculate_final_score(ats, screening, interview, behavior):
    """
    Calculate final weighted score.
    """

    final_score = (
        ats * 0.30 +
        screening * 0.20 +
        interview * 0.35 +
        behavior * 0.15
    )

    logger.info(f"Final Score Calculated: {final_score}")

    return round(final_score, 2)