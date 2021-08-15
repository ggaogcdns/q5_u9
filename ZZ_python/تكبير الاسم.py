import requests
import telebot
from time import sleep
token = input('[~] Enter Token :')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*Hello {first} , Send Your Name To BigHim \nملاحضة فقط بالـeng*",parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, text="صبر شوي")
        url = requests.get(f'https://artii.herokuapp.com/make?text={msg}').text
        bot.send_message(message.chat.id,f'*Name :\n{url}\n\nBy @X888E | @E999G*')
    except:
        pass
bot.polling(True)
