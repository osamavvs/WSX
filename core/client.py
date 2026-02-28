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

# اكتشاف المحرك تلقائياً لتجنب أخطاء Version 2 vs Version 3
def get_call_instance(app_instance):
    # قائمة الأسماء الممكنة للمحرك في 2026
    for name in ["PyTgCalls", "Client", "GroupCallFactory"]:
        if hasattr(pytgcalls, name):
            class_attr = getattr(pytgcalls, name)
            print(f"✅ تم اكتشاف المحرك بنجاح: {name}")
            return class_attr(app_instance)
    
    # محاولة استيراد مباشرة كحل أخير
    from pytgcalls import PyTgCalls
    return PyTgCalls(app_instance)

# تشغيل المحرك المكتشف
call_py = get_call_instance(app)
