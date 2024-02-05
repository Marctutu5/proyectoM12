from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from .models import Product, Category, BlockedUser, BannedProduct
from .forms import ProductForm, DeleteForm, ProductBannedForm
from werkzeug.utils import secure_filename
from . import db_manager as db
import uuid
import os
from .helper_role import require_admin_role, require_moderator_role, require_create_permission, require_read_permission, require_update_permission, require_delete_permission, Role

# Blueprint
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route('/')
def init():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.product_list'))
    else:
        return redirect(url_for("auth_bp.login"))

@main_bp.route('/products/lista')
@login_required
@require_read_permission.require(http_exception=403)
def product_list():
    current_user_id = current_user.id if current_user.is_authenticated else None

    # Fetch products with categories using get_all_with method
    products_with_category_and_ban = Product.get_all_with(Category, BannedProduct)

    # Render the template with the product information
    return render_template('products/list.html', products_with_category_and_ban=products_with_category_and_ban, current_user_id=current_user_id)

@main_bp.route('/products/create', methods=['POST', 'GET'])
@login_required
@require_create_permission.require(http_exception=403)
def product_create():
    if BlockedUser.query.filter_by(user_id=current_user.id).first():
        flash("No puedes crear productos porque tu cuenta está bloqueada.", "error")
        return redirect(url_for('main_bp.product_list'))

    categories = Category.get_all()

    form = ProductForm()
    form.category_id.choices = [(category.id, category.name) for category in categories]

    if request.method == 'POST' and form.validate_on_submit():
        new_product = Product()
        new_product.seller_id = current_user.id

        form.populate_obj(new_product)

        # handle photo upload here

        new_product.save()

        flash("Nou producte creat", "success")
        return redirect(url_for('main_bp.product_list'))

    return render_template('products/create.html', form=form)


@main_bp.route('/products/read/<int:product_id>')
@login_required
@require_read_permission.require(http_exception=403)
def product_read(product_id):
    try:
        # Query the database to get product details with join
        product, category = Product.get_with(product_id, Category)
        
        if not product:
            flash("Product not found", "error")
            return redirect(url_for('main_bp.product_list'))

        return render_template('products/read.html', product=product, category=category)
    except Exception as e:
        flash(f"Error fetching product details: {str(e)}", "error")
        return redirect(url_for('main_bp.product_list'))

@main_bp.route('/products/update/<int:product_id>', methods=['POST', 'GET'])
@login_required
@require_update_permission.require(http_exception=403)
def product_update(product_id):
    try:
        product = Product.get(product_id)

        # Check if the current user is the owner of the product
        if current_user.role == Role.wanner and product.seller_id != current_user.id:
            flash("No tienes permiso para editar este producto.", "danger")
            return redirect(url_for('main_bp.product_list'))

        categories = Category.get_all()

        form = ProductForm(obj=product)
        form.category_id.choices = [(category.id, category.name) for category in categories]

        if form.validate_on_submit():
            form.populate_obj(product)

            # Handle photo upload here
            # filename = __manage_photo_file(form.photo_file)
            # if filename:
            #     product.photo = filename

            product.save()

            flash("Producte actualitzat", "success")
            return redirect(url_for('main_bp.product_read', product_id=product_id))

        return render_template('products/update.html', product_id=product_id, form=form)
    except Exception as e:
        flash(f"Error updating product: {str(e)}", "error")
        return redirect(url_for('main_bp.product_list'))

@main_bp.route('/products/delete/<int:product_id>', methods=['GET', 'POST'])
@login_required
@require_delete_permission.require(http_exception=403)
def product_delete(product_id):
    try:
        product = Product.get(product_id)

        # Check if the current user is the owner of the product
        if current_user.role == Role.wanner and product.seller_id != current_user.id:
            flash("No tienes permiso para eliminar este producto.", "danger")
            return redirect(url_for('main_bp.product_list'))

        form = DeleteForm()
        if form.validate_on_submit():
            product.delete()

            flash("Producte esborrat", "success")
            return redirect(url_for('main_bp.product_list'))

        return render_template('products/delete.html', form=form, product=product)
    except Exception as e:
        flash(f"Error deleting product: {str(e)}", "error")
        return redirect(url_for('main_bp.product_list'))

def __manage_photo_file(photo_file):
    # si hi ha fitxer
    if photo_file.data:
        filename = photo_file.data.filename.lower()

        # és una foto
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # M'asseguro que el nom del fitxer és únic per evitar col·lissions
            unique_filename = str(uuid.uuid4())+ "-" + secure_filename(filename)
            photo_file.data.save(__uploads_folder + unique_filename)
            return unique_filename

    return None

