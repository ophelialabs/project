from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_caching import Cache
from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension
from redis import Redis
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

# Initialize Flask extensions
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
cache = Cache()
redis = Redis()
toolbar = DebugToolbarExtension()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    cache.init_app(app)
    Session(app)
    toolbar.init_app(app)
    csrf.init_app(app)

    # Add security headers
    Talisman(app, content_security_policy={
        'default-src': "'self'",
        'img-src': "'self' data: https:",
        'script-src': "'self' 'unsafe-inline' 'unsafe-eval'",
        'style-src': "'self' 'unsafe-inline'"
    })

    # Register blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Add admin blueprint registration
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Error handlers
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app