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

# طباعة محتويات المكتبة في اللوج لنعرف الاسم المخفي
print(f"DEBUG: Pytgcalls members are: {dir(pytgcalls)}")

def get_call_instance():
    # في نسخة v3 الحديثة، المحرك غالباً ما يكون Scaffolder أو Client
    # سنحاول جلب أي كلاس متاح
    if hasattr(pytgcalls, "Client"):
        print("✅ Using pytgcalls.Client")
        return pytgcalls.Client(app)
    
    # محاولة جلب المحرك من مسار فرعي (للنسخ الحديثة جداً)
    try:
        from pytgcalls import PyTgCalls
        print("✅ Using standard PyTgCalls")
        return PyTgCalls(app)
    except ImportError:
        # إذا فشل كل شيء، نبحث عن أول كلاس يبدأ بحرف كبير
        for name in dir(pytgcalls):
            if name[0].isupper() and name not in ["GroupCallFactory", "Stream"]:
                target = getattr(pytgcalls, name)
                print(f"✅ Auto-detected Engine: {name}")
                return target(app)
    
    raise AttributeError("Could not find a valid PyTgCalls class.")

call_py = get_call_instance()
