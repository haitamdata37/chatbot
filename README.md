# Resume Scoring Application

This application scores resumes based on job requirements and uses OpenAI's GPT-3.5-turbo model to generate questions and answers related to the resumes and job offers.

## Features

- Upload multiple resume JSON files and a job offer JSON file.
- Score resumes based on the job requirements.
- Visualize the scores.
- Use a chatbot to generate and answer questions about the resumes and job offers.

## Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload resume JSON files and a job offer JSON file through the sidebar.

4. Enter the full name of the candidate whose resume you want to evaluate.

5. View the scores and use the chatbot to ask questions about the resumes and job offers.

## File Structure

- `app.py`: The main application file containing the Streamlit app logic.
- `requirements.txt`: The list of dependencies required to run the application.

## Functions

- `load_resume_data(file)`: Loads resume data from a JSON file or Streamlit's `UploadedFile`.
- `score_resumes(resumes, job_requirements)`: Scores resumes based on job requirements.
- `get_chatgpt_response(prompt)`: Calls the OpenAI ChatGPT API with dynamic prompts.
- `generate_questions(resume, job_offer)`: Generates questions based on the comparison between a resume and a job offer.
- `generate_answer(resume, job_offer, question)`: Generates answers for a selected question using ChatGPT.
- `get_resume_by_name(resumes, candidate_name)`: Retrieves a resume by candidate name.
- `chat_css()`: Injects custom CSS for chat bubbles.
- `main()`: The main function for the Streamlit app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)

## Json Examples to test

# Resume
{
    "CONTACT DETAILS": {
        "FullName": "Sarah Miller",
        "Email": "sarah.miller@example.com",
        "Address": "6789 Broad Way, NewCity, NC",
        "Phone_number": "123-987-6543",
        "URLs": []
    },
    "EXPERIENCE": [
        {
            "company_name": "Innovative Designs",
            "job_title": "Junior Developer",
            "Start date": "February 2019",
            "End date": "Present",
            "Is_current": true,
            "tasks": [
                "Assisted in the development of Java applications",
                "Worked on SQL database optimization",
                "Supported senior developers in large scale projects"
            ]
        }
    ],
    "EDUCATION": [
        {
            "school_name": "Tech Institute",
            "graduation_title": "B.Sc. Information Systems",
            "Start_date": "2014",
            "End_date": "2018",
            "Is_current": false
        }
    ],
    "OTHER": {
        "skills": ["Java", "SQL", "HTML"],
        "languages": ["English", "Spanish"],
        "certificates": "Java Developer Certificate",
        "summary": "Energetic junior developer with a solid foundation in software development and database management."
    }
}


# job offer:
{
    "Company Name": "Innovative Devs",
    "Job Post Title": "Senior Software Developer",
    "Skills Needed": "JavaScript, Python, SQL",
    "Education Required": "B.Sc. in Computer Science",
    "Years of Experience": "3+ years",
    "Tasks": "Lead projects, Develop critical applications",
    "Benefits": "Health, Insurance, Bonuses",
    "Type of Work": "Full-time",
    "Proposed Salary": "$85,000",
    "Company Email": "hr@innovativedevs.com",
    "Location": "Casablanca, Maroc",
    "Description": "We are looking for a Senior Software Developer to lead our development team."
}
