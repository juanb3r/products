import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


def _get_date():
    return datetime.datetime.now()


class Category(Base):
    __tablename__ = "categorias"
    id = Column("idCat", Integer, primary_key=True)
    name = Column("categoria", String(80), nullable=False)
    date = Column("fecha", Date, default=_get_date)


class Product(Base):
    __tablename__ = "productos"
    id = Column("id", Integer, primary_key=True)
    category_id = Column("id_categoria", Integer, ForeignKey('category.id'))
    code = Column("codigo", String(250), nullable=False)
    name = Column("descripcion", String(250))
    image = Column("imagen", String(80), nullable=False)
    stock = Column(Integer)
    current_stock = Column("cantidad", Integer)
    price = Column("precio_compra", Integer)
    sell_price = Column("precio_venta", Integer)
    sells = Column("ventas", Integer)
    date = Column("fecha", Date, default=_get_date)
    category = relationship(Category)


class Rol(Base):
    __tablename__ = 'rol'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    state = Column(Boolean)


# Engine = \
#   create_engine('mysql://jeltexbdUser:juan123..@localhost:3308/alquiler_bd')
# engine = create_engine("sqlite:///alquiler_bd.db")
# Base.metadata.create_all(engine)
