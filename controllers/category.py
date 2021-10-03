from controllers.database_setup import Category
from controllers.db_session import DBSession


class CategoryBD(DBSession):

    def __init__(self) -> None:
        super().__init__()
        self.session = self.get_session()

    def show_categories_tb(self):
        categories = self.session.query(Category).all()
        return categories

    def get_category_by_id_tb(self, id):
        category = self.session.query(Category).filter_by(idCat=id).one()
        return category

    def new_category_tb(self, name):
        new_category = Category(name=name)
        self.session.add(new_category)
        self.session.commit()
        self.session.close()
        return True

    def edit_category_tb(self, category):
        self.session.add(category)
        self.session.commit()
        self.session.close()
        return True

    def delete_category_tb(self, id):
        category = self.get_category_by_id_tb(id)
        self.session.delete(category)
        self.session.commit()
        self.session.close()
        return True
