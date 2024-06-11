from aiogram import Bot, Router
import os
from .handlers.common import router as common_router
from .handlers.command import r as command_router
from .handlers.user.auth import r as user_auth_router
from .handlers.admin.catalogue import r as admin_catalogue_router
from .handlers.admin.apartment import r as admin_apartment_router
from .handlers.admin.statistics import r as admin_statistic_router
router = Router()

router.include_routers(command_router,user_auth_router,admin_catalogue_router,admin_apartment_router,admin_statistic_router)
router.include_router(common_router)

bot = Bot(os.getenv("BOT_TOKEN"))