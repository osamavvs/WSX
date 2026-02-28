import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, STRING_SESSION

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins={"root": "plugins"}
)

call_py = PyTgCalls(app)

async def start():
    await app.start()
    await call_py.start()
    print("✅ تم تشغيل البوت بنجاح!")
    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())
