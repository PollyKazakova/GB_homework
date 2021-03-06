'''
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
'''

subjects = {}
nums = set('0123456789')

with open('subjects.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for i in text.split('\n'):
        subj = i.split(':')[0]
        sum_ = 0
        num = ''
        for j in i.split(':')[1]:
            if j in nums:
                num += j
            if j == '(':
                sum_ += int(num)
                num = ''
        subjects[subj] = sum_
    print(subjects)
    