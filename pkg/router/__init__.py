from aiogram import Bot, Router
import os
from .handlers.command import r as command_router
from .handlers.user.auth import r as auth_router
from .handlers.admin.catalogue import r as admin_router
router = Router()

router.include_routers(command_router,auth_router,admin_router)


bot = Bot(os.getenv("BOT_TOKEN"))