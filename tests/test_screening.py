from screening_ai.screening_engine import screen_candidate

score = 66.67

result = screen_candidate(score)

print(f"ATS Score: {score}%")
print(f"Screening Decision: {result}")