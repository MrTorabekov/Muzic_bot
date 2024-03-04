import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from button import catalog
from web_uzb import audio
from web_turk import audio1
from web_rus import audio2
from web_azarb import audio3
from web_kazak import audio4

TOKEN = "7163530590:AAEQ_e86WsCKTgOxPtRdY2Vw81-n0MTFCyk"

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"<b>Hello</b> {message.from_user.full_name} <b>which country music do you need?</b>",reply_markup=catalog,parse_mode="HTML")


@dp.callback_query(F.data == "uzbek")
async def uzb(call:CallbackQuery):
    for a in audio:
        await call.message.answer_audio(audio=a)

@dp.callback_query(F.data == "turk")
async def uzb(call:CallbackQuery):
    for b in audio1:
        await call.message.answer_audio(audio=b)


@dp.callback_query(F.data == "rus")
async def uzb(call:CallbackQuery):
    for d in audio2:
        await call.message.answer_audio(audio=d)


@dp.callback_query(F.data == "azar")
async def uzb(call:CallbackQuery):
    for e in audio3:
        await call.message.answer_audio(audio=e)


@dp.callback_query(F.data == "kazak")
async def uzb(call:CallbackQuery):
    for f in audio4:
        await call.message.answer_audio(audio=f)





async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
