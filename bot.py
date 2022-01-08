from spell import correction
import os
from pyrogram import Client, filters
from virastar import PersianEditor


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

"""
def read_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        words = f.read().split()
    words.extend(['!', '؟' ,'؛', '،', '.'])
    return words

words=read_file('big.txt')

@Bot.on_message(filters.private & filters.text)
async def main(bot, m):
    text = m.text
    new_text = ""
    # for a non-persian/arabic language spell correcting, use split() instead of rsplit() to splitting lines/words
    for sntnce in text.rsplit("\n"):
        sntnce_splited = sntnce.rsplit()
        for x in sntnce_splited:
            if x not in words:
                for w in words:
                    if len(list(x))==len(list(w)):
                        if len(list(x)) - len(commons) 

            """
            if x not in words:
                corrected_word = correction(x)
                sntnce_splited[sntnce_splited.index(x)] = str(corrected_word)
            """
        new_text += " ".join(sntnce_splited)
        new_text += "\n"
    await m.reply(new_text)
"""


@Bot.on_message(filters.private & filters.text)
async def main(bot, m):
    text = m.text
    textt = PersianEditor(text)
    print(textt)
    await m.reply(textt)


Bot.run()


