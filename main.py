import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")


@dp.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")


# @dp.message()
# async def echo(message: types.Message):
# await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
