import random

import telebot

from init_bot import bot

def func(f, message: telebot.types.Message, n):
    with open(f"handlers/{f}.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex = random.choice(s)
        image = f"handlers/{f}_img/{ex[0]}.jpeg"
        with open(image, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=f"{n}. "+ex[3:])


@bot.message_handler(commands=["day_one"])
def get_day_one(message: telebot.types.Message):
    group = ["grudak", "triceps"]
    part = ["verh", "midle", "niz"]
    bot.send_message(message.chat.id, "1 часть тренировки. Проработка грудных мышц.")
    for p in part:
        func(f"{group[0]}/{p}", message, part.index(p)+1)
    bot.send_message(message.chat.id, "2 часть тренировки. Проработка трицепса.")
    for p in part:
        func(f"{group[1]}/{p}", message, part.index(p) + 1)
