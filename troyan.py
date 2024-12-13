import telebot

from logictroyan import gen_pass, gen_emodji, flip_coin

bot = telebot.TeleBot("7919758551:AAEtoUnxG7Wy1jKvoxh7p7dQwgZ6QP73Kpk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['монетка'])
def send_bye(message):
    bot.reply_to(message, flip_coin())

@bot.message_handler(commands=['эмодзи'])
def send_bye(message):
    bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['пароль'])
def send_bye(message):
    bot.reply_to(message, gen_pass(1999999))
    bot.reply_to(message, "(он уже на доксбине)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
     bot.reply_to(message, message.text)

bot.polling()