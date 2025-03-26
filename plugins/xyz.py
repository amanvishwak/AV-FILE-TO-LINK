import asyncio
import os
import time
from web.utils.file_properties import get_hash
from pyrogram import Client, filters, enums
from info import *
from utils import get_size
from Script import script
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# ✅ File Limit Control
ENABLE_LIMIT = False  # ⚡ True = Limit ON, False = Limit OFF

# 🕒 Dictionary for Rate Limit (User ID -> [File Count, Last Upload Time])
rate_limit = {}

# ⏳ TIMEOUT (Seconds) for Resetting Limit
RATE_LIMIT_TIMEOUT = 60  # 5 minutes
MAX_FILES = 2  # Maximum files per user

@Client.on_message((filters.private) & (filters.document | filters.video | filters.audio), group=4)
async def private_receive_handler(c: Client, m: Message):
    user_id = m.from_user.id
    current_time = time.time()

    if ENABLE_LIMIT:
        # अगर यूजर पहले से लिस्ट में है
        if user_id in rate_limit:
            file_count, last_time = rate_limit[user_id]

            # अगर यूजर ने 10 फाइल भेज दी और 5 मिनट पूरे नहीं हुए
            if file_count >= MAX_FILES and (current_time - last_time) < RATE_LIMIT_TIMEOUT:
                remaining_time = int(RATE_LIMIT_TIMEOUT - (current_time - last_time))
                await m.reply_text(f"🚫 **आप 10 फाइल पहले ही भेज चुके हैं!**\nकृपया **{remaining_time} सेकंड** बाद फिर से प्रयास करें।", quote=True)
                return  # लिंक जनरेट नहीं होगा

            # अगर 5 मिनट पूरे हो चुके हैं, तो लिमिट रीसेट करें
            elif file_count >= MAX_FILES:
                rate_limit[user_id] = [1, current_time]
            else:
                rate_limit[user_id][0] += 1  # फाइल काउंट बढ़ाएं
        else:
            rate_limit[user_id] = [1, current_time]

    # ⏳ अगर लिमिट OFF है या यूजर लिमिट के अंदर है, तो प्रोसेस जारी रखें
    file_id = m.document or m.video or m.audio
    file_name = os.path.splitext(file_id.file_name)[0].replace("_", " ")
    file_size = get_size(file_id.file_size)
    
    try:
        msg = await m.forward(chat_id=BIN_CHANNEL)
        
        stream = f"{URL}watch/{msg.id}?hash={get_hash(msg)}"
        download = f"{URL}{msg.id}?hash={get_hash(msg)}"
        file_link = f"https://t.me/{BOT_USERNAME}?start=file_{msg.id}"

        await msg.reply_text(
            text=f"Requested By: [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUser ID: {m.from_user.id}\nStream Link: {stream}",
            disable_web_page_preview=True, quote=True
        )
        await m.reply_text(
            text=script.CAPTION_TXT.format(file_name, file_size, stream, download),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• Stream •", url=stream),
                 InlineKeyboardButton("• Download •", url=download)],
                [InlineKeyboardButton('Get File', url=file_link)]
            ])
        )

    except FloodWait as e:
        print(f"Sleeping for {e.value}s")  # e.x की जगह e.value करें
        await asyncio.sleep(e.value)
        await c.send_message(
            chat_id=BIN_CHANNEL,
            text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {e.value}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{m.from_user.id}`",
            disable_web_page_preview=True
                                           )
