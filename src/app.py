from flask import Flask
from routes.user_routes import user_routes
from routes.menu_routes import menu_routes
from models.usuario import db  
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://AdminWeb:admin145_w@127.0.0.1:1433/DesarrolloPerf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  


ma = Marshmallow(app)
app.register_blueprint(user_routes)
app.register_blueprint(menu_routes)

if __name__ == '__main__':
    app.run(port = 6000, debug=True)



