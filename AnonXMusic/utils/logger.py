from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f""" ━━━━━━━━━━━━━━━━━━━━━━━     
**{MUSIC_BOT_NAME} 𝐏𝐥𝐚𝐲 𝐋𝐨𝐠𝐠𝐞𝐫**
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐂𝐡𝐚𝐭 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛      
┣★**𝐂𝐡𝐚𝐭:** {message.chat.title} [`{message.chat.id}`]
┣★**𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤:** {chatusername}
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐔𝐬𝐞𝐫:** {message.from_user.mention}

┣★**𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞:** @{message.from_user.username}
┣★**𝐈𝐝:** `{message.from_user.id}`
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐏𝐥𝐚𝐲 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐒𝐞𝐚𝐫𝐜𝐡 𝐒𝐨𝐧𝐠:** {message.text}

┣★**𝐒𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞:** {streamtype}
━━━━━━━━━━━━━━━━━━━━━━━"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    LOGGER_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
