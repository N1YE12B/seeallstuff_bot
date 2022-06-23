from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# btn_crypt = KeyboardButton('/crypt')
# btn_ip = KeyboardButton('/ip')
# btn_dice = KeyboardButton('/dice')

in_kb_user_menu = InlineKeyboardMarkup(row_width=3)
btn_dice = InlineKeyboardButton(text='🎲', callback_data='dice')
btn_crypt = InlineKeyboardButton(text='💵crypt💵', callback_data='crypt')
btn_ip_parse = InlineKeyboardButton(text='🔭ip🔭', callback_data='ip')
btn_site_ip_parse = InlineKeyboardButton(text='🌐domain🌐', callback_data='ip-site')
btn_neko = InlineKeyboardButton(text='😻neko😻', callback_data='neko')
in_kb_user_menu.row(btn_crypt, btn_ip_parse, btn_dice).row(btn_site_ip_parse, btn_neko)
# kb_user_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb_user_menu.row(btn_crypt, btn_ip, btn_dice)
