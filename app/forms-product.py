from flask_wtf import FlaskForm
from wtforms import StringField,\
    validators, SubmitField, IntegerField
from wtforms.fields import SelectField
from controllers.category import CategoryBD


class ProductForm(FlaskForm):

    categories = CategoryBD().show_categories_tb()
    name = StringField(
        'Nombre',
        [validators.DataRequired(
            message="Favor ingrese el nombre del producto")],
        render_kw={'class': 'catName'})
    description = StringField(
        'Descripción',
        [validators.DataRequired(
            message="Favor ingrese la descripcion del producto")])
    code = StringField(
        'Código',
        [validators.DataRequired(
            message="Favor ingrese el código del producto")])
    stock = IntegerField(
        'Cantidad',
        [validators.DataRequired(
            message="Favor ingrese la cantidad total del producto")])
    available_stock = IntegerField(
        'Cantida disponible',
        [validators.DataRequired(
            message="Favor ingrese la cantidad disponible\
                en bodega del producto")])
    price = IntegerField(
        'Precio',
        [validators.DataRequired(
            message="Favor ingrese el código del producto")])
    category_id = SelectField(
        'Categoría',
        choices=[(category.id, category.name) for category in categories])
    select = SelectField('Estado', choices=[
            (1, 'Activo'), (0, 'Inactivo')])
    submit = SubmitField("Crear Producto")
