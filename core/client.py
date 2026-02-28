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

# اكتشاف المحرك تلقائياً (عشان ما يوقف البوت لو تغيرت نسخة المكتبة)
def get_call_instance(app_instance):
    for name in ["PyTgCalls", "Client", "GroupCallFactory"]:
        if hasattr(pytgcalls, name):
            attr = getattr(pytgcalls, name)
            print(f"✅ تم اكتشاف المحرك: {name}")
            return attr(app_instance)
    from pytgcalls import PyTgCalls
    return PyTgCalls(app_instance)

call_py = get_call_instance(app)
