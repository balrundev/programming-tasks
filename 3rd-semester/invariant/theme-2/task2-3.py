'''
2.3. Разработать скрипт с функцией, которая для ряда Фибоначчи,
где количество элементов, n = 22, возвращает подмножество значений
или единственное значение (по вариантам).
Для нахождения элемента требуется использовать слайсы.
'''


def fib(n):
    res_lst = [0, 1]
    if n > 1:
        while True:
            cur_el = sum(res_lst[len(res_lst) - 2:])
            if cur_el <= n:
                res_lst.append(cur_el)
            else:
                break
    return res_lst


if __name__ == "__main__":
    print(fib(22))