'''
2.3. Разработать программу, которая для заданного количества значений возвращала бы список
из уникальных элементов, содержащихся во входном наборе значений. Используйте упаковку и распаковку элементов.
'''

import random


def find_unique(*args):
    return set(args)
    
    
if __name__ == '__main__':
    values = [random.randint(1, 5) for _ in range(10)]
    print('Values:', *values)
    unique = find_unique(*values)
    print('Unique values:', *unique)