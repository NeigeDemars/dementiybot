import telebot, random
from telebot.types import Message
aqualang = [
    'https://i.ytimg.com/vi/weZUdSpSfJg/maxresdefault.jpg',
    'http://www.tetis.ru/img/articles/equip/prodive_scuba/prodive_scuba_02.jpg',
    'http://s019.radikal.ru/i634/1305/db/483b1aca4a8a.jpg',
    'https://memegenerator.net/img/instances/56409190/aqualung.jpg',
    'http://creamroyal.ru/upload/iblock/66b/66b9629a9060d33fc3c58fed4dec3cc4.png',
    'https://www.open-dive.ru/UPLOAD/diver01.jpg',
]

TOKEN = '797480817:AAGbVW6GHQV6yTO61cMFlnFzn7B3876y0z4';
bot = telebot.TeleBot(TOKEN)

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