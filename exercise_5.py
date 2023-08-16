"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 5

Створіть декоратор retry який приймає першим аргументом число - кількість разів, яку потрібно буде повторити
виконання функції у разі викидання нею помилки. (приклад можно знайти у презентації)
"""


def retry(number_of_repetitions_param: int):
    """
    декоратор retry приймає першим аргументом число - кількість разів, яку потрібно буде повторити
    виконання функції у разі викидання нею помилки.
    """

    def decorator(func):

        def inner(*args, **kwargs):
            print("Inner start")
            attempt_counter = 1
            while attempt_counter <= number_of_repetitions_param:
                try:
                    print("Try inner")
                    func(1*args, **kwargs) # тут помилка
                    break
                except Exception as e:
                    print("This is exception")
                    print(e)
                    print(f"Спроба номер {attempt_counter}")
                    attempt_counter += 1

            print("Inner end")

        return inner

    return decorator


@retry(3)
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
