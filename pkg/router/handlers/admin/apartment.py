from aiogram import Router,F,Bot
import os
from aiogram.types import CallbackQuery, Message
from aiogram.utils.media_group import MediaGroupBuilder
from pkg.models.repository.db import DB
from pkg.models.keyboard.admin_keyboard import *
from aiogram.fsm.context import FSMContext
from pkg.models.states import States

r = Router()
bot = Bot(os.getenv("BOT_TOKEN")) 
adminStates = States.Admin

@r.callback_query(F.data.startswith("apartment_callback_"))
async def admin_apartment_info(cb:CallbackQuery):
    _, _, id = cb.data.split("_")
    
    apartment = DB.get_apartment_byId(int(id))
    
    if apartment:
        info_text = (
            f"Адрес: {apartment['address']}\n"
            f"Описание: {apartment['description']}\n"
            f"Цена: {apartment['price']} рублей"
        )
        
        media_list = MediaGroupBuilder(caption=info_text)
        
        for media in apartment["media"]:
            media_type,id = media["media_id"].split("|")
            media_list.add(type=media_type,media=id)

        await cb.message.answer_media_group(media=media_list.build(),reply_markup=admin_options_apartment(apartment["id"]))
        await cb.message.answer("Действия", reply_markup=admin_options_apartment(apartment["id"]))
        
    else:
        await cb.answer("Квартира не найдена", show_alert=True)
        
@r.callback_query(F.data.startswith("admin_apartment_delete_"))
async def admin_apartment_delete(cb:CallbackQuery):
    _,_,_,id = cb.data.split("_")
    if DB.remove_apartment_byId(int(id)):
        await cb.message.answer("Квартира успешно удалена")
        await cb.message.answer("Меню", reply_markup=admin_main_menu())
    else:
        await cb.message.answer("Произошла ошибка")
@r.callback_query(F.data.startswith("admin_apartment_edit_"))
async def admin_apartment_edit(cb:CallbackQuery):
    _,_,_,id = cb.data.split("_")
    if id:
        await cb.message.answer("Что вы желаете изменить?", reply_markup=admin_edit_options(id))

@r.callback_query(F.data.startswith("admin_apartment_editparameter_"))
async def admin_apartment_edit(cb:CallbackQuery, state:FSMContext):
    _,_,_,parameter,id = cb.data.split("_")
    if id and parameter:
        await cb.message.answer(f"Введите новое значение для {parameter}")
        await state.update_data(parameter=parameter,id=id)
        await state.set_state(adminStates.EditingApartment.user_input)
@r.message(adminStates.EditingApartment.user_input)
async def edit_apartment(msg:Message, state:FSMContext):
    payload = await state.get_data()
    new_value = msg.text
    if DB.edit_apartment_byParameter(int(payload["id"]),payload["parameter"],new_value):
        await msg.answer(f"{payload["parameter"]} успешно изменен")
        await state.clear()
        await msg.answer("Меню", reply_markup=admin_main_menu())
    else:
        await msg.answer(f"Для изменения {payload["parameter"]} пожалуйста используйте числовой формат")




