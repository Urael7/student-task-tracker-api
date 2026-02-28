# Student Task and Deadline Tracker API

## Project Overview
The Student Task and Deadline Tracker API is a backend system built using Django and Django REST Framework. 
It allows students to manage academic tasks, track deadlines, and organize priorities securely.

## Features
- User registration
- JWT Login Authentication
- Refresh Token Support
- Persistent Login (Frontend Local Storage)
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

### Frontend Interface
- Login & Registration UI
- Persistent session handling
- Create / Edit / Delete tasks
- Deadline date-time picker
- Filtering & Sorting controls
- Priority-based color styling
- Completed task visual indicators

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (default development database)
- HTML, CSS, JavaScript (Frontend)

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

## Includes automated unit tests for:
Task creation
Filtering
Validation
Authentication
CRUD operations

## Security Features
JWT-based authentication
User-specific data isolation
Deadline validation enforcement
Secure password hashing (Django default)

## Author
Yafet Haileslassie
