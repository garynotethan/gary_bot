import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent

COGS_DIR = BASE_DIR / "cogs"
