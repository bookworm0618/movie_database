from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key = True)
    title = Column('Title', String)
    director = Column('Director', String)
    release_date = Column('Release', Date)
    rating = Column('Rating', Integer)

    def __repr__(self):
        return f'Title:{self.title} Director: {self.director} Release: {self.release_date} Rating: {self.rating}'
