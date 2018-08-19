__author__ = 'Мишин Егор Олегович'
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up !

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in !

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys !
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

"""
OpenWeather
"""
import json
import sys
import datetime
import sqlite3

"""
В программе реализовано 3 варианта работы. 
1. Запуск через командную строку + имя города и 2 буквы страны на англ языке
пример: python openweather.py Moscow RU, и она выведет погоду, так же там появятся строки с проверкой данных, не стал
их удалять. Однако она некоректно работает с городами состоящими из двух слов, например New York US

2. Запуск просто на исполнение и она попросит ввести название города и страны, пример: "Введите название" >>> Moscow RU

3. Запуск через командную строку с несколькими городами: python openweather.py Moscow RU, Kazan RU и тп. 
Код скрыт со 151 строки. 

Айди для доступа к сайту хранится в app.id
Список городов в json формате так же в папке, как и app.id
Там же создается БД, но реализовать не успел. Так же не успел реализовать экспорт погоды из бд в разных форматах, 
поэтому присутствует только файл openweather.py, который и является основным.

Программа выполнена в соавторстве с Снегиревым Виктором и Швецом Александром

"""



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time

# def get_city():
#     if len(sys.argv)==3:
#         a = {}
#         city = sys.argv[1]
#         country = sys.argv[2]
#         with open('city_list.json', 'r', encoding='utf-8') as fh:
#             cities = json.load(fh)
#         for item in cities:
#             if city in item.values() and country in item.values():
#                 a = item
#         return a['id']
#     elif len(sys.argv) % 2 != 0:
#         a = {}
#         b=''
#         for x in range(1,len(sys.argv),2):
#             city = sys.argv[x]
#             country = sys.argv[x+1]
#             with open('city_list.json', 'r', encoding='utf-8') as fh:
#                 cities = json.load(fh)
#             for item in cities:
#                     if city in item.values() and country in item.values():
#                         a = item
#             b += str(a['id']) + ','
#         return b
#
#
# def get_data(city_id):
#     import urllib.request
#     count = 1
#     data_forecast2 = []
#     with open('app.id', 'r') as f:
#         api_id = f.read()
#     if not ',' in str(city_id):
#         url = 'https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&&units=metric$&' \
#           'appid={}'.format(str(city_id), str(api_id))
#     else:
#         url = 'https://api.openweathermap.org/data/2.5/group?id={}&mode=json&&units=metric$&' \
#               'appid={}'.format(str(city_id[:-1]), str(api_id))
#     data_forecast = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
#     try:
#         count = data_forecast['cnt']
#         data_forecast = data_forecast['list']
#         data_forecast2 = data_forecast
#     except Exception:
#         data_forecast2 += [data_forecast]
#     return data_forecast2, count
#
# def data_organizer(raw_api_dict):
#     for x in range(raw_api_dict[1]):
#         data = dict(
#             city=raw_api_dict[0][x].get('name'),
#             country=raw_api_dict[0][x].get('sys').get('country'),
#             temp=raw_api_dict[0][x].get('main').get('temp'),
#             temp_max=raw_api_dict[0][x].get('main').get('temp_max'),
#             temp_min=raw_api_dict[0][x].get('main').get('temp_min'),
#             humidity=raw_api_dict[0][x].get('main').get('humidity'),
#             pressure=raw_api_dict[0][x].get('main').get('pressure'),
#             sky=raw_api_dict[0][x]['weather'][0]['main'],
#             sunrise=time_converter(raw_api_dict[0][x].get('sys').get('sunrise')),
#             sunset=time_converter(raw_api_dict[0][x].get('sys').get('sunset')),
#             wind=raw_api_dict[0][x].get('wind').get('speed'),
#             wind_deg=raw_api_dict[0][x].get('deg'),
#             dt=time_converter(raw_api_dict[0][x].get('dt')),
#             cloudiness=raw_api_dict[0][x].get('clouds').get('all')
#         )
#         m_symbol = '\xb0' + 'C'
#         print('---------------------------------------')
#         print('Current weather in: {}, {}:'.format(data['city'], data['country']))
#         print(data['temp'], m_symbol, data['sky'])
#         print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
#         print('')
#         print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
#         print('Humidity: {}'.format(data['humidity']))
#         print('Cloud: {}'.format(data['cloudiness']))
#         print('Pressure: {}'.format(data['pressure']))
#         print('Sunrise at: {}'.format(data['sunrise']))
#         print('Sunset at: {}'.format(data['sunset']))
#         print('')
#         print('Last update from the server: {}'.format(data['dt']))
#         print('---------------------------------------')
#         data.clear()

def get_city():
    a = {}
    city = sys.argv[1]
    country = sys.argv[2]
    with open('city_list.json', 'r', encoding='utf-8') as fh:
        cities = json.load(fh)
    for item in cities:
        if city in item.values() and country in item.values():
            a = item

    print('a=', type(a), a)
    print(a['id'])
    return a['id']

# def get_city(vvod):    # здесь алгоритм для ввода с клавиатуры
#     a = {}
#     city = vvod[0]
#     country = vvod[1]
#     with open('city_list.json', 'r', encoding='utf-8') as fh:
#         cities = json.load(fh)
#     for item in cities:
#         if city in item.values() and country in item.values():
#             a = item
#     return a['id']



def get_data(city_id):
    import urllib.request
    with open('app.id', 'r') as f:
        api_id = f.read()

    print(city_id)
    print(api_id)
    url = 'http://api.openweathermap.org/data/2.5/' \
          'weather?id={}&units=metric&appid={}'.format(str(city_id), str(api_id))


    data_forecast = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

    #print(data_forecast)
    return data_forecast




def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data



def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')


if __name__ == '__main__':
    try:
        # vvod = input('Введите название города на английском и 2 буквы страны ').split(' ')
        # data_output(data_organizer(get_data(get_city(vvod))))  # включить для ввода с клавиатуры
        data_output(data_organizer(get_data(get_city())))
    except IOError:
        print('no internet')




conn = sqlite3.connect('weather.db')      # создается БД, дальше не успел
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS weather(
                            city_id integer primary key,
                            city varchar(255),
                            data DATE,
                            temperature integer,
                            weather_id integer
                 )''')
cursor.execute('''SELECT * FROM weather''')
print(cursor.fetchall())