from aiogram import Dispatcher
import asyncio
from pkg.router import bot,router
import logging
async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())