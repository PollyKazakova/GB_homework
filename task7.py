'''
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
'''

def int_func():
    '''
    Функция, принимающая слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой
    '''
    
    args = input('Введите слова из латинских букв через пробел: ').split()
    new_list = []
    for el in range(len(args)):
        word = args[el].title()
        new_list.append(word)
    print(str(new_list))


int_func()
