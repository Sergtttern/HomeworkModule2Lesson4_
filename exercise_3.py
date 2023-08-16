"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 3

Створіть простий декоратор логування log_func, який буде прінтити будь яке повідомлення перед визовом
декорованої функції, та після.
"""


def log_func(func):
    """
    декоратор логування log_func, який буде прінтити будь яке повідомлення перед визовом
    декорованої функції, та після.

    """
    def inner(*args, **kwargs):
        print('Цей рядок - це робота декоратора, який вказує номер уроку'
              'Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 3 start')
        func(*args, **kwargs)
        print('Цей рядок - це робота декоратора, який вказує номер уроку'
              'Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 3 start')

    return inner


@log_func
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


digit_sum_in_number(10)
