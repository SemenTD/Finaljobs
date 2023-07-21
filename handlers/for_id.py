from pydoc import classname
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery,Message
from pip._internal.utils import logging

from callback.callbackdota import DotaIdCallbackData
from staiti.idstate import IdStateGroup

import opendota


client = opendota.OpenDota()

iD_router = Router()

LOGGER = logging.getLogger(__name__)


@iD_router.callback_query(DotaIdCallbackData.filter())
async def get_player(query: CallbackQuery, state: FSMContext):
    await query.message.answer("🌀Введите nickname пользователя,\nПрофиль которого вам нужно найти🌀")
    await state.set_state(IdStateGroup.fill_id)


@iD_router.message(StateFilter(IdStateGroup.fill_id))
async def api_say(message: Message, state: FSMContext):
    await message.answer('Ищем...')
    finded = client.search_player(message.text)[0]
    print(finded)
    full_info = client.get_player(finded['account_id'])
    g = full_info['profile']['avatarfull']
    print(full_info)
    await message.answer_photo(g, caption=f"Username: {full_info['profile']['personaname']}")
