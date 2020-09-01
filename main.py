# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:28:14 2020

@author: 79771
"""

import telebot
import os
from flask import Flask, request
import logging
bot = telebot.TeleBot('1337907902:AAE1naK0IgF-pHrun--35cmzeZf566-rIGg')
# Проверим, есть ли переменная окружения Хероку 
if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://drkb-bot.herokuapp.com/") 
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80)) #5000
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)

#описываем клавиатуру
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Что мы делаем?')

#первое сообщение бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'successfully' , reply_markup=keyboard1)

    #обработка пользовательских ответов
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, начнем?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Увидимся!')
    elif message.text.lower() == 'что мы делаем?':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHlF9NKKMwcfPQXkA82mMx4evVW-tzAAIBAAPw3d0i5QpogBGmE64bBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling()

