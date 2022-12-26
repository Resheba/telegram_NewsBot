from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

class SearchInlineButton:
    button_search = InlineKeyboardButton(text='🔍Конечно!', switch_inline_query_current_chat='Россия')
    Keyboard = InlineKeyboardMarkup().add(button_search)
