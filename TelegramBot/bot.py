import requests
import telebot
import config
import dbworker
import time
import functions
from functions import *

bot = telebot.TeleBot(config.token)

#Cтартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет!")
    time.sleep(1)
    bot.send_message(message.chat.id,"Меня зовут Микото Мисака, хотя ты наверное уже догадался :)")
    time.sleep(1)
    bot.send_message(message.chat.id, "Я умею создавать картинки с погодой")
    time.sleep(1)
    bot.send_message(message.chat.id, "Мне уже не терпится, давай скорее приступим к созданию!")
    time.sleep(1)
    bot.send_message(message.chat.id, "И помни, что в любой момент можешь начать сначала, прописав /reset")
    time.sleep(1)
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SITE.value)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["konachan.net", "deviantart.com"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выбери сайт, с которого мы возьмём картинку:", reply_markup=markup)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SITE.value)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["konachan.net", "deviantart.com"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выбери сайт, с которого мы возьмём картинку:", reply_markup=markup)

# Обработка введённого сайта
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SITE.value)
def site(message):
    text = message.text
    if text != "konachan.net" and text != "deviantart.com":
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста, выбери из предложенного списка')
        return
    else:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_CITY.value)
        # Сохраняем сайт
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SITE.value), text)
        bot.send_message(message.chat.id, 'Теперь напиши мне название любого города:', reply_markup=telebot.types.ReplyKeyboardRemove())

# Обработка введённых городов
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_CITY.value)
def city(message):
    city = message.text
    if city_check(city):
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Кажется, такого города не существует...')
        bot.send_message(message.chat.id, 'Попробуй ввести название города ещё раз:')
        return
    else:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_TAG.value)
        # Сохраняем город
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_CITY.value), city)
        bot.send_message(message.chat.id, 'Отлично! И, наконец, выскажи мне предпочтения по картинкам:', reply_markup=telebot.types.ReplyKeyboardRemove())

# Обработка введённых тегов и создание демонтиватора
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_TAG.value)
def tag(message):
    tag = message.text
    site = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SITE.value))
    image_url = ""
    if site == "konachan.net":
        image_url = konachan(tag)
    elif site == "deviantart.com":
        image_url = deviantart(tag)
    if image_url == "ERROR":
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'К сожалению, по такому запросу ничего не найдено...')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Попробуй ввести другой:')
        return
    else:
        city = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_CITY.value))
        weather = functions.weather(city)
        try: #отправляем найденную картинку с подписью о погоде
            bot.send_photo(message.chat.id, requests.get(image_url).content, caption=weather)
        except:
            bot.send_message(message.chat.id, "Что-то пошло не так...")
        # Начинаем сначала
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SITE.value)
        time.sleep(1)
        bot.send_message(message.chat.id, "А теперь всё по новой!")
        time.sleep(1)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["konachan.net", "deviantart.com"]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Выбери сайт, с которого мы возьмём картинку:", reply_markup=markup)

bot.polling(none_stop=True, interval=0)