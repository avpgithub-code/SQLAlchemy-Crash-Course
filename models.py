from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker, mapped_column, Mapped
from typing import Optional
from typing_extensions import Annotated

# SQLite engine URL format:
sqlite_db_url = 'sqlite:///mydbsqlite.db'
engine = create_engine(sqlite_db_url, echo=True)

str_20 = Annotated[Optional[str], mapped_column(String(20))]
str_30 = Annotated[Optional[str], mapped_column(String(30))]

# Define base class for declarative models
class Base(DeclarativeBase):
    type_annotation_map = {
        int: Integer,
        str: String,
    }

# Define User model
class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str_20]
    last_name: Mapped[str_30]
    age: Mapped[int] = mapped_column()

# Create all tables in the database
Base.metadata.create_all(engine)

# class User(Base):
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[Optional[str]] = mapped_column()
#     age: Mapped[int] = mapped_column()



# from sqlalchemy import Column, Integer, String, create_engine
# Base = declarative_base()
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)

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
       