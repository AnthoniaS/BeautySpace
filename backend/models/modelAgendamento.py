from banco import db

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    data = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.String(50), nullable=False)
    

    servico_id = db.Column(db.Integer, db.ForeignKey(
        'servicos.id'),nullable=False)

    servico = db.relationship('Servico')
    
    def to_json(self):
        json_agendamentos = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'servico_id': self.servico_id,
            'servico': self.servico.nome_servico,
            'data': self.data,
            'hora': self.hora            
        }
        return json_agendamentos

    @staticmethod
    def from_json(json_agendamentos):
        nome = json_agendamentos.get('nome')
        email = json_agendamentos.get('email')
        telefone = json_agendamentos.get('telefone')
        servico_id = json_agendamentos.get('servico_id')
        data = json_agendamentos.get('data')
        hora = json_agendamentos.get('hora')

        return Agendamento(nome=nome, email=email, telefone=telefone, servico_id=servico_id, data=data, hora=hora)
