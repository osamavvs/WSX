from pyrogram import Client
import pytgcalls
import config

# تهيئة تطبيق التليجرام
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# محاولة الاستدعاء بأكثر من طريقة لتجنب ImportError
try:
    from pytgcalls import Client as PyTgCallsClient
    call_py = PyTgCallsClient(app)
except ImportError:
    try:
        from pytgcalls import PyTgCalls
        call_py = PyTgCalls(app)
    except ImportError:
        # إذا فشل كل شيء، نستخدم الاستدعاء المباشر من المجلد
        from pytgcalls.pytgcalls import PyTgCalls as PyCall
        call_py = PyCall(app)

print("✅ Cristal Music Engine: Started Successfully!")
