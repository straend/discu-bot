from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    messages = relationship("Message")
    discussions = relationship("Discussion")
    
    def __repr__(self):
        return "<Channel({})>".format(self.name)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    nick = Column(String, index=True)
    color = Column(String)
    messages = relationship("Message")
    discussions = relationship("Discussion")
    
    def __repr__(self):
        return "<User({})>".format(self.nick)

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=False)
    when = Column(DateTime, index=True)
    author_id = Column(ForeignKey('users.id'))
    channel_id = Column(ForeignKey('channels.id'))
    
    channel = relationship("Channel")
    author = relationship("User")

    def __repr__(self):
        return "<Message({})>".format(self.id)

class Discussion(Base):
    __tablename__ = 'discussions'
    
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    starter_id = Column(ForeignKey('users.id'))
    channel_id = Column(ForeignKey('channels.id'))
    
    time_start = Column(DateTime, index=True)
    time_end = Column(DateTime, index=True)

    
    starter = relationship("User", back_populates="discussions")
    channel = relationship("Channel", back_populates="discussions")

    @property
    def messages(self):
        return object_session(self).query(Message).filter(Message.channel_id==self.channel_id).filter(Message.when.between(self.time_start, self.time_end)).all()

    def __repr__(self):
        return "<Discussion({})>".format(self.topic)
