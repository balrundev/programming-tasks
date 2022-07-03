'''
1.1. Разработать программу с реализацией функции для считывания json-данных из файла
и вывод их в табличном виде на экран. Реализовать базовый синтаксис
для обработки исключений (try .. except).

1.2. Дополнение программы для считывания данных проверкой утверждений или высказываний (assert).
Создание отдельного блока для такой проверки (с помощью __name__)
и скрипта командной строки для запуска этих проверок.

1.3. Дополнение программы для считывания данных с использованием менеджера контекстов
и реализации расширенного синтаксиса для обработки исключений.
'''

import json
from tabulate import tabulate

class TablePrinter:
    
    def __init__(self, filename='data.json', fields=None):
        self._data = []

        try:
            with open(filename) as f:
                self._data = json.load(f)
        except FileNotFoundError:
            print('file not found')
        except json.decoder.JSONDecodeError:
            print('JSON decode error')
            
        if fields:
            for field in fields:
                if field not in self._data[0]:
                    raise ValueError(f'field {field} is not found in file')
    
    
    @property
    def header(self):
        header = self._data[0].keys()
        header = [h.capitalize() for h in header]
        return header
    
    
    @property
    def first(self):
        row = [self._data[0].values()]
        return tabulate(row, tablefmt='tsv')
    
    
    @property
    def data(self):
        return self._data


    def render_table(self):
        header = self._data[0].keys()
        header = [h.capitalize() for h in header]

        data = [d.values() for d in self._data]

        return tabulate(data, header)


if __name__ == '__main__':
    printer = TablePrinter(fields=['login', 'email', 'active'])
    print('Table:')
    print(printer.render_table())
    print('Header:')
    print(printer.header)
    print('First row:')
    print(printer.first)


if __debug__:
    fields=['login', 'email', 'active']
    printer = TablePrinter(fields=fields)
    for field in fields:
        if field not in printer.data[0]:
            raise ValueError(f'field {field} is not found in file')
    print('Table:')
    print(printer.render_table())
