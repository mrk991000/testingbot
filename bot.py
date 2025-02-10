from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7748063981:AAG1UdfUtcp8Qip8TXzmYWcyXiYFLhE1EpU"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot.")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()