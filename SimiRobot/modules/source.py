from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from SimiRobot import OWNER_ID, dispatcher
from SimiRobot import pbot as client

Simi = "https://te.legra.ph/file/998e3c89f9d0674371c86.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Simi,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ♥️𝐌𝐲 𝐋𝐞𝐠𝐞𝐧𝐝 :** [𝐀𝐧𝐚𝐧𝐝](https://t.me/Brahman_Anand)
**» ♥️𝐥𝐨𝐯𝐞 𝐯𝐢𝐫𝐬𝐨𝐧  :** `{y()}`
**» ♥𝐛𝐨𝐨𝐤 𝐬𝐭𝐨𝐫𝐞  :** `{o}` 
**» ♥️𝐮𝐝𝐢 𝐛𝐚𝐛𝐚  :** `{s}` 
**» ♥️𝐛𝐨𝐫𝐢𝐧𝐠😁  :** `{z}`

**۝ SιMι ۝࿐ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•𝐁𝐫𝐚𝐡𝐦𝐚𝐧_𝐀𝐧𝐚𝐧𝐝", url="https://t.me/pandit_Andy",
                    ),
                    InlineKeyboardButton(
                        "• ʀᴇᴘᴏ •",
                        url="https://github.com/BadshahAk/SimiRobot",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✤ Rᴇᴩᴏ ✤"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
