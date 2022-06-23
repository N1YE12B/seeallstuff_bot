from aiogram import types
from create_bot import bot, dp
from aiogram.dispatcher import Dispatcher
import requests
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboard import kb_user_ip
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMControll(StatesGroup):
    ip_send = State()





async def ip_request(callback: types.CallbackQuery):
    await FSMControll.ip_send.set()
    await callback.message.answer("🖊Enter IP:🖊",reply_markup=ReplyKeyboardRemove())

    reg_handlers_ip_parse(dp)
    await callback.answer()

async def ip_parse(message: types.Message, state: FSMContext):
    #async with state.proxy() as data:
        try:
            response = requests.get(url=f"http://ip-api.com/json/{message.text}").json()

            data = {
                '[IP]': response.get('query'),
                '[Provider]': response.get('isp'),
                '[Country]': response.get('country'),
                '[RegionName]': response.get('regionName'),
                '[City]': response.get('city'),
                '[Lat]': response.get('lat'),
                '[Lon]': response.get('lon')
            }


            for k, v in data.items():
                if v == None:
                    await bot.send_message(message.from_user.id, '♿️Invalid IP♿️', reply_markup=kb_user_ip)
                    break
                else:
                    await bot.send_message(message.from_user.id,
                    f"🌎{k}: {v}🌎", reply_markup=kb_user_ip)

        except requests.exceptions.ConnectionError:
            await bot.send_message(message.from_user.id, '🔌Troubles with connection or wrong shit🔌')
        await state.finish()

def reg_handlers_ip_request(dp: Dispatcher):
    dp.register_callback_query_handler(ip_request, text='ip', state=None)

def reg_handlers_ip_parse(dp : Dispatcher):
    dp.register_message_handler(ip_parse, state=FSMControll.ip_send)

