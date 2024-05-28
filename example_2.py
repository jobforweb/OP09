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
    # Работа с потоком
    render_thread = threading.Thread(target=send_remainders, args=(message.chat.id,))
    render_thread.start()

@bot.message_handler(commands=['fact'])
def fact_massage(message):
    list = [
        "1. Вода мокрая",
        "2. Килограмм Воды по весу равен килограмму песка",
        "3. Воды много"        
    ]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Вот тебе Факт: ... {random_fact}")

# Работа со временем и потоком
def send_remainders(chat_id):
    first_rem = "16:02"
    second_rem  =  "14:00"
    end_rem =   "18:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Время для отдыха!")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)