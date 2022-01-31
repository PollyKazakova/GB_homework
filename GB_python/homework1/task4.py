'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

var = input('Enter a positive integer: ')
i = 0
max_var = int(var[i])

while i < (len(var)):
    if int(var[i]) > max_var:
        max_var = int(var[i])
    i = i + 1
print(max_var)
