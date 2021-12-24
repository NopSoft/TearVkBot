import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables.

bot_settings = {
    "TOKEN": os.environ.get("BOT_TOKEN"),
    "GROUP_ID": os.environ.get("BOT_GROUP_ID"),
}
