Threat Monitoring & Alert Management Backend

CYETHACK Assignment

Project Overview

This project is a backend API system built using Django and Django REST Framework (DRF) for a simplified Threat Monitoring & Alert Management Platform.

The system ingests security events, automatically generates alerts for high-severity threats, and provides secure, role-based access to alert data using JWT authentication.

Tech Stack

Backend: Python, Django

API Framework: Django REST Framework (DRF)

Authentication: JWT (SimpleJWT)

Database: SQLite

Filtering: django-filter

Pagination: DRF built-in pagination

Version Control: Git

📂 Project Structure
CYETHACK_Assignment/
│
├── CYETHACK_Assignment/     # Django project (settings, urls)
│
├── Events/                 # Event / threat ingestion
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── Alert/                  # Alert generation & management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── users/                  # User authentication & roles
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── db.sqlite3              # Database
├── manage.py
├── .env
├── .gitignore
└── README.md

Features Implemented

JWT-based authentication

Role-based access control (Admin / Analyst)

Event ingestion API

Automatic alert generation for High & Critical events

Alert status management (Open / Acknowledged / Resolved)

Filtering alerts by severity and status

Built-in pagination for list APIs

Secure API access with permissions

👥 User Roles & Permissions
Role	Permissions
Admin	Full access (create events, update alerts, manage users)
Analyst	Read-only access to alerts
🔐 Authentication


for Admin username and password for testing
username =Admin
password =Admin

JWT authentication is implemented using SimpleJWT.

Login
POST /api/auth/login/

Token Refresh
POST /api/auth/refresh/

Authorization Header
Authorization: Bearer <access_token>

🔁 API Endpoints
🔹 Events (Admin Only)
POST   /api/events/
GET    /api/events/

🔹 Alerts (Admin & Analyst)
GET    /api/alerts/
GET    /api/alerts/?status=OPEN
GET    /api/alerts/?event__severity=HIGH
PATCH  /api/alerts/{id}/     # Admin only

🔹 Users (Admin Only)
GET    /api/users/
POST   /api/users/

📄 Pagination

Built-in DRF pagination is used for all list APIs.

Default page size:

10


Example:

GET /api/alerts/?page=2

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <repository-url>
cd CYETHACK_Assignment

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver

🔐 Environment Variables

Create a .env file:

SECRET_KEY=your-secret-key
DEBUG=True

🧪 Testing

APIs can be tested using:

Postman

Curl

DRF Browsable API

📌 Assumptions

SQLite is used for simplicity

Events are ingested by trusted sources

Alerts are automatically generated only for High and Critical severity events

JWT tokens are required for all protected APIs

✅ Assignment Coverage

✔ Django & DRF fundamentals
✔ Secure REST APIs
✔ Role-based access control
✔ Database design
✔ Pagination & filtering
✔ Clean project structure

🧾 Submission

GitHub repository contains complete project

Project runs locally without issues

README provides setup & API details

