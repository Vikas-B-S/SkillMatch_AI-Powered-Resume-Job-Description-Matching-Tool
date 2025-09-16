# SkillMatch: AI-Powered Resume & Job Description Matching Tool

🚀 **SkillMatch** is an AI-driven resume optimization tool that helps job seekers align their resumes with job descriptions in real time.  
Built with **Google Gemini**, **LangChain**, and **Streamlit**, this project empowers users to maximize their chances of getting shortlisted by Applicant Tracking Systems (ATS) and recruiters.

---

## 📌 Problem Statement
In today’s competitive job market:
- Job seekers often submit generic resumes that don’t match specific job descriptions.
- Recruiters face overwhelming numbers of irrelevant applications.
- Applicant Tracking Systems (ATS) filter out poorly optimized resumes, reducing selection chances.

---

## 🎯 Solution
SkillMatch bridges this gap by:
1. Analyzing resumes against job descriptions.
2. Highlighting **matching skills** and **missing competencies**.
3. Estimating **ATS scores** and **shortlist probability**.
4. Providing **customized resume suggestions**.
5. Performing a **SWOT analysis** to identify strengths, weaknesses, opportunities, and threats.

---

## ✨ Features
- 📂 **Upload Resume (PDF)** and paste a **Job Description**.  
- 🤖 **AI-powered skill gap analysis** using Google Gemini (via LangChain).  
- 📊 **ATS score prediction & match percentage**.  
- 📝 **SWOT analysis of your resume**.  
- 💡 **Actionable recommendations** to improve your resume.  
- 📑 **Auto-generated customized resumes** for better alignment.  
- 🌐 Deployed on **Streamlit Cloud** for easy access.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python, LangChain  
- **LLM:** Google Gemini (`gemini-2.5-flash-lite`)  
- **File Handling:** PDF, Text Extraction  
- **Deployment:** Streamlit Cloud  
- **Version Control:** Git & GitHub  

---

## ⚙️ Architecture Overview
1. **Input Layer:** Upload Resume (PDF) & Job Description (text).  
2. **Text Extraction:** Parse PDF content using a text extractor.  
3. **AI Processing:** LangChain prompts Google Gemini for skill analysis.  
4. **Analysis & Output:** ATS score, skill gaps, SWOT, recommendations.  
5. **UI Feedback:** Interactive Streamlit interface displays results.  

---

## 📊 Business Impact
- **For Job Seekers:**  
  - Increase chances of shortlisting.  
  - Save time tailoring resumes.  
  - Improve ATS compatibility.  

- **For Recruiters/HR Teams:**  
  - Higher quality applications.  
  - Reduced filtering time.  
  - More efficient hiring pipeline.  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vikas-B-S/SkillMatch_AI-Powered-Resume-Job-Description-Matching-Tool.git
cd SkillMatch_AI-Powered-Resume-Job-Description-Matching-Tool
```

### 2️⃣ Create a Virtual Environment & Activate
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Your Google API Key
Add your Google Gemini API key to the environment:
```bash
# Mac/Linux
export GOOGLE_API_KEY="your_api_key_here"

# Windows
setx GOOGLE_API_KEY "your_api_key_here"
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run skill_match.py
```

---

## 🌍 Live Demo
Try it here: https://skillmatch-ai-powered-resume-job-description-matching-tool.streamlit.app/

---

## 📌 Use Cases
- Job seekers tailoring resumes for applications.  
- University placement cells supporting students.  
- HR consultants and recruitment agencies.  
- Freelancers offering resume services.  

---

### 💡 Inspiration
SkillMatch demonstrates how **Generative AI** can transform hiring by bridging the gap between resumes and job requirements.  

