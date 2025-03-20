import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))


# ----- V2 Features Configs -----
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://your-mongo-url")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "your-shortlink-token")
PREMIUM_USERS = os.environ.get("PREMIUM_USERS", "").split()
PAID_TIMER = int(os.environ.get("PAID_TIMER", 60))
FREE_TIMER = int(os.environ.get("FREE_TIMER", 300))
ADMINS = os.environ.get("ADMINS", "").split()
TELEGRAM_BOT_SESSION = os.environ.get("TELEGRAM_BOT_SESSION", "")
MAUTRIX_TOKEN = os.environ.get("MAUTRIX_TOKEN", "")
