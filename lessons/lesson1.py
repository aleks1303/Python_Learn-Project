 # решітка це коментар до кінця строки

'''
це блочний коментар
'''

"""
це також блочний коментар
"""

# kkkkkdjfjj
# dkdkddkk command + /

# print('Hello from python')
#
# print(12, 2, "text", "text2", sep='-')

# i = 3
# f = 1.3
# b = True
# s = "string"
# n = None
#
# print(type(i))
# print(type(s))
# print(type(f))
# print(type(b))
# print(type(n))
#
# print(int(f))
# r=e=10
# print(r,e)
# r=11+2+e+r
# print(r,e)
#
# a=1
# a+=1
# print(a)

#математика
# a=7
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #float
# print(a//b) #int
#
# print(a%b)
#
# print(a**b)   #степінь
# print(round(a/b)) # округлює до ближчого парного числа

# print(2525**254)

# nun=input('Enter nun: ')
# print(nun)

# все пусте це --- False і нуль(0)

# a=2
# b=4
#
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)
# print(a is b)
# print(a is not b)

# res=isinstance("test", str)
# res1=isinstance("test", int)
# res12=isinstance(22, int)
# print(res)
# print(res1)
# print(res12)

# a=5
# b=6
# if a<b:
#  print("no")
# elif a>b:
#  print("yes")
# else:
#  print("else")


# num=int(input("Enter a number: "))
# res = 'yes' if num>5 else 'no'
# print(res)



# ###########################################

# list

#############################################

# lists=[1,2,3,4,5,6]
# print(lists)
# print(lists[0])
# print(lists[-1])
# lists[1]=22
# print(lists)



# l=[1,2,3,4,5,6]
# l.append(5)
# print(l)
# l.insert(2,33)
# print(l)
#
# pop=l.pop(2)
# print(pop)
# print(l)

# print(l[1:4]) # зріз

# print(l[::-2]) # з кроком два



#########################################

# tuple - незмінний

##########################################

# my_tuple = (1, 2, 3)
# # print(my_tuple)
# # print(type(my_tuple))
# # print(my_tuple[0])
#
# #змінити
#
# l = list(my_tuple)
# print(l)
# l[1]=55
# print(l)
# print(my_tuple)


#########################################

# dictionary

##########################################

# dictionary = {
#     'name': "Max",
#     True: 2,
#     False: 3,
#     "age": 33
# }

# print(dictionary)
# print(dictionary["name"])
# print(dictionary.get("name1", "Some"))
#
# # dictionary.clear()
# # dictionary.copy()
#
# print(dictionary.items())
# print(dictionary.keys())
# print(dictionary.values())
# print(list(dictionary.values()))

# pop = dictionary.pop("age")
# print(pop)
# print(dictionary)
#
# deleteItem = dictionary.popitem()
#
# print(dictionary)

#додати
# dictionary = {
#     "name":"Van"
# }
# # dictionary['house']='100'
# # dictionary.setdefault('name','Peter') # не спрацює
#
# dictionary2 = {
#     "lastName":"Var"
# }
# # dictionary.update(dictionary2)
# dictionary|=dictionary2
#
# print(dictionary)
# print(dictionary2)


#########################################

# SET

##########################################

# прибрав дублі

# l = [1,2,2,3,3,4,5,]
#
# lis =list(set(l))
# print(lis)
#
# s = set()
#
# d = {}
# print(type(s))
# print(type(d))
# s.add(1)
# s.add(2)
# s.add(3)
# print(s)

# s = {6,7,8, 4, 1}
# s1 = {1,2,3,4,}
# #
# print(s.issuperset(s1))
# print(s.issubset(s1))
# print(s.isdisjoint(s1))
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.difference(s1))
# print(s.symmetric_difference(s1))
# print(s.update(s1))
#
# s.remove(1)
# print(s)


#########################################

# string

##########################################
#
# lin = {1,2,3,4,5,6,7,8,9}
# #довжина
# print(len(lin))
#
# name = "Max"
# age = 22
# weight = 70
#
# string = 'Hello my name is {name}. I am {age} and my wight is {weight} kg'.format(name=name, age=age, weight=weight)
# string1 = f'Hello my name is {name}. I am {age} and my wight is {weight} kg'
#
# print(string)
# print(string1)

# string = 'Hello my name is Max. I am 22 and my wight is 70 kg'
#
# print(['   sssss    '.strip()])
# print(['   sssss    '.lstrip()])
# print(['   sssss    '.rstrip()])
# print(['aaa   sssss    rrr'.strip("a r")])
#
# print(['Hello world'.split()])
# print(['Hello-world'.split('-')])

# l1 = ['hello', 'world', 'apple']
# print((' '.join(l1)))

# min(2,3,4,5)
# min([1,2,3,4,5])
#
# max([1,2,3,4,5])
# print(sorted([-1, 2, 3, 4, -5]))
# print(sorted([-1, 2, 3, 4, -5], reverse=True))
# sum([1,2,3,4,5])

#function
#
# def fun (name, *args, **kwargs):
#     print("Hello", name)
#     print(args)
#     print(kwargs)
# fun("Max", "Roma", 11, True, last="Kevin", age=20 )



# def func (a, b,c ):
#     print(a, b, c)
# l= [1,2,3]
# func(*l)
# func(1,2,3)


#########################################

#loops

#########################################

# i = 5
# while i > 0:
#     i-=1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('finish')


# for i in range(1,101, 5):
#     print(i)
# else:
#     print("finished")


# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
# }
# for k, v in d.items():
#     print(f'{k=}, {v=}')
#     print(k,v)


#-----------------------------------------
#----list comprehension
#---------------------------------------

# l1 = [1, 2, 3, 4, 5]
# l2 = [i for i in range(1,6)]
#
# print(l1)
# print(l2)

# l3 = [1,2,3,4,4,5,6,6,78,]

# res = [i for i in l3 if i % 2 == 0]
# res = [i*2 for i in l3]
# res = [i*2 for i in l3 if i % 2 == 0]
# res = [i*2 if i %2==0 else i for i in l3]
# print(res)

# l2 = [
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ]
# res = [i for j in l2 for i in j]
# res1 = [i for i in l2]
# print(res)
# print(res1)
#
# # повтор
#
# l =[]
#
# for j in l2:
#     for i in j:
#         l.append(i)
# print(l)
#python3 lessons/lesson1.py