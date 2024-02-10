
import telebot

bot = telebot.TeleBot('Ваш_токен')

users = {}

@bot.message_handler(commands=['help'])
def send_welcome(message):
        bot.reply_to(message, "Поддержка @ВашАккаунт поддержки, Скинуть денюжку (благотворительность) - https://www.donationalerts.com/r/youraccountdonationalerts.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я бот мессенджер. Если хочешь найти собеседника напиши команду /fine")



@bot.message_handler(commands=['fine'])
def find_partner(message):
    chat_id = message.chat.id
    users[chat_id] = message.from_user.username
    bot.send_message(chat_id, "Поиск собеседника...")
    for user_id in users:
        if user_id != chat_id:
            partner_username = users[user_id]
            bot.send_message(user_id, f"Ваш собеседник присоединился к чату.")
            bot.send_message(chat_id, f"Вы связаны с собеседником!. Можете начинать общение!")
            break

@bot.message_handler(commands=['disconn'])
def disconnect(message):
    chat_id = message.chat.id
    partner_chat_id = None
    for user_id in users:
        if user_id != chat_id:
            partner_chat_id = user_id
            break
    bot.send_message(chat_id, "Вы покинули чат. Напишите команду /fine, чтобы найти нового собеседника.")
    if partner_chat_id:
        bot.send_message(partner_chat_id, f"Собеседник покинул чат.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    for user_id in users:
        if user_id != chat_id:
            bot.send_message(user_id, f"{message.text}")
            break

bot.polling()
