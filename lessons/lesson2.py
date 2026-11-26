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