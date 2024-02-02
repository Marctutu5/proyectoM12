from flask import request, jsonify
from . import api_bp
from ..models import Order
from .. import db_manager as db

@api_bp.route('/orders', methods=['POST'])
def crear_oferta():
    data = request.get_json()
    # Validar datos recibidos aquí
    order = Order.create(**data)
    if order:
        return jsonify({'data': order.to_dict(), 'success': True}), 201
    else:
        return jsonify({'error': 'Bad Request', 'message': 'No se pudo crear la oferta', 'success': False}), 400

@api_bp.route('/orders/<int:id>', methods=['PUT'])
def editar_oferta(id):
    order = Order.query.get_or_404(id)
    data = request.get_json()
    # Validar datos recibidos aquí
    updated_order = order.update(**data)
    if updated_order:
        return jsonify({'data': updated_order.to_dict(), 'success': True}), 200
    else:
        return jsonify({'error': 'Bad Request', 'message': 'No se pudo actualizar la oferta', 'success': False}), 400

@api_bp.route('/orders/<int:id>', methods=['DELETE'])
def anular_oferta(id):
    order = Order.query.get_or_404(id)
    if order.delete():
        return jsonify({'success': True}), 204
    else:
        return jsonify({'error': 'Bad Request', 'message': 'No se pudo anular la oferta', 'success': False}), 400
