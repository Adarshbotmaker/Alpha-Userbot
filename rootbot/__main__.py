from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, PYTHONversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
l2= Config.SUDO_COMMAND_HAND_LER
Alpha_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/566ab704cb91e6669073e.jpg"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"Alpha_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()
print("Loading Modules / Plugins")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

        extra_repo = "https://github.com/ADARSHBOTMAKER/Alpha-userbot"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "Alphauserbot/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[Alpha-userbot 1.0.8] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[Alpha-userbot 1.0.8] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""
bot.loop.run_until_complete(module())

print(f"""『🔱ALPHA-USERBOT🔱』➙𖤍࿐ IS ON!!! PYTHON VERSION :- {PYTHONversion}
TYPE :- " .gpromote @Hackmer_xd " OR .alive OR .ping CHECK IF I'M ON!
╔════❰PYTHONBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - Adarsh
║┣⪼{Alpha_PIC}
║┣⪼ CREATOR -@Hackmer_xd
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱ALPHA USERBOT 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def python_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                Alpha_PIC,
                caption=f"#START \n\nDeployed ALPHA-USERBOT Successfully\n\n**AlphaBOT- {PYTHONversion}**\n\nType `{l1}python` or `{l1}pyalive` to check! \n\nJoin [PythonBot Channel](t.me/Python_Updata) for Updates & [PythonBot Chat](t.me/Python_Userbot_Support) for any query regarding PythonBot",
            )
    except Exception as e:
        print(str(e))

# Join ALPHABOT Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Alpha_bot_Updates"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Alpha_bot_Support"))
    except BaseException:
         pass


bot.loop.create_task(Alpha_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
