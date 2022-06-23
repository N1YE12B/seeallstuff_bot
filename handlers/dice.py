from aiogram import types
from create_bot import bot
from aiogram.dispatcher import Dispatcher
import random

from keyboard import kb_return

async def dice_throw(callback: types.CallbackQuery):
    await callback.message.answer(f'Кубик выдал: {random.randint(1,6)}🎲',reply_markup=kb_return)
    await callback.answer()

def reg_handlers_dice(dp: Dispatcher):
    #dp.register_message_handler(dice_throw, commands='dice')
    dp.register_callback_query_handler(dice_throw, text='dice')
