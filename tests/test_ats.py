from ats_engine.ats_matcher import calculate_match

resume = ["Python", "SQL", "Power BI"]
job = ["Python", "SQL", "Machine Learning"]

score = calculate_match(resume, job)

print(f"ATS Score: {score}%")