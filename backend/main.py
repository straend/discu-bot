from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate

from models import Channel, User, Message, Discussion
from schema import Discussion as DiscussionOut, ChannelDiscussions as ChannelOut
import os
from config import DB_URL
from sqlalchemy.pool import StaticPool
app = FastAPI()
if DB_URL.startswith('sqlite://'):
    app.add_middleware(DBSessionMiddleware, 
        db_url=DB_URL,
        engine_args={'connect_args': {'check_same_thread':False},'poolclass': StaticPool}
    )
else:
    app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/channels")
def get_channels():
    channels = db.session.query(Channel).all()
    return channels

@app.get("/channels/{channel_name}", response_model=ChannelOut)
def get_channel_discussions(channel_name: str) :
    channel = db.session.query(Channel).filter(Channel.name==channel_name).all()[0]
    return channel

@app.get("/discussions/{discussion_id}", response_model=DiscussionOut)
def get_channel_discussion_messages(discussion_id: int) :
    discussion = db.session.query(Discussion).filter(Discussion.id==discussion_id).first()
    return discussion
