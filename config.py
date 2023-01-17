import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22745599")

API_HASH = os.environ.get("API_HASH", "3f0b55d67e0357d426afc5dc3c27145c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5986168289:AAGfK-48y5UA0JSCOESMMctC5PXIc2vO19w") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001861252300") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://hmoelwaseaf:ghZvWN9xDWkbjizg@cluster0.gqmhx8j.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5440235697').split()]

PORT = os.environ.get("PORT", "8080")
