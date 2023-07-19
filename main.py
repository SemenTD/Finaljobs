import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import common
import handlers.for_facts

from config import config  # Config
from handlers.for_id import iD_router


def register_all_router(dp: Dispatcher):
    dp.include_router(handlers.common.common_router)
    # dp.include_router(handlers.profile_handler.get_profile_router)
    dp.include_router(handlers.for_facts.facts_router)
    dp.include_router(iD_router)

async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())  # Менеджер бота

    register_all_router(dp)

    try:
        print('Bot Started')
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
