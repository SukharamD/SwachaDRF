Swaccha Backend

A Django REST Framework–based backend for a waste collection and pickup management system with role-based access control, booking workflows, and ops-driven collector assignment.

====================
FEATURES
====================
- JWT Authentication (Login / Register / Me)
- Role-Based Access Control (Customer, Collector, Ops Manager)
- Waste pickup booking lifecycle
- FIFO-based booking assignment for Ops Managers
- Collector availability & service-area based filtering
- Collector online/offline management
- Django Admin for operational control

====================
USER ROLES
====================
Customer:
- Register & login
- Create waste pickup bookings
- View active, cancelled, and completed bookings

Ops Manager:
- View unassigned bookings in FIFO order
- See available collectors by service area
- Assign bookings to collectors

Collector:
- Mark availability (online/offline)
- View assigned bookings
- Accept or reject assignments (planned)

====================
TECH STACK
====================
- Python
- Django
- Django REST Framework
- SQLite (development)
- JWT Authentication

====================
PROJECT STRUCTURE
====================
swacha_backend/
│
├── apps/
│   ├── accounts/
│   ├── bookings/
│   ├── collectors/
│
├── common/
├── config/
├── manage.py
├── requirements.txt
├── .env
└── README.txt

====================
SETUP INSTRUCTIONS
====================

1. Clone the repository
   git clone https://github.com/<your-username>/swacha-backend.git
   cd swacha-backend

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate  (Linux / Mac)

3. Install dependencies
   pip install -r requirements.txt

4. Create .env file in project root

   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost

5. Run migrations
   python manage.py migrate

6. Create superuser
   python manage.py createsuperuser

7. Run server
   python manage.py runserver

====================
AUTHENTICATION
====================
- JWT-based authentication
- Use Authorization header for protected APIs:

  Authorization: Bearer <access_token>

====================
PROJECT STATUS
====================
- Core backend complete
- Ops assignment workflow implemented
- Collector availability implemented
- Collector accept/reject flow planned
- Notifications planned

====================
AUTHOR
====================
Built as a backend-focused project to demonstrate real-world system design,
RBAC, and workflow-based APIs using Django REST Framework.
