from sqlalchemy import Column, Integer, String
from application.database.mysqldb import Base

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    password = Column(String(32), nullable=False)

    def __init__(self, id=None, name=None, password=None):
        self.id = id
        self.name = name
        self.password = password