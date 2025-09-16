import streamlit as st
from pdf_to_text import text_extractor
import google.generativeai as genai
import os

key  = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

resume_text = job_desc = None

#Upload Resume
st.sidebar.title(':blue[Upload Your Resume [PDF Only]]')
file = st.sidebar.file_uploader('Resume', type=['PDF'])
if file:
    resume_text = text_extractor(file)

#Lets Define the Main Page

st.title('SkillMatch: AI-Powered Resume & Job Description Matching Tool')
st.markdown('#### This application will match your resume and the job description. It will create a detailed report on the match')

tips = '''Follow these steps to proceed:
* Upload your updated resume in the sidebar. (PDF only)
* Copy and Paste the job description below for which you are applying.
* Click the button and see the match.'''

st.write(tips)

job_desc = st.text_area('Copy and Paste the Job Description here[Press ctrl + enter]', max_chars=100000)

prompt = f"""
You are an expert ATS (Applicant Tracking System) and career consultant. 
Your task is to analyze the resume and job description provided, and produce a detailed, structured evaluation.

### Input Data:
- Resume Text:
{resume_text}

- Job Description:
{job_desc}

### Output Requirements:

1. **Candidate Overview (3–5 lines)**  
   - Summarize the applicant’s background, strengths, and key experience relevant to the JD.

2. **ATS Match Analysis**  
   - Predicted ATS Score: give a range (e.g., 60–70%).  
   - Highlight **matching keywords/skills** (table format).  
   - Highlight **missing/weak keywords** that should be added (table format).  

3. **Shortlist Probability**  
   - Give the estimated probability of getting shortlisted (%) with a one-line justification.

4. **SWOT Analysis** (bullet points)  
   - **Strengths** (skills & experience aligned with JD).  
   - **Weaknesses** (gaps or missing competencies).  
   - **Opportunities** (where resume can be improved to stand out).  
   - **Threats** (factors reducing chances like lack of certifications, limited domain exposure, etc.).  

5. **Improvement Recommendations**  
   - Actionable edits to improve ATS compatibility (e.g., adding keywords, reformatting sections, quantifying achievements).  
   - Mention at least **3–5 specific improvements**.

6. **Customized Resume Versions**  
   - **Version 1:** Focused on technical/skill alignment (insert missing keywords).  
   - **Version 2:** Focused on achievements and results (rewrite experience with quantifiable impact).  
   - Provide bullet-pointed examples of how job experiences should be rewritten for better ATS results.  

### Formatting:
- Use **headings, bullet points, and tables** where needed.  
- Keep content professional and concise.  
- Prioritize **ATS-friendly keywords**. 

Give a proper conclusion at last.
"""


if job_desc:
    if resume_text:
        response = model.generate_content(prompt)
        st.write(response.text)
    else: 
        st.write('Please upload the resume and provide job description')




