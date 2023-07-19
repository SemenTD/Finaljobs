from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboard.inline import user_keyboard

common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer(
        "Привет!\n Можешь ввести ID игрока для поиска профиля ,который тебя интересует.\n либо же я могу рассказать\n тебе парочку "
        "интересных фактов о Dota2", reply_markup=user_keyboard)
