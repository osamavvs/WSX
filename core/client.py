from pyrogram import Client
from pytgcalls import Client as PyTgCalls
import config
import asyncio

# تهيئة تطبيق التليجرام مع حل مشكلة تزامن الوقت والجلسة
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=180,  # ليتجنب حظر تليجرام المؤقت
    in_memory=True        # أهم خيار لحل خطأ [16] msg_id is too low
)

# تشغيل المحرك لنسخة 2026 (v3)
call_py = PyTgCalls(app)

print("✅ Cristal Music Engine (v3) is Synchronizing...")
