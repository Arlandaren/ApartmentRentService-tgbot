from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import types
def admin_main_menu():

    kb = InlineKeyboardBuilder()
    
    kb.button(text="Управление каталогом",callback_data="admin_manage_catalogue")
    kb.button(text="Статистика", callback_data="aaa")

    kb.button(text="Добавить квартиру",callback_data="admin_add_appartment")

    return kb.as_markup()
def admin_catalogue_menu():
    kb = InlineKeyboardBuilder()

    kb.button(text="Добавить квартиру",callback_data="admin_add_apartment")



