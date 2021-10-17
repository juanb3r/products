from controllers.database_setup import User
from app.app import db


class UserDB():

    def __init__(self) -> None:
        self.db = db

    def show_users_tb(self):
        try:
            users = self.db.session.query(User).all()
            return users
        except Exception:
            return {"data": "error"}

    def get_user_by_tb(self, username, password):
        user = self.db.session.query(User).filter_by(
            username=username,
            password=password).one()
        return user

    def new_user_tb(self, name):
        new_user = User(name=name)
        self.db.session.add(new_user)
        self.db.session.commit()
        self.db.session.close()
        return True

    def edit_user_tb(self, user):
        self.db.session.add(user)
        self.db.session.commit()
        self.db.session.close()
        return True

    def delete_user_tb(self, id):
        user = self.db.get_user_by_id_tb(id)
        self.db.session.delete(user)
        self.db.session.commit()
        self.db.session.close()
        return True
