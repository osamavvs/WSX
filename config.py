import os
from os import getenv
from dotenv import load_dotenv

# إذا كنت تجرب الكود محلياً سيقرأ من ملف .env
if os.path.exists("local.env"):
    load_dotenv("local.env")

# جلب البيانات من هيروكو
API_ID = int(getenv("API_ID", "0")) # ضع ايديك هنا أو اتركه ليقرأه من هيروكو
API_HASH = getenv("API_HASH")
STRING_SESSION = getenv("STRING_SESSION")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split())) # يدعم أكثر من مطور
