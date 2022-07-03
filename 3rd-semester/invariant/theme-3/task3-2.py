'''
3.2. Разработка сценария с реализацией операции поиска подстроки в тексте.
'''


def search_string(substr, source):
    i = 0
    index = None
    while i < len(source):
        if i + len(substr) - 1 < len(source) and source[i:i+len(substr)] == substr:
            index = i
            i = len(source) - 1   
        i += 1
    return index


if __name__ == '__main__':
    substr = input("Введите подстроку для поиска: ")
    source_str = input("Введите исходную строку: ")
    substr_pos = search_string(substr, source_str)
    if substr_pos:
        print('Подстрока найдена на позиции', substr_pos)
    else:
        print('Подстрока не найдена')