'''
2.1. Разработать скрипт с функцией, которая строит таблицу истинности
для логического выражения (по вариантам) для двух и трех аргументов
(используются различные наборы значений аргументов).

2.2. Разработать программу, которая выводит на экран с помощью ASCII-графики
таблицу истинности на основе переданных ей на вход аргументов
(логическое выражение, аргументы, результат вычисления выражения).
'''


from prettytable import PrettyTable

def bool_expression(a, b, c):
    a = bool(a)
    b = bool(b)
    c = bool(c)

    result = (a and b) ^ c

    return result


def table(bool_expr):
    th = ["A", "B", "C", str(bool_expr)]
    table = PrettyTable(th)
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                table.add_row((str(a), str(b), str(c), str(bool_expression(a, b, c))))
    print(table)


if __name__ == "__main__":
    table("(a AND b) XOR c")