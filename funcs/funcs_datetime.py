import datetime


def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 23 <= current_time.hour or current_time.hour < 5:
        return "Доброй ночи!"
    if 5 <= current_time.hour < 11:
        return "Доброе утро!"
    if 11 <= current_time.hour < 17:
        return "Добрый день!"
    if 17 <= current_time.hour < 23:
        return "Добрый вечер!"
