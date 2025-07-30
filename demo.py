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
