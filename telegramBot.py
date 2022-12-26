from Keyboards import SearchInlineButton
from apiNews import clearData, searchNews
from config import TELEGRAM_API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.markdown import hlink
import logging

logging.basicConfig(level = logging.INFO)
bot = Bot(token=TELEGRAM_API_TOKEN)
dispatcher = Dispatcher(bot)

async def messageText(description: str, url: str, title: str):
    return f'{title}\n\n{description}\n\n{url}\n\nНужен Telegram бот или разработчик?\nТебе сюда -> @sheixebat'

@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, хочешь немного новостей?', reply_markup=SearchInlineButton.Keyboard)

@dispatcher.inline_handler()
async def inlineFilmSearch(query: InlineQuery):
    text = query.query or None
    items = []
    if text:
        newsList = await searchNews(q=text)
        for id, new in enumerate(newsList):
            if len(items) > 20: break
            data = await clearData(new)
            items.append(InlineQueryResultArticle(
                id=id,
                input_message_content=InputTextMessageContent(await messageText(data.get('description'), data.get('url'), data.get('title')), disable_web_page_preview=True),
                title=data.get('title'),
                description=data.get('description'),
                thumb_url=data.get('thumb_url'),
            ))
    else:
        newsList = await searchNews('Новости')
        for id, new in enumerate(newsList):
            if len(items) > 20: break
            data = await clearData(new)
            items.append(InlineQueryResultArticle(
                id=id,
                input_message_content=InputTextMessageContent(await messageText(data.get('description'), data.get('url'), data.get('title')), disable_web_page_preview=True),
                title=data.get('title'),
                description=data.get('description'),
                thumb_url=data.get('thumb_url'),
            ))
    if not items:
        items.append(InlineQueryResultArticle(
            id='none',
            input_message_content=InputTextMessageContent('Ничего не нашли...', disable_web_page_preview=True),
            title='Пусто...',
            description='Новостей по такому запросу не нашлось.(',
        ))
    await query.answer(items, switch_pm_text='Новости', switch_pm_parameter='redirect')


if __name__ == '__main__':
	executor.start_polling(dispatcher, skip_updates=True)