from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_return = KeyboardButton('/menu')


kb_return = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_return.row(btn_return)
