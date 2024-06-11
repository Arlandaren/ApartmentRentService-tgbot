from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder

def admin_main_menu():

    kb = InlineKeyboardBuilder()
    
    kb.button(text="Управление каталогом",callback_data="admin_manage_catalogue")
    kb.button(text="Статистика", callback_data="admin_statistics")

    return kb.as_markup()

def admin_add_apartment():
    kb = InlineKeyboardBuilder()
    kb.button(text="Добавить квратиру", callback_data="admin_add_apartment")

    return kb.as_markup()

def admin_options_apartment(id: int):
    kb = InlineKeyboardBuilder()
    kb.button(text="Удалить", callback_data=f"admin_apartment_delete_{id}")
    kb.button(text="Редактировать", callback_data=f"admin_apartment_edit_{id}")   

    return kb.as_markup()
def admin_edit_options(id):
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data=f"admin_apartment_editparameter_address_{id}")
    kb.button(text="Описание", callback_data=f"admin_apartment_editparameter_description_{id}")   
    kb.button(text="Цена", callback_data=f"admin_apartment_editparameter_price_{id}")   
    return kb.as_markup()
