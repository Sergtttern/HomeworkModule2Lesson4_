"""
Візьмемо фрагмент коду - поговоримо про нього
Цю тему обовязково слід повторювати - бо про це запитують на кожній співбесіді
Той код нашого декоратора, який ми створили раніше - ми помістили всередину іншої ф-ї декоратора

Ф-я decorator_maker повертає нам декоратор. Нічого не нагадує?
Декоратор - це фактично фабрика яка змінює нашу ф-ю
decorator_maker - це фабрика для декоратора

Ми зробили ф-ю яка робить певну логіку і повертає нам наш декоратор

Щоб це використати ми створюємо змінну:
my_decorator = decorator_maker()

Ми маємо ф-ю
def say_hi(name):
    print(f"Hello, {name}")

Цим рядком ми декоруємо нашу ф-ю:
say_hі = my_decorator(say_hі)
"""

def decorator_maker():

    def decorator(func):

        def inner(*args, **kwargs):
            print(10*'#')
            func(*args, **kwargs)
            print(10 * '#')

        return inner

    return decorator

my_decorator = decorator_maker()
print(my_decorator)

def say_hi(name):
    print(f"Hello, {name}")

say_hi = my_decorator(say_hi)

say_hi("Vlad")

"""
Навіщо ми так ускладнили код? Навіщо додали декоратор мейкер?
Спочатку спростимо трохи код за допомогою цукру
@my_decorator

Я спочатку написав @decorator_maker - і це видало помилку - потрібно буде зясувати чому так
"""
def decorator_maker():

    def decorator(func):

        def inner(*args, **kwargs):
            print(10*'#')
            func(*args, **kwargs)
            print(10 * '#')

        return inner

    return decorator

my_decorator = decorator_maker()
print(my_decorator)

@my_decorator
def say_hi(name):
    print(f"Hello, {name}")



say_hi("Vlad")

"""
тепер спростимо ще: замість конструкції 
my_decorator = decorator_maker()

@my_decorator
def say_hi(name):
    print(f"Hello, {name}")
    
    напишемо

decorator_maker

@decorator_maker
def say_hi(name):
    print(f"Hello, {name}")
    
Але цей код виводить помилку TypeError: decorator_maker() takes 0 positional arguments but 1 was given
"""
print(100*"*")
# def decorator_maker():
#
#     def decorator(func):
#
#         def inner(*args, **kwargs):
#             print(10*'#')
#             func(*args, **kwargs)
#             print(10 * '#')
#
#         return inner
#
#     return decorator
#
#
# @decorator_maker
# def say_hi(name):
#     print(f"Hello, {name}")
#
#
#
# say_hi("Vlad")

"""
Для того щоб працювало правильно - слід писати @decorator_maker з дужками:
@decorator_maker()
"""
def decorator_maker():

    def decorator(func):

        def inner(*args, **kwargs):
            print(10*'#')
            func(*args, **kwargs)
            print(10 * '#')

        return inner

    return decorator


@decorator_maker()
def say_hi(name):
    print(f"Hello, {name}")



say_hi("Vlad")

"""
@decorator_maker() викликаємо з дужками - він викликається і там вже декорує нашу ф-ю
Але як практичне використання цього на практиці? 
Яке питання я задаю на співбесіді?
Навіть стронг джуніорів
Часто всі використовують декоратори щоб додати функціонал
Питаю: Як ми можемо створити декоратор, який приймає якісь аргументи?
Якщо ми хочемо кастомізувати декоратор, та передати змінні за допомогою дужок?
Але ось так як ми написали вище - ми це можемо робити
Давайте створимо більш реальний приклад
"""

def repeat(num=3):

    def decorator(func):

        def inner(*args, **kwargs):
            for i in range(num):
                print(10*'#')
                print(f'i = {i} ')
                func(*args, **kwargs)
                print(10 * '#')

        return inner

    return decorator


@repeat(5)
def say_hi(name):
    print(f"Hello, {name}")



say_hi("Vlad")

"""
Тепер в конструкції 
@repeat(5)
def say_hi(name):
    print(f"Hello, {name}")
    
можемо писати кількість разів яку ми хочемо, щоб відбувся повтор

також тепер ми можемо дописувати нові ф-ї і використовувати
"""

def repeat(num=3):

    def decorator(func):

        def inner(*args, **kwargs):
            for i in range(num):
                print(10*'#')
                print(f'i = {i} ')
                func(*args, **kwargs)
                print(10 * '#')

        return inner

    return decorator


@repeat(5)
def say_hi(name):
    print(f"Hello, {name}")

@repeat(3)
def say_by(name):
    print(f"Bye, {name}")



say_hi("Vlad")
print(100*'`')
say_by("Vlad")

"""
Коли ми передаємо аргументи - то це крутіше, оскільки ми можемо декорувати різні ф-ї по різному
Наприклад одну повторювати 5 разів, а іншу 3 рази 
Як простіше це запамятати? Повторю концепцію декораторів, та повторю питання які питають на співбесіді:
Декоратор виглядає як ф-я всередині якої знаходиться інша ф-я 
Декоратор обовязково приймає ф-я як аргумент
Як створити декоратор який приймає якісь аргументи - ми просто передаємо додатковий рівень зверху, додаткову
ф-ю яка приймає якісь аргументи - далі в цьому випадку працює замикання - ми замикаємо значення із цієї 
зовнішньої ф-ї у середині цієї зовнішньої ф-ї - а що є всередині нашої зовнішньої ф-ї? - Там є наш декоратор.

Це по факту буде фабрика нашого декоратора - це буде ф-я створена лише для того щоб створити декоратор та повернути його
Тому використовуємо таку складну ієрархію
Декоратор з параметром - це три ф-ї: Зовнішня - декоратор - внутрішня.
Простий декоратор - це дві ф-ї: декоратор - внутрішня

Якщо декоратор з параметрами - то у дужках передаємо параметри

Стосовно декораторів: не сама проста тема - необхідна практика

Якщо якусь тему не докінця зрозуміли - йдіть далі, буде практика, стане ясніше
"""