from banco import db
import hashlib
from config import config


class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    nome_servico = db.Column(db.String(60), nullable=False)
    foto = db.Column(db.String(120), nullable=False)


    def to_json(self):
        json_servicos = {
            'id': self.id,
            'nome_servico': self.nome_servico,
            'foto' : self.foto,
        }
        return json_servicos
    
    @staticmethod
    def from_json(json_servicos):
        nome_servico = json_servicos.get('nome_servico')
        foto = json_servicos.get('foto')
        return Servico(nome_servico=nome_servico, foto=foto)        
