from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/ура')
button3 = types.KeyboardButton(text='/инфо')
button4 = types.KeyboardButton(text='/fox')

keyboard1 = [
    [button1, button2, button3],
    [button4, button1],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
