"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 6

Реалізувати декоратор кешування memoize, який кешує результати декорованої функції для покращення
продуктивності при повторних викликах з тими самими аргументами. Тобто він повинен запамʼятовувати
аргументи з якими функція визивалась і результат роботи функції з цими аргументами. І у випадку,
якщо ми вже маємо результат для цих аргументів, просто повернути закешований результат, замість
виклику функції.
"""


def memoize(func):
    """
    декоратор кешування memoize, який кешує результати декорованої функції для покращення
    продуктивності при повторних викликах з тими самими аргументами. Він запамʼятовує
    аргументи з якими функція визивалась і результат роботи функції з цими аргументами. І у випадку,
    якщо ми вже маємо результат для цих аргументів, просто повертає закешований результат, замість
    виклику функції.
    """

    cashe = {}

    def inner(*args, **kwargs):
        print("Inner block")
        if args in cashe:
            print("Значення з кешу")
            print(f'Сума чисел від 1 до {args[0]} = {cashe[args]}')
            #print(cashe[args])
            print("\n")
            return cashe[args]
        result = func(*args, **kwargs)
        cashe[args] = result
        #for key, value in cashe.items():
            #print(key[0], value)
            #print("\n")

    return inner


@memoize
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


digit_sum_in_number(50)

digit_sum_in_number(70)

digit_sum_in_number(50)

digit_sum_in_number(70)
