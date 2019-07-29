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

# add_article(knowledge_link="https://en.wikipedia.org/wiki/HIV2" , topic="hiv" , title="human immunodeficiency viruses", rating=8)

def query_all_articles():
	all_articles=session.query(Knowledge).all()
	return all_articles

print(query_all_articles())


def query_article_by_topic(articaltopic):
	articles_topic=session.query(all_articles).filter_by(topic=articaltopic).first()
	return articles_topic
print(query_article_by_topic(hiv))


def delete_article_by_topic(deletetopic):
	session.query(Knowledge).filter_by(topic=deletetopic).delete()
	session.commit()
delete_article_by_topic(hiv)


def delete_all_articles():
	session.query(all_articles).delete()
	session.commit()
delete_all_articles()

def edit_article_rating(knowledge_link, rating):
	article=session.query(Knowledge).filter_by(knowledge_link).first()
	article.rating=rating
edit_article_rating()

