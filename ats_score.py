import re
from skills import SKILL_WEIGHTS


def extract_skills(text):
    """
    Extract skills from any text (resume or job description).
    """

    text = text.lower()

    found_skills = set()

    for skill in SKILL_WEIGHTS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return found_skills


def calculate_match_score(resume_text, job_description):

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    matched = resume_skills.intersection(jd_skills)

    missing = jd_skills - matched

    total_weight = 0
    matched_weight = 0

    for skill in jd_skills:
        total_weight += SKILL_WEIGHTS[skill]

    for skill in matched:
        matched_weight += SKILL_WEIGHTS[skill]

    if total_weight == 0:
        score = 0
    else:
        score = round((matched_weight / total_weight) * 100)

# Bonus points
    if "2 years" in resume_text.lower():
       score += 2

    if "aws certification" in resume_text.lower():
        score += 2

    score = min(score,100)

    return {
    "score": score,
    "matched": sorted(list(matched)),
    "missing": sorted(list(missing)),
    "matched_weight": matched_weight,
    "total_weight": total_weight
}

