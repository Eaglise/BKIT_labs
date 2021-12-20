from requests import get
import random
import config
import pymorphy2
from rss_parser import Parser

def konachan(args):
    """поиск картинки по тэгам на сайте konachan.net"""
    arg = (str(args).replace(' ', '_')).lower()
    r = get(f'https://konachan.net/post.json?page=1&tags={arg}%20rating:safe&limit=1000')
    json_data = r.json()
    if json_data:
        posts_count = len(json_data)
        try:
            rand = random.randint(0, posts_count - 1)
        except ValueError:
            rand = 0
        try:
            json_data = json_data[rand]
        except TypeError:
            print("ERROR")
        return str(json_data['file_url'])
    else:
        return "ERROR"

def deviantart(args):
    """поиск картинки по тэгам на deviantart.com"""
    arg = (str(args).replace(' ', '-')).lower()
    try:
        #print("starting parsing")
        xml = get(f'https://backend.deviantart.com/rss.xml?q={arg}')
        parser = Parser(xml=xml.content)
        feed = parser.parse()
        url_list = []
        for item in feed.feed:
            url_list.append(item.link)
        #print("starting choosing")
        if len(url_list)==0:
            return "ERROR"
        else:
            if len(url_list) == 1:
                r = get(f'https://backend.deviantart.com/oembed?url={url_list[0]}')
                json_data = r.json()
                return json_data['url']
            else:
                count = 0
                while(True):
                    count += 1
                    if count > 50:
                        break
                    url = url_list[random.randint(0, len(url_list)-1)]
                    r = get(f'https://backend.deviantart.com/oembed?url={url}')
                    json_data = r.json()
                    if json_data['safety'] == "nonadult":
                        return json_data['url']
                return "ERROR"
    except:
        return "ERROR"

def city_check(city: str):
    '''Проверка на существование городов'''
    r = get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={config.weather_api["key"]}')
    json_weather = r.json()
    if json_weather['cod'] != 200:
        if json_weather['message'] == "city not found":
            return True
    return False

def weather(city):
    '''Создание описания с погодой'''
    try:
        r = get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={config.weather_api["key"]}')
        json_weather = r.json()
    except:
        return "ERROR"
    '''Склонение названия города'''
    morph = pymorphy2.MorphAnalyzer()
    city_parse = morph.parse(json_weather['name'])[0]
    arr = [city.split]
    if len(arr) > 1:
        tmp_city = ""
        for wrd in arr:
            tmp_city = tmp_city + morph.parse(wrd)[0].inflect({'loct'}).word.capitalize() + " "
        city_parse = tmp_city.rstrip()
    else:
        city_parse = city_parse.inflect({'loct'}).word.capitalize()
        if '-' in city_parse:
            city_parse = "-".join(list(map(lambda x: x[0].upper() + x[1:], city_parse.split('-'))))
    if json_weather['main']['temp'] > 0:
        plus = '+'
    else:
        plus = ''
    temperature = "В " + city_parse + " сейчас " + plus + str(round(json_weather['main']['temp'])) + "°C"
    weather_description = json_weather['weather'][0]['description'].capitalize()
    return str(temperature + "\n" + weather_description)


