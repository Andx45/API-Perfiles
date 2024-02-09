from flask import jsonify
from models.menus import Menu, MenuProfiles, db  
from flask_sqlalchemy import SQLAlchemy

def get_menusdin(id):
    queryMenus = db.session.query(Menu, MenuProfiles).join(MenuProfiles, Menu.MenuID == MenuProfiles.MenuId).filter(MenuProfiles.PerfilId == id).all()

    if queryMenus:
        result_menusdin = []
        for menu, menuprofiles in queryMenus:
            result = {
                'MenuID' : menu.MenuID,
                'NombreMenu': menu.NombreMenu,
                'URL': menu.URL,
                'MenuPadre': menu.MenuPadreID,
                'PerfilId': menuprofiles.PerfilId
            }
            result_menusdin.append(result)
    else:
        result_menusdin = {
            'error': 'Ningún registro'
        }

    return jsonify(result_menusdin)
