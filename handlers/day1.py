import random

import telebot

from init_bot import bot


@bot.message_handler(commands=["day_one"])
def get_day_one(message: telebot.types.Message):
    bot.send_message(message.chat.id, "1 часть тренировки. Проработка грудных мышц.")
    with open("handlers/grudak/verh.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex1 = random.choice(s)
        image1 = f"handlers/grudak/verh_img/{ex1[0]}.jpeg"
        with open(image1, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="1. "+ex1[3:])
    with open("handlers/grudak/midle.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex2 = random.choice(s)
        image2 = f"handlers/grudak/midle_img/{ex2[0]}.jpeg"
        with open(image2, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="2. " + ex2[3:])
    with open("handlers/grudak/niz.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex3 = random.choice(s)
        image3 = f"handlers/grudak/niz_img/{ex3[0]}.jpeg"
        with open(image3, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="3. " + ex3[3:])
    bot.send_message(message.chat.id, "2 часть тренировки. Проработка трицепса.")
    with open("handlers/triceps/verh.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex1 = random.choice(s)
        image1 = f"handlers/triceps/verh_img/{ex1[0]}.jpeg"
        with open(image1, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="1. " + ex1[3:])
    with open("handlers/triceps/midle.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex2 = random.choice(s)
        image2 = f"handlers/triceps/midle_img/{ex2[0]}.jpeg"
        with open(image2, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="2. " + ex2[3:])
    with open("handlers/triceps/niz.txt", encoding="utf-8") as file:
        s = file.read().split("$\n")
        ex3 = random.choice(s)
        image3 = f"handlers/triceps/niz_img/{ex3[0]}.jpeg"
        with open(image3, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="3. " + ex3[3:])