import sys
import toml
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from pathlib import Path

from src.handlers import routers


config = toml.load(Path(__file__).with_name('config.toml'))
TELEGRAM_BOT_TOKEN = config['bot']['token']


async def main() -> None:
    bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(*routers)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
