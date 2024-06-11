from aiogram.fsm.state import State,StatesGroup

class States(StatesGroup):
    class User(StatesGroup):
        auth = State()
    class Admin(StatesGroup):
        class AddingApartment(StatesGroup):
            address = State()
            description = State()
            images = State()
            price = State()
        class EditingApartment(StatesGroup):
            user_input = State()