import os
import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5615930372:AAEg6J4KKubuFXmXBq6wUN4M4kCpx9khKtY'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hallo *{message.from_user.first_name}* \n"
                        f"Ich bin der TecDays echo bot. \n"
                        f"Hinweis: Katzen sind _nicht_ mein Ding",
                        parse_mode='Markdown')


@dp.message_handler(regexp='(^cat[s]?$|katze)')
async def send_cats(message: types.Message):
    cat_source_dir = 'public/cats'
    cats = os.listdir(cat_source_dir)
    cat = random.choice(cats)
    with open(os.path.join(cat_source_dir, cat), 'rb') as photo:
        await message.reply_photo(photo, caption=f'Ich habe *{message.text}* gehört. Hier ist deine Katze',
                                  parse_mode='Markdown')


@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)