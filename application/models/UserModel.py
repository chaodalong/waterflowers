# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from application.core.msqldb import Base


class UserModel(Base):
    """
    用户模型类
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    password = Column(String(32), nullable=False)

    def __init__(self, id=None, name=None, password=None):
        self.id = id
        self.name = name
        self.password = password