'''
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
'''

with open('staff.txt', 'r', encoding='utf-8') as staff:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in staff}
    print(f'Средняя зарплата составляет {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Зарплата меньше 20000 у следующих сотрудников: '
          f'{[el[0] for el in employees_dict.items() if el[1] < 20000]}')
