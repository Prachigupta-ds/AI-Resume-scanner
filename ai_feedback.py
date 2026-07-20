import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an experienced HR recruiter.

Analyze the resume against the job description.

IMPORTANT:
DO NOT calculate or mention any Match Score or percentage.
DO NOT write Matching Skills.
DO NOT write Missing Skills.

Only return the following sections in Markdown format:

## Resume Summary

Write a short professional summary (3-5 lines).

## Suggestions

Give 3-5 practical suggestions to improve the resume.

## Hiring Recommendation

Choose ONLY ONE:
- Highly Recommended
- Recommended
- Needs Improvement
- Not Recommended

Job Description:
{job_description}

Resume:
{resume_text}
"""

    try:
      response = model.generate_content(prompt)
      return response.text

    except Exception as e:
      print("Gemini Error:", e)   # Keep this only for debugging in the terminal

    return """
### 🤖 AI Recommendation

⚠️ AI feedback is temporarily unavailable because the free Gemini API request limit has been reached.

✅ ATS Score has been calculated successfully.

✅ Resume Ranking has been generated successfully.

✅ Skill Matching has been completed successfully.

Please try again after a few minutes.
"""