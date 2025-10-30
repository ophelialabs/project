import unittest
from flask import url_for
from app import create_app, db
from app.models import User
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False

class MainTestCase(unittest.TestCase):
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

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_home_page_with_auth(self):
        # Create and login a test user
        user = User(username='test', email='test@example.com')
        user.set_password('test123')
        db.session.add(user)
        db.session.commit()
        
        self.client.post('/auth/login', data={
            'username': 'test',
            'password': 'test123'
        })
        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)