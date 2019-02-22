import telebot, random
from telebot.types import Message
import token
aqualang = [
    'https://i.ytimg.com/vi/weZUdSpSfJg/maxresdefault.jpg',
    'https://memegenerator.net/img/instances/56409190/aqualung.jpg',
    'https://www.open-dive.ru/UPLOAD/diver01.jpg',
]


bot = telebot.TeleBot(token.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Я вас категорически приветсвую.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Бог поможет...")

@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    if message.text == "Дементий, подрочи":
        bot.send_photo(message.chat.id, "https://pp.userapi.com/c848636/v848636954/124278/SsaAqngIuiU.jpg")
    elif message.text == "Акваланг":
        bot.send_photo(message.chat.id, random.choice(aqualang))
    else:
        bot.send_message(message.chat.id, "Ты сам понял, какую хуйню написал, чёрт?")







bot.polling()