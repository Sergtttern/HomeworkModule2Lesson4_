"""
Модуль 2 Python Advanced, Урок №4. Контекстні менеджери та декоратори, Вправа 7

Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції протягом певного періоду часу.
Декоратор повинен приймати два параметри `max_calls` та `period`. Перший парметр - максимальна кількість допустимих
викликів функції. Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів. Вам
допоможе модуль `datetime` для вирішення цієї задачі.
"""

from datetime import datetime, timedelta
from time import sleep


def rate_limit(max_calls:int, period:int):
    """
    декоратор rate_limit, який обмежує кількість викликів декорованої функції протягом певного періоду часу.
    Декоратор приймає два параметри `max_calls` та `period`. Перший парметр - максимальна кількість допустимих
    викликів функції. Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів.
    """

    def decorator(func):

        start_of_countdown = datetime.now()
        time_interval = timedelta(seconds=period)
        calls_counter = 1
        cycle_counter = 1

        def inner(*args, **kwargs):
            nonlocal calls_counter
            nonlocal start_of_countdown
            nonlocal cycle_counter
            print(100 * '`')
            print("Inner block")
            start = datetime.now()
            print(100 * '`')
            sleep(2)

            if (start_of_countdown + time_interval > start) and (calls_counter <= max_calls):
                print(f"Знаходимося у часових межах. Це {calls_counter} виклик ф-ї. Цикл номер {cycle_counter} ")
                func(*args, **kwargs)
                calls_counter += 1
            elif calls_counter > max_calls:
                print(f"calls_counter= {calls_counter}")
                print(f"max_calls= {max_calls}")
                print(f"Перевищена допустима кількість викликів ф-ї ({max_calls}) протягом {period} секунд")
            elif start_of_countdown + time_interval < start:
                print("Знаходимося поза часовими межами")

            if start_of_countdown + time_interval < start:
                print(100 * '`')
                print(100 * '`')
                print(100 * '`')
                print(f"Розпочато новий відлік: надано {max_calls} викликів ф-ї протягом {period} секунд")
                start_of_countdown = datetime.now()
                calls_counter = 1
                cycle_counter +=1

        return inner

    return decorator


@rate_limit(5, 20)
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


digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)

digit_sum_in_number(100000)
