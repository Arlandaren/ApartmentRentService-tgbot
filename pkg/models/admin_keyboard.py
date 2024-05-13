from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import types
def admin_main_menu():

    kb = InlineKeyboardBuilder()
    kb.button(text="Добавить квартиру",request_contact=True,callback_data="aaaa")
    kb.button(text="Статистика", callback_data="aaa")
    return kb.as_markup()

