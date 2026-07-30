from ats_engine.ats_matcher import calculate_match
from screening_ai.screening_engine import screen_candidate
from scoring.scoring_engine import calculate_final_score
from scoring.final_decision import hiring_decision

# Sample data
resume = ["Python", "SQL", "Power BI"]
job = ["Python", "SQL", "Machine Learning"]

# ATS Engine
ats_score = calculate_match(resume, job)

# Screening AI
screening_result = screen_candidate(ats_score)

# Final Scoring
final_score = calculate_final_score(
    ats=ats_score,
    screening=70,
    interview=82,
    behavior=90
)

# Hiring Decision
decision = hiring_decision(final_score)

print("=== AI Recruitment System ===")
print(f"ATS Score: {ats_score}%")
print(f"Screening: {screening_result}")
print(f"Final Score: {final_score}")
print(f"Decision: {decision}")