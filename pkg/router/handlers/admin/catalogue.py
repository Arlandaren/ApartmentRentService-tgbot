from aiogram.types import Message,CallbackQuery
from aiogram import Router,F
from pkg.models.repository.db import DB
from pkg.models.admin_keyboard import admin_catalogue_menu
from pkg.models.paginator import Admin_catalogue_list_paginator
r = Router()

@r.callback_query(F.data == "admin_add_appartment")
async def add_apartment(cb:CallbackQuery):
    if DB.add_apartment("Asddsad","ASdasda",[1,2]):
        await cb.message.answer("усё")
    else:
        await cb.message.answer("гг")


@r.callback_query(F.data == "admin_manage_catalogue")
async def menu_manage_catalogue(cb:CallbackQuery):
    apartments = DB.get_apartments_list()
    if apartments:
        await cb.message.edit_text("Меню каталога", reply_markup=await Admin_catalogue_list_paginator(apartments).form())
    else:
        await cb.message.answer("Вы еще не добавили квартир")