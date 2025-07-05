# 🧠 AI Resume Generator (using Gemini API)

An intelligent resume and cover letter generator built using Flask and Google’s Gemini API. This web application allows users to enter their details and instantly generate a professional resume along with a formal cover letter using Generative AI.

---

## 🚀 Features

* ✍ Automatically generates resumes and cover letters based on user input
* 🧠 Uses Google Gemini 1.5 Flash (via google-generativeai)
* 🖥 Clean user interface built with Flask, HTML, and CSS
* 💡 Custom input fields: Name, Education, Experience, Job Role, Skills, Certifications, Achievements
* 🔒 Secure environment variable handling using .env

---

## 🛠 Tech Stack

* *Backend*: Python, Flask
* *Frontend*: HTML5, CSS3
* *AI Integration*: Google Gemini 1.5 Flash
* *Environment Management*: python-dotenv

---

## 📂 Project Structure

text
resume_writer_project/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and folders
├── .env                    # Contains Gemini API key (not tracked)
│
├── templates/
│   └── index.html          # Web UI
│
└── static/
    └── style.css           # Styling for the app


---

## 🔧 Setup Instructions

### 1. Clone the repository

bash
git clone https://github.com/KarthikKaja10/resume-writer-project.git
cd resume-writer-project


### 2. Install dependencies

bash
pip install -r requirements.txt


### 3. Add your Gemini API key

Create a .env file in the project root and add:

env
GEMINI_API_KEY=your_api_key_here


### 4. Run the application

bash
python app.py


Visit http://127.0.0.1:5000/ in your browser to use the app.

---

## ✅ Sample Use Flow

1. Enter your name, education, experience, job role, skills, certifications, and achievements.
2. Click *Generate Resume*.
3. The app displays a personalized resume and cover letter using AI.

---

## 🧪 Testing Strategy

The system was tested across a variety of use cases to ensure its reliability, coherence, and user-friendliness. Both manual and functional testing methods were used to verify the following:

* *Input Handling:*
  Ensured the app could handle varied combinations of user data (e.g., freshers, experienced users, incomplete fields).

* *Content Relevance:*
  Checked if generated outputs matched user-entered job roles, education, and skills.

* *Form Validation:*
  Verified that required fields were validated and appropriate messages were shown for missing inputs.

* *User Experience:*
  Evaluated the interface layout, responsiveness, and clarity of the generated content.

* *Edge Case Testing:*
  Used unexpected or unusual inputs to ensure the model generates sensible, robust outputs.

---

## 🔮 Future Enhancements

1. 📄 PDF Export Support
 Allow users to download the resume and cover letter as a well-formatted PDF.

2. 🧾 Profile Saving and Editing
 Let users save their data and make edits without re-entering everything.

3. 🎨 Template Customization
 Enable switching between different resume styles or formats.

4. 🗣 AI Feedback Loop
 Include a feedback form to rate results and improve future generations.

5. 🌐 Multilingual Support
 Add the ability to generate documents in other languages such as Hindi or Spanish.

6. 💼 Job Suggestions
 Recommend job roles based on inputted experience and skills.

---

## 👨‍💻 Author

*KAJA KARTHIK*
B.Tech Student | AI Enthusiast
Email: [karthik.23bce7860@vitapstudent.ac.in](mailto:karthik.23bce7860@vitapstudent.ac.in)
College: VELLORE INSTITUTE OF TECHNOLOGY, AMARAVATI

---

## 📄 License

This project is created for academic and educational purposes only.
