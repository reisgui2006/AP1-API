from . import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key =True)
    description = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable = False)
    data_nascimento = db.Column(db.DATE, nullable = False)
    first_note = db.Column(db.Float, nullable = False)
    second_note = db.Column(db.Float, nullable = False)
    media = db.Column(db.Float, nullable = False)