from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# In an engine, we connect to db (SQLite, Postgresql(my turn), Mysql and so on)
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres", echo=True)

Base = declarative_base()  # Declarative way


class Book(Base):
    __tablename__ = 'Books'  # A simple name of db, which will show in your database program.

    id_book = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("Authors.id_author"))
    genre = Column(String(250))
    price = Column(Integer, nullable=False)
    Author = relationship("Author")


class Author(Base):
    __tablename__ = 'Authors'

    id_author = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    book = relationship("Book")  # Relations will be One to Many


Base.metadata.create_all(engine)  # Finally, we create databases...
