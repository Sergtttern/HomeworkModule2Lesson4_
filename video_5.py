"""
Зараз будемо розглядати більш зручний, більш практичний спосіб застовування декораторів, більш
динамічне рішення

У попередньому уроці ми використовували декоратор для ф-й, які не приймають аргументів

Але як бути якщо ф-я яку ми будемо декорувати буде приймати якийсь аргумент
say_hi(name):
    print(f"Hello, {name}")
"""

# def decorator_1(func):
#
#     def inner():
#         print(10*'#')
#         func()
#         print(10 * '#')
#
#     return inner
#
# @decorator_1
# def say_hi(name):
#     print(f"Hello, {name}")
#
# say_hi()

"""
Помилка TypeError: say_hi() missing 1 required positional argument: 'name'
На цьому етапі помилка у внутрішній ф-ї func()
пропишемо func(name)
також відповідно слід прописати inner(name)

можливість переходу name з inner(name) в func(name) є через те що після декорування func() стає inner()
"""


def decorator_1(func):
    def inner(name):
        print(10 * '#')
        func(name)
        print(10 * '#')

    return inner


@decorator_1
def say_hi(name):
    print(f"Hello, {name}")


say_hi("Vlad")

"""
Ще такий приклад:
    def inner(name):
        print(10*'#')
        func(name)
        print(10 * '#')
Заберемо параметр name

    def inner():
        print(10*'#')
        func()
        print(10 * '#')

Але залишемо name в say_hi:
@decorator_1
def say_hi(name):
    print(f"Hello, {name}")


Викличемо:
say_hi("Vlad")

Ніби в say_hi(name) є аргумент і помилки не мало би бути, але насправді say_hi(name) це вже inner():, а
в inner() вже не має параметра name - тому буде помилка
 decorator_1.<locals>.inner() takes 0 positional arguments but 1 was given
"""

# def decorator_1(func):
#
#     def inner():
#         print(10*'#')
#         func()
#         print(10 * '#')
#
#     return inner
#
# @decorator_1
# def say_hi(name):
#     print(f"Hello, {name}")
#
# say_hi("Vlad")

""" 
Уявимо що у нас є 
def another_hi(a,b,c):
    return f'Hello, {a}, {b}, {c}'

Створили іншу ф-ю, яка приймає три різні аргументи, і хочемо задекорувати її за допомогою декоратора @decorator_1
Але виникає помилка decorator_1.<locals>.inner() takes 1 positional argument but 3 were given
Що робити?
Можна створити інший декоратор
Наприклад декоратор для трьох параметрів
Але потім будуть ф-ї з іншими кількостями параметрів
Як зробити так щоб можна було використовувати декоратор для ф-й з будь якою кількістю параметрів
"""

# def decorator_1(func):
#
#     def inner(name):
#         print(10*'#')
#         func(name)
#         print(10 * '#')
#
#     return inner
#
# @decorator_1
# def say_hi(name):
#     print(f"Hello, {name}")
#
# @decorator_1
# def another_hi(a, b, c):
#     return f'Hello, {a}, {b}, {c}'
#
# say_hi("Vlad")
# another_hi(1,2,3)

"""
Зробимо більш реальний приклад - декоратор, який буде рахувати час виконання ф-ї
Такий декоратор часто використовується для того щоб заміряти швидкість виконання ф-ї
Але якщо ми хочемо заміряти час усіх ф-й які у нас є і які мають різні параметри
використаємо *args, **kwargs
*args - приймає будь яку кількість параметрів
**kwargs - приймає будь яку кількість параметрів за імям(ключові параметри)
"""
# from time import time, sleep
# def decorator_1(func):
#
#     def inner(name):
#         print(10*'#')
#         start = time()
#         func(name)
#         end = time()
#         print(10 * '#')
#         print(f"Function time: {end - start}")
#
#     return inner
#
# @decorator_1
# def say_hi(name):
#     sleep(1)
#     print(f"Hello, {name}")
#
# @decorator_1
# def another_hi(a, b, c):
#     return f'Hello, {a}, {b}, {c}'
#
# say_hi("Vlad")
# another_hi(1,2,3)

"""
Щоб наша ф-я працювала нам слід передати параметри з *args, **kwargs 
"""
from time import time, sleep


def decorator_1(func):
    def inner(*args, **kwargs):
        print(10 * '#')
        start = time()
        func(*args, **kwargs)
        end = time()
        print(10 * '#')
        print(f"Function time: {end - start}")

    return inner


@decorator_1
def say_hi(name):
    sleep(1)
    print(f"Hello, {name}")


@decorator_1
def another_hi(a, b, c):
    return f'Hello, {a}, {b}, {c}'


say_hi("Vlad")
another_hi(a=1, b=2, c=3)

"""
Тепер можемо використовувати наш декоратор для ф-й з будь якою кількістю параметрів
Поки що для створення декораторів ми використали знання які вже мали
Декоратори практично завжди виглядають так як ми зробили - такий стандартний формат
Є ще один тип складнішого декоратора - розглянемо його у наступному відео
"""