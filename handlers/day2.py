import random

import telebot

from init_bot import bot


@bot.message_handler(commands=["day_two"])
def get_day_two(message: telebot.types.Message):
    bot.send_message(message.chat.id, "1 часть тренировки. Проработка бицепса.\n2 часть тренировки. Проработка спины.\n\nНа данный момент находится в разработке и подборе упражнений.")

