from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite engine URL format:
sqlite_db_url = 'sqlite:///mydbsqlite.db'
engine = create_engine(sqlite_db_url, echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()
# class Person(Base):
#     __tablename__ = 'people'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)

# Postgres engine URL format:
# postgress_db_url = postgresql+psycopg2://<username>:<password>@<host>:<port>/<database_name>

# MySQL engine URL format:
# mysql_db_url = mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>

# Create Postgres engine that connects to a remote Postgres database.   
# engine = create_engine(postgress_db_url, echo=True)
# Create Postgres engine that stores data in the local directory's
# mydatabase.db file.
# engine = create_engine('sqlite:///mydatabase.db', echo=True)
#
# Base = declarative_base()
# Session = sessionmaker(bind=engine)

# class Person(Base):
#     __tablename__ = 'people'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)
       