from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import bot
from keyboard import kb_return

import requests
from datetime import datetime

#@dp.message_handler(commands=['crypt'])
async def crypto_parse(callback: types.CallbackQuery):
    bitreq = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = bitreq.json()
    bit_sell_price = response["btc_usd"]["sell"]

    # eth parse
    ethreq = requests.get("https://yobit.net/api/3/ticker/eth_usd")
    response = ethreq.json()
    eth_sell_price = response["eth_usd"]["sell"]

    await callback.message.answer(
        f"\n💸PriceList💸:"
        "\n"
        f"\n🕔On: {datetime.now().strftime('%Y-%m-%d %H:%M')}🕔\n💵Sell BTC (USD)💵: {bit_sell_price} $"
        f"\n----------------------------------------"
        f"\n🕔On: {datetime.now().strftime('%Y-%m-%d %H:%M')}🕔\n💵Sell ETH (USD)💵: {eth_sell_price} $",reply_markup=kb_return)
    await callback.answer()


def reg_handlers_crypt_parse(dp: Dispatcher):
    #dp.register_message_handler(crypto_parse, commands=['crypt'])
    dp.register_callback_query_handler(crypto_parse, text ='crypt')