from aiogram.fsm.state import State,StatesGroup

class States(StatesGroup):
    class User(StatesGroup):
        auth = State()