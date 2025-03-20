# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client

# Imported from V2 Bot
from TechVJ.modules import login, ytdl, shrink, plans, stats
from TechVJ.modules import func, get_func

from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# --- V2 Bot Commands Integration ---

@app.on_message(filters.command("login"))
async def login_handler(client, message):
    await login.login_user(client, message)

@app.on_message(filters.command(["ytdl", "yt", "insta", "tw", "fb"]))
async def ytdl_handler(client, message):
    await ytdl.ytdl_downloader(client, message)

@app.on_message(filters.command("short"))
async def short_handler(client, message):
    await shrink.short_link(client, message)

@app.on_message(filters.command("premium"))
async def premium_handler(client, message):
    await plans.check_plan(client, message)

@app.on_message(filters.command("stats"))
async def stats_handler(client, message):
    await stats.user_stats(client, message)
