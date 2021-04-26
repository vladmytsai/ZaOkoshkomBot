import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('e0fd68f9b1e19aa2cbb3254ecc8b3568', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("1755477855:AAF-4bWdPeXjG6PSFcmTvVgd9D5UeI2s354")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + ".\n"
    answer += "За окошком около " + str(temp) + "°C\n"
    if temp <= 0:
        answer += "Морозец!!\U0001F628"
    elif temp <= 10:
        answer += "Свежачок!"
    elif temp <= 20:
        answer += "Та норм там!"
    elif temp <= 27:
        answer += "Теплооо!\U0001F60B"
    else:
        answer += "Жараа!\U0001F613"

    bot.send_message(message.chat.id, answer)
    #bot.reply_to(message, message.text)

bot.polling(none_stop = True)
