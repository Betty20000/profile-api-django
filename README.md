# Profile API — Django + Cat Facts
A simple RESTful API built with Django REST Framework that returns your profile information along with a dynamic random cat fact fetched from the Cat Facts API
.

## This project demonstrates how to:

1. Consume a third-party API

2. Format structured JSON responses

3. Use environment variables and logging

Deploy Django to production ( Railway)

## 🚀 Endpoint
GET /me
Example Response:
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Beatrice Mwangi",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T12:34:56.789Z",
  "fact": "Cats sleep for around 70% of their lives."
}`


## ✅ Response Details

`Field	Description`
status	Always "success"
user.email	Your email address
user.name	Your full name
user.stack	Your backend stack
timestamp	Current UTC time in ISO 8601 format
fact	Random cat fact from Cat Facts API

## 🛠️ Tech Stack

. Language: Python 3.11+

. Framework: Django 5.2.7 + Django REST Framework

. Server: Gunicorn

 . Static Files: Whitenoise

. HTTP Client: Requests

. Hosting: Railway

## 🧩 Features

Dynamic timestamp on each request

Random cat fact fetched via API

Proper JSON response formatting

Graceful fallback handling for API errors

Deploy-ready configuration (Gunicorn + Whitenoise)

## ⚙️ Setup Instructions
### 1. Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Migrations
python manage.py migrate

### 5. Collect Static Files
python manage.py collectstatic --noinput

### 6. Start the Server
python manage.py runserver


Then visit:
`👉 http://127.0.0.1:8000/me/`

## 🌍 Deployment (Railway Example)

Push code to GitHub

Create a new project on Railway

Connect your GitHub repo

Ensure the following files are in place:

Procfile

web: gunicorn profile_api.wsgi


requirements.txt

.gitignore

Railway auto-detects your Django project and deploys it.

### 🔒 Environment Variables (optional)
Variable	Description
SECRET_KEY	Django secret key for production
DEBUG	Set to False in production
PORT	(Automatically set by Railway)

## 🧰 Dependencies

See requirements.txt:

`asgiref==3.10.0`
`certifi==2025.10.5`
`charset-normalizer==3.4.4`
`Django==5.2.7`
`djangorestframework==3.16.1`
`gunicorn==23.0.0`
`idna==3.11`
`packaging==25.0`
`requests==2.32.5`
`sqlparse==0.5.3`
`tzdata==2025.2`
`urllib3==2.5.0`
`whitenoise==6.11.0`

### 📋 Project Structure
backend_api/
│
├── api/
│   ├── views.py         # Core /me endpoint logic
│   ├── urls.py          # API routes
│   └── __init__.py
│
├── profile_api/
│   ├── settings.py      # Django settings (includes Whitenoise)
│   ├── urls.py          # Root URL config
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.md

👩🏽‍💻 Author

Beatrice Mwangi
📧 [beatricegachigi@gmail.com
]
💻 Backend Stack: Python / Django
