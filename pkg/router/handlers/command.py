from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from pkg.models.user_keyboard import user_main_menu,user_share_phone
from pkg.models.admin_keyboard import admin_main_menu
import os
from aiogram.fsm.context import FSMContext
from pkg.models.repository.db import DB
from pkg.models.states import States

r = Router()
@r.message(CommandStart())
async def start(msg:Message, state:FSMContext):
    admins_list = [admin.strip() for admin in os.getenv("ADMINS").split(",")]
    print(msg.from_user.username, admins_list)
    if msg.from_user.username in admins_list:
        await msg.answer(text="привет админ",reply_markup=admin_main_menu())
    else:
        if DB.check_user(msg.from_user.id):
            await msg.answer(f"Привет {msg.from_user.username}", reply_markup=user_main_menu())
        else:
            await msg.answer(text="Для начала необходимо зарегистрироваться", reply_markup=user_share_phone())
            await state.set_state(States.User.auth)
            