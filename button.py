from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Uzbek', callback_data='uzbek'),InlineKeyboardButton(text='Turk', callback_data='turk')],
    [InlineKeyboardButton(text="Rus", callback_data='rus'), InlineKeyboardButton(text="Azarbayjan",callback_data="azar")],
    [InlineKeyboardButton(text="Kazak", callback_data='kazak')]

])
