'''
2.1 Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия
и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.
2.2 Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.
2.3 Рефакторинг (модификация) программы с декоратором модулем functools и использование его функционала.
'''

import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        if args[2] == '+':
            name = 'Сложение'
        elif args[2] == '-':
            name = 'Вычитание'
        elif args[2] == '*':
            name = 'Умножение'
        elif args[2] == '/':
            name = 'Деление'
        with open('calc.log', 'a') as f:
            f.write('{}: {} {} {} = {}\n'.format(name, args[0], args[2], args[1], result))
        return result
    
    return wrapper


@logger
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op =='/':
        return a / b
    
    
if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите первое число: '))
    op = input('Выберите действие (+, -, *, /): ')
    result = calc(a, b, op)
    print(result)