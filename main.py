# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:28:14 2020

@author: 79771
"""

import telebot
bot = telebot.TeleBot('1337907902:AAE1naK0IgF-pHrun--35cmzeZf566-rIGg')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Что мы делаем?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'successfully' , reply_markup=keyboard1)

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