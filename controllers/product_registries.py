from controllers.database_setup import ProductRegistries
from app.app import db


class ProductRegistryDB():

    def __init__(self) -> None:
        self.db = db

    def show_products_registries_tb(self) -> ProductRegistries:
        try:
            products = self.db.session.query(ProductRegistries).all()
        except Exception:
            self.db.session.rollback()
        finally:
            self.db.session.close()
            return products

    def new_registry_tb(
            self,
            product_id: int,
            stock: int,
            description: str,
            responsible: str,
            state: bool) -> bool:

        new_product_registry = ProductRegistries(
            product_id=product_id,
            stock=stock,
            description=description,
            responsible=responsible,
            state=state)
        try:
            self.db.session.add(new_product_registry)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True

    def get_product_registry_by_id_tb(self, id):
        try:
            product_registry = self.db.session.query(
                ProductRegistries).filter_by(id=id).one()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return product_registry

    def edit_product_registry_tb(self, product_registry):
        try:
            self.db.session.add(product_registry)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True

    def delete_new_product_registry_tb(self, id):
        try:
            new_product_registry = self.get_product_by_id_tb(id)
            self.db.session.delete(new_product_registry)
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            return False
        finally:
            self.db.session.close()
            return True
