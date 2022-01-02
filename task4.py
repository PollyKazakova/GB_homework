'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('numerals.txt', 'r', encoding='utf-8') as file:
    with open('numerals_rus.txt', 'w', encoding='utf-8') as rus:
        rus.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in file]))
