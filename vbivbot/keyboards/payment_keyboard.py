from aiogram.utils.keyboard import InlineKeyboardBuilder


def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Оплатить 350 ⭐️", pay=True)

    return builder.as_markup()
