import telebot
import secrets
from telebot import types
import time

users = {}
token = '5608454988:AAF3XxlXaZ66QMVAr1rlnd35aDfdCwkwxvc'
s = 'Plastmassovyj mir pobedil Maket okazalsya silnej Poslednij korablik ostyl Poslednij fonarik ustal avgorle sopyat komya vospominanij moya oborona Solnechnyj zajchik steklyannogo glaza moya oborona Traurnyj myachik nelepogo mira Traurnyj myachik deshyovogo mira Plastmassovyj mir pobedil likuet kartonnyj nabat komu nuzhen lomtik iyulskogo neba'.lower()
words = s.split()
symbols = ['!', '@', '#', '%', '&', '?', '+', '-', '=', '_']

bot = telebot.TeleBot(token)

# команда start
@bot.message_handler(commands=["start"])
def start(message):
        # генерируем пароль и делаем три кнопки
        password = ''
        i = secrets.randbelow(len(words)-1) + 1
        x = secrets.randbelow(2) - 2
        password = words[i-1][:x] + words[i][:x] + words[i+1][:x]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Больше цифр!')
        item2 = types.KeyboardButton('Больше спецсимволов!')
        item3 = types.KeyboardButton('Больше заглавных букв!')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        users[message.chat.id] = password
        bot.send_message(message.chat.id, "Пароль: " + password + "\nНу чё, беспонтовый пирожок, улучшить пароль?\nЗахочешь начать заново - введи /start .", reply_markup=markup)

# модификация пароля с учётом нажатых кнопок
@bot.message_handler(content_types=["text"])
def handle_text(message):
    password = users.get(message.chat.id)
    if message.text.strip() == 'Больше цифр!':
            i = secrets.randbelow(len(password))
            password = password[:i] + str(1 + secrets.randbelow(99)) + password[i:]
            users[message.chat.id] = password
    if message.text.strip() == 'Больше спецсимволов!':
            i = secrets.randbelow(len(password))
            password = password[:i] + symbols[secrets.randbelow(len(symbols))] + password[i:]
            users[message.chat.id] = password
    if message.text.strip() == 'Больше заглавных букв!':
            i = secrets.randbelow(len(password))
            while s.find(password[i]) == -1:
                    i = secrets.randbelow(len(password))
            password = password[:i] + password[i].upper() + password[i+1:]
            users[message.chat.id] = password
    bot.send_message(message.chat.id, password)

bot.infinity_polling()