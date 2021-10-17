from flask_wtf import FlaskForm
from wtforms import StringField,\
    validators, SubmitField, IntegerField


class CategoryForm(FlaskForm):
    name = StringField(
        'Nombre',
        [validators.DataRequired(
            message="Favor ingrese el nombre de la categoría")],
        render_kw={'class': 'form-control', 'type': 'text'})
    submit = SubmitField("Crear categoría")


class ProductForm(FlaskForm):

    name = StringField(
        'Responsable',
        [validators.DataRequired(
                message="Favor ingrese el nombre del producto")],
        render_kw={'class': 'form-control', 'type': 'text'})
    description = StringField(
        'Descripción',
        [validators.DataRequired(
            message="Favor ingrese el código del producto")],
        render_kw={'class': 'form-control', 'type': 'text'})
    stock = IntegerField(
        'Cantidad',
        [
            validators.DataRequired(
                message="Favor ingrese la cantidad a registrar de producto"),
            validators.NumberRange(min=0, message="No puede ser menor que 0")],
        render_kw={'class': 'form-control', 'type': 'number'})
    submit = SubmitField("Crear registro",
            render_kw={'class': 'btn btn-primary'})


class UserForm(FlaskForm):
    name = StringField(
        'Nombre',
        [validators.DataRequired(
            message="Favor ingrese el nombre de la categoría")],
        render_kw={'class': 'form-control', 'type': 'text'})
    password = StringField(
        'Password',
        [validators.DataRequired(
            message="Favor ingrese el nombre de la categoría")],
        render_kw={'class': 'form-control', 'type': 'password'})
    submit = SubmitField("Ingresar")