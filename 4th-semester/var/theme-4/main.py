'''
3.1 Создание программы с реализацией вручную одного из алгоритмов сортировки (вставки, плавной сортировки).
'''

import random

def sort(n):
    for i in range(len(n)):
        j = i - 1
        k = n[i]
        while n[j] > k and j >= 0:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = k
    return n


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for _ in range(10)]
    print("Numbers:", numbers)
    print("Insertion sort:", sort(numbers))