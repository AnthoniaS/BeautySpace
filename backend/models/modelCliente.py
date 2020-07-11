from banco import db
from datetime import datetime
import hashlib
from config import config


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(11), nullable=False)
    senha = db.Column(db.String(32), nullable=False)


    servico_id = db.Column(db.Integer, db.ForeignKey(
        'servicos.id'), nullable=False)

    servico = db.relationship('Servico')
    

    def to_json(self):
        json_clientes = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
        return json_clientes


    @staticmethod
    def from_json(json_funcionarios):
        nome = json_funcionarios.get('nome')
        email = json_funcionarios.get('email')
        senha = json_funcionarios.get('senha') + config.SALT
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()
        return Cliente(nome=nome, email=email, senha=senha_md5)