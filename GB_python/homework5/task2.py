'''
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

with open('data.txt') as f:
    count_str = sum(1 for _ in f)
    print(f'Количество строк в исходном файле: {count_str}')

with open('data.txt') as f:
    lines = f.readlines()
    for i, value in enumerate(lines):
        count_words = len(value.split())
        print(f'{i + 1}-ая строка содержит {count_words} слов(а)')
