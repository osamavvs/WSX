from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import InputStream, AudioPiped
import yt_dlp

app = Client("music_bot", api_id=12345, api_hash="your_api_hash", bot_token="your_bot_token")
call = PyTgCalls(app)

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.mp3',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "song.mp3"

@app.on_message(filters.text)
async def handler(client, message):
    text = message.text.strip()

    if text.startswith("شغل"):
        url = text.replace("شغل", "").strip()
        file = download_audio(url)
        await call.join_group_call(
            message.chat.id,
            InputStream(
                AudioPiped(file)
            )
        )
        await message.reply("🎶 تم تشغيل الموسيقى")

    elif text == "وقف":
        await call.leave_group_call(message.chat.id)
        await message.reply("⏹️ تم إيقاف الموسيقى")

app.start()
call.start()
idle()
