'''
3.2 Создание программы по распределению списка с случайными значениями
на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).
'''

import random

numbers = [random.randint(-100, 100) for _ in range(10)]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for i in numbers:
    if i < 0:
        negative_numbers.append(i)
    elif i > 0:
        positive_numbers.append(i)
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 2 != 0:
        odd_numbers.append(i)

print('Numbers:', numbers)
print('Positive numbers:', positive_numbers)
print('Negative numbers:', negative_numbers)
print('Even numbers:', even_numbers)
print('Odd numbers:', odd_numbers)