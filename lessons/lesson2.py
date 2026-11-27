#

#_____Деструктурізація________________________

# tuple1 =(1,2)
# a,b = tuple1
# print(a)
# print(b)
#
# a = 4
# print(a)
#
# a =4
# b = 1
#
# a,b = b,a
# print(a)
# print(b)


# l= [1,2,3,4,5,6,7,8,9]
#
# _,b,*_,x,y,z,some = l
# print(b)
# print(_)
# print(x)
# print(z)
# print(some)
# print(y)


#______Розпаковка________________-

# args = [1,2,3]
#
# args_dict = {
#     'arg1':4,
#     'arg2':5,
#     'arg3':6,
# }
# def func(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
#

# func(*args_dict) #ключи
# func(**args_dict) # ключ_значення
# func(*args)



#__________Декоратор_____________________

# def decor1 (func):
#     def inner (*args, **kwargs):
#        print("++++++++++++++++++++++++++++++")
#        func(*args, **kwargs)
#        print("++++++++++++++++++++++++++++++")
#     return inner
#
# @decor1
# def greeting (name):
#     print(f'Hello {name}')
# greeting("Olha")


#__________Scope______глобальні та локальні змінні__________________

#----globals scope____

# def square(num):
#     ...
# def square1(num):
#     pass
#
# name = 'Alex'
#
# for i in range(5):
#     print(i)
#
# print(i)
#
# print(globals())


#___local_scope_______

# name = "Alex"
#
# def a ():
#     name = "Something"
#     print(locals())
#
# print(globals())
# a()


#
# name = "Max"
#
# def a ():
#     # global name
#     # nonlocal name
#     name = "Alex"
#     def b ():
#         # global name
#         nonlocal name
#         name = "Bob"
#         print (name)
#     b()
#     print (name)
#
# a()
# print (name)


#____counter_на замикання

# def counter():
#     count = 0
#     def inner():
#       nonlocal count
#       count += 1
#       return count
#     return inner
#
# counter1 = counter()
# counter2 = counter()
#
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter2())


#______lambda_________________

# func = lambda a,b: a+b
# print(func(2,3))

# l = [2,3,5,5,4,44,55,66,]
#
# m = map(lambda item: item*2, l)
# f = filter(lambda item: item%2==0, l)
# # print(m)
# # for i in m:
# #     print(i)
# for i in f:
#     print(i)

#
# users = [
#     { "name": "Alex","age": 4 },
#     { "name": "Max","age": 55 },
#     { "name": "Olha","age": 33 },
#     { "name": "Bob","age": 22 }
# ]
#
# users.sort(key=lambda x: x["age"])
# users.sort(key=lambda x: len(x["name"]))
# print(users)



#______анотація_типів__________________


# def types (name: str) -> str:
#     return name.upper()
#
# print (types('Vasia'))
#
# def types1 (name: list[str]) -> str:
#     return name[2].upper()
#
# print (types1('Vasia'))


# from typing import Any, TypedDict, Callable

# a: int = 7
#
# print(a)


# def func() -> Any:
#     return ['dkdkd']
#
#
# def func2() -> str|int|bool:
#     return ['dkdkd'] # помилка
#
#
# my_type = str|int|bool
# def func3() -> my_type:
#     return ['dkdkd'] # помилка
#
#
# def func4() -> None:
#         return

#______________TypedDisc______

# User = TypedDict('User', {'name': str, 'age': int, 'house': int})
#
# users: list[User] = [
#     {'name': 'Max', 'age': 45, 'house': 44},
#     {'name': 'Alex', 'age': 5, 'house': 57},
#     {'name': 'Mary', 'age': 12, 'house': 40},
#     {'name': 'Sonia', 'age': 23, 'house': 103},
# ]
#
# def counter(a: int, b: int) -> Callable[[bool, list[str]], int]:
#     count = 0
#     def inner(c: bool, d: list[str]) -> int:
#       nonlocal count
#       count += 1
#       return count
#     return inner
#
# counter1 = counter(1,3)
# counter2 = counter(3,4)
#
# print(counter1(True, ['Max', 'Alex']))
# print(counter2(True, ['Max', 'Alex']))



#_______________HOMEWORK____________________--


#
#BE. Python core. task 2
# 1) написати функцію (notebook) на замикання, котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
#
# – перший записує в список нову справу
#
# – другий повертає всі записи
#
# (приклад сигнатури функції notebook у вкладенні )
#
# def notebook():
#     todo_list: list[str] = []
#     def add_todo (to_do: str) -> None:
#         nonlocal todo_list
#         todo_list.append(to_do)
#
#     def show_todos() -> list[str]:
#         nonlocal todo_list
#         return todo_list.copy()
#
#     return add_todo, show_todos

# add1, get_all1 = notebook()
# add2, get_all2 = notebook()
#
# add1('buy something')
# add1('buy apple')
# add1('buy a car')
# add2('buy a car')
# add2('buy a notebook')
# add2('buy a bottle')
#
# print(get_all1())
# print('-----------------------------')
# print(get_all2())


# 2) протипізувати перше завдання
#
#
#
#
#
# 3) створити функцію, котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)
# Приклад:
# expanded_form(12) # return ’10 + 2′
# expanded_form(42) # return ’40 + 2′
# expanded_form(70304) # return ‘70000 + 300 + 4’
#
#
# def expanded_form( num:str)-> str:
#     st = str(num)
#     length = len(st) - 1
#     res = []
#     for i, char in enumerate(st):
#         if char != '0':
#             res.append(char + '0' * (length - i))
#     return ' '.join(res) + f' = {st}'
#
#
# print(expanded_form('2034305'))
#
#
#
#
# 4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, та буде виводити це значення після виконання функцій
#
# def count_decor (func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         func(*args, **kwargs)
#         print(f'{count =}')
#     return inner
#
# @count_decor
# def func1 ():
#     print('func1')
# @count_decor
# def func2 ():
#     print('func2')
#
#
# func1()
# func1()
# func1()
# func2()
# func2()
# func2()
# приклад декоратору у вкладенні











