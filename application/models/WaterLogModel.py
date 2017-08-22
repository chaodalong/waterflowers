# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, TIMESTAMP, text
from application.core.msqldb import Base


class WaterLogModel(Base):
    """
    浇花日志类
    """
    __tablename__ = 'water_log'

    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP, nullable=False, index=True,
        server_default=text("CURRENT_TIMESTAMP")
    )

    def __init__(self, id=None, created_at=None):
        self.id = id
        self.created_at = created_at