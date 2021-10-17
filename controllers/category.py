from controllers.database_setup import Category
from app.app import db


class CategoryBD():

    def __init__(self) -> None:
        self.db = db

    def show_categories_tb(self):
        try:
            categories = self.db.session.query(Category).all()
            return categories
        except Exception:
            return {"data": "error"}

    def get_category_by_id_tb(self, id):
        category = self.db.session.query(Category).filter_by(id=id).one()
        return category

    def new_category_tb(self, name):
        new_category = Category(name=name)
        self.db.session.add(new_category)
        self.db.session.commit()
        self.db.session.close()
        return True

    def edit_category_tb(self, category):
        self.db.session.add(category)
        self.db.session.commit()
        self.db.session.close()
        return True

    def delete_category_tb(self, id):
        category = self.db.get_category_by_id_tb(id)
        self.db.session.delete(category)
        self.db.session.commit()
        self.db.session.close()
        return True
