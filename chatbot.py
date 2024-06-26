import pandas as pd
import numpy as np
import json
import streamlit as st
import openai

# Function to load resume data from a JSON file or Streamlit's UploadedFile
def load_resume_data(file):
    if isinstance(file, str):
        with open(file) as f:
            data = json.load(f)
    else:
        data = json.load(file)
    return data

# Function to score resumes based on job requirements
def score_resumes(resumes, job_requirements):
    scores = []
    for resume in resumes:
        score = 0
        # Add your scoring logic here based on skills, experience, and education
        scores.append(score)
    return scores

# Function to call the OpenAI ChatGPT API with dynamic prompts
def get_chatgpt_response(prompt):
    api_key = 'Your-Api-Key-Here'  # Add your API key here
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message['content']

# Function to generate questions based on the comparison
def generate_questions(resume, job_offer):
    questions = [
        "Does the candidate have the skills needed?",
        "Does the candidate meet the educational requirements?",
        "Does the candidate have the required years of experience?",
        "What schools did the candidate study at?",
        "What companies did the candidate work for?",
        "How many years of experience does the candidate have?"
    ]
    return questions

# Function to generate answers for a selected question using ChatGPT
def generate_answer(resume, job_offer, question):
    prompt = f"Based on the resume and job offer below, {question}. Provide a short answer.\n\nJob Offer:\n{job_offer}\n\nResume:\n{resume}"
    answer = get_chatgpt_response(prompt)
    return answer

# Function to get the resume by candidate name
def get_resume_by_name(resumes, candidate_name):
    for resume in resumes:
        if resume.get("CONTACT DETAILS", {}).get("FullName", "").lower() == candidate_name.lower():
            return resume
    return None

# CSS for chat bubbles
def chat_css():
    st.markdown(
        """
        <style>
        .chat-container {
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 10px;
            background-color: #f7f7f7;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .chat-bubble {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 25px;
            margin-bottom: 10px;
            font-size: 16px;
            line-height: 1.4;
        }
        .chat-bubble.user {
            background-color: #0084ff;
            color: white;
            align-self: flex-end;
        }
        .chat-bubble.assistant {
            background-color: #e4e6eb;
            color: black;
            align-self: flex-start;
        }
        .chat-header {
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Main function for Streamlit app
def main():
    st.set_page_config(page_title='Resume Scoring Application', layout='wide')
    st.title('Resume Scoring Application')
    chat_css()

    st.sidebar.header('Upload Files')
    resume_files = st.sidebar.file_uploader('Upload Resume JSON files', type='json', accept_multiple_files=True)
    job_offer_file = st.sidebar.file_uploader('Upload Job Offer JSON file', type='json')
    candidate_name = st.sidebar.text_input("Enter Candidate Full Name")

    if resume_files and job_offer_file:
        resumes = [load_resume_data(file) for file in resume_files]
        job_offer = load_resume_data(job_offer_file)

        # Score resumes
        scores = score_resumes(resumes, job_offer)

        # Display scores in a dashboard
        st.header('Scores and Classification')
        st.write(scores)

        # Visualization
        st.header('Visualization')
        # Add your visualization logic here

        if candidate_name:
            resume = get_resume_by_name(resumes, candidate_name)
            if resume:
                st.sidebar.success(f"Resume for {candidate_name} found!")
                questions = generate_questions(resume, job_offer)

                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []

                st.header("Chatbot")
                chat_placeholder = st.empty()

                with chat_placeholder.container():
                    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                    for i, chat in enumerate(st.session_state.chat_history):
                        if chat['role'] == 'user':
                            st.markdown(f'<div class="chat-bubble user">**You:** {chat["content"]}</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="chat-bubble assistant">**Chatbot:** {chat["content"]}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                selected_question = st.selectbox("Select a question to ask the chatbot:", questions)
                if st.button("Ask"):
                    st.session_state.chat_history.append({"role": "user", "content": selected_question})
                    st.session_state.chat_history.append({"role": "assistant", "content": "..."})

                    chat_placeholder.empty()
                    with chat_placeholder.container():
                        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                        for i, chat in enumerate(st.session_state.chat_history):
                            if chat['role'] == 'user':
                                st.markdown(f'<div class="chat-bubble user">**You:** {chat["content"]}</div>', unsafe_allow_html=True)
                            else:
                                st.markdown(f'<div class="chat-bubble assistant">**Chatbot:** {chat["content"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    answer = generate_answer(resume, job_offer, selected_question)
                    st.session_state.chat_history[-1] = {"role": "assistant", "content": answer}
                    chat_placeholder.empty()
                    with chat_placeholder.container():
                        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                        for i, chat in enumerate(st.session_state.chat_history):
                            if chat['role'] == 'user':
                                st.markdown(f'<div class="chat-bubble user">**You:** {chat["content"]}</div>', unsafe_allow_html=True)
                            else:
                                st.markdown(f'<div class="chat-bubble assistant">**Chatbot:** {chat["content"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.sidebar.error(f"Resume for {candidate_name} not found.")
    else:
        st.sidebar.info("Please upload the job offer and resume files.")

if __name__ == "__main__":
    main()
