from aiogram import types
from create_bot import bot
from aiogram.dispatcher import Dispatcher
import requests
import os
from keyboard import kb_return


async def get_neko(callback: types.CallbackQuery):
    resp = requests.get("https://nekos.best/api/v2/neko")
    results = resp.json()

    img_url = results['results'][0]['url']
    artist = results['results'][0]['artist_name']
    artist_url = results['results'][0]['artist_href']

    response = requests.get(url=img_url)
    with open('nek_img.png', 'wb') as file:
        file.write(response.content)

    path = open('nek_img.png', 'rb')
    await bot.send_photo(photo=path, chat_id=callback.from_user.id, reply_markup=kb_return)
    await bot.send_message(chat_id=callback.from_user.id, text=f'🖍Artist: {artist}. \nLink: {artist_url}')
    os.remove('nek_img.png')
    await callback.answer()



def reg_handlers_neko_grab(dp: Dispatcher):
    dp.register_callback_query_handler(get_neko, text='neko')