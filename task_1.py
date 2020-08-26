# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
from random import randint
from sys import getsizeof

result = []


def object_iter(array):
    '''
    Рекурсивная функция для раскрытия основных итерируемых объектов
    '''
    for z in array:
        if (type(z) == list or type(z) == tuple or
                type(z) == set or type(z) == frozenset):
            result.append(getsizeof(z))
            object_iter(z)
        elif type(z) == dict:
            result.append(getsizeof(z))
            for k, v in z.items():
                result.append(getsizeof(k))
                if (type(v) == list or type(v) == tuple or
                        type(v) == set or type(v) == frozenset):
                    result.append(getsizeof(v))
                    object_iter(v)
                else:
                    result.append(getsizeof(v))
        else:
            result.append(getsizeof(z))
    return sum(result)


print('Измерение занимаемой скриптами ОП поризводились на коде из задачи 3, занятия 3, в среде:\n'
      '1. Python 3.8 Module Docs (32-bit);\n'
      '2. Имя ОС: Майкрософт Windows 10 Домашняя для одного языка\n'
      '   Версия: 10.0.18362 Сборка 18362\n'
      '   Тип: Компьютер на базе x64\n'
      '   Установленная оперативная память(RAM): 8,00 ГБ\n\n'
      'Измерения загрузки ОП скриптами:')


def change_max_min_loop():
    COUNT_ITEMS = 10
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]

    max_item_index = 0
    min_item_index = 0

    for n, i in enumerate(my_list):
        if my_list[max_item_index] < i:
            max_item_index = n
        elif my_list[min_item_index] > i:
            min_item_index = n

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]

    # Может и можно обойтись без этой строки в каждой функции, но пока не знаю как.
    values = list(locals().values())

    return values


print(f'Скрипт change_max_min_loop занимает: {object_iter(change_max_min_loop())} байт в ОП')


def change_max_min_python():
    COUNT_ITEMS = 10
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]

    max_item_index = my_list.index(max(my_list))
    min_item_index = my_list.index(min(my_list))

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]

    # Может и можно обойтись без этой строки в каждой функции, но пока не знаю как.
    values = list(locals().values())

    return values


print(f'Скрипт change_max_min_python занимает: {object_iter(change_max_min_python())} байт в ОП')


def change_max_min_broken_list():
    COUNT_ITEMS = 10
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = []
    while COUNT_ITEMS != 0:
        my_list.append(randint(START_ITEMS, STOP_ITEMS))
        COUNT_ITEMS -= 1

    max_item_index = 0
    min_item_index = 0

    for n, i in enumerate(my_list):
        if my_list[max_item_index] < i:
            max_item_index = n
        elif my_list[min_item_index] > i:
            min_item_index = n

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]

    # Может и можно обойтись без этой строки в каждой функции, но пока не знаю как.
    values = list(locals().values())

    return values


print(f'Скрипт change_max_min_broken_list занимает: {object_iter(change_max_min_broken_list())} байт в ОП\n')
print('Вывод:\nЕсли исходить только из имеющихся данных, то наиболее\n'
      'выгодно, относительно загрузки ОП, имспользовать скрипт\n'
      'change_max_min_loop, что видно из представленных данных.')
