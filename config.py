import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22745599")

API_HASH = os.environ.get("API_HASH", "3f0b55d67e0357d426afc5dc3c27145c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5855550294:AAGUumch418LHmU0luyjVH1a3rI_MlmxfWo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001860403687") 

DB_NAME = os.environ.get("DB_NAME","MahmoudElwaseaf")     

DB_URL = os.environ.get("DB_URL","postgres://mahmoudelwaseaf_user:YLKFV4uboH6RT0NikB00v6mLWk0mBXga@dpg-cf2uohp4reb5o46uujvg-a.frankfurt-postgres.render.com/mahmoudelwaseaf")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5440235697').split()]

PORT = os.environ.get("PORT", "8080")
