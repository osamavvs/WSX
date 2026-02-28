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

# اكتشاف المحرك وتسميته تلقائياً لتجنب الانهيار
def get_call_py(app_instance):
    # قائمة بأسماء الكلاسات المحتملة في مكتبة pytgcalls لعام 2026
    possible_names = ["PyTgCalls", "Client", "GroupCallFactory"]
    
    for name in possible_names:
        if hasattr(pytgcalls, name):
            attr = getattr(pytgcalls, name)
            print(f"✅ تم اكتشاف المحرك بنجاح: {name}")
            return attr(app_instance)
    
    # محاولة أخيرة إذا كان الاستيراد يتطلب مساراً داخلياً
    try:
        from pytgcalls import PyTgCalls
        return PyTgCalls(app_instance)
    except ImportError:
        from pytgcalls import Client as PyCall
        return PyCall(app_instance)

# تشغيل المحرك المكتشف
call_py = get_call_py(app)
