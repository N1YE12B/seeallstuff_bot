from aiogram.utils import executor
from create_bot import dp
from handlers import crypt_parse, bot_menu, ip_parse, dice, ip_site_parse, neko_grab


async def on_startup(_):
    print("Bot Online")


bot_menu.reg_handlers_bot_menu(dp)
crypt_parse.reg_handlers_crypt_parse(dp)
ip_parse.reg_handlers_ip_request(dp)
dice.reg_handlers_dice(dp)
ip_site_parse.reg_handlers_site_ip_request(dp)
neko_grab.reg_handlers_neko_grab(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


