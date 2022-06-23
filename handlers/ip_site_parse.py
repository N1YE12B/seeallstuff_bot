from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import bot, dp
import socket
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import user_kb_return

class FSMControll(StatesGroup):
    domain_send = State()


async def ip_site_request(callback: types.CallbackQuery):
    await FSMControll.domain_send.set()
    await callback.message.answer("🖊Enter site's domain:🖊", reply_markup=ReplyKeyboardRemove())
    reg_handlers_site_ip_parse(dp)
    await callback.answer()




async def ip_site_parse(message: types.Message, state: FSMContext):
    try:
        address = socket.gethostbyname(message.text)
        await bot.send_message(message.from_user.id, f'🌎IP: {address}🌎')


    except socket.gaierror as error:
        await bot.send_message(message.from_user.id, f'🛑{error}🛑')

    await state.finish()




def reg_handlers_site_ip_request(dp: Dispatcher):
    dp.register_callback_query_handler(ip_site_request, text='ip-site', state=None)

def reg_handlers_site_ip_parse(dp : Dispatcher):
    dp.register_message_handler(ip_site_parse, state=FSMControll.domain_send)





