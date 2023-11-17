from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User
from . import db_manager as db
from .helper_role import require_admin_role, require_moderator_role

# Blueprint
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates/admin", static_folder="static"
)

@admin_bp.route('/admin')
@login_required
@require_admin_role.union(require_moderator_role).require(http_exception=403)
def admin_index():
    return render_template('index.html')

@admin_bp.route('/admin/users')
@login_required
@require_admin_role.require(http_exception=403)
def admin_users():
    users = User.query.all()
    return render_template('users_list.html', users=users)
