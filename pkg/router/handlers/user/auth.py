from aiogram import F,Router
from aiogram.types import Message

r = Router()

@r.message(F.contact)
async def get_contact(msg:Message):
    await msg.answer("asdasdasdad")
