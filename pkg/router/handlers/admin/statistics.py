from aiogram import F, Router
from aiogram.types import CallbackQuery,BufferedInputFile, InputFile, FSInputFile
from pkg.models.repository.db import DB
from pkg.utils.convert_to_csv import convert_to_csv
import os
r = Router()

@r.callback_query(F.data == "admin_statistics")
async def admin_statistics(cb:CallbackQuery):
    users = DB.get_all_users()
    if users:
        csv = convert_to_csv(users,cb.from_user.id)

        file = FSInputFile(csv, filename="users.csv")       
        await cb.message.answer_document(file,caption=f"Количество пользователей: {len(users)}")
        os.remove(csv)
    else:
        await cb.message.answer("У вас нет пользователей")