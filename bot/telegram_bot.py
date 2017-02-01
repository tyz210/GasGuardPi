#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import keyring

from credentials import BOT_KEY_NAMESPACE, BOT_TOKEN

TOKEN = keyring.get_password(BOT_KEY_NAMESPACE, BOT_TOKEN)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):


    bot.send_message(message.chat.id, 'You say: {}'.format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
