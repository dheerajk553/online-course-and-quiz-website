# Online Course and Quiz Website ✨

> A clean Django app where students enroll in courses, study lessons, take quizzes, and instantly download a PDF certificate when they pass.

<p align="center">
	<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white"></a>
	<a href="https://www.djangoproject.com/"><img alt="Django" src="https://img.shields.io/badge/Django-5.x-0C4B33?logo=django&logoColor=white"></a>
	<a href="#certificate-generation-xhtml2pdf"><img alt="PDF" src="https://img.shields.io/badge/PDF-xhtml2pdf-blue"></a>
</p>

A Django-based web application that enables students to enroll in courses, study lessons, take quizzes, and earn certificates — all under one roof.

---

## Table of Contents
- Features
- Technology Use
- Quickstart (Windows)
- Project Goals
- Certificate generation
- Admin look & theme (django-admin-interface)
- Deploying to PythonAnywhere
- Troubleshooting

## Features

-  Student enrollment and course browsing  
-  Lesson viewing and quiz participation  
-  Certificate generation in PDF format  
-  Admin panel for managing courses, lessons, quizzes, and users  
-  Mobile-friendly and responsive design

---

## Technology Use

| Layer       | Tools & Frameworks                          |
|------------|---------------------------------------------|
| Backend     | Python, Django Framework                    |
| Frontend    | HTML5, CSS3, JavaScript, Bootstrap          |
| Database    | SQLite (default) or MySQL                   |
| Other Tools | Django Admin Panel, GitHub, VS Code, PDF Generator |

---

## Quickstart (Windows PowerShell)

Prerequisites: Python 3.11+, Git.

```powershell
# 1) Clone and enter
git clone https://github.com/dheerajk553/online-course-and-quiz-website.git
cd online-course-and-quiz-website

# 2) Create and activate a venv (PowerShell)
py -3.11 -m venv venv
./venv/Scripts/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Database and admin
python manage.py migrate
python manage.py createsuperuser   # choose username/password

# 5) Run
python manage.py runserver
```

Open http://127.0.0.1:8000/ and log into /admin using the superuser you created.


## Project Goals

- Build a fully functional online learning platform using Django and SQLite  
- Provide students with interactive lessons, quizzes, and certificates  
- Implement secure access control for students and admins  
- Ensure the site is attractive, responsive, and easy to use


##  Learning Reflection

This project helped me apply full-stack development skills in a real-world context. I focused on originality, academic integrity, and practical implementation. From backend logic to frontend design, every step was manually built and documented. It reflects my commitment to hands-on learning and building something that can be applied in real life.

---

## Certificate generation (xhtml2pdf)

- The app generates certificates using xhtml2pdf (no wkhtmltopdf needed).
- Template: `courses/templates/courses/certificate_template.html`.
- Only a single outer border is used; there are no boxes around each line for reliable PDF output.
- Preview HTML (useful for debugging/printing): append `?format=html` to the certificate download URL.

If the PDF looks different from HTML, clear your browser cache and try again, or re-open the HTML preview.

---

## Admin look & theme (django-admin-interface)

This project uses `django-admin-interface` to control the admin colors and layout (like the green theme in the screenshots). We avoid injecting custom CSS so the theme can render consistently on all pages.

What’s already set up:
- `admin_interface` and `colorfield` are installed in `INSTALLED_APPS`.
- Admin branding is set via `admin.site.site_header/site_title/index_title`.
- Our `base_site.html` does not inject extra CSS, preventing layout conflicts.

Enable or customize the theme:
1) Log in to `/admin/` and open “Admin interface” → “Themes”.
2) Use the Default theme or create a new one, set “Active = True”, and Save.
3) Optionally upload a logo, tweak colors, and switch between light/dark.

Tip: If you previously added custom admin CSS, remove or narrow it. In this repo, we deliberately removed the override link in `courses/templates/admin/base_site.html` so the theme fully controls styles.

---

## Deploying to PythonAnywhere (summary)

1) Upload project or pull from GitHub to your PythonAnywhere home directory.

2) Create a virtualenv (Python 3.11 recommended), then install deps:
```
pip install -r requirements.txt
```

3) Web app configuration:
- WSGI points to the Django project: `online_course_and_quiz_website.wsgi`
- Static files mapping: URL `/static` → your `STATIC_ROOT` folder (this project uses `staticfiles`).
	- If your project folder has spaces, wrap the path in quotes in the PA UI.
	- Example: `/home/<your_username>/Online Course and Quiz Website/staticfiles`
- Run `python manage.py collectstatic` in the virtualenv

4) Settings:
- Add your domain to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` (e.g., `yourusername.pythonanywhere.com`)

5) Initialize DB and admin on the server:
```
python manage.py migrate
python manage.py createsuperuser
```

6) Reload the web app from the PythonAnywhere Web tab.

Optional server-side commands (quotes help with spaces in paths):

```bash
source ~/.virtualenvs/<env>/bin/activate
pip install -r "/home/<your_username>/Online Course and Quiz Website/requirements.txt"
python "/home/<your_username>/Online Course and Quiz Website/manage.py" collectstatic -c --noinput
python "/home/<your_username>/Online Course and Quiz Website/manage.py" migrate
```

---

## Troubleshooting

<details>
<summary>FortiGuard / Firewall block</summary>
If you see “FortiGuard Intrusion Prevention – Access Blocked” when opening your PythonAnywhere URL, your network is filtering the site. Try another network (mobile hotspot/home) or ask IT to allowlist `*.pythonanywhere.com` on ports 80/443. You can also request reclassification at https://www.fortiguard.com/webfilter.
</details>

<details>
<summary>Admin CSS looks broken</summary>
Confirm Static mapping is set and run `python manage.py collectstatic`, then reload the app from the Web tab.
</details>

<details>
<summary>CSRF failures on login/forms</summary>
Ensure your domain is in `CSRF_TRUSTED_ORIGINS` and `ALLOWED_HOSTS` in settings.
</details>

<details>
<summary>“No module named django” on the server</summary>
Activate the correct virtualenv for all commands and in the Web app configuration.
</details>

<details>
<summary>PDF shows unexpected boxes</summary>
Use the provided `certificate_template.html` (single outer border) and ensure `showBoundary=0, debug=0` in xhtml2pdf. Preview with `?format=html` to verify the template first.
</details>

