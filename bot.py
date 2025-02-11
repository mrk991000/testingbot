from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = os.getenv("TOKEN")  # Get the token from Render environment variables

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your bot.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()  # Keep the bot running

if __name__ == "__main__":
    main()
