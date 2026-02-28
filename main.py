import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, STRING_SESSION

# إعداد عميل التليجرام (اليوزربوت)
app = Client(
    "MusicUserbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins=dict(root="plugins") # هذا السطر يخبر البوت أن الأوامر موجودة في مجلد plugins
)

# إعداد مشغل المكالمات
call_py = PyTgCalls(app)

async def start_bot():
    print("--------------------------")
    print("جاري بدء تشغيل اليوزربوت...")
    await app.start()
    await call_py.start()
    print("تم تشغيل البوت بنجاح!")
    print("انتظر الآن أوامر التشغيل...")
    print("--------------------------")
    await idle() # يبقي البوت يعمل ولا يغلق البرنامج
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
  
