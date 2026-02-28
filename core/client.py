from pyrogram import Client
from pytgcalls import Client as PyTgCalls
import config

# تهيئة تطبيق التليجرام (حساب البوت)
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# في إصدار v3، المحرك اسمه Client حصراً
# سنقوم بتسميته call_py ليتوافق مع باقي ملفات السورس عندك
call_py = PyTgCalls(app)

print("✅ Cristal Music Engine (v3) Started!")
