from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("Id")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    email=EmailField("Correo")