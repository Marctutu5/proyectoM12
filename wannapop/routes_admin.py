from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, BlockedUser
from .forms import UserBlockForm
from . import db_manager as db
from .helper_role import require_admin_role, require_moderator_role
from datetime import datetime

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
    for user in users:
        user.is_blocked = BlockedUser.query.filter_by(user_id=user.id).first() is not None
    return render_template('users_list.html', users=users)

@admin_bp.route('/admin/users/<int:user_id>/block', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def block_user(user_id):
    user = User.query.get_or_404(user_id)
    if BlockedUser.query.get(user_id):
        flash('El usuario ya está bloqueado', 'warning')
    else:
        message = request.form.get('message', 'Sin razón especificada')  # Obtener el mensaje del formulario
        blocked_user = BlockedUser(user_id=user_id, message=message, created=datetime.utcnow())
        db.session.add(blocked_user)
        db.session.commit()
        flash('Usuario bloqueado con éxito', 'success')
    return redirect(url_for('admin_bp.admin_users'))


@admin_bp.route('/admin/users/<int:user_id>/unblock', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def unblock_user(user_id):
    BlockedUser.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    flash('Usuario desbloqueado con éxito', 'success')
    return redirect(url_for('admin_bp.admin_users'))