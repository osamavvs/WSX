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

# فرض استخدام المحرك المتوافق مع أوامر Start/Stop
def get_call_instance(app_instance):
    # نحاول جلب PyTgCalls أولاً لأنه هو الذي يحتوي على attribute 'start'
    if hasattr(pytgcalls, "PyTgCalls"):
        print("✅ تم اختيار المحرك القياسي: PyTgCalls")
        return pytgcalls.PyTgCalls(app_instance)
    elif hasattr(pytgcalls, "Client"):
        print("✅ تم اختيار المحرك الحديث: Client")
        return pytgcalls.Client(app_instance)
    else:
        # إذا لم يجد شيئاً، نقوم باستيراده قسراً من المسار الرئيسي
        from pytgcalls import PyTgCalls as FinalTry
        return FinalTry(app_instance)

call_py = get_call_instance(app)
