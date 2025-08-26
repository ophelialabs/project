from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.utils.helpers import admin_required
from app.models import User
from app import db

bp = Blueprint('admin', __name__)

@bp.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    return render_template('admin/dashboard.html', users=users)

@bp.route('/admin/user/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.')
    return redirect(url_for('admin.admin_dashboard'))