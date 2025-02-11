import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from classes import init_async_db
from handler_menu import router

TOKEN = os.getenv("TOKEN")

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

    # Delete any active webhook before polling (fixes conflict issue)
    await bot.delete_webhook(drop_pending_updates=True)
    return bot, dp

async def main():
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)
    
    await init_async_db()
    bot, dp = await start_bot()
    await set_commands(bot)

    print("Bot is running...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
