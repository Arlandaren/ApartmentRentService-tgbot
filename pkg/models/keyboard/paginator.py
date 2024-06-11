from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
import math

class Admin_catalogue_list_paginator:
    def __init__(self, data):
        self.pages = math.ceil(len(data) / 10)
        self.data = data
        self.page = 1
        
    async def form(self):
        kb = []
        nav_row = []
        manage_row = []
        current_page_data = self.get_current_page_data()  
        index = 1
        for i in range(0, len(current_page_data), 2):
            options_row = []
            for j in range(2):
                if i + j < len(current_page_data):
                    options_row.append(InlineKeyboardButton(text=f'{index}.{current_page_data[i + j]["address"]}', callback_data=f'apartment_callback_{current_page_data[i + j]["id"]}'))
                    index +=1
            kb.append(options_row)

        if self.page > 1:
            nav_row.append(InlineKeyboardButton(text="⏮️", callback_data=f"apartment_page_{self.page-1}"))
        
        nav_row.append(InlineKeyboardButton(text=f"{self.page}/{self.pages} стр.",callback_data="page"))

        if self.page < self.pages:
            nav_row.append(InlineKeyboardButton(text="⏭️", callback_data=f"apartment_page_{self.page+1}"))
        
        manage_row.append(InlineKeyboardButton(text="поиск", callback_data=f"search_apartment_by_name"))
        manage_row.append(InlineKeyboardButton(text="назад", callback_data=f"admin_back_to_main_menu"))
        manage_row.append(InlineKeyboardButton(text="Добавить", callback_data="admin_add_apartment"))

        kb.append(nav_row)
        kb.append(manage_row)
        return InlineKeyboardMarkup(inline_keyboard=kb)
    
    async def update(self, cb:CallbackQuery):
        await cb.message.edit_reply_markup(reply_markup=await self.form())

    async def process(self, cb:CallbackQuery, cb_data:str):
        if cb_data.startswith("apartment_page_"):
            _,_, page = cb_data.split("_")
            self.page = int(page)
            await self.update(cb)
            
    def get_current_page_data(self):
        start_index = (self.page - 1) * 10
        end_index = start_index + 10
        return self.data[start_index:end_index]