import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from button import catalog
from web_uzb import audio
from web_turk import audio1


TOKEN = ""

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Salom {message.from_user.full_name}",reply_markup=catalog)


@dp.callback_query(F.data == "uzbek")
async def uzb(call:CallbackQuery):
    for x in audio:
        await call.message.answer_audio(audio=x)

@dp.callback_query(F.data == "turk")
async def uzb(call:CallbackQuery):
    for x in audio1:
        await call.message.answer_audio(audio=x)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
