from controllers.database_setup import Product
from controllers.db_session import DBSession


class ProductDB(DBSession):

    def __init__(self) -> None:
        super().__init__()
        self.session = self.get_session()

    def show_products_tb(self) -> Product:
        products = self.session.query(Product).all()
        return products

    def new_product_tb(
            self,
            name: str,
            description: str,
            code: str,
            stock: int,
            c_stock,
            price,
            category_id,
            state) -> bool:

        new_product = Product(
            name=name,
            description=description,
            code=code,
            current_stock=c_stock,
            stock=stock,
            price=price,
            category_id=category_id,
            state=state)

        self.session.add(new_product)
        self.session.commit()
        self.session.close()
        return True

    def get_product_by_id_tb(self, id):
        product = self.session.query(Product).filter_by(id=id).one()
        return product

    def edit_product_tb(self, product):
        self.session.add(product)
        self.session.commit()
        self.session.close()
        return True

    def delete_product_tb(self, id):
        product = self.get_product_by_id_tb(id)
        self.session.delete(product)
        self.session.commit()
        self.session.close()
        return True
