import asyncio
import logging
import sys
import os
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from classes import init_async_db
from handler_menu import router

TOKEN = os.getenv("TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_URL")  # Example: "https://yourapp.onrender.com"
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Flask app to respond to Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!", 200

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Start"),
        types.BotCommand(command="/menu", description="Menu"),
        types.BotCommand(command="/help", description="Help"),
        types.BotCommand(command="/null", description="Default Settings"),
    ]
    await bot.set_my_commands(commands=commands)

async def start_bot():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    # Set Webhook
    await bot.set_webhook(url=WEBHOOK_URL)

    return bot, dp

async def handle_update(request: web.Request):
    bot = request.app["bot"]
    dp = request.app["dp"]
    update = await request.json()
    tg_update = types.Update.model_validate(update)
    await dp.feed_update(bot=bot, update=tg_update)
    return web.Response()

async def run_webhook():
    bot, dp = await start_bot()
    await set_commands(bot)

    app = web.Application()
    app["bot"] = bot
    app["dp"] = dp
    app.router.add_post(WEBHOOK_PATH, handle_update)

    # Start webhook server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 5000)))
    await site.start()

async def main():
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)

    bot_task = asyncio.create_task(run_webhook())
    flask_task = asyncio.to_thread(flask_app.run, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

    await asyncio.gather(bot_task, flask_task)

if __name__ == "__main__":
    asyncio.run(main())
