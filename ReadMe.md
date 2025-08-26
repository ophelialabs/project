# Flask Application

A full-featured Flask application with authentication, user profiles, admin panel, and more.

## Features

- User Authentication
  - Login/Register
  - Password Reset
  - Social Authentication (Google)
- User Profiles
  - Profile Pictures
  - About Me
  - Last Seen
- Admin Panel
  - User Management
  - Content Management
- API
  - Token Authentication
  - RESTful Endpoints
- File Upload
  - Secure File Handling
  - Image Processing

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Copy `.env.example` to `.env`
- Update the values in `.env`

4. Initialize database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Development

1. Run tests:
```bash
pytest
```

2. Generate coverage report:
```bash
coverage run -m pytest
coverage report
```

## Deployment

1. Set up production server (e.g., gunicorn):
```bash
gunicorn -w 4 "app:create_app()"
```

2. Configure nginx as reverse proxy

3. Set up SSL certificates

To use all these features:

Initialize the database with migrations
Create an admin user
Set up OAuth credentials in Google Developer Console
Configure email server settings
Set up Redis for session management
Create necessary directories for file uploads