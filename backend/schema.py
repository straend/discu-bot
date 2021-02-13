from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nick: str
    color: str
    
    class Config:
        orm_mode = True

class Message(BaseModel):
    id: int
    text: str
    when: datetime
    author: User
    class Config:
        orm_mode = True

class Channel(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True

class Discussion(BaseModel):
    id: int
    topic: str
    time_start: datetime
    time_end: datetime
    channel: Channel
    starter: User
    messages: List[Message] = []
    
    class Config:
        orm_mode = True

class DiscussionShort(BaseModel):
    id: int
    topic: str
    time_start: datetime
    channel: Channel
    starter: User
    
    class Config:
        orm_mode = True

class ChannelDiscussions(BaseModel):
    id: int
    name: str
    discussions: List[DiscussionShort]=[]
    class Config:
        orm_mode = True



