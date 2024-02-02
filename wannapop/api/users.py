from flask import request, jsonify
from . import api_bp
from ..models import User, Product

@api_bp.route('/users', methods=['GET'])
def listar_usuarios():
    name = request.args.get('name')
    if name:
        users = User.query.filter(User.name.contains(name)).all()
    else:
        users = User.query.all()
    return jsonify({'data': [user.to_dict() for user in users], 'success': True}), 200

@api_bp.route('/users/<int:id>', methods=['GET'])
def ver_perfil_usuario(id):
    user = User.query.get_or_404(id)
    return jsonify({'data': user.to_dict(), 'success': True}), 200

@api_bp.route('/users/<int:id>/products', methods=['GET'])
def listar_productos_usuario(id):
    products = Product.query.filter_by(seller_id=id).all()
    return jsonify({'data': [product.to_dict() for product in products], 'success': True}), 200
