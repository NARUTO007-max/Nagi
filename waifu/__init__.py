# waifu/__init__.py

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging

bot = Client(
    "BeybladeBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="waifu/Modules")
)

logging.basicConfig(
  format="[KuroAI-Beta] %(name)s - %(levelname)s - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)