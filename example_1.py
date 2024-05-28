import telebot
import datetime
import time
import threading
import random
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()
# Получение параметров из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_massage(message):
    bot.reply_to(message, "Привет! Я твой эхо-бот фактов... набери: /fact")

@bot.message_handler(commands=['fact'])
def fact_massage(message):
    list = [
        "1. Вода мокрая",
        "2. Килограмм Воды по весу равен килограмму песка",
        "3. Воды много"        
    ]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Вот тебе Факт: ... {random_fact}")

bot.polling(none_stop=True)