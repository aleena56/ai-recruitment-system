from scoring.scoring_engine import calculate_final_score

score = calculate_final_score(
    ats=66.67,
    screening=70,
    interview=82,
    behavior=90
)

print(f"Final Candidate Score: {score}")