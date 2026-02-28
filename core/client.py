from pyrogram import Client
from pytgcalls import PyTgCalls
import config

# تهيئة تطبيق التليجرام
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# تشغيل المحرك للنسخة 2.1.0 (الاسم الصحيح هو PyTgCalls وليس Client)
call_py = PyTgCalls(app)

print("✅ Cristal Music Engine Connected Successfully!")
