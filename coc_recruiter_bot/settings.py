import os

from dotenv import load_dotenv

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CLAN_TAG = os.getenv("CLAN_TAG")
SEND_MESSAGE = os.getenv("SEND_MESSAGE", "False")

if SEND_MESSAGE == "True":
    SEND_MESSAGE = True
elif SEND_MESSAGE == "False":
    SEND_MESSAGE = False
else:
    raise Exception("SEND_MESSAGE env var does not equal 'False' or 'True'")
