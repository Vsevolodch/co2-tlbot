import telebot

TOKEN = '7636089675:AAHswTYri2a1syaUFy_Hn4utfpOgv8Ok5GI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот, рассказывающий об углекислом газе (CO₂). "
        "Напиши /info, /effect или /reduce, чтобы узнать больше."
    )

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(
        message.chat.id,
        "Углекислый газ (CO₂) — это бесцветный газ без запаха. Он образуется при сгорании органических веществ "
        "и является важным парниковым газом, влияющим на изменение климата."
    )

@bot.message_handler(commands=['effect'])
def effect(message):
    bot.send_message(
        message.chat.id,
        "CO₂ задерживает тепло в атмосфере, вызывая парниковый эффект. "
        "Это ведёт к глобальному потеплению, таянию ледников и изменению погодных условий.\n"
        "Для более подробной информации напиши /effect1"
    )

@bot.message_handler(commands=['effect1'])
def effect1(message):
    bot.send_message(
        message.chat.id,
        "В результате повышается уровень мирового океана, увеличивается частота экстремальных погодных явлений — "
        "таких как засухи, ливни, ураганы и лесные пожары.\n"
        "Эти изменения угрожают биоразнообразию, сельскому хозяйству и водным ресурсам, "
        "а также усиливают социально-экономическое неравенство в уязвимых регионах."
    )

@bot.message_handler(commands=['reduce'])
def reduce(message):
    bot.send_message(
        message.chat.id,
        "Как можно снизить выбросы CO₂:\n"
        "• Использовать общественный транспорт или велосипед\n"
        "• Переходить на возобновляемые источники энергии\n"
        "• Уменьшать потребление и перерабатывать отходы\n"
        "• Есть меньше продуктов животного происхождения"
    )

print("Бот запущен")
bot.polling()
