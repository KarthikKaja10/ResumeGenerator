# 📄 AI-Based Resume & Cover Letter Generator using Gemini API

This project is a dynamic resume and cover letter generator built using Flask and Google’s Gemini 1.5 Flash API. By simply entering key personal and professional details, users can quickly receive a well-structured resume and a formal cover letter tailored to their profile.

---

## 🚀 Key Highlights

- 🤖 Integrates Google Gemini 1.5 Flash for AI-generated content  
- 📝 Instantly creates resumes and cover letters from user inputs  
- 📋 Supports fields like Name, Contact Info, Education, University, Experience, Skills, Certifications, and Achievements  
- 🔐 Environment variables managed using a `.env` file to secure API keys  
- 💡 Results displayed on the same page with neat formatting, ready to copy

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python)  
- **Frontend**: HTML5, CSS3  
- **AI Integration**: Gemini 1.5 Flash API  
- **Environment Config**: `python-dotenv`

---

## 📂 Project Directory

```text
resume_writer_project/
├── app.py                 # Main application script
├── .env                   # Environment config for API key (excluded from GitHub)
├── .gitignore             # Ignored files for cleanliness and security
├── requirements.txt       # Required packages for the project
├── tempCodeRunnerFile.py  # Scratchpad file from development
│
├── templates/
│   └── index.html         # Web form UI template
│
└── static/
    └── style.css          # Stylesheet for UI
```

---

## ⚙️ How to Set Up

### 1. Clone this repository

```bash
git clone https://github.com/your-username/resume_writer_project.git
cd resume_writer_project
```

### 2. Install all dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API Key

Create a `.env` file in the root folder and include:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the app locally

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/` to use the app.

---

## ✅ How It Works

1. Users fill out a simple form with relevant information.  
2. The form data is passed to Gemini AI, which generates a customized resume and cover letter.  
3. The formatted output is displayed on the same page, easy to review and copy.

---

## 🧪 Testing Summary

- 🔹 Tested for various user types: fresher, 1+ years, 5+ years of experience  
- 🔹 Form validations ensure mandatory fields are filled correctly  
- 🔹 Handled edge cases like blank fields and unrealistic job roles gracefully  
- 🔹 Verified on different devices and screen sizes for UI consistency  
- 🔹 Ensured Gemini-generated content aligns with user input and role

---

## 📊 Test Observations

- ⚡ Output time: ~2-3 seconds  
- 📌 Content: Relevant and grammatically correct resumes and cover letters  
- 🧱 Stability: No crashes or form failures observed during testing

---

## 🌟 Planned Enhancements

1. **Download as PDF** feature for resume & cover letter  
2. **User Account System** to save multiple versions  
3. **More Layout Options** for resume themes  
4. **Smart Recommendations** for job roles and skills  
5. **Multi-language Output** support  
6. **External API integration** for job listings

---

## 👨‍💻 Developed By

**Kaja Karthik**  
B.Tech in Computer Science   
📧 karthik.23bce7860@vitapstudent.ac.in  
🎓 Vellore Institute of Technology, Amaravati

---

## 📄 License

This project is intended for academic and personal learning use. Please ensure to verify and customize AI-generated content before using it in real-world applications.
