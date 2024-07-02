import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboard import kb1
from random_fox import fox
from random import randint
API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение", reply_markup=kb1)


@dp.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")


@dp.message(F.text.lower() == "num")
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")


@dp.message(Command("инфо"))
async def send_info(message: types.Message):
    await message.answer('Я бот, созданный отвечать тебе')


@dp.message(Command("fox"))
@dp.message(Command("лиса"))
async def cmd_fox_command(message: types.Message):
    img_fox = fox()
    if img_fox:
        await message.answer("Держи лису")
        await message.answer_photo(photo=img_fox)
    else:
        await message.answer("Не удалось получить изображение лисы.")


@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.strip().lower()
    if "привет" in msg_user:
        await message.answer("Привет-привет")
    elif "пока" in msg_user:
        await message.answer("Пока-пока")
    elif "ты кто" in msg_user:
        await message.answer("Я бот")
    elif message.text == "инфо":
        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
