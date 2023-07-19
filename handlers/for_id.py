from idlelib import query

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from python_opendota.apis.tags import benchmarks_api
from python_opendota.apis.tags.players_api import PlayersApi

from data import facts
from callback.callbackdota import DotaIdCallbackData
from aiogram.types import CallbackQuery, Message
import python_opendota

iD_router = Router()

configuration = python_opendota.Configuration(
    host="http://api.opendota.com/api"
)


@iD_router.callback_query(DotaIdCallbackData.filter())
async def Id_poisck(query: CallbackQuery, callback_data: ..., state: FSMContext):
    with python_opendota.ApiClient(configuration) as api_client:
        api_instance = PlayersApi(api_client)

        print(api_instance.players_account_id_get({
            'account_id': 10
        },
        accept_content_types={"application", "json",}))
