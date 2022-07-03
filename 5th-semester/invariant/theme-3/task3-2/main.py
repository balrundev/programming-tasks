"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ. Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.

Страница документации: https://cbr.ru/development/
"""

# http://www.cbr.ru/scripts/XML_daily.asp
import time
import json
import requests
from datetime import datetime
from xml.etree import ElementTree as ET  # исследовать библиотеки для парсинга xml и использовать более оптимальную библиотеку для парсинга xml (если такая есть)


class CurrencyInfo():
    def __init__(self):
        self.c = False
        self.t = time.time()
        self.dt = datetime.now().day
        self.rates = None

    def get_currencies(self, currencies_ids_lst=None):
        t = time.time()
        dt = datetime.today().day

        result = {}
        
        if self.c:
            result = self.rates
            
        if not self.c or (t - self.t >= 3600 or dt != self.dt):
            # one request per hour
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
            self.rates = result

        return result


class Decorator(CurrencyInfo):

    _compoment: CurrencyInfo = None

    def __init__(self, component: CurrencyInfo) -> None:
        self._component = component

    def get_currencies(self):
        return self._compoment.get_currencies()


class CurrencyInfoJSON(Decorator):

    def __str__(self):
        return 'JSON data:\n' + self.get_currencies()
    
    def get_currencies(self, currencies_ids_lst=None):
        return json.dumps(self._component.get_currencies(currencies_ids_lst), ensure_ascii=False, indent=4)


class CurrencyInfoCSV(Decorator):

    def __str__(self):
        return 'CSV data:\n' + self.get_currencies()
    
    def get_currencies(self, currencies_ids_lst=None):
        currency_data = self._component.get_currencies(currencies_ids_lst)

        if type(currency_data) is str:
            currency_data = json.loads(currency_data)
        
        csv_data = "ID;Rate;Name\n"
        for currency, val in currency_data.items():
            row = [currency, *val]
            csv_data += ';'.join(row) + '\n'
        csv_data = csv_data.rstrip()
        return csv_data


def print_data(component: CurrencyInfo) -> None:
    print(component.get_currencies())


if __name__ == '__main__':
    print('Plain data:')
    c_info = CurrencyInfo()
    print_data(c_info)

    print('JSON:')
    cinfo_json = CurrencyInfoJSON(c_info)
    #print(cinfo_json)
    print_data(cinfo_json)

    print('CSV:')
    cinfo_csv = CurrencyInfoCSV(c_info)
    #print(cinfo_csv)
    print_data(cinfo_csv)

    print('CSV (from JSON data):')
    cinfo_csv = CurrencyInfoCSV(cinfo_json)
    #print(cinfo_csv)
    print_data(cinfo_csv)