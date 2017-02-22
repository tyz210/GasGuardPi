#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import keyring

from telebot import types

from bot.credentials import BOT_KEY_NAMESPACE, BOT_TOKEN

TOKEN = keyring.get_password(BOT_KEY_NAMESPACE, BOT_TOKEN)

bot = telebot.TeleBot(TOKEN)

LOCATION_KEYS = ['home', 'paren_home']


def test():
    print('sdfsdf')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    markup = types.ReplyKeyboardRemove()
    markup.selective(test)

    bot.send_message(message.chat.id, 'Choose:', reply_markup=markup)


@bot.message_handler(commands=LOCATION_KEYS)
def handle_status_help(message):
    bot.send_message(message.chat.id, 'Status: {}'.format('data'))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text in LOCATION_KEYS:
        bot.send_message(message.chat.id, 'Status at {}: {}'.format(message.text, '{"data": 42}'))


if __name__ == '__main__':
    bot.polling(none_stop=True)
