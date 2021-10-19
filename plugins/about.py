from presets import Presets
from pyrogram.types import Message


# About Message
@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Preset.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(aboutdata.ABOUT_BUTTONS),
    )
