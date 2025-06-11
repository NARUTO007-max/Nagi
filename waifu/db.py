#database.py
from motor.motor_asyncio import AcyncIOMotorClient
#MONGO_CLIENT
MONGO_URI = "mongodb+srv://sufyan532011:2011@bey-wars.oji9phy.mongodb.net/?retryWrites=true&w=majority&appName=Bey-Wars"
monogo_client = AsyncIOMotorClient(MONGO_URI)
DB = mongo_client["Waifu"]
#All Database
users = DB["USERS"]
BannedUser = DB["BANNED USERS"]
guilds = DB["GUILDS"]