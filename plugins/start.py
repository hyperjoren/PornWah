# (C) ᯏ 𝚮𝚼𝚸𝚬꧊᱂ ! श्रेष्ठDont Remove Credit

import asyncio, datetime, pytz
from config import *
from .database import db
from .fsub import checkSub
from .script import DS_TEXT, DST_TEXT, LOG_TEXT, SUBS_TXT, VERIFIED_LOG_TEXT, VERIFICATION_TEXT, ABOUT_TXT, DSMYPLANTXT
from utils import verify_user, check_token, check_verification, get_token, check_and_increment
from pyrogram.errors import *
from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)

keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Desi Video"),
            KeyboardButton("Videsi video")
        ],
        [
            KeyboardButton("My Plan"),
            KeyboardButton("Get Premium")
        ],
        [
            KeyboardButton("Bot & Repo Details")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False  # Set to True if you want the keyboard to disappear after a button press
)

@Client.on_message(filters.private & filters.command("users") & filters.user(DS_ADMINS))
async def sts(client, message):
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**Total Users in DB:** `{total_users}`",
        quote=True
    )

# (C) ᯏ 𝚮𝚼𝚸𝚬꧊᱂ ! श्रेष्ठ Remove Credit

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        is_joined = await checkSub(client, message)
        if not is_joined: return
            
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
            await client.send_message(DS_LOG_CHANNEL, LOG_TEXT.format(message.from_user.id, message.from_user.mention))
        
            
        payload = message.command[1] if len(message.command) > 1 else None
        if payload == "disclaimer":
            a = await message.reply_text(DS_TEXT, parse_mode=enums.ParseMode.HTML)
            await asyncio.sleep(180)
            await a.delete()

        if payload == "terms":
            b = await message.reply_text(DST_TEXT, parse_mode=enums.ParseMode.HTML)
            await asyncio.sleep(180)
            await b.delete()

        if payload and payload.startswith("verify-"):
            try:
                _, userid, token = payload.split("-", 2)
            except ValueError:
                return await message.reply_text("<b>⚠️ Invalid verification link.</b>")

            if str(message.from_user.id) != str(userid):
                return await message.reply_text("<b>⚠️Invalid link or Expired link !</b>", protect_content=True)

            is_valid = await check_token(client, userid, token)
            if is_valid:
                t = await message.reply_text(
                        f"<b>✅ Hey {message.from_user.mention}, you are successfully verified! \n\nYou now have access until midnight today ✓</b>",
                        protect_content=True
                    )
                await client.send_message(DS_LOG_CHANNEL, VERIFIED_LOG_TEXT.format(message.from_user.mention, message.chat.id, str(datetime.datetime.now(pytz.timezone("Asia/Kolkata")).date())))
                await verify_user(client, userid, token) 
                await asyncio.sleep(70)
                await t.delete()
            else:
                return await message.reply_text(
                    "<b>⚠️ This link is either expired or already used.\nClick Verify again to get a new one.</b>",
                    protect_content=True
                )

    
        await message.reply_photo(
            photo=DS_PIC,
            caption=f"""<b><blockquote>𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖢𝗈𝗇𝗍𝖺𝗂𝗇𝗌 18+ 𝖢𝗈𝗇𝗍𝖾𝗇𝗍 𝖲𝗈 𝖪𝗂𝗇𝖽𝗅𝗒 𝖠𝖼𝖼𝖾𝗌𝗌 𝖨𝗍 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖮𝗐𝗇 𝖱𝗂𝗌𝗄. 𝖳𝗁𝖾 𝖬𝖺𝗍𝖾𝗋𝗂𝖺𝗅 𝖬𝖺𝗒 𝖨𝗇𝖼𝗅𝗎𝖽𝖾 𝖤𝗑𝗉𝗅𝗂𝖼𝗂𝗍 𝖮𝗋 𝖦𝗋𝖺𝗉𝗁𝗂𝖼 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖳𝗁𝖺𝗍 𝖨𝗌 𝖴𝗇𝗌𝗎𝗂𝗍𝖺𝖻𝗅𝖾 𝖥𝗈𝗋 𝖬𝗂𝗇𝗈𝗋𝗌. 𝖲𝗈 𝖢𝗁𝗂𝗅𝖽𝗋𝖾𝗇𝗌 𝖯𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗒 𝖠𝗐𝖺𝗒.</blockquote>\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖢𝗁𝖾𝖼𝗄 𝖮𝗎𝗋 <a href="https://t.me/{DS_BOT_USERNAME}?start=disclaimer">𝖣𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋</a> 𝖠𝗇𝖽 <a href="https://t.me/{DS_BOT_USERNAME}?start=terms">𝖳𝖾𝗋𝗆𝗌</a> 𝖡𝖾𝖿𝗈𝗋𝖾 𝖴𝗌𝗂𝗇𝗀 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍.</b>""",
            reply_markup=keyboard,
            has_spoiler=True,
            parse_mode=enums.ParseMode.HTML
        )
        await message.reply_text("𝖲𝖾𝗅𝖾𝖼𝗍 𝖸𝗈𝗎𝗋 𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖥𝗂𝗅𝖾 𝖢𝖺𝗍𝖾𝗀𝗈𝗋𝗒 👇🏻")

# (C) ᯏ 𝚮𝚼𝚸𝚬꧊᱂ ! श्रेष्ठ # Dont Remove Credit

@Client.on_message(filters.private & filters.text & ~filters.command("start"))
async def handle_request(bot, message):
    user_id = message.from_user.id
    text = message.text.lower().strip()
    
    if "videsi video" in text:
        is_joined = await checkSub(bot, message)
        if not is_joined: return
        if not await db.has_premium_access(user_id):
            if not await check_verification(bot, user_id) and DS_VERIFICATION == True:
                btn = [[
                    InlineKeyboardButton("𝗩𝗘𝗥𝗜𝗙𝗬 ✅", url=await get_token(bot, user_id, f"https://telegram.me/{DS_BOT_USERNAME}?start="))
                ],[
                    InlineKeyboardButton("𝗛𝗢𝗪 𝗧𝗢 𝗩𝗘𝗥𝗜𝗙𝗬 🔓", url=DS_VERIFY_TUTORIAL)
                ]]
                k = await message.reply_text(
                        text=VERIFICATION_TEXT.format(message.from_user.mention),
                        protect_content=True,
                        reply_markup=InlineKeyboardMarkup(btn)
                    )
                await asyncio.sleep(300)
                await k.delete()
                return
        tag, channel = "videsi", DS_VIDESI_FILE_CHANNEL
        allowed = await check_and_increment(user_id, tag)
        if not allowed:
            return await message.reply("Daily limit reached. Upgrade to premium.")

        file = await db.random_file(tag)
        if not file:
            return await message.reply("No video found.")

        try:
            qw = await bot.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=channel,
                    message_id=file['msg_id'],
                    caption=f"""<b>Powered By <a href='https://t.me/Pronwahbot'>𝐏ʀᴏɴᴡᴀʜ !</a></b>\n\n<blockquote>This Message Will Be Deleted In 10 Minutes Due To Copyright Issue So Save It Somewhere.</blockquote>"""
                )
            await asyncio.sleep(600)
            await qw.delete()
        except Exception as e:
            print(f"❌ Error sending file: {e}")
            await db.delete_file(file['msg_id'])  # ← Use the function here
            await message.reply("⚠️ Failed to send video. It may have been deleted.")
    
    elif "desi video" in text:
        is_joined = await checkSub(bot, message)
        if not is_joined: return
        if not await db.has_premium_access(user_id):
            if not await check_verification(bot, user_id) and DS_VERIFICATION == True:
                btn = [[
                    InlineKeyboardButton(" 𝗩𝗘𝗥𝗜𝗙𝗬 ✅", url=await get_token(bot, user_id, f"https://telegram.me/{DS_BOT_USERNAME}?start="))
                ],[
                    InlineKeyboardButton("𝗛𝗢𝗪 𝗧𝗢 𝗩𝗘𝗥𝗜𝗙𝗬 🔓", url=DS_VERIFY_TUTORIAL)
                ]]
                i = await message.reply_text(
                        text=VERIFICATION_TEXT.format(message.from_user.mention),
                        protect_content=True,
                        reply_markup=InlineKeyboardMarkup(btn)
                    )
                await asyncio.sleep(300)
                await i.delete()
                return
            
        tag, channel = "desi", DS_DESI_FILE_CHANNEL
        allowed = await check_and_increment(user_id, tag)
        if not allowed:
            return await message.reply("Daily limit reached. Upgrade to premium.")

        file = await db.random_file(tag)
        if not file:
            return await message.reply("No video found.")

        try:
            la = await bot.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=channel,
                    message_id=file['msg_id'],
                    caption=f"""<b>Powered By <a href='https://t.me/Pronwahbot'>𝐏ʀᴏɴᴡᴀʜ !</a></b>\n\n<blockquote>This Message Will Be Deleted In 10 Minutes Due To Copyright Issue So Save It Somewhere.</blockquote>"""
            )
            await asyncio.sleep(600)
            await la.delete()
        except Exception as e:
            print(f"❌ Error sending file: {e}")
            await db.delete_file(file['msg_id'])  # ← Use the function here
            await message.reply("⚠️ Failed to send video. It may have been deleted.")
    
    elif "my plan" in text:
        user = await db.get_user(user_id)
        if not user:
            return await message.reply("User not found.")

        name = message.from_user.mention
        plan = "Premium" if await db.has_premium_access(user_id) else "Free"

        if plan == "Premium":
            desi_limit = PREMIUM_LIMIT_DESI
            videsi_limit = PREMIUM_LIMIT_VIDESI
        else:
            desi_limit = FREE_LIMIT_DESI
            videsi_limit = FREE_LIMIT_VIDESI

        used = await db.get_free_used(user_id)
        if not isinstance(used, dict):
            used = {"desi": 0, "videsi": 0}

        desi_used = used.get("desi", 0)
        videsi_used = used.get("videsi", 0)

        desi_remain = desi_limit - desi_used
        videsi_remain = videsi_limit - videsi_used
        today = str(datetime.datetime.now(pytz.timezone("Asia/Kolkata")).date())
    
        await message.reply(
            DSMYPLANTXT.format(name, user_id, plan, desi_limit, videsi_limit, desi_used, desi_limit, videsi_used, videsi_limit, desi_remain, videsi_remain, today),
            parse_mode=enums.ParseMode.HTML
        )
    
    elif "get premium" in text: 
        buttons = [[
            InlineKeyboardButton('𝗕𝗨𝗬 𝗥𝗘𝗣𝗢 ✅', url='https://t.me/ishowdrift')
        ]] [[ InlineKeyboardButton('𝗕𝗨𝗬 𝗥𝗘𝗣𝗢 ✅', url='https://t.me/ishowdrift')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=SUBS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML)

    elif "bot & repo details" in text:
        buttons = [[
            InlineKeyboardButton('𝗕𝗨𝗬 𝗥𝗘𝗣𝗢 ✅', url='http://t.me/ishowdrift') ]] 
        InlineKeyboardButton('𝗕𝗨𝗬 𝗥𝗘𝗣𝗢 ✅', url='https://t.me/ishowdrift')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        c = await message.reply_text(text=ABOUT_TXT,
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML)
        await asyncio.sleep(300)
        await c.delete()

# (C) ᯏ 𝚮𝚼𝚸𝚬꧊᱂ ! श्रेष्ठ# Dont Remove Credit
