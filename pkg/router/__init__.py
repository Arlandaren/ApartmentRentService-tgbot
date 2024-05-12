from aiogram import Bot, Router
import os
from .handlers.command import r
router = Router()
router.include_routers(r)


bot = Bot(os.getenv("BOT_TOKEN"))