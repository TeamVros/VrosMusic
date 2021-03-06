import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Vros Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/904a877f2eae2da8d28be.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/ee0deae23239523701ac5.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/27f66ce2a6a1c26697495.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/8f27a47a1807f0a30c2ac.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "vrosmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vrosassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VrosMusicSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TeamVros")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/TeamVros/VrosMusic")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
