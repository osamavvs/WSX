from pyrogram import Client
from pytgcalls import Client as PyTgCallsClient
import config

# تهيئة التطبيق
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# استخدام الاسم الجديد المتوافق مع إصدار 2026
call_py = PyTgCallsClient(app)
