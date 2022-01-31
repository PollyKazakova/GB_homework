'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Enter an integer: ')
nn = n + n
nnn = nn + n
amount = int(n) + int(nn) + int(nnn)

print('{} + {} + {} = {}'.format(n, nn, nnn, amount))
