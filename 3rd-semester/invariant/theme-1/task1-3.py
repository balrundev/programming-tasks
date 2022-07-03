'''
1.3. Разработка скрипта, позволяющего вычислить площадь треугольника с помощью формулы Герона.
'''

def square(a, b, c):
    if (a + b > c) or (a + c > b) or (b + c > a):
        p = (a + b + c) / 2
        result = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
        return result
    else:
        return
    
    
if __name__ == '__main__':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    sq = square(a, b, c)
    if sq:
        print('Площадь треугольника:', sq)
    else:
        print('Треугольник не существует')