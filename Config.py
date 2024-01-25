import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "25114508"))
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6699387584:AAELyGCQvFr5Jw5tOczwYPHgrbvyUco_9io")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "SiriusTagger_bot")
    BOT_NAME = os.environ.get("BOT_NAME" , "Sirius Tagger")
    BOT_ID = int(os.environ.get("BOT_ID" , "6699387584"))
    SUDO_USERS = os.environ.get("SUDO_USERS" , "6481578614").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT" , "sohbetsirius")
    OWNER_ID = int(os.environ.get("OWNER_ID" , "6481578614"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" , "deniziinkizi")
