import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "25114508"))
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6937121302:AAFOJenG6jTL69ZDUbOd10YFSqDZPVNvgUY")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "laisTagger_bot")
    BOT_NAME = os.environ.get("BOT_NAME" , "Lais User Tagger")
    BOT_ID = int(os.environ.get("BOT_ID" , "6937121302"))
    SUDO_USERS = os.environ.get("SUDO_USERS" , "6308601705").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT" , "laisbots")
    OWNER_ID = int(os.environ.get("OWNER_ID" , "6308601705"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" , "lusttqw")
