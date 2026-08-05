from parsers.jd_parser import parse_job_description, save_jd_profile

with open("data/jd_raw/data_analyst.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

profile = parse_job_description(jd_text)
output = save_jd_profile(profile, "data_analyst")

print(f"Structured JD saved to: {output}")