import os
from flask import Flask
from models.professor import Professor
from models.turma import Turma
from models.aluno import Aluno
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.professor_controller import registrar_rotas_professor

db = SQLAlchemy()

def criar_app():
    app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    registrar_rotas_professor(app)

    return app


if __name__ == "__main__":
    app = criar_app()
    app.run(debug=True)