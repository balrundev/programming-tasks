'''
4.1 Написать программу, в которой пользователь вводит число от 0 до 9 включительно,
а программа выводит название введённого числа, а если второй входной аргумент type
имеет значение bin, oct, hex, то функция преобразует это число в бинарную, восьмеричную
или шестнадцатеричную форму. Предусмотреть проверку корректности введённого пользователем значения.
При реализации используемые библиотеки должны находиться в виртуальном окружении (использовать virtualenv).
'''

# Установка virtualenv: pip install virtualenv
# Создание виртуального окружения: virtualenv venv
# Активация виртуального окружения: venv\Scripts\activate.bat
# Деактивация виртуального окружения: venv\Scripts\deactivate.bat

def number_form(number: int, num_type: str=''):
    
    if type(number) is not int:
        raise TypeError('number must be integer')
    
    if number not in range(0, 10):
        raise ValueError('number must be in range [0; 9]')
    
    if num_type:
        if num_type == 'bin':
            return format(number, 'b')
        elif num_type == 'oct':
            return format(number, 'o')
        elif num_type == 'hex':
            return format(number, 'x')
        else:
            raise ValueError('num_type can be bin, oct, hex')
        
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return nums[number]


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(number_form(n))
    print(number_form(n, 'bin'))
    print(number_form(n, 'oct'))
    print(number_form(n, 'hex'))