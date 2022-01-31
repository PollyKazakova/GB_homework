'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
'''

def user_parameters(name, last_name, birth_year, city_living, email, tel_number):
    '''
    Функция, принимающая параметры пользователя
    '''

    print((f'Информация о пользователе - имя: {name}, фамилия: {last_name}, '
                       f'год рождения: {birth_year},город проживания: {city_living}, '
                       f'email: {email}, номер телефона: {tel_number}'))


info_user = (user_parameters(name='Ann', last_name='Simmons', birth_year=1988,
                             city_living='Tokio', email='asimmons@gmail.com', tel_number='+922456780'))
