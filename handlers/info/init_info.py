import telebot

from funcs.funcs_datetime import get_welcome
from init_bot import bot


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = f"{get_welcome()} Я бот для составления тренировки по программе \"Сплит\".\n\n" \
           f"Список команд:\n" \
           f"/what_is_split - Что такое программа \"Сплит\"?\n" \
           f"/day_one - План упражнений на группы мышц груди и трицепса\n" \
           f"/day_two - План упражнений на группы мышц бицепса и спины\n" \
           f"/day_three - План упражнений на группы мышц плечей и ног"
    with open("building.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=text)


@bot.message_handler(commands=["what_is_split"])
def get_info(message: telebot.types.Message):
    text = "Трехдневный сплит на массу – классическая программа тренировок для набора мышечной массы. Её используют как начинающие, так и опытные спортсмены. Три тяжёлые тренировки в неделю гарантируют стабильную прибавку в объеме мышц и силовых показателях без перетренированности и с полноценным восстановлением.\n\n" \
           "Тренировочный принцип под названием “сплит” означает, что мы “разбиваем” тело на отдельные мышечные группы и тренируем их в разные дни. Преимущество такого подхода заключается в том, что мышечные группы получают больше времени на восстановление и рост. Пока одна мышца отдыхает, мы тренируем другую. Если делать всего три тренировки в неделю, в долгосрочной перспективе это приведёт к прогрессу.\n\n" \
           "[Узнать подробнее](https://cross.expert/programmy-trenirovok/trehdnevnyj-split-na-massu.html)"
    bot.send_message(message.chat.id, text, parse_mode='Markdown')