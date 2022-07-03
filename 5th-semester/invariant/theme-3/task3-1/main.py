"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ. Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.

Страница документации: https://cbr.ru/development/
"""

# http://www.cbr.ru/scripts/XML_daily.asp
import time
import requests
from datetime import datetime
from xml.etree import ElementTree as ET  # исследовать библиотеки для парсинга xml и использовать более оптимальную библиотеку для парсинга xml (если такая есть)

# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
'''
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
'''


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CurrencyInfo(metaclass=Singleton):
    def __init__(self):
        self.c = False
        self.t = time.time()
        self.dt = datetime.now().day
        self.rates = None
        print('init')

    def get_currencies(self, currencies_ids_lst=None):
        t = time.time()
        dt = datetime.today().day

        result = {}
        
        if self.c:
            result = self.rates
        if not self.c or (t - self.t >= 3600 or dt != self.dt):
            # one request per hour
            print(self.c, 'new request')
            if currencies_ids_lst is None:
                currencies_ids_lst = [
                    'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                    'R01625', 'R01670', 'R01700J', 'R01710A'
                ]
            res = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
            cur_res_str = res.text

            root = ET.fromstring(cur_res_str)

            valutes = root.findall("Valute")

            for _v in valutes:
                valute_id = _v.get('ID')

                if str(valute_id) in currencies_ids_lst:
                    valute_cur_val = _v.find('Value').text
                    valute_cur_name = _v.find('Name').text

                    result[valute_id] = (valute_cur_val, valute_cur_name)

            self.c = True
            print(self.c == True)
            self.rates = result

        return result


c_info = CurrencyInfo()
r = c_info.get_currencies()
print(id(c_info))

x = CurrencyInfo()
r = x.get_currencies()
print(id(x))

y = CurrencyInfo()
r = y.get_currencies()
print(id(y))

print(r)