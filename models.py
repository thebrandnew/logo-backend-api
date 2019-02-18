# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    SmallInteger,
    Sequence,
    DateTime,
    create_engine,
)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    tel = Column(String(20))
    email = Column(String(128))
    name = Column(String(20))
    company = Column(String(30))
    position = Column(String(30))
    rem = Column(String(30))
    created_at = Column(DateTime, default=func.now())


class Order(Base):
    __tablename__ = 'orders'

    id = Column(String(20), primary_key=True)
    type = Column(SmallInteger)
    logo = Column(String(20))
    channel = Column(String(20))
    credential = Column(Text)
    status = Column(SmallInteger)
    paid_at = Column(DateTime)
    created_at = Column(DateTime)
