from datetime import datetime

from controllers.database_setup import Product
from app.app import db


class ProductDB():

    def __init__(self) -> None:
        self.db = db

    def show_products_tb(self) -> Product:
        try:
            products = self.db.session.query(Product).all()
        except Exception:
            self.db.session.rollback()
        finally:
            self.db.session.close()
            return products

    def new_product_tb(
            self,
            category_id: int,
            code: str,
            name: str,
            image: str,
            stock: int,
            current_stock: int,
            price: int,
            sell_price: int,
            sells: int,
            date: datetime) -> bool:

        new_product = Product(
            category_id=category_id,
            code=code,
            name=name,
            image=image,
            stock=stock,
            current_stock=current_stock,
            price=price,
            sell_price=sell_price,
            sells=sells,
            date=date)
        try:
            self.db.session.add(new_product)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True

    def get_product_by_id_tb(self, id):
        try:
            product = self.db.session.query(Product).filter_by(id=id).one()
        except Exception:
            self.db.session.rollback()
        finally:
            self.db.session.close()
            return product

    def edit_product_tb(self, product):
        try:
            self.db.session.add(product)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True

    def delete_product_tb(self, id):
        try:
            product = self.get_product_by_id_tb(id)
            self.db.session.delete(product)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True
