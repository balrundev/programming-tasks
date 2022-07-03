'''
1.2. Разработка скрипта, вычисляющего сумму первых n-членов арифметической прогрессии
(использование функций, условных операторов).
'''

def progression_sum(a1, d, n):
    return (2*a1 + d*(n-1)) / 2 * n


if __name__ == '__main__':
    a = int(input('a1 = '))
    d = int(input('d = '))
    n = int(input('n = '))
    if n >= 2:
        print('Сумма =', progression_sum(a, d, n))
    else:
        print('Значение n должно быть больше 1.')