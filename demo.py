# from typing import List, Tuple, Callable, Type, Any
# from functools import wraps


# def dec_args(handlers: List[Tuple[Type[Exception], Callable[[Exception], Any]]]):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 for exc_type, callback in handlers:
#                     if isinstance(e, exc_type):
#                         return callback(e)
#                 raise

#         return wrapper

#     return decorator


# def on_key_error(e: Exception):
#     print("Key Error was handled")


# def on_value_error(e: Exception):
#     print("Value Error was handled")


# @dec_args(
#     [
#         (KeyError, on_key_error),
#         (ValueError, on_value_error),
#     ]
# )
# def foo():
#     if 2 > 3:
#         print("Yes")
#     else:
#         raise ValueError("Key Error")


# foo()
# print(foo.__name__)


# class Stack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, el: int):
#         "Add element"

#         self.stack.append(el)

#         if not self.min_stack or el <= self.min_stack[-1]:
#             self.min_stack.append(el)

#     def pop(self):
#         "Get last added element and out him"

#         if self.stack:
#             pop_el = self.stack.pop()
#             if self.min_stack:
#                 if pop_el == self.min_stack[-1]:
#                     self.min_stack.pop()

#             return pop_el

#     def top(self):
#         "Get last added element"

#         return self.stack[-1] if self.stack else None

#     def get_min(self):
#         "Get min element from stack"

#         return self.min_stack[-1] if self.min_stack else None


# stack = Stack()
# stack.push(3)
# stack.push(2)
# stack.push(1)
# print(stack.get_min())
# stack.pop()
# print(stack.stack)
# print(stack.get_min())


# def add(a, b):
#     """
#     Возвращает сумму двух чисел.

#     Параметры:
#     a (int, float): Первое число.
#     b (int, float): Второе число.

#     Возвращает:
#     int, float: Сумма a и b.
#     """
#     return a + b


# print(add.__doc__)


# def other_closure_func(num):
#     num2 = 0

#     def multiplier(mlt_value):
#         nonlocal num2
#         num2 += 1
#         return mlt_value * num + num2

#     return multiplier


# foo1 = other_closure_func(5)
# print(foo1(2))
# print(foo1(2))
# print(foo1(2))

# a_re = 10
# a_im = 5

# a = complex(a_re, a_im)
# print(abs(a))
# abs_a = abs(a)
# print(a.conjugate())

# print("-----")

# x = 5
# y = 10


# def my_func(z):
#     a = 3
#     print("-----")
#     print(globals())  # выводит все глобальные переменные
#     print(locals())  # выводит все локальные переменные


# my_func(7)


# from memory_profiler import profile


# @profile
# def my_func():
#     a = []
#     a.append(1)
#     print(a)


# my_func()

# import objgraph

# my_list = [1, 2, 3]
# objgraph.show_refs([my_list], filename="my_list.png")

# a = [x for x in range(5)]
# iter_a = iter(a)
# print(next(iter_a))
# print(next(iter_a))

# num_uppercase = sum(1 for line in open("file.txt") for chr in line if chr.isupper())
# print(num_uppercase)


# def f(*args, **kwargs):
#     print(*args, kwargs)


# f(1, 2, 3, x=4, y=5)


# # Longest Polindrom
# class Solution:
#     def longest_palindrome(self, s: str) -> int:
#         chars = dict()
#         for ch in s:
#             chars[ch] = chars.get(ch, 0) + 1

#         length = 0
#         odd_found = False

#         for el in chars.values():
#             if el % 2 == 0:
#                 length += el
#             else:
#                 length += el - 1
#                 odd_found = True

#         if odd_found:
#             length += 1

#         return length


# s = Solution()
# result = s.longest_palindrome("abccccdd")
# print(result)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print("Hello, my name is", self.name)


# person1 = Person("Alice")
# person1.age = 25
# person1.__dict__["name"] = "Gogi"
# print(person1.__dict__)
# print(id(person1))

# import asyncio


# async def f():
#     await asyncio.sleep(1)
#     return 1


# async def main_f():
#     # r1 = await f()
#     # r2 = await f() + 1
#     t1 = asyncio.create_task(f())
#     t2 = asyncio.create_task(f())
#     await asyncio.sleep(1)
#     r1 = await t1
#     r2 = await t2 + 1
#     print(r1)
#     print(r2)


# asyncio.run(main_f())


# import threading
# import time


# # Определение функции, которая будет выполняться в потоке
# def print_numbers():
#     for i in range(5):
#         print(i)
#         time.sleep(1)


# # Создание потока
# thread = threading.Thread(target=print_numbers)

# # Запуск потока
# thread.start()

# # Ожидание завершения потока
# thread.join()

# # Проверка состояния потока
# if thread.is_alive():
#     print("Поток все еще выполняется")
# else:
#     print("Поток завершил выполнение")


# import multiprocessing


# def worker(num):
#     print("Worker:", num)


# if __name__ == "__main__":
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,))
#         p.start()


# import multiprocessing


# def square_sum(numbers):
#     return sum(x * x for x in numbers)


# if __name__ == "__main__":
#     numbers = range(1, 1000001)
#     pool = multiprocessing.Pool()
#     # разбиваем данные на чанки по 100 000 элементов
#     chunk_size = 100_000
#     chunks = [numbers[i : i + chunk_size] for i in range(0, len(numbers), chunk_size)]
#     # запускаем обработку чанков в разных процессах
#     results = pool.map(square_sum, chunks)
#     total = sum(results)
#     print(total)

# import time
# import numpy as np

# # Python list
# lst = list(range(10_000_000))
# start = time.time()
# lst_squared = [x * x for x in lst]
# print("List:", time.time() - start)

# # NumPy array
# arr = np.arange(10_000_000)
# start = time.time()
# arr_squared = arr * arr  # векторная операция
# print("NumPy:", time.time() - start)


# class Descriptor:
#     def __init__(self, default: int = 0):
#         self.default = default
#         self.name = None

#     def __set_name__(self, owner, name):
#         self.name = name  # сохраняем имя атрибута, например "value"

#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Value should be greater or equal to 0")
#         instance.__dict__[self.name] = value
#         print(instance.__dict__)
#         print(self.__dict__)

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.name, self.default)

#     def __delete__(self, instance):
#         print(f"{self.name} was deleted")
#         if self.name in instance.__dict__:
#             del instance.__dict__[self.name]


# class MyClass:

#     value = Descriptor()


# x = MyClass()
# y = MyClass()
# x.value = 11
# y.value = 88
# print(x.value)  # 10
# del x.value  # value was deleted
# print(x.value)  # 10 (default)


def process(input_string: str) -> str:

    m_zero = 0
    l_zero = 0
    eq_zero = 0

    input_lst = list(input_string.split(" "))
    print(input_lst)

    for num in input_lst:
        try:
            num = int(num)
            if num > 0:
                m_zero += 1
            if num < 0:
                l_zero += 1
            if num == 0:
                eq_zero += 1
        except:
            pass

    return f"выше нуля:{m_zero},ниже нуля:{l_zero},равна нулю:{eq_zero}"


input_string = input()
output_string = process(input_string)
print(output_string)
