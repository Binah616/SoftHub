import sqlalchemy
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    association_table = sqlalchemy.Table(
        'association',
        SqlAlchemyBase.metadata,
        sqlalchemy.Column('user', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('users.id')),
        sqlalchemy.Column('news', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('news.id'))
    )