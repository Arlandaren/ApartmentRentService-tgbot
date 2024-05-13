from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
def user_main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Каталог",callback_data="")
    kb.button(text="Связь с администратором", callback_data="")
    return kb.as_markup()

def user_share_phone():
    kb = []
    row = []
    
    row.append(types.KeyboardButton(text="Зарегистрироваться", request_contact=True))
    kb.append(row)

    return types.ReplyKeyboardMarkup(keyboard=kb)