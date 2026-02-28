import sys
import pytgcalls
from pyrogram import Client
import config

# تهيئة تطبيق التليجرام
app = Client(
    "CristalBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# محاولة الاستدعاء المباشر (Direct Access)
try:
    # الطريقة المتوافقة مع نسخ 2026 المستقرة
    call_py = pytgcalls.PyTgCalls(app)
    print("✅ تم التشغيل: PyTgCalls")
except AttributeError:
    try:
        # الطريقة المتوافقة مع نسخ v3
        call_py = pytgcalls.Client(app)
        print("✅ تم التشغيل: Client")
    except AttributeError:
        # إذا كانت المكتبة مخفية (Hidden class)
        from pytgcalls.methods import PyTgCalls as MethodCall
        call_py = MethodCall(app)
        print("✅ تم التشغيل: Methods.PyTgCalls")

print("🚀 المحرك جاهز للعمل!")
