import telebot

from telebot import types # noqa

from info import ( # noqa
    help_message,
    start_message,
    information, 
    about,
    portfolio,
    contacts,
    text,
    projects,
    show_info)

filename = "buildings.jpg"


token = '6442534302:AAEN8cebwVk_IMk-RgLmpUL6nCjCxh8GGOo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def bot_start_message(message):
    photo = open('media/start_image.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=start_message)


@bot.message_handler(commands=['help'])
def bot_help_message(message):
    photo = open('media/help_image.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=help_message)


@bot.message_handler(commands=['about'])
def bot_about(message):
    photo = open('media/dog.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=about)


@bot.message_handler(commands=['portfolio'])
def bot_portfolio(message):
    photo = open('media/family.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=show_info())


@bot.message_handler(commands=['contacts'])
def bot_contacts(message):
    photo = open('media/contacts.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=contacts)


@bot.message_handler(content_types=["text"])
def bot_text(message):
    bot.send_message(message.chat.id, text)


bot.polling()
