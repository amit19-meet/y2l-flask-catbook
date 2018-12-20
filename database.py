from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name, vote=0)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat_by_id(id):
	c1= session.query(Cat).filter_by(id=id).one()
	return c1

def cat_vote(id):
	cat= get_cat_by_id(id)
	cat.vote+=1
	session.commit()



