from flask import Blueprint, jsonify, request
from banco import db
from models.modelServico import Servico
from flask_jwt_extended import jwt_required

servicos = Blueprint('servicos', __name__)

@servicos.route('/servicos')

def cadastro():
    servicos = Servico.query.order_by(Servico.nome_servico).all()
    return jsonify([servico.to_json() for servico in servicos])


@servicos.route('/servicos', methods=['POST'])
#@jwt_required
def inclusao():
    servico = Servico.from_json(request.json)
    db.session.add(servico)
    db.session.commit()
    return jsonify(servico.to_json()), 201


@servicos.route('/servicos/<int:id>')

def consulta(id):
    servico = Servico.query.get_or_404(id)
    return jsonify(servico.to_json()), 200


@servicos.errorhandler(404)

def id_invalido(error):
    return jsonify({'id': 0, 'message': 'not found'}), 404


@servicos.route('/servicos/<int:id>', methods=['PUT'])

def alteracao(id):
    servico = Servico.query.get_or_404(id)
    servico.nome_servico = request.json['nome_servico']
    servico.foto = request.json['foto']


    db.session.add(servico)
    db.session.commit()
    return jsonify(servico.to_json()), 204


@servicos.route('/servicos/<int:id>', methods=['DELETE'])

def exclui(id):
    Servico.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Serviço excluído com sucesso'}), 200


@servicos.route('/servicos/pesq/<palavra>')

def pesquisa(palavra):
    
    servicos = Servico.query.order_by(Servico.nome_servico).filter(
        Servico.nome_servico.like(f'%{palavra}%')).all()
    
    return jsonify([servico.to_json() for servico in servicos])
