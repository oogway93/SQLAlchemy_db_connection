from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Book, Author

# In an engine, we connect to db (SQLite, Postgresql(my turn), Mysql and so on)
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres", echo=True)

session = sessionmaker(bind=engine)  # here we create a session
s = session()

# first added data
author_one = Author(name="Ramalho")
s.add(author_one)
s.commit()

author_two = Author(name="Mark Lutz")
s.add(author_two)
s.commit()

author_three = Author(name="Lev Tolstoy")
s.add(author_three)
s.commit()

s.add_all([Book(title="Fluent Python", author_id=1, genre="IT technologies", price=100),
           Book(title="Learning Python", author_id=2, genre="IT technologies", price=35),
           Book(title="Learning Python: Part 2", author_id=2, genre="IT technologies", price=55),
           Book(title="Peace and War", author_id=3, genre="Classic Literature", price=1000)])
s.commit()

# SOME TESTS

print(s.query(Book).first().title)

for title, price in s.query(Book.title, Book.price).order_by(Book.title).limit(3):
    print(f'{title}. It costs {price}$')

print()

print([(row.Book.title, row.Author.name) for row in s.query(Book, Author).join(Author).all()])

print()
