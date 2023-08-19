import self
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Config. Base de datos

USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'flask_sqlalchemy'
FULL_URL_DB = f'mysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Config. de la migración
migrate = Migrate()
migrate.init_app(app, db)

Class Person(db.Model):
	id = db.Column(db.lnteger, primary_key=True)
	nombre = db.Column(db.String(250))
	apellide = db.Column(db.String(250))
	correo = db.Column(db.String(250))

def int (self, id, nombre, apellido, correo):
	self.id = id
	self.nombre = nombre
	self.apellido = apellido
	self.correo = correo

def json(self):
	return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'correo': self.correo}

def _ Str (self):
	return str(self.__class__) + ":" + str(self__dict__)