from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai
import json


#Configuring environment vairables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Defining function for gemini pro response
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page_obj=reader.pages[page]
        text+=str(page_obj.extract_text())
    return text
    



st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Check - Align Your Resume Fit")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume in PDF",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improve My Skills to Match this Job Needs")

submit3 = st.button("Check Percentage Match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a career development expert with deep knowledge in data science and the tech industry. 
Your task is to evaluate the candidate's current skill set against the provided job description. 
Start by giving actionable steps on how the candidate can improve their skills to better align with the job requirements. 
Follow this with a list of key skills or knowledge areas that are currently lacking. 
Conclude with final thoughts on the most effective ways for the candidate to bridge the gap and enhance their qualifications.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt1)
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt2)
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt3)
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")