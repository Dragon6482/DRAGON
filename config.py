from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("21119621")
APP_HASH = os.environ.get("a0f65f563064446e09a5f240c2d4d4d7")
BOT_USERNAME = os.environ.get("kwhosowhwhsiwbot")
session = os.environ.get("1BJWap1sBu5-WcnDEdimlGfmryhINcMX6ycVEXukZyRvqFLnXBPsvL0I6bIxdBJ58nK2uIA6UdNBWX4peyUJjQe_-fQGbky_DKMI811OF3zq--Xke0DPYUPsov6Frfv3AQmbqXpcZUqPNpLP5cqLkHnzKUWAUtw3plHcDKf3fZvSXXmZPVhlTlByp2U8itM0qkLQFFSZ8Xjv9N6IGvvycU2-xHv4V8oyIw5boVMHCM-G4uRkQ_qqZuOzxC1_4yW5bFZf__vvB8jltzB3JorVQL73nnzS_OE15wofCszIHrZBh4N-F7uggeAGWB40Wq6cpY04M1R93phJ6LJNAXpt59vHF9kX5Jlc=")
SESSION = os.environ.get("1BJWap1sBu5-WcnDEdimlGfmryhINcMX6ycVEXukZyRvqFLnXBPsvL0I6bIxdBJ58nK2uIA6UdNBWX4peyUJjQe_-fQGbky_DKMI811OF3zq--Xke0DPYUPsov6Frfv3AQmbqXpcZUqPNpLP5cqLkHnzKUWAUtw3plHcDKf3fZvSXXmZPVhlTlByp2U8itM0qkLQFFSZ8Xjv9N6IGvvycU2-xHv4V8oyIw5boVMHCM-G4uRkQ_qqZuOzxC1_4yW5bFZf__vvB8jltzB3JorVQL73nnzS_OE15wofCszIHrZBh4N-F7uggeAGWB40Wq6cpY04M1R93phJ6LJNAXpt59vHF9kX5Jlc=")
token = os.environ.get("TOKEN")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
