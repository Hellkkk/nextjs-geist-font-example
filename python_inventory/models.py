from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_bem = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    objeto = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    data_aquisicao = db.Column(db.Date, nullable=False)
    nota_fiscal = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    estado_conservacao = db.Column(db.String(50), nullable=False)
    setor_alocado = db.Column(db.String(50), nullable=False)
    responsavel_operador = db.Column(db.String(50), nullable=False)
    data_entrega = db.Column(db.Date, nullable=True)
    manutencao_dada = db.Column(db.String(50), nullable=True)
    servico_realizado = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Equipment {self.num_bem}: {self.objeto}>'
