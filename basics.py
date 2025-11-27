from sqlalchemy import Column, text, Integer, String, create_engine, MetaData, Table, Column 

engine = create_engine('sqlite:///mydatabase.db', echo=True)
meta = MetaData()
people = Table(
    'people', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String,nullable=False),
    Column('age', Integer,nullable=False)
)
meta.create_all(engine)
# conn = engine.connect()