from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

plans_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔥 ACCESO DE PRUEBA – GRATIS", callback_data='free_sub')
    ],
    [
        InlineKeyboardButton(text="🔞 30 días de acceso VIP – $60", callback_data='vip_sub')
    ],
    [
        InlineKeyboardButton(text="👅 Acceso PREMIUM de por vida – $200", callback_data='premium_sub')
    ]
])