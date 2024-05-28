import telebot
import datetime
import time
import threading
import random
from dotenv import load_dotenv
from telebot import types
import os

# Загрузка переменных окружения из файла .env
load_dotenv()
# Получение параметров из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_massage(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['О чат боте', 'Прайс-лист']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Акции', 'Контакты']])
    bot.send_message(m.chat.id, 'Привет! Я твой эхо-бот фактов... набери: /help или /fact',
        reply_markup=keyboard)
    # Работа с потоком
    render_thread = threading.Thread(target=send_remainders, args=(m.chat.id,))
    render_thread.start()

@bot.message_handler(commands=['help'])
def start_massage(message):
    bot.reply_to(message, "С помощью этого бота можно узнать несколько фактов с помощью команды: /fact")

@bot.message_handler(commands=['fact'])
def fact_massage(message):
    list = [
        "1. Вода мокрая",
        "2. Килограмм Воды по весу равен килограмму песка",
        "3. Воды много"        
    ]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Вот тебе Факт: ... {random_fact}")

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'О чат боте':
      bot.send_message(message.chat.id, 'Привет! Это чат бот для проверки фактов. Набери: /fact')
    elif message.text == 'Прайс-лист':
      bot.send_message(message.chat.id, 'Прайс-лист на услуги по созданию Чат Бота')
    elif message.text == 'Акции':
      bot.send_message(message.chat.id, 'Акции на предоставляемые услуги')
    elif message.text == 'Контакты':
      bot.send_message(message.chat.id, 'Контактная информаци об авторах Бота')

# Работа со временем и потоком
def send_remainders(chat_id):
    first_rem = "10:00"
    second_rem  =  "13:00"
    end_rem =   "17:34"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "ВРЕМЯ ОТДОХНУТЬ!")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)