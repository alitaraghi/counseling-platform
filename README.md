# Counseling Platform

A full-stack web app for counselors and clients, built with Django (backend), React (frontend), and PostgreSQL (database).

## Features

- Counselors can create blogs, courses, and manage client files.
- Clients can book sessions and track course progress.
- Admins can verify counselor licenses and manage compliance.
- Includes AI triage chatbot and community forum.

## Installation

### Prerequisites

- Python 3.13+
- Node.js 22+
- PostgreSQL 17+
- Git

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/alitaraghi/counseling-platform.git
   cd counseling-platform/backend
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL database:

   ```bash
   psql -U postgres -c "CREATE DATABASE counseling_db;"
   ```
5. Update database settings in `backend/counseling_backend/settings.py`.
6. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend Setup

1. Go to frontend folder:

   ```bash
   cd ../frontend
   ```
2. Install dependencies:

   ```bash
   npm install
   ```
3. Start the development server:

   ```bash
   npm start
   ```
## Diagrams
[Entity Relationship Diagram](docs/ERD.md)
## Database Design

![ERD](docs/ERD.png)The database includes tables for users, profiles, sessions, and consents. See ERD.md for details.