import os
import markdown
from flask import Flask, render_template, request

from parser import extract_text
from ai_feedback import analyze_resume
from ats_score import calculate_match_score

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

import re

def get_experience(text):
    text = text.lower()

    match = re.search(r'(\d+)\+?\s*(year|years|yr|yrs)', text)

    if match:
        return int(match.group(1))

    return 0


def get_projects(text):
    text = text.lower()

    return text.count("project")


def get_certifications(text):
    text = text.lower()

    return (
        text.count("certification") +
        text.count("certificate") +
        text.count("certified")
    )
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resumes = request.files.getlist("resume")
    job_description = request.form["job_description"]

    all_candidates = []

    for resume in resumes:

        file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
        resume.save(file_path)

        resume_text = extract_text(file_path)

        ats = calculate_match_score(
            resume_text,
            job_description
        )

        # -------- Resume Summary (Without Gemini) --------

        summary = resume_text.replace("\n", " ")
        summary = " ".join(summary.split()[:70]) + "..."

        all_candidates.append({

    "name": resume.filename,

    "score": ats["score"],

    "experience": get_experience(resume_text),

    "projects": get_projects(resume_text),

    "certifications": get_certifications(resume_text),

    "matched_skills": ats["matched"],

    "missing_skills": ats["missing"],

    "matched_weight": ats["matched_weight"],

    "total_weight": ats["total_weight"],

    "resume_text": resume_text,

    "summary": summary,

    "result": ""

})

    # ---------------- Sort ----------------

    all_candidates.sort(
    key=lambda x: (
        x["score"],
        x["experience"],
        x["projects"],
        x["certifications"]
    ),
    reverse=True
)

    # -------------- Best Candidate AI -------------

    if all_candidates:

        best_candidate = all_candidates[0]

        ai_result = analyze_resume(

            best_candidate["resume_text"],
            job_description

        )

        ai_result = markdown.markdown(ai_result)

        best_candidate["result"] = ai_result

    else:

        best_candidate = None

    # ---------------- Dashboard ----------------

    total_candidates = len(all_candidates)

    highest_score = max(
        (candidate["score"] for candidate in all_candidates),
        default=0
    )

    average_score = round(

        sum(candidate["score"] for candidate in all_candidates)

        / total_candidates,

        1

    ) if total_candidates else 0

    recommended = sum(

        1

        for candidate in all_candidates

        if candidate["score"] >= 75

    )

    return render_template(

        "index.html",

        all_candidates=all_candidates,

        total_candidates=total_candidates,

        highest_score=highest_score,

        average_score=average_score,

        recommended=recommended,

        best_candidate=best_candidate

    )

if __name__ == "__main__":
    app.run(debug=True)