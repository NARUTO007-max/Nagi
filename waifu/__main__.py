#__main__.py
from pyrogram import Client, filters
from waifu import bot
from Modules import *

if __name__=="__main__":
    bot.run()
    with bot:
        await bot.send_message(chat_id=7576729648,
                               text="BOT IS STARTED")