# Swaccha Backend

Backend API for a waste collection management system built using Django REST Framework.

## Features
- JWT Authentication
- Role Based Access Control (Customer, Collector, Ops Manager)
- Booking lifecycle management
- FIFO booking assignment
- Collector availability & service area matching
- Admin-managed configuration

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (development)
- JWT Authentication

## Setup Instructions

```bash
git clone https://github.com/yourusername/swaccha-backend.git
cd swaccha-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
