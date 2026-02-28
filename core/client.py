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

# كود ذكي لاكتشاف المحرك مهما كان اسمه
print(f"DEBUG: Pytgcalls content -> {dir(pytgcalls)}")

try:
    # المحاولة 1: الاسم القياسي للنسخ الحديثة
    from pytgcalls import PyTgCalls
    call_py = PyTgCalls(app)
    print("✅ تم التشغيل باستخدام PyTgCalls")
except ImportError:
    try:
        # المحاولة 2: الاسم القياسي للنسخ v3
        from pytgcalls import Client as PyCall
        call_py = PyCall(app)
        print("✅ تم التشغيل باستخدام Client")
    except ImportError:
        # المحاولة 3: في حال كانت المكتبة داخل مجلد Scaffolding
        from pytgcalls.main import PyTgCalls as PyCall
        call_py = PyCall(app)
        print("✅ تم التشغيل باستخدام main.PyTgCalls")
