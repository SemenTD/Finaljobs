from pydoc import classname
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery,Message
from pip._internal.utils import logging

from callback.callbackdota import DotaIdCallbackData
from staiti.idstate import IdStateGroup

import opendota

# Initialize the API-connection object
client = opendota.OpenDota()

# client.get_player('player-id')

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