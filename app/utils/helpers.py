import os
from PIL import Image
from flask import current_app, abort
from functools import wraps
from flask_login import current_user
from werkzeug.exceptions import Forbidden

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def save_picture(form_picture, folder='profile_pics'):
    """Save and resize uploaded pictures"""
    # Create folder if it doesn't exist
    folder_path = os.path.join(current_app.root_path, 'static', folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    # Generate random filename
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(folder_path, picture_fn)
    
    # Resize image
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return os.path.join(folder, picture_fn)

def send_async_email(app, msg):
    """Send email asynchronously"""
    with app.app_context():
        mail.send(msg)