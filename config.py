import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "20860620")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "25d2343b36fc5aea3604c6c50a8e2b59")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7334452310:AAFtdl9zLec-rW8YDP2hPiMtWxd9EEqA7Fs")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "20860620")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "25d2343b36fc5aea3604c6c50a8e2b59")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQE-TswAufGr8UJe6rl2pRoU_7VsTwFwuE4X04XcXsi8K-F-w3tJ4aaukTQPf5pD2vfQcIfXPbjVWW8OOyCpVHgA_w9E2QH46OROu2DBVJ-50bt5GAYIvcdTtnBdL6griXiqXHduKWKY-DkZVWZUlijKOyg6ZTQgxyCse96DJ4RXHCBSzp_5KOHH5S1PHnn8IjAnVhBgB32VDbXANV3jErrWqA7r7mIzRNKX4B3jVud511vDIuC-lJJfGVlO7vjMm0K3r26xakDBg34JmjRWLvtC881gnvQJLndRjyNS1lVmiYT8FU8VcMcZr0_RAO74TK7NOKpa2mWIkDAd55pDCJKlacHrFwAAAAFxh5BjAA")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster00")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/qdw.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '6199677027').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "renamexxxlog") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001956549798"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8030"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
"""

    ABOUT_TXT = """<b>╭───────────⍟
• ᴍy ɴᴀᴍᴇ : {}
• ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/sewxiy>ᴍɪᴋᴇʏ</a>
• ɴᴇᴛᴡᴏʀᴋ : <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx</a> 
• ᴍᴏᴠɪᴇs : <a href=https://t.me/movieflix_original>ᴍᴏᴠɪᴇғʟɪx</a>
• sᴇʀɪᴇs : <a href=https://t.me/seriesflix_original>sᴇʀɪᴇsғʟɪx</a>
• ᴀɴɪᴍᴇ: <a href=https://t.me/anime_cruise_netflix>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
• ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/weebzonex>ᴡᴇᴇʙᴢᴏɴᴇ</a>
• ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://codeflix_bots>ᴠᴘs</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Anime_Bloodline" -metadata author="@Anime_Bloodline" -metadata:s:s title="Subtitled By :- @Anime_Bloodline" -metadata:s:a title="By :- @Anime_Bloodline" -metadata:s:v title="By:- @Anime_Bloodline" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Codeflix_bots
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱➜
➜ 🗃️ sɪᴢᴇ: {1} | {2}
➜ ⏳️ ᴅᴏɴᴇ : {0}%
➜ 🚀 sᴘᴇᴇᴅ: {3}/s
➜ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➜ </b>"""
