from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Configuración de la base de datos MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'oa'

# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/oa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos MySQL y SQLAlchemy
mysql = MySQL(app)
db = SQLAlchemy(app)

# Importar modelos para que SQLAlchemy los reconozca al crear la base de datos
from app.models import User, Course, Module, Role

# Crear la base de datos y los roles si no existen
@app.before_request
def setup_database():
    db.create_all()

    # Crear roles si no existen
    roles = ['Admin', 'Instructor', 'Student']
    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if role is None:
            role = Role(name=role_name)
            db.session.add(role)
    db.session.commit()

# Importar las rutas para que Flask las reconozca
from app import routes
