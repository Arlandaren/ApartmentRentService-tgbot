from aiogram.filters import StateFilter
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router,F
from pkg.models.keyboard.admin_keyboard import admin_main_menu
router = Router()

@router.message(StateFilter(None))
async def warning(msg:Message,):
    await msg.answer("👋Привет \nЧтобы начать напиши /start⭐", reply_markup=to_menu())

@router.callback_query(F.data == "back")
async def back(cb:CallbackQuery,state:FSMContext):
    await cb.message.delete()
    # await state.clear()

@router.callback_query(F.data == "admin_back_to_main_menu")
async def back(cb:CallbackQuery,state:FSMContext):
    await cb.message.edit_text("Меню", reply_markup=admin_main_menu())
    await state.clear()