from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resume = ""
    cover_letter = ""
    show_output = False

    education_options = ["12th Class", "BSc", "BTech - IT", "MTech - AI", "MCA"]
    experience_options = ["Fresher", "1 Year", "2 Years", "3-5 Years", "5+ Years"]

    if request.method == 'POST':
        name = request.form['name']
        education = request.form['education']
        experience = request.form['experience']
        job_role = request.form['job_role']
        skills = request.form['skills']

        prompt = f"""
        Generate a professional resume and a formal cover letter.

        Name: {name}
        Education: {education}
        Work Experience: {experience}
        Job Role: {job_role}
        Skills: {skills}

        Resume Format:
        1. Objective
        2. Skills
        3. Education
        4. Experience (if applicable)

        The cover letter should be formal and relevant to the job role.
        """

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            output_text = response.text

            if "Cover Letter:" in output_text:
                parts = output_text.split("Cover Letter:")
                resume = parts[0].strip()
                cover_letter = "Cover Letter:\n" + parts[1].strip()
            else:
                resume = output_text
                cover_letter = ""  # hide cover letter section if missing

            show_output = True

        except Exception as e:
            resume = "Error: " + str(e)
            cover_letter = ""
            show_output = True

    return render_template(
        'index.html',
        resume=resume,
        cover_letter=cover_letter,
        show_output=show_output,
        education_options=education_options,
        experience_options=experience_options
    )

if __name__ == '__main__':
    app.run(debug=True)
