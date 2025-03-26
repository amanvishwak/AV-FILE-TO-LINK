import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Bot information
SESSION = environ.get('SESSION', 'Webavbot')
API_ID = int(environ.get('API_ID', '21956488'))
API_HASH = environ.get('API_HASH', '812529f879f06436925c7d62eb49f5d1')
BOT_TOKEN = environ.get('BOT_TOKEN', "7091587168:AAGpX2rHu-DVYmXUdlxM3vZRnaLBrx8k3-c")
BOT_USERNAME = environ.get("BOT_USERNAME", 'AMAN_TESTS_BOT') # without @ 

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002114619001')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002114619001')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5977931010').split()] # 3567788, 678899, 5889467
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'BOT_OWNER26') # without @ 

# pics information
PICS = environ.get('PICS', 'https://envs.sh/b6H.jpg')

# channel link information
CHANNEL = environ.get('CHANNEL', 'https://t.me/')
SUPPORT = environ.get('SUPPORT', 'http://t.me/')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ](https://telegram.me/AV_OWNER_BOT) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://aman727587:aman@cluster0.bk39x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")

# fsub  information
AUTH_PICS = environ.get('AUTH_PICS', 'https://envs.sh/AwV.jpg')              
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002114619001"))
FSUB = environ.get("FSUB", True)

# port information
PORT = int(getenv('PORT', '8080'))
NO_PORT = bool(getenv('NO_PORT', False))

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'avbotz'))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
else:
    ON_HEROKU = False
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}{}/".format(FQDN, "" if NO_PORT else ":" + str(PORT))
    
#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
