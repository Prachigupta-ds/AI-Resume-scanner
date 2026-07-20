# AI-Resume-scanner
This is my AI Scanning Resume and Ranking Candidate project 
Author-Prachi Gupta 
# 🤖 AI Resume Screening and Candidate Ranking System

An AI-powered Resume Screening and Candidate Ranking System built using **Python**, **Flask**, and **Google Gemini AI**. The application automates resume analysis by comparing candidate resumes with a Job Description (JD), calculating ATS scores, ranking candidates, identifying missing skills, generating AI-powered recommendations, and producing PDF reports.

---

## 📌 Project Overview

Recruiters often spend significant time manually reviewing resumes. This project streamlines the recruitment process by automatically analyzing resumes, calculating ATS (Applicant Tracking System) scores, ranking candidates, and providing AI-generated hiring recommendations.

The system extracts text from PDF and DOCX resumes, compares candidate skills against the job description, highlights matching and missing skills, ranks candidates based on weighted ATS scoring, and presents results in an interactive recruiter dashboard.

---

## ✨ Features

- 📄 Upload multiple PDF and DOCX resumes
- 📝 Enter a custom Job Description
- 🎯 Weighted ATS Score Calculation
- 👥 Automatic Candidate Ranking
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- 🤖 AI-Powered Resume Summary using Google Gemini
- 💡 AI Hiring Recommendation
- 📊 Interactive Analytics Dashboard
- 🥇 Best Candidate Highlight
- 📥 PDF Report Generation
- 🎨 Modern Responsive Recruiter Dashboard

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### AI & Libraries
- Google Gemini API
- PyPDF2
- python-docx
- ReportLab
- Markdown

### Visualization
- Chart.js

---

## 📂 Project Structure

```
AI-Resume-Screening-and-Candidate-Ranking-System/
│
├── app.py
├── ats_score.py
├── skills.py
├── resume_parser.py
├── gemini.py
├── report_generator.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── templates/
│   └── index.html
│
├── uploads/
├── reports/
└── screenshots/
```

---

## ⚙️ How It Works

1. Recruiter uploads one or more resumes.
2. Recruiter enters the Job Description.
3. Resume text is extracted.
4. Skills are identified from each resume.
5. ATS score is calculated using weighted skill matching.
6. Candidates are ranked automatically.
7. Google Gemini generates:
   - Resume Summary
   - AI Suggestions
   - Hiring Recommendation
8. Dashboard displays:
   - Candidate Ranking
   - ATS Scores
   - Analytics
   - Best Candidate
9. Recruiter can download a PDF report.

---

## 🧠 ATS Scoring Logic

The ATS score is calculated using weighted skill matching.

```
ATS Score = (Matched Skill Weight / Total JD Skill Weight) × 100
```

If two candidates have the same ATS score, the ranking is determined using:
- Professional Experience
- Number of Projects
- Certifications

---


## 🔮 Future Enhancements

- User Authentication
- Database Integration
- Resume History
- Email Notifications
- Interview Scheduling
- NLP-Based Semantic Matching
- Multi-language Resume Support
- Cloud Deployment

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Flask Web Development
- Resume Parsing
- Google Gemini API Integration
- ATS Scoring Mechanism
- Frontend Dashboard Design
- Python Backend Development
- PDF Report Generation
- AI-assisted Recruitment Systems

---

## 👩‍💻 Author

**Prachi**

B.Tech (Computer Science & Engineering - Data Science)

---

## ⭐ If you found this project helpful, don't forget to star the repository!
