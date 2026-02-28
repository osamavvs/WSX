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

# كود استخراج المحرك ديناميكياً (مهما كان اسمه)
def find_call_client():
    # يبحث عن أي كلاس داخل المكتبة يبدأ اسمه بـ PyTg أو Client
    for attr_name in dir(pytgcalls):
        if attr_name.lower() in ["pytgcalls", "client"]:
            target = getattr(pytgcalls, attr_name)
            if callable(target):
                print(f"✅ Found and using: {attr_name}")
                return target(app)
    # إذا فشل البحث الذكي، نستخدم الاستدعاء الخام
    return pytgcalls.PyTgCalls(app)

call_py = find_call_client()
