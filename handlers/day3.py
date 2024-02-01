import random

import telebot

from init_bot import bot


@bot.message_handler(commands=["day_three"])
def get_day_three(message: telebot.types.Message):
    bot.send_message(message.chat.id, "1 часть тренировки. Проработка плечей.\n2 часть тренировки. Проработка ног.\n\nНа данный момент находится в разработке и подборе упражнений.")

