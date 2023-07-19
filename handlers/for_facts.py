from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from data import facts
from callback.callbackdota import DotaFactsCallbackData
from aiogram.types import CallbackQuery, Message

facts_router = Router()


@facts_router.callback_query(
    DotaFactsCallbackData.filter()
)
async def start_command(query: CallbackQuery, state=FSMContext):
    await query.message.answer(facts.generate_facts())
