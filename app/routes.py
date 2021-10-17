from controllers.category import CategoryBD
from controllers.user import UserDB
from utils.form_checker import ProductForm, UserForm
from controllers.product import ProductDB
from controllers.product_registries import ProductRegistryDB
from flask import render_template,\
    redirect, url_for, flash, session
from app.app import app
from utils.generals import md5_encrypt


categories_bd = CategoryBD()
products_bd = ProductDB()
registries_bd = ProductRegistryDB()
user_bd = UserDB()


# LOGIN/LOGOUT ROUTES
@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get("username") and session.get("state"):
        return redirect(url_for("show_products"))

    form = UserForm()

    if form.validate_on_submit():
        username = form.name.data
        password = md5_encrypt(form.password.data)
        user = user_bd.get_user_by_tb(username, password)
        if user.username == username and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.username
            session["state"] = user.state
            return redirect(url_for('show_products'))
        else:
            return render_template(
                'login/login.html',
                form=form)
    else:
        return render_template(
            'login/login.html',
            form=form)


@app.route("/logout")
def logout():
    """Ruta que permite la terminación de la sesión"""

    session["user_id"] = False
    session.pop("username", None)
    return redirect(url_for("login"))


# PRODUCTS ROUTES
@app.route('/productos')
@app.route('/productos/')
def show_products():
    if not session.get("username") and not session.get("state"):
        return redirect(url_for("login"))

    products = products_bd.show_products_tb()
    return render_template('products/products.html', products=products)


@app.route(
    '/productos/<int:product_id>/<string:action>',
    methods=['GET', 'POST'])
def edit_product(product_id, action):

    if not session.get("username") and not session.get("state"):
        return redirect(url_for("login"))

    form = ProductForm()
    product = products_bd.get_product_by_id_tb(product_id)

    if form.validate_on_submit():
        name = form.name.data.upper()
        description = form.description.data
        stock = form.stock.data
        if action == "entrada":
            product.stock += stock
            product.real_stock += stock
            state = True
        elif action == "salida":
            product.stock -= stock
            product.real_stock -= stock
            state = False
        result_registry = registries_bd.new_registry_tb(
            product.id, stock, description, name, state)
        result_product = products_bd.edit_product_tb(product=product)
        if result_registry and result_product:
            flash('Se realizó registro')
            render = redirect(url_for('show_products'))
        else:
            flash('No se pudo realizar registro')
            render = render_template(
                        'products/register_product.html',
                        action=action,
                        product=product,
                        form=form)
    else:
        render = render_template(
                        'products/register_product.html',
                        action=action,
                        product=product,
                        form=form)

    return render


# CATEGORIES ROUTES
@app.route('/registros')
@app.route('/registros/')
def show_registries():
    if not session.get("username") and not session.get("state"):
        return redirect(url_for("login"))

    registries = registries_bd.show_products_registries_tb()
    return render_template(
            'products/registries.html',
            registries=registries)
