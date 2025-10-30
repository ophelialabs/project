from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.main import bp

@bp.route('/')
@bp.route('/home')
@login_required
def index():
    return render_template('main/index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')