from pyrogram import Client
import pytgcalls
from config import API_ID, API_HASH, BOT_TOKEN

# تهيئة تطبيق التليجرام
app = Client("CristalBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# كود ذكي لاكتشاف المحرك الصحيح للنسخة المثبتة
if hasattr(pytgcalls, "Client"):
    # للنسخة v3
    call_py = pytgcalls.Client(app)
else:
    # للنسخة v2
    call_py = pytgcalls.PyTgCalls(app)
