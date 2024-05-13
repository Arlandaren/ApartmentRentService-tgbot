from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from pkg.models.user_keyboard import user_main_menu,user_share_phone
from pkg.models.admin_keyboard import admin_main_menu
import os
from pkg.models.repository.db import DB


r = Router()
@r.message(CommandStart())
async def start(msg:Message):
    admins_list = [admin.strip() for admin in os.getenv("ADMINS").split(",")]
    print(msg.from_user.username, admins_list)
    if msg.from_user.username in admins_list:
        await msg.answer(text="привет админ",reply_markup=admin_main_menu())
    else:
        if DB.check_user:
            await msg.answer(f"Привет {msg.from_user.username}", reply_markup=user_main_menu())
        else:
            await msg.answer(text="Для начала необходимо зарегистрироваться", reply_markup=user_share_phone())
            # DB.create_user(id=msg.from_user.id,phone=,username=msg.from_user.username)
            pass
            