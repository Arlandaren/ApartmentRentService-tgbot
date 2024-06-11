from aiogram import F,Router
from aiogram.types import Message
from pkg.models.states import States
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from pkg.models.repository.db import DB
from pkg.router.handlers.command import start
r = Router()

@r.message(F.contact, States.User.auth)
async def get_contact(msg:Message, state:FSMContext):
    if DB.create_user(msg.from_user.id,msg.contact.phone_number,msg.from_user.username):
        await msg.answer(f"Вы успешно зарегистрировались под номером {msg.contact.phone_number}", reply_markup=ReplyKeyboardRemove())
        await state.clear()
        await start(msg,state)
    else:
        await msg.answer("не удалось зарегистрироваться")
