import re
import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from config_reader import config

logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hiiiii  ヾ(・ω・*)")

@dp.message(Command("dice"))
async def cmd_start(message: types.Message):
    await message.answer_dice(emoji="🎲")
    await asyncio.sleep(4)
    await message.answer("Get ratioed lmao  (─‿‿─)")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())