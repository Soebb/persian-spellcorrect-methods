from spell import correction
import os
from pyrogram import Client, filters

# config vars
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {}
I am Persian Text Corrector Bot.

> `I can correct the spell mistakes in the text.`

Send me a text message to get started.
"""

@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
    )


@Bot.on_message(filters.private & filters.text)
async def main(bot, m):
    text = m.text
    new_text = ""
    for sntnce in text.rsplit("\n"):
        sntnce_splited = sntnce.rsplit()
        for x in sntnce_splited:
            if x not in words:
                corrected_word = correction(word)
                sntnce_splited[sntnce_splited.index(x)] = str(corrected_word)
        new_text += " ".join(sntnce_splited)
        new_text += "\n"
    await m.reply(new_text)



Bot.run()


