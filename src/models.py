import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer, ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
  
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password= Column(String(250))
    User = relationship(Followers)



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String(250))
    created = Column(String(250))
    updated = Column(String(250))
    followers = relationship(User)

class Tipos(enum.Enum):
    photo = 'photo'
    pictures = 'pictures'
    video = 'video'

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    types= Column(Enum(Tipos))
    url= Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    content = Column(String(250))
    created= Column(String(250))
    updated= Column(String(250))
    comments = relationship(User)
    comments = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    likes = relationship(User)
    

    


  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
