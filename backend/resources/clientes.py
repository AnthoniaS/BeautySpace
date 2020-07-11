from flask import Blueprint, jsonify, request
from banco import db
from config import config
from models.modelCliente import Cliente
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
import hashlib
from blacklist import blacklist
import smtplib

clientes = Blueprint('clientes', __name__)

@clientes.route('/login_cliente', methods=['POST'])
def login_cliente():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    senha = request.json.get('senha', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not senha:
        return jsonify({"msg": "Missing senha parameter"}), 400

    senha += config.SALT
    senha_md5 = hashlib.md5(senha.encode()).hexdigest()

    cliente = Cliente.query \
        .filter(Cliente.email == email) \
        .filter(Cliente.senha == senha_md5) \
        .first()
    if cliente:
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=email)
        return jsonify({"user": cliente.name, "access_token": access_token}), 200
    else:
        return jsonify({"user": None, "access_token": None}), 200

@clientes.route('/logout_cliente')
@jwt_required
def logout_cliente():
    jti = get_raw_jwt()['jwi']
    blacklist.add(jti)
    return jsonify({'msg': 'Successfuly logged out'})

@clientes.route('/clientes')
@jwt_required
def listar_cliente():
    clientes = Cliente.query.order_by(Cliente.name).all()
    return jsonify([cliente.to_json() for cliente in clientes])

@clientes.route('/clientes', methods=['POST'])
def incluir_cliente():
    cliente = Cliente.from_json(request.json)
    db.session.add(cliente)
    db.session.commit()
    return jsonify(cliente.to_json()), 201