from pyrogram import Client
import pytgcalls
import config
import time

# تهيئة تطبيق التليجرام مع ميزة 'إزاحة الوقت'
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=240,
    in_memory=True  # ضروري جداً عشان ما يستخدم جلسات قديمة
)

# محاولة الاستدعاء حسب النسخة الموجودة في هيروكو
try:
    from pytgcalls import Client as PyTgCalls
    call_py = PyTgCalls(app)
except ImportError:
    from pytgcalls import PyTgCalls
    call_py = PyTgCalls(app)

print("✅ Cristal Engine: Time Synchronizing...")
