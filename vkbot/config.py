import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # take environment variables.

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "utils" / "media"

bot_settings = {
    "TOKEN": os.environ.get("BOT_TOKEN"),
    "GROUP_ID": os.environ.get("BOT_GROUP_ID"),
}
