"""
Давайте подивимося на те як ми самостійно можемо створювати контекстні менеджери
Конструкція with - Це не контекстний менеджер - а конструкція яка працює із контекстним менеджером
з ф-ї open повертався обєкт конт менд з прикладу попереднього урока
"""

from contextlib import contextmanager

@contextmanager
def context_manager():
    # Before yield as the enter method
    print("Enter method called")
    yield

    # After yield as the exit method
    print("Exit method called")

with context_manager() as manager:
    print('with statement block')

"""
Є два способи робити контекстні менеджери.
Але перший спосіб - це погана практика.
В деякий кейсах необхідний 1 спосіб - але ці обидва способи потібно обовязково знати
Код вище створюється за допомогою генератора та декоратора

from contextlib import contextmanager - із бібліотеки contextlib ми імпортуємо декоратор contextmanager

декоратор contextmanager - створить для нас контекстний менеджер

далі всередні декоратора ми по факту створюємо прості ф-ї

але що відрізняє генератор від простої ф-ї - це те що замість return ми вказуємо yield

пишемо код
    # Before yield as the enter method
    print("Enter method called")
    
до yield
і пишемо код 
    # After yield as the exit method
    print("Exit method called")

після yield

Як буде відбуватися робота з цим контекстним менеджером - пишемо конструкцію with
 
with context_manager() as manager:

context_manager() - повертає контекстний менеджер, який зберігаємо у змінну manager

подивимося яким буде порядок виведення

Enter method called
with statement block
Exit method called
це найпростіший шаблонний вигляд як виглядає контекстний менеджер

дія яку контекстний менеджер виконає - відбутеться у будь якому випадку - і якщо буде помилка в коді, і 
якщо не буде помилки в коді

у наступному відео розглянемо як контекстний менеджер виглядає під коробкою
"""