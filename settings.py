import os

from dotenv import load_dotenv

load_dotenv()
GUILD_ID = int(os.getenv('GUILD_ID'))
TOKEN = os.getenv('TOKEN')
VOICE_CATEGORY_ID = int(os.getenv('VOICE_CATEGORY_ID'))
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
ALLOW_ANNOUNCEMENT_ROLE = int(os.getenv('ALLOW_ANNOUNCEMENT_ROLE'))


PERMISSION_ROLE_ID = 875489052663611402
DISCORD_ROLEBOT_SETTINGS_CHANNEL = 873269921264594984
