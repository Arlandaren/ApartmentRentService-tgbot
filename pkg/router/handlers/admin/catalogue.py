from aiogram.types import Message,CallbackQuery
from aiogram import Router,F
from pkg.models.repository.db import DB
from pkg.models.keyboard.paginator import Admin_catalogue_list_paginator
from aiogram.fsm.context import FSMContext
from pkg.models.states import States
from pkg.models.keyboard.admin_keyboard import *

r = Router()
adminStates = States.Admin

@r.callback_query(F.data == "admin_add_apartment")
async def add_apartment(cb:CallbackQuery, state:FSMContext):
    await cb.message.answer("Укажите адрес квартиры")
    await state.set_state(adminStates.AddingApartment.address)

@r.message(adminStates.AddingApartment.address)
async def input_address(msg:Message,state:FSMContext):
    address = msg.text
    await state.update_data(address=address)
    await msg.answer("Добавьте описание")
    await state.set_state(adminStates.AddingApartment.description)
@r.message(adminStates.AddingApartment.description)
async def input_description(msg:Message,state:FSMContext):
    description = msg.text
    await state.update_data(description=description)
    await msg.answer("Укажите цену")
    await state.set_state(adminStates.AddingApartment.price)
@r.message(adminStates.AddingApartment.price)
async def input_price(msg:Message, state:FSMContext):
    price = msg.text
    await state.update_data(price=price)
    await msg.answer("Отправьте медиафайлы(видео/фото)")
    await state.set_state(adminStates.AddingApartment.images)
@r.message(F.photo,  adminStates.AddingApartment.images)
async def input_images(msg:Message,state:FSMContext):
    data = await state.get_data()
    
    medias = data.get('medias', [])
    
    medias.append(f"photo|{msg.photo[-1].file_id}")
    
    await state.update_data(medias=medias)
    
    await msg.reply("Изображение добавлено.\nВведите /confirm, чтобы завершить")
@r.message(F.video, adminStates.AddingApartment.images)
async def input_videos(msg:Message,state:FSMContext):
    data = await state.get_data()
    
    medias = data.get('medias', [])
    
    medias.append(f"video|{msg.video.file_id}")

    await state.update_data(medias=medias)
    
    await msg.reply("Видео добавлено.\nВведите /confirm, чтобы завершить")

@r.message(adminStates.AddingApartment.images, F.text == "/confirm")
async def input_confirm(msg:Message,state:FSMContext):
    data = await state.get_data()
    if DB.add_apartment(data["address"], data["description"],data["medias"], data["price"]):
        await msg.answer("Квартира успешно добавлена") 
        await msg.answer("Меню", reply_markup=admin_main_menu())
    else:
        await msg.answer("Ошибка при добавлении квартиры")

@r.message(adminStates.AddingApartment.images)
async def input_videos(msg:Message):
    await msg.reply("Пожалуйста отправьте медиафайл(видео/фото)")

@r.callback_query(F.data == "admin_manage_catalogue")
async def menu_manage_catalogue(cb:CallbackQuery):
    apartments = DB.get_apartments_list()
    if apartments:
        await cb.message.edit_text("Меню каталога", reply_markup=await Admin_catalogue_list_paginator(apartments).form())
    else:
        await cb.message.answer("Вы еще не добавили квартир", reply_markup=admin_add_apartment())
