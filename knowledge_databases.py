from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(knowledge_link, topic, title, rating):
	article=Knowledge(knowledge_link=knowledge_link , topic=topic , title=title, rating=rating)
	session.add(article)
	session.commit()

add_article(knowledge_link="https://en.wikipedia.org/wiki/HIV" , topic="hiv" , title="human immunodeficiency viruses", rating=8)
print(add_article())

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
