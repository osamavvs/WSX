import os
from os import getenv

# جلب البيانات من هيروكو
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
STRING_SESSION = getenv("STRING_SESSION") # تأكد أن الاسم هنا يطابق ما في هيروكو
OWNER_ID = int(getenv("OWNER_ID"))
