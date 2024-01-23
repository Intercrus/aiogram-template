from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from src.keyboards.first_keyboard import first_keyboard
from src.utils.states import States


registration_router = Router()


@registration_router.message(CommandStart())
async def first_handler(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text=(
            'First'
        ),
        reply_markup=first_keyboard
    )
    await state.set_state(States.first_state)


@registration_router.message(States.first_state, F.text == 'Second')
async def second_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text=(
            'Second'
        ),
    )
    await state.set_state(States.second_state)
