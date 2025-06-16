from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your details
BOT_USERNAME = "Testvmrobot"  # without @
OWNER_USERNAME = "Uzumaki_X_Naruto_6"
SUPPORT_CHAT = "Animeheaven_community"
UPDATES_CHANNEL = "Bey_war_updates"

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/fdb36c8df0c11d88e3b8d.jpg",  # Change to your image
        caption=f"""👋 **Hey {message.from_user.mention}**\n\n🙈 Welcome to *Epic Game Bot*! Here begins your fun journey.

Use the buttons below to explore or add me to your group!""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add me to your group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("🛠 Support", url=f"https://t.me/{SUPPORT_CHAT}"),
                InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATES_CHANNEL}")
            ],
            [InlineKeyboardButton("🔘 Owner", url=f"https://t.me/{OWNER_USERNAME}")]
        ])
    )