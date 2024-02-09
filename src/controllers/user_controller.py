from flask import jsonify, request
from models.usuario import Usuario, db  
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('UsuarioId', 'Usuario')

usuario_schema = UsuarioSchema()

usuarios_schema = UsuarioSchema(many=True)

def get_users():
    all_users = Usuario.query.all()
    result = usuarios_schema.dump(all_users)
    return jsonify(result)

def validate(usuario, contra, patron):
    sql = text('''
        SELECT U.UsuarioId, U.Usuario, U.Contra, PU.PerfilId
        FROM ProyectoWeb.Usuario AS U
        INNER JOIN ProyectoWeb.Perfiles_Usuarios AS PU
        ON U.UsuarioId = PU.UsuarioID
        WHERE U.Usuario = :usuario
        AND CONVERT(varchar(50), DECRYPTBYPASSPHRASE(:patron, U.Contra)) = :contra;
    ''')

    result = db.session.execute(sql, {
        'usuario': usuario,
        'contra': contra,
        'patron': patron
    })

    row = result.fetchone()

    if row:
        response_json = {
            'UsuarioId': row.UsuarioId,
            'Usuario': row.Usuario,
            'PerfilId': row.PerfilId,
            'message': 'Credenciales Correctas'
        }
        return jsonify(response_json)
    else:
        return jsonify({'UsuarioId': 0, 'message': 'Credenciales Incorrectas'})
