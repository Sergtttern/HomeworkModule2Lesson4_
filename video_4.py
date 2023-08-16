"""
Поговоримо як ми ще можемо використовувати декоратори
Як можна використовувати декілька декораторів, 5,10
Простими словами:
Як ще можемо використати другий декоратор?

say_hi = decorator_1(say_hi) - тут в say_hi потрапляє ф-я inner, це просто ф-я - тому ми можемо викликати
say_hi()
Якщо say_hi() є ф-єю, то ми можемо передати її в другий декоратор
Давайте спробуємо

decorator_1(say_hi) в інтерпретаторі пайтон заміниться нв ф-ю inner

print(say_hi) видає <function decorator_1.<locals>.inner at 0x000001F71EE92320>
показує що лежить обєкт

say_hi = decorator_2(decorator_1(say_hi))
print(say_hi) тепер показує що <function decorator_2.<locals>.inner at 0x0000014E09D32440> - це  вже інший обєкт

"""

def decorator_1(func):

    def inner():
        print(10*'#')
        func()
        print(10 * '#')

    return inner


def decorator_2(func):
    def inner():
        print(10 * '-')
        func()
        print(10 * '-')

    return inner

def say_hi():
    print('MAIN CONTENT')


# say_hi = decorator_1(say_hi)
# say_hi()
print(100*'~')
print(say_hi)
print(100*'~')
say_hi = decorator_2(decorator_1(say_hi))
print(say_hi)
print(100*'~')
say_hi()

"""
тепер у самій середині наша оригінальна ф-я say_hi - біля неї функціонал декоратора 1, а ще зовніше функціонал 
декоратора 2 

Можна зробити за допомогою цукру:
@decorator_2
@decorator_1

Те що ближче до ф-ї - те буде декорувати перешим
"""

def decorator_2(func):
    def inner():
        print(10 * '-')
        func()
        print(10 * '-')

    return inner

@decorator_2
@decorator_1
def say_hi():
    print('MAIN CONTENT')


print(100*"!")
say_hi()

""" 
Можна зробити декілька вкладених декораторів
На практиці не варто робити більше 5 декораторів
Порядок декораторів важливий
Ф-ю можна декорувати декількома декораторами
"""