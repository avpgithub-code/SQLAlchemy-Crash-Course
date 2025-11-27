from sqlalchemy import Column, text, Integer, String, create_engine 

engine = create_engine('sqlite:///mydatabase.db', echo=True)
conn = engine.connect()
conn.execute(text("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name str,age INTEGER);    """
))
conn.commit()

from sqlalchemy.orm import Session, declarative_base
session = Session(engine)
session.execute(text('INSERT INTO people (name, age) VALUES ("Mike", 30);'))
session.commit()