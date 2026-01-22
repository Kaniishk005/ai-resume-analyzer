def find_missing_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    missing = jd_set - resume_set
    return sorted(missing)
