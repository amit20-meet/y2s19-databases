from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__= 'knowledge'
	knowledge_link=Column(String, primary_key=True)
	topic=Column(String)
	title=Column(String)
	rating=Column(Integer)

	def __repr__(self):
		return("Topic : {}\n"
			"Title : {}\n"
			"Rating : {}\n"
			"Knowledge Link AMIT : {}").format(self.topic,self.title,self.rating,self.knowledge_link)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	