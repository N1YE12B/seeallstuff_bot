from aiogram import types
from create_bot import bot
from aiogram.dispatcher import Dispatcher
from pyfiglet import Figlet
from create_bot import dp
from keyboard import in_kb_user_menu

#wellcome_text = Figlet(font='digital')

#@dp.message_handler(commands=['start'])


async def bot_menu(message: types.Message):
    #if message.text == '👾menu👾':
        await bot.send_message(message.from_user.id,
        #f"{wellcome_text.renderText('SeeAllStuff')}"
        '''🩸------------------------------------------------🩸
            🖤🖤🖤
          🖤╔══╗🖤
          🖤╚╗╔╝🖤
          🖤╔╝(¯`v´¯)🖤
          🖤╚══`.¸.[S.A.S]🖤
🩸------------------------------------------------🩸
           '''
        "\nIt's 👾SeeAllStuff_Bot👾"
        "\n"
        "\n📱Commands:"
        "\n💵crypt💵 - view crypto-price"
        "\n🔭ip🔭 - collect info about IP"
        "\n🌐domain🌐 - grab IP form domain"
        "\n😻neko😻 - get neko"
        "\n🎲 - dice ", reply_markup=in_kb_user_menu)



def reg_handlers_bot_menu(dp: Dispatcher):
    dp.register_message_handler(bot_menu, commands=['start', 'menu'])
