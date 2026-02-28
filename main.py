import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, STRING_SESSION

app = Client(
    "MusicUserbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins=dict(root="plugins")
)

call_py = PyTgCalls(app)

async def start_bot():
    await app.start()
    await call_py.start()
    print("✅ تم التشغيل بنجاح!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
