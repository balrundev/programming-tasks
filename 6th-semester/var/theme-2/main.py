'''
2.1 Написать программу, позволяющую выполнять подсчет слов в тексте,
а также вычислять размер (в символах) каждого слова.
Используйте для возвращения результатов подсчета механизм генераторов.
'''

def calc_length(text):
    for symbol in [',', '.', '!', '?', ':', ';', '-', '(', ')']:
        text = text.replace(symbol, ' ')
    print('Words count:', len(text.split()))
    for word in text.split():
        yield f'{word}: {len(word)}'
        
        
if __name__ == '__main__':
    text = input('Enter text: ')
    for word in calc_length(text):
        print(word)