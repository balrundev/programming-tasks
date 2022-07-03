'''
3.4. Реализовать программу шифрующую строку, задаваемую пользователем,
с помощью алгоритма шифрования ROT13.
'''


def encrypt(text: str) -> str:
    alphabet_lat = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for symbol in text:
        is_letter = False
        for alphabet in [alphabet_lat, alphabet_lat.upper()]:
            if symbol in alphabet:
                s += alphabet[(alphabet.index(symbol) + 13) % len(alphabet)]
                is_letter = True
        if not is_letter:
            s += symbol
    return s

if __name__ == '__main__':
    text = input('Введите текст: ')
    encrypted_text = encrypt(text)
    print(encrypted_text)
