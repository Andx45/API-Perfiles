from flask import Blueprint
from controllers.menu_controller import get_menusdin

menu_routes = Blueprint('menu_routes', __name__)

@menu_routes.route('/menus/<id>', methods=['GET'])
def get_menusdin_route(id):
    return get_menusdin(id)
