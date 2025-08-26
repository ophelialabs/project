# filepath: /home/jesse/Templates/flask/Op/app/utils/upload.py
import os
from werkzeug.utils import secure_filename
from flask import current_app

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, directory='uploads'):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], directory)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        file.save(os.path.join(filepath, filename))
        return filename
    return None