from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="ingrese un valor valido")
        ])
    
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="ingrese nombre valido")])
    aparteno=StringField("Apaterno",[
        validators.DataRequired(message="El campo es requerido"),])
    amaterno=StringField("Amaterno",[
        validators.DataRequired(message="El campo es requerido"),])
    correo=EmailField("Correo",[
        validators.email(message="ingrese un correo valido"),])