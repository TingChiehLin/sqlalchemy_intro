# Engine => to connect to database and execute SQL
from sqlalchemy import Column, Integer, String, create_engine
#sqlalchemy.orm  => to Create different model
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

## Create a new table in the database
class Book(Base):
    __tablename__ = 'books' 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)

# metadata.create_all => create all database and all of tables associated with 
Base.metadata.create_all(engine)




