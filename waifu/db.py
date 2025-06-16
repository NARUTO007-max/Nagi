#database.py
from motor.motor_asyncio import AcyncIOMotorClient
#MONGO_CLIENT
MONGO_URI = "mongodb+srv://sufyan532011:5042@auctionbot.5ms20.mongodb.net/?retryWrites=true&w=majority&appName=AuctionBot"
monogo_client = AsyncIOMotorClient(MONGO_URI)
DB = mongo_client["Waifu"]
#All Database
users = DB["USERS"]
BannedUser = DB["BANNED USERS"]
guilds = DB["GUILDS"]