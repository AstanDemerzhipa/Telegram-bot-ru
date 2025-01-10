import telebot

# Укажите ваш токен от BotFather

bot = telebot.TeleBot("ТОКЕН")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Телеграм-бот. Чем могу помочь?")


@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "Бот был создан для оброзавательных целей и много для чего другого")

# Запуск бота
bot.polling()
