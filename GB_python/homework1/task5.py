'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

rev = int(input('Введите значение выручки Вашей фирмы: '))
cost = int(input('Введите значение издержек Вашей фирмы: '))

if rev >= cost:
    print('Финансовый результат Вашей фирмы: прибыль')
    cost_eff = (rev - cost) / rev
    print('Рентабельность Вашей фирмы составляет'.format(cost_eff))
    amount = int(input('Введите количество сотрудников в Вашей фирме: '))
    cost_eff_pers = cost_eff / amount
    print('Прибыль Вашей фирмы в расчете на одного сотрудника составляет', cost_eff_pers)
else:
    print('Финансовый результат Вашей фирмы: убыток')
