import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
from vbivbot.handlers import payment



logging.basicConfig(level=logging.INFO)
bot = Bot(token="bottoken")
dp = Dispatcher()

dp.message.register(payment.send_invoice_handler, Command(commands="start"))
dp.pre_checkout_query.register(payment.pre_checkout_handler)
dp.message.register(payment.success_payment_handler, F.successful_payment)
dp.message.register(payment.pay_support_handler, Command(commands="paysupport"))


async def run():
    await dp.start_polling(bot)

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()
