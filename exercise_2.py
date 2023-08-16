"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 2

Створіть контекстний менеджер DividerContext, який буде прінтити символ, який ми до нього передамо як
розділитель для основного блоку коду до та після його виконання. Реалізувати контекстний менеджер потрібно
2 способами, за допомогою декоратора contextmanager та за допомогою класу.
(приклад можно знайти у презентації)
"""

######################### 1 спосіб #####################################################
from contextlib import contextmanager

print("\n1 спосіб: Контекстний менеджер створений за допомогою декоратора")
print(100*'`')


@contextmanager
def divider_context(symbol_param:str):
    """
    контекстний менеджер divider_context, який прінтить символ, який ми до нього передамо як
    розділитель для основного блоку коду до та після його виконання.
     """

    # Before yield as the enter method
    print("Enter method called")
    print(100 * f'{symbol_param}')
    yield

    # After yield as the exit method
    print(100 * f'{symbol_param}')
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


with divider_context("#") as manager:
    digit_sum_in_number(100)
    print('with statement block')

######################### 2 спосіб #####################################################

print("\n\n\n2 спосіб: Контекстний менеджер створений за допомогою класу")
print(100*'`')


class DividerContext:
    """
    контекстний менеджер divider_context, який прінтить символ, який ми до нього передамо як
    розділитель для основного блоку коду до та після його виконання.
    """

    def __init__(self, symbol_param:str, func):
        self.symbol_param = symbol_param
        self.func = func

    def __enter__(self):
        print(100 * f'{self.symbol_param}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(100 * f'{self.symbol_param}')


with DividerContext("@", digit_sum_in_number) as manager:
    manager.func(50)
