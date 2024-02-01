from init_bot import bot

from handlers import init_handlers

if __name__ == "__main__":
    init_handlers.register_handlers()
    print("Bot is active!")
    bot.infinity_polling()


