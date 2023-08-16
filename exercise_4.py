"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 4

Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його. Для отримання часу
роботи скористуйтесь модулем time і функцією time.time()
"""

from time import time


def timeit(func):
    """
    декоратор timeit, який вимірює час виконання декорованої функції і виводить його.
    """

    def inner(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"Function time: {end - start}")

    return inner


@timeit
def digit_sum_in_number(num_param:int):
    """
    Рахує суму чисел від 1 до числа num_param
    :param num:
    :return: int
    """
    #sleep(1)
    sum_aggregator = 0
    for i in range(num_param):
        sum_aggregator = sum_aggregator + i

    print(f'Сума чисел від 1 до {num_param} = {sum_aggregator}')
    return sum_aggregator


digit_sum_in_number(10000000)
