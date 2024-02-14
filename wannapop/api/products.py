from flask import request, jsonify
from .helper_auth import basic_auth, token_auth
from . import api_bp
from ..models import Product, Order, db



@api_bp.route('/products', methods=['GET'])
def listar_productos():
    title = request.args.get('title')
    if title:
        products = Product.query.filter(Product.title.contains(title)).all()
    else:
        products = Product.query.all()
    return jsonify({'data': [product.to_dict() for product in products], 'success': True}), 200

@api_bp.route('/products/<int:id>', methods=['GET'])
def ver_detalle_producto(id):
    product = Product.query.get_or_404(id)
    return jsonify({'data': product.to_dict(), 'success': True}), 200

@api_bp.route('/products/<int:id>', methods=['PUT'])
@token_auth.login_required
def editar_producto_propio(id):
    current_user = token_auth.current_user()
    current_user_id = current_user.id
    product = Product.query.get_or_404(id)
    if current_user_id == product.seller_id:
        data = request.get_json()

        # Intenta obtener el producto de la base de datos
        product = Product.query.get(id)

        # Si no se encuentra el producto, devuelve un error 404
        if product is None:
            return jsonify({'error': 'Not Found', 'message': 'Producto no encontrado', 'success': False}), 404

        # Actualiza los campos del producto con los datos proporcionados
        try:
            product.update(**data)
            return jsonify({'data': product.to_dict(), 'success': True}), 200
        except Exception as e:
            return jsonify({'error': 'Internal Server Error', 'message': str(e), 'success': False}), 500
    else:
        return jsonify({'error': 'Sin permisos de edicion', 'success': False}), 500

@api_bp.route('/products/<int:id>/orders', methods=['GET'])
def listar_ofertas_recibidas(id):
    orders = Order.query.filter_by(product_id=id).all()
    return jsonify({'data': [order.to_dict() for order in orders], 'success': True}), 200
