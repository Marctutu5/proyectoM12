from flask import jsonify
from . import api_bp

# Simulando datos de estados; reemplazar con consulta a base de datos si es necesario
ESTADOS_DISPONIBLES = ['Activo', 'Inactivo', 'Pendiente']

@api_bp.route('/statuses', methods=['GET'])
def listar_estados():
    return jsonify({'data': ESTADOS_DISPONIBLES, 'success': True}), 200
