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

# تشغيل المحرك للنسخة المستقرة v2
call_py = PyTgCalls(app)

print("✅ Cristal Music Engine Started!")
