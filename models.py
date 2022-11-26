#Aqui crearemos el modelo de base de datos

#Se importa sqlAlchemy
from flask_sqlalchemy import SQLAlchemy

#Creacion de los objetos con los cual manipularemos la BD
db = SQLAlchemy()
Model = db.Model
Column = db.Column

#Mapeo de la tabla Estudiantes a una clase(es decir convertir a un objeto)
class pacientes(Model):
	__tablename__ = "users"
	id = Column(db.Integer, primary_key=True)
	rol_id = Column(db.Integer,nullable=True)
	nombres = Column(db.Text, nullable=True)
	apellidos = Column(db.Text, nullable=True)
	correo = Column(db.Text, nullable=True)
	telefono = Column(db.Text, nullable=True)
	direccion = Column(db.Text, nullable=True)
	sexo = Column(db.Text, nullable=True)
	cedula = Column(db.Text, nullable=True)


	#def __repr__(self):
		#return "{}-{}-{}-{}".format(self.nombres,self.apellidos,self.grupo,self.departamento)

