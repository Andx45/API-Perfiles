from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    __table_args__ = {'schema': 'ProyectoWeb'}
    UsuarioId = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Apellido = db.Column(db.String(100))
    Email = db.Column(db.String(200))
    Usuario = db.Column(db.String(100), nullable=False)
    Contra = db.Column(db.LargeBinary(100), nullable=False)

    def __init__(self, Usuario, Contra):
        self.Usuario = Usuario
        self.Contra = Contra
