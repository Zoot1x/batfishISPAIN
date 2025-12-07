from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

access_age_free_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎀 Obtener", callback_data='age_check')
    ],
    [
        InlineKeyboardButton(text="⬅️ Atrás", callback_data='back_to_plans')
    ]
])

access_age_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💳 Pagar", callback_data='age_check')
    ],
    [
        InlineKeyboardButton(text="⬅️ Atrás", callback_data='back_to_plans')
    ]
])