# Online Course and Quiz Website 🎓

This is a Django-based web application where students can enroll in courses, study lessons, take quizzes, and earn PDF certificates — all in one place. The goal was to build a complete learning platform using only the essential tools, keeping everything simple, responsive, and easy to use.

---

## 🚀 Features

- Student registration and course browsing  
- Lesson viewing with interactive quizzes  
- Auto-generated PDF certificates after quiz completion  
- Admin panel to manage courses, lessons, quizzes, and users  
- Fully responsive design — works on mobile and desktop

---

## 🛠️ Tech Stack

| Layer       | Tools & Frameworks                          |
|-------------|---------------------------------------------|
| Backend     | Python, Django                              |
| Frontend    | HTML5, CSS3, JavaScript, Bootstrap          |
| Database    | SQLite (default) or MySQL                   |
| Tools       | Django Admin, GitHub, VS Code, xhtml2pdf, pdfkit |

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/dheerajk053/online-course-and-quiz-website.git
cd online-course-and-quiz-website
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Requirements
The project uses only the necessary Python packages:
# Django framework for building the web app
Django>=5.2.7

# For generating PDF certificates
pdfkit==1.0.0
xhtml2pdf>=0.2.5

# For handling images (used in certificate generation)
pillow>=11.3.0

# To limit API requests (used in quiz or certificate endpoints)
ratelimit>=2.2.1

# For making HTTP requests (used in external API calls)
requests>=2.32.5

# Required by Django for database parsing
sqlparse>=0.5.3



Project Goals
Build a complete online learning platform using Django

Allow students to learn, take quizzes, and earn certificates

Implement secure login for students and admins

Keep the UI clean, responsive, and easy to navigate

Learning Reflection
This project helped me apply full-stack development skills in a real-world scenario. I built everything manually — from backend logic to frontend design — with a focus on originality and academic integrity. It reflects my commitment to hands-on learning and building something practical and deployable.

Deployment Ready

This project is configured for deployment on PythonAnywhere. All static and media paths are validated, and the requirements.txt is clean and optimized for production.