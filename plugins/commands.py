from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("فحص", "") & filters.me)
async def alive_command(client, message):
    await message.edit_content("أهلاً بك يا مطوري! البوت شغال الآن بنجاح. ✅")

@Client.on_message(filters.command("بنج", "") & filters.me)
async def ping_command(client, message):
    await message.edit_content("بونج! 🏓")
