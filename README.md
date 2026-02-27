# Student Task and Deadline Tracker API

## Project Overview
The Student Task and Deadline Tracker API is a backend system built using Django and Django REST Framework. 
It allows students to manage academic tasks, track deadlines, and organize priorities securely.

## Features
- User registration
- User authentication using token-based authentication
- Create, retrieve, update, and delete tasks
- User-specific task access (ownership enforced)
- Filter tasks by status and priority
- Ordering by deadline or creation date
- Overdue task detection
- Pagination support
- Validation for deadlines and title length
- Field validation
- Automated unit tests

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default development database)

## Installation & Setup

1. Clone the repository:
   git clone https://github.com/Urael7/student-task-tracker-api.git

2. Navigate into the project directory:
   cd student-task-tracker-api

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Apply migrations:
   python manage.py migrate

7. Run the development server:
   python manage.py runserver

## API Endpoints

Authentication:
- POST /api/auth/login/

Register
- POST /api/auth/register/

Login
- POST /api/auth/login/

Tasks:
- GET /api/tasks/
- POST /api/tasks/
- GET /api/tasks/<id>/
- PUT /api/tasks/<id>/
- PATCH /api/tasks/<id>/
- DELETE /api/tasks/<id>/

Filtering examples:
- /api/tasks/?status=pending
- /api/tasks/?priority=high
- /api/tasks/?ordering=deadline
- /api/tasks/?overdue=true

## Testing

To run unit tests:
python manage.py test

## Author
Yafet Haileslassie
