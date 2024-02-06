from flask import jsonify
from . import api_bp

# Simulando datos de categorías; reemplazar con consulta a base de datos si es necesario
CATEGORIAS_DISPONIBLES = ['Category 1', 'Category 2', 'Category 3']

@api_bp.route('/categories', methods=['GET'])
def listar_categorias():
    return jsonify({'data': CATEGORIAS_DISPONIBLES, 'success': True}), 200
