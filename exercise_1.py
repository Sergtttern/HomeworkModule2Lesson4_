"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 1

Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду. Контекстний менеджер повинен
виводити час,що минув, при виході з контексту. Використовуйте контекстний менеджер для вимірювання часу
виконання певного фрагменту коду. Реалізувати контекстний менеджер потрібно 2 способами, за допомогою
декоратора contextmanager та за допомогою класу.
"""
from contextlib import contextmanager
from time import time


@contextmanager
def timer_decorator_variant():
    """
    менеджер контексту timer_decorator_variant, який вимірює час виконання блоку коду. Контекстний менеджер виводить
    час,що минув,при виході з контексту.Реалізований за допомогою декоратора contextmanager
    """

    # Before yield as the enter method
    print("Enter method called")
    start = time()
    #print("Start=", start)
    yield

    # After yield as the exit method
    end = time()
    #print("End=", end)
    print(f"Function time: {end - start}")
    print("Exit method called")

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

with timer_decorator_variant() as manager:
    print(100 * '`')
    print("Контекстний менеджер створений за допомогою декоратора contextmanager")
    print(100 * '`')
    digit_sum_in_number(100000000)
    print('with statement block')

print(100*'`')

######################### 2 спосіб #####################################################

class TimerContextManagerClassVariant:
    """
    менеджер контексту TimerContextManagerClassVariant, який вимірює час виконання блоку коду. Контекстний менеджер
    виводить час,що минув,при виході з контексту.Реалізований за допомогою класу
    """

    def __init__(self, func):
        self.func = func
        print('init method called')


    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method called')

print("Контекстний менеджер створений за допомогою класу")
print(100*'`')

def digit_sum_in_number_2(num_param:int):
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

with TimerContextManagerClassVariant(digit_sum_in_number_2) as manager:
    start = time()
    manager.func(100000000)
    end = time()
    print(f"Function time: {end - start}")
    print('with statement block')

print(100*'`')
