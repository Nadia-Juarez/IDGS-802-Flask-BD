from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("id")
    nombre=StringField("nombre")
    apellidos=StringField("apellidos")
    email=EmailField("correo")