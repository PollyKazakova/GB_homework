'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
'''

import json

profits = {}
average = {}

with open('firms.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for i in text.split('\n'):
        line = i.split()
        profits[line[0]] = int(line[2]) - int(line[3])
    sum_ = 0
    count = 0
    for i in profits:
        if profits[i] > 0:
            sum_ += profits[i]
            count += 1
    average["average_profit"] = "%.1f" % (sum_ / count)

list_to_print = [profits, average]

with open('output.json', 'x') as file:
    list_to_print = json.dump(list_to_print, file)
