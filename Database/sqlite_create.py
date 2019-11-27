from sqlalchemy import Column, Integer, String, Boolean, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(32))
    in_stock = Column('in_stock', Boolean)
    quantity = Column('quantity', Integer)
    price = Column('price', Numeric)


engine = create_engine('sqlite:///Sqlite-Data/example.db')

Base.metadata.create_all(engine)
