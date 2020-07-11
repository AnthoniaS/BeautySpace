from banco import db
import hashlib
from config import config


class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    foto = db.Column(db.String(120), nullable=False)

    carros = db.relationship('Cliente')    

    def to_json(self):
        json_servicos = {
            'id': self.id,
            'nome': self.nome,
            'foto' : self.foto,
        }
        return json_servicos
    
    @staticmethod
    def from_json(json_servicos):
        nome = json_servicos.get('nome')
        foto = json_servicos.get('foto')
        return Servico(nome=nome, foto=foto)        
