import os
import time
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import InputStream, AudioPiped
import yt_dlp

# ضبط المنطقة الزمنية لتفادي مشكلة BadMsgNotification
os.environ["TZ"] = "UTC"
time.tzset()

# تهيئة تطبيق التليجرام
app = Client(
    "CristalBot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

# تهيئة محرك المكالمات الصوتية
call_py = PyTgCalls(app)

# دالة لتحميل الصوت من يوتيوب
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.mp3',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "song.mp3"

# أوامر عربية للتحكم
@app.on_message(filters.text)
async def handler(client, message):
    text = message.text.strip()

    if text.startswith("شغل"):
        url = text.replace("شغل", "").strip()
        file = download_audio(url)
        await call_py.join_group_call(
            message.chat.id,
            InputStream(
                AudioPiped(file)
            )
        )
        await message.reply("🎶 تم تشغيل الموسيقى")

    elif text == "وقف":
        await call_py.leave_group_call(message.chat.id)
        await message.reply("⏹️ تم إيقاف الموسيقى")

app.start()
call_py.start()
