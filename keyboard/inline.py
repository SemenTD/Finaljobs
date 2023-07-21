from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.callbackdota import DotaIdCallbackData, DotaFactsCallbackData

user_ID = InlineKeyboardButton(
        text='Ввести nikname игрока',
        callback_data=DotaIdCallbackData().pack())

dota_facts =InlineKeyboardButton(
        text='Интересные факты \n про доту2',
        callback_data=DotaFactsCallbackData().pack())

user_keyboard = InlineKeyboardMarkup(inline_keyboard=[
     [user_ID, dota_facts]
])

