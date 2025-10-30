from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

bp = Blueprint('api', __name__)
limiter = Limiter(key_func=get_remote_address)

# Apply rate limiting to all API routes
@bp.before_request
@limiter.limit("100 per minute")
def limit_api_requests():
    pass

from app.api import routes