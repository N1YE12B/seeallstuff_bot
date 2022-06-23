from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_menu = KeyboardButton('/menu')

kb_user_ip = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_user_ip.add(btn_menu)
