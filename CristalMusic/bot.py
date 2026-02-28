import asyncio
from pyrogram import filters, idle
from core.client import app, call_py
from config import OWNER_ID

@app.on_message(filters.command("start"))
async def start(c, m):
    await m.reply_text("✨ أهلاً بك في سورس كرستال بايثون\nالبوت يعمل الآن بنظام المجلدات القديم ✅")

async def main():
    await app.start()
    await call_py.start()
    print("💎 Cristal Music is Online!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
