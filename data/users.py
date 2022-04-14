import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import *


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Posts(SqlAlchemyBase):
    __tablename__ = 'Posts'

    id_post = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date_creation = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Coments(SqlAlchemyBase):
    __tablename__ = 'Coments'

    id_coment = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_post_comments = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)