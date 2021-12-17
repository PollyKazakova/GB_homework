'''
 Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
'''

var = int(input('Enter a positive integer: '))
hours = var // 3600
minutes = var // 60 - 60 * hours
seconds = var % 60

print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
