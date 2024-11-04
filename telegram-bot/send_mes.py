import asyncio
from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = ''
CHANNEL_ID = ''


async def send_message_to_channel():
    bot = Bot(token=API_TOKEN)

    try:
        # Текст сообщения
        text = (
            "🔔 Бот с ПРОМОКОДАМИ и бот с ТОВАРАМИ для экономии ваших денег и времени"
        )

        # Создаем клавиатуру с двумя кнопками
        keyboard = InlineKeyboardMarkup(row_width=2)
        button_promo_bot = InlineKeyboardButton(text="ПРОМОКОДЫ✅", url="")
        button_product_bot = InlineKeyboardButton(text="ТОВАРЫ✅", url="")
        keyboard.add(button_promo_bot, button_product_bot)

        # Отправляем сообщение с кнопками
        await bot.send_message(CHANNEL_ID, text=text, reply_markup=keyboard, parse_mode="Markdown")

    finally:
        # Закрываем сессию
        await bot.session.close()


if __name__ == '__main__':
    # Запуск асинхронной функции для отправки сообщения
    asyncio.run(send_message_to_channel())
