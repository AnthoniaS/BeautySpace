from flask import Flask
from config import config
from banco import db
from resources.servicos import servicos
from resources.usuarios import usuarios
from resources.agendamentos import agendamentos
from flask_jwt_extended import JWTManager
from blacklist import blacklist
import smtplib
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(servicos)
app.register_blueprint(usuarios)
app.register_blueprint(agendamentos)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/')
def raiz():
    db.create_all()
    return '<h2>Beauty Space</h2>'


@app.route('/envia_email')
def envia():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('anthoniasr6@gmail.com', 'anthoniasr6')
    server.set_debuglevel(1)
    msg = 'Subject: Teste PI2\nÓla Teste de Envio de e-mail pelo Python\nÉ bom esse Python!!'.encode(
        'utf-8')
    server.sendmail('conta.teste.laravel@gmail.com',
                    'anthoniasr@gmail.com', msg)
    server.quit()
    return "OK! E-mail Enviado."


if __name__ == '__main__':
    app.run(debug=True)
