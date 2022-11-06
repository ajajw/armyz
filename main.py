#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 11849455, #get it from https://my.telegram.org/auth
    api_hash="0956032efc5694f60156fe65f9c19764", #get it from https://my.telegram.org/auth
    bot_token="5752243326:AAHvTPls-tnNkyrOTpOlguEX6PqZYnPHfXM", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
