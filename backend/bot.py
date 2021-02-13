#from fastapi import FastAPI
#from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
#from fastapi_sqlalchemy import db

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_get_or_create import get_or_create

import re
import os
import discord
from models import Channel, User, Message, Discussion

from config import DB_URL, FRONT_BASE
from colorhash import ColorHash

if DB_URL.startswith('sqlite://'):
    engine = create_engine(
        DB_URL, 
        convert_unicode=True, 
        connect_args={'check_same_thread':False},
        poolclass=StaticPool
    )
else:
    engine = create_engine(
        DB_URL, 
        convert_unicode=True, 
    )
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Disco(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        channel_id = message.channel.id
        channel_name = message.channel.name
        author_id = message.author.id
        author_name = message.author.name
        text = message.content
        
        #with db as db_session:
        channel, _ = get_or_create(db_session, Channel, name = channel_name )
        author, created = get_or_create(db_session, User, nick = author_name )
        if created:
            author.color = ColorHash(author_name).hex
        if message.content.startswith('!save'):
            print("Discussion:", message.content)
            reg = re.compile(r"!save (?P<nick>.+) (?P<lines>\d+) (?P<topic>.+)")
            m = reg.match(message.content)
            if m:
                # Create a discussion
                starter, _ = get_or_create(db_session, User, nick = m.group('nick'))
                msg_count = int(m.group('lines'))
                # First message
                am = db_session.query(Message).filter(channel==channel).order_by(Message.when.desc()).limit(msg_count)
                start_time = am[am.count()-1].when
                disc = Discussion(starter=starter, channel=channel, topic=m.group('topic'), time_start=start_time, time_end=message.created_at)
                db_session.add(disc)
                db_session.commit()
                reply = "Discussion saved, {}/{}/{}".format(FRONT_BASE, channel_name, disc.id)
                await message.channel.send(reply)
        else:
            msg,_ = get_or_create(db_session, Message, author=author, when=message.created_at, channel=channel)
            for m in message.mentions:
                print(m)
            # Append attachments
            for a in message.attachments:
                if len(text)>0:
                    text += "\r\n"
                text += a.url
            msg.text = text
            db_session.commit()


client = Disco()
discord_token = os.environ.get('DISCORD_TOKEN', None)
discord_is_bot = os.environ.get('DISCORD_IS_BOT', 'True')

client.run(discord_token, bot = discord_is_bot=='True')
