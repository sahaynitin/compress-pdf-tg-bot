from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Here's How to Use Me **\n" + preset.HELP,
        reply_markup=InlineKeyboardMarkup(markups.close)
    )

