import datetime
from app.app import db


def _get_date():
    return datetime.datetime.now()


class Category(db.Model):
    __tablename__ = "categorias"
    id = db.Column("idCat", db.Integer, primary_key=True)
    name = db.Column("categoria", db.String(80), nullable=False)
    date = db.Column("fecha", db.Date, default=_get_date)


class Product(db.Model):
    __tablename__ = "productos"
    id = db.Column("id", db.Integer, primary_key=True)
    category_id = db.Column(
        "id_categoria",
        db.Integer,
        db.ForeignKey("categorias.idCat"))
    code = db.Column("codigo", db.String(250), nullable=False)
    name = db.Column("descripcion", db.String(250))
    image = db.Column("imagen", db.String(80))
    stock = db.Column(db.Integer)
    real_stock = db.Column("cantidad", db.Integer)
    price = db.Column("precio_compra", db.Integer)
    sell_price = db.Column("precio_venta", db.Integer)
    sells = db.Column("ventas", db.Integer)
    date = db.Column("fecha", db.Date, default=_get_date)
    category = db.relationship(Category, lazy='subquery')


class ProductRegistries(db.Model):
    __tablename__ = "registro_productos"
    id = db.Column("id", db.Integer, primary_key=True)
    product_id = db.Column(
        "id_productos",
        db.Integer,
        db.ForeignKey("productos.id"))
    stock = db.Column("cantidad", db.Integer)
    description = db.Column("descripcion", db.String(250))
    responsible = db.Column("responsable", db.String(50))
    state = db.Column("estado", db.Boolean)
    date = db.Column("fecha", db.Date, default=_get_date)
    product = db.relationship(Product, lazy='subquery')


class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("nombre", db.String(250))
    username = db.Column("usuario", db.String(250))
    password = db.Column("password", db.String(80))
    profile = db.Column("perfil", db.String(250))
    image = db.Column("foto", db.String(250))
    state = db.Column("estado", db.Boolean)
    last_login = db.Column("ultimo_login", db.String(250))
    date = db.Column("fecha", db.Date, default=_get_date)
