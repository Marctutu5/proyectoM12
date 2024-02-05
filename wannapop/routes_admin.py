from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, BlockedUser, Product, Category, BannedProduct
from .forms import UserBlockForm, ProductBannedForm
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
    users = User.get_all()
    for user in users:
        user.is_blocked = BlockedUser.query.filter_by(user_id=user.id).first() is not None
    return render_template('users_list.html', users=users)

@admin_bp.route('/admin/products')
@login_required
@require_moderator_role.require(http_exception=403)
def admin_products():
    # Obtener la lista de productos y sus categorías
    # products_with_category = db.session.query(Product, Category).join(Category).order_by(Product.id.asc()).all()
    products_with_category = Product.get_all_with(Category, BannedProduct)

    # Obtener también el estado de prohibición para cada producto
    # products_info = []
    # for product, category in products_with_category:
    #     banned = BannedProduct.query.filter_by(product_id=product.id).first()
    #     products_info.append((product, category, banned))

    return render_template('products_list.html', products_info=products_with_category)


@admin_bp.route('/admin/users/<int:user_id>/block', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def block_user(user_id):
    if BlockedUser.get_filtered_by(user_id=user_id):
        flash('El usuario ya está bloqueado', 'warning')
    else:
        message = request.form.get('message', 'Sin razón especificada')
        BlockedUser.create(user_id=user_id, message=message, created=datetime.utcnow())
        flash('Usuario bloqueado con éxito', 'success')
    return redirect(url_for('admin_bp.admin_users'))


@admin_bp.route('/admin/users/<int:user_id>/unblock', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def unblock_user(user_id):
    blocked_user = BlockedUser.get_filtered_by(user_id=user_id)
    if blocked_user:
        blocked_user.delete()
        flash('Usuario desbloqueado con éxito', 'success')
    else:
        flash('El usuario no está bloqueado', 'warning')
    return redirect(url_for('admin_bp.admin_users'))


@admin_bp.route('/admin/products/<int:product_id>/ban', methods=['POST'])
@login_required
@require_moderator_role.require(http_exception=403)
def ban_product(product_id):
    reason = request.form.get('reason', 'No especificada')

    # Try to ban the product, and handle the result
    if BannedProduct.create(product_id=product_id, reason=reason):
        flash('Producto prohibido con éxito', 'success')
    else:
        flash('Este producto ya está prohibido', 'warning')

    return redirect(url_for('admin_bp.admin_products'))

@admin_bp.route('/admin/products/<int:product_id>/unban', methods=['POST'])
@login_required
@require_moderator_role.require(http_exception=403)
def unban_product(product_id):
    banned_product = BannedProduct.get(product_id)

    if banned_product and banned_product.delete():
        flash('Prohibición del producto retirada', 'success')
    else:
        flash('Este producto no está prohibido', 'warning')

    return redirect(url_for('admin_bp.admin_products'))