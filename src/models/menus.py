from flask_sqlalchemy import SQLAlchemy
from .usuario import db

class Menu(db.Model):
    __tablename__ = 'Menu'
    __table_args__ = {'schema': 'ProyectoWeb'}
    MenuID = db.Column(db.Integer, primary_key=True)
    NombreMenu = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.String(200))
    URL = db.Column(db.String(200))
    MenuPadreID = db.Column(db.Integer, db.ForeignKey('Menu.MenuID'))

    def __init__(self, NombreMenu, Descripcion, URL, MenuPadreID=None):
        self.NombreMenu = NombreMenu
        self.Descripcion = Descripcion
        self.URL = URL
        self.MenuPadreID = MenuPadreID


class MenuProfiles(db.Model):
    __tablename__ = "Perfil_Menu"
    __table_args__ = {'schema': 'ProyectoWeb'}
    PerfilId = db.Column(db.Integer, primary_key = True)
    MenuId = db.Column(db.Integer, primary_key = True)

    def __init__ (self, PerfilId, MenuId):
        self.PerfilId = PerfilId
        self.MenuId = MenuId