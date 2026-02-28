from pyrogram import Client
from pytgcalls import Client as PyTgCallsClient
import config

# تهيئة تطبيق التليجرام
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# استخدام المحرك المتوافق مع نسخة v3 (3.0.0.dev24)
call_py = PyTgCallsClient(app)

print("✅ Cristal Music Engine v3 Online!")
