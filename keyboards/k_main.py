from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
k_main =[
    [KeyboardButton(text="🚀 PERÍODO DE PRUEBA 🚀")],
    [KeyboardButton(text='❤️ Planes'), KeyboardButton(text='👤 Suscripción')],
    [KeyboardButton(text='🎁 Ingresar código promocional'), KeyboardButton(text='💌 Mis contactos')],
]

keyboard_main = ReplyKeyboardMarkup(keyboard=k_main, resize_keyboard=True)