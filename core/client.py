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

# محاولة جلب المحرك بأي طريقة ممكنة (Compatibility Mode)
try:
    # للنسخ v3 الحديثة
    from pytgcalls import Client as PyCall
    call_py = PyCall(app)
except ImportError:
    try:
        # للنسخ v2 المستقرة
        from pytgcalls import PyTgCalls
        call_py = PyTgCalls(app)
    except ImportError:
        # إذا كانت المكتبة مخفية في المسار الداخلي
        from pytgcalls.pytgcalls import PyTgCalls as PyCall
        call_py = PyCall(app)

print("✅ تم اكتشاف محرك المكالمات وتشغيله بنجاح!")
