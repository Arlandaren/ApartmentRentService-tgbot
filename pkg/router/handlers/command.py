from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router


r = Router()
@r.message(CommandStart())
async def start(msg:Message):
    await msg.answer("Привет")