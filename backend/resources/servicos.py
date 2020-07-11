from flask import Blueprint, jsonify, request
from banco import db
from models.modelServico import Servico
from flask_jwt_extended import jwt_required


servicos = Blueprint('servicos', __name__)

@servicos.route('/servicos')
def listagem_servicos():
    servicos = Servico.query.order_by(Servico.id).all()
    return jsonify([servico.to_json() for servico in servicos])

@servicos.route('/servicos', methods=['POST'])
@jwt_required
def inclusao_servicos():
    servico = Servico.from_json(request.json)
    db.session.add(servico)
    db.session.commit()
    return jsonify(servico.to_json()), 201

@servicos.route('/servicos/<int:id>', methods=['PUT'])
@jwt_required
def alterar_servicos(id):
    servicos = Servico.query.get_or_404(id)
    servicos.nome_servico = request.json['nome_servico']
    servicos.foto = request.json['foto']
    db.session.add(servicos)
    db.session.commit()
    return jsonify(servicos.to_json()), 204

@servicos.route('/servicos/<int:id>', methods=['DELETE'])
def excluir_marca():
    Servico.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Servico excluido.'}), 200