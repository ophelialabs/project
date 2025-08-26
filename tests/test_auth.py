Templates/flask/Op/tests/test_auth.py
import unittest
from flask import url_for
from app import create_app, db
from app.models import User
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/auth/register', data={
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test123',
            'password2': 'test123'
        })
        self.assertEqual(response.status_code, 302)
        user = User.query.filter_by(username='test').first()
        self.assertIsNotNone(user)

    def test_login(self):
        # Create a test user
        user = User(username='test', email='test@example.com')
        user.set_password('test123')
        db.session.add(user)
        db.session.commit()

        # Test login with correct credentials
        response = self.client.post('/auth/login', data={
            'username': 'test',
            'password': 'test123'
        })
        self.assertEqual(response.status_code, 302)