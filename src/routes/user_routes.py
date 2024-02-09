from flask import Blueprint, request
from controllers.user_controller import get_users, validate

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/usuarios', methods=['GET'])
def get_users_route():
    return get_users()

@user_routes.route('/login', methods=['POST'])
def validate_route():
    usuario = request.json['usuario']
    contra = request.json['contra']
    patron = 'InfoToolsSV'
    return validate(usuario, contra, patron)
