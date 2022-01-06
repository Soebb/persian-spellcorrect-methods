from videocr import save_subtitles_to_file
import os, glob
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, MessageHandler, CallbackQueryHandler, CallbackContext, Filters


BOT_TOKEN = " "

vdir = "C:/dlmacvin/1aa"
main = vdir.rsplit('/', 1)[1] + '\\'
refresh_button = [
    InlineKeyboardButton(
        text='Refresh List',
        callback_data='refresh'
    )
]

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    keyboard = []
    keyboard.append(refresh_button)
    try:
        for file in glob.glob(vdir+'/*'):
            if file.endswith(('.ts', '.mp4', '.mkv')):
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            text=file.rsplit('/', 1)[1].replace(main, ''),
                            callback_data=file.rsplit('/', 1)[1].replace(main, '')
                        )
                    ]
                )
    except Exception as e:
        print(e)
        return
    keyboard.append(refresh_button)
    #await bot.send_message(chat_id=id, text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
    update.effective_message.reply_text(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))



def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    if query.data == "refresh":
        keyboard = []
        keyboard.append(refresh_button)
        try:
            for file in glob.glob(vdir+'/*'):
                if file.endswith(('.ts', '.mp4', '.mkv')):
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                text=file.rsplit('/', 1)[1].replace(main, ''),
                                callback_data=file.rsplit('/', 1)[1].replace(main, '')
                            )
                        ]
                    )
        except Exception as e:
            print(e)
            return
        keyboard.append(refresh_button)
        query.edit_message_text(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    input = vdir + '/' + query.data
    output = 'subs/' + query.data + '.srt'
    #if __name__ == '__main__':  # This check is mandatory for Windows.
    save_subtitles_to_file(input, output, lang='fa', time_start='0:00', time_end='', conf_threshold=75, sim_threshold=80, use_fullframe=False, det_model_dir=None, rec_model_dir=None, use_gpu=False, brightness_threshold=None, similar_image_threshold=100, similar_pixel_threshold=25, frames_to_skip=1, crop_x=None, crop_y=None, crop_width=None, crop_height=None)
    update.effective_message.reply_text(text="saved.\n\n output path: subs/"+output)


if __name__=='__main__':
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text, start))
    updater.start_polling()
    updater.idle()
