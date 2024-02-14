from flask import request, jsonify
from .helper_auth import basic_auth, token_auth
from . import api_bp
from ..models import Order, ConfirmedOrder
from .. import db_manager as db

@api_bp.route('/orders', methods=['POST'])
@token_auth.login_required
def crear_oferta():
    current_user = token_auth.current_user()
    current_user_id = current_user.id

    # # Obtener el producto asociado con la orden
    # order = Order.query.get_or_404(id)
    # if current_user_id == order.buyer_id:
    data = request.get_json()
    # Validar datos recibidos aquí
    data['buyer_id'] = current_user_id
    order = Order.create(**data)
    if order:
        return jsonify({'data': order.to_dict(), 'success': True}), 201
    else:
        return jsonify({'error': 'Bad Request', 'message': 'No se pudo crear la oferta', 'success': False}), 400

@api_bp.route('/orders/<int:id>', methods=['PUT'])
@token_auth.login_required
def editar_oferta(id):
    current_user = token_auth.current_user()
    current_user_id = current_user.id

    order = Order.query.get_or_404(id)
    if current_user_id == order.buyer_id:
        data = request.get_json()
        # Validar datos recibidos aquí
        updated_order = order.update(**data)
        if updated_order:
            return jsonify({'data': updated_order.to_dict(), 'success': True}), 200
        else:
            return jsonify({'error': 'Bad Request', 'message': 'No se pudo actualizar la oferta', 'success': False}), 400
    else:
        return jsonify({'error': 'Forbidden', 'message': 'No tiene permiso para aceptar esta oferta', 'success': False}), 403


@api_bp.route('/orders/<int:id>', methods=['DELETE'])
@token_auth.login_required
def anular_oferta(id):
    current_user = token_auth.current_user()
    current_user_id = current_user.id

    order = Order.query.get_or_404(id)
    if current_user_id == order.buyer_id:
        if order.delete():
            return jsonify({'success': True}), 204
        else:
            return jsonify({'error': 'Bad Request', 'message': 'No se pudo anular la oferta', 'success': False}), 400
    else:
        return jsonify({'error': 'Forbidden', 'message': 'No tiene permiso para aceptar esta oferta', 'success': False}), 403


@api_bp.route('/orders/<int:id>/confirmed', methods=['POST'])
@token_auth.login_required
def aceptar_oferta(id):
    current_user = token_auth.current_user()
    current_user_id = current_user.id

    # Obtener el producto asociado con la orden
    order = Order.query.get_or_404(id)
    product = order.product

    # Verificar si el usuario actual es el vendedor del producto
    if current_user_id == product.seller_id:
        try:
            # Creamos una instancia de ConfirmedOrder utilizando el método create del mixin
            confirmed_order = ConfirmedOrder.create(order=order)
            return jsonify({'message': 'Oferta aceptada exitosamente', 'success': True}), 200
        except Exception as e:
            return jsonify({'error': 'Internal Server Error', 'message': str(e), 'success': False}), 500
    else:
        return jsonify({'error': 'Forbidden', 'message': 'No tiene permiso para aceptar esta oferta', 'success': False}), 403


@api_bp.route('/orders/<int:id>/confirmed', methods=['DELETE'])
@token_auth.login_required
def anular_oferta_aceptada(id):
    current_user = token_auth.current_user()
    current_user_id = current_user.id

    # Obtener la orden correspondiente
    order = Order.query.get_or_404(id)

    # Obtener el producto asociado con la orden
    product = order.product

    # Verificar si el usuario actual es el vendedor del producto
    if current_user_id == product.seller_id:
        confirmed_order = ConfirmedOrder.query.filter_by(order_id=id).first_or_404()
        
        try:
            confirmed_order.delete()
            return jsonify({'message': 'Oferta aceptada anulada exitosamente', 'success': True}), 200
        except Exception as e:
            return jsonify({'error': 'Internal Server Error', 'message': str(e), 'success': False}), 500
    else:
        return jsonify({'error': 'Forbidden', 'message': 'No tiene permiso para anular esta oferta', 'success': False}), 403