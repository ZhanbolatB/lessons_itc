# len()
# print()
# input()
# range()
# min()
# max()
# # (int(), str(), ...)
# type()
# id()
# sorted()
# reversed()
# exit()
# open()

# a = [1,2,4,5,6,7,8,8,8]

# a1 = [True if i % 2 == 0 else False if i == 1 else 'ok' for i in a]

# for i in a:
#     if i % 2 == 0:
#         a1.append(True)
#     elif i == 1:
#         a1.append(False)
#     else:
#         a1.append('ok')

# print(all(a1))

# a = [2,5,66,7,8,9,66,3,32,78, 78]

# print(min(a))
# print(max(a))


# while True: print(eval(input(">> ")))
# print(eval('[True if i % 2 == 0 else False  for i in [1,2,4,6,7]]'))


# print(abs(-8768))

# import math 

# print(round(math.pi, 50))
# print(round(123.335345345345, 145))

# a = 'iojfldksjljsdlfkslvxhcl'
# s = slice(1, 7, 2)
# print(a[1:7:2] + a[1:7:2] + a[1:7:2] + a[1:7:2])
# print(a[s] + a[s] + a[s])


# SyntaxError
# AttributeError 
# IndentationError
# ValueError
# KeyError
# IndexError
# ModuleNotFoundError


# sudo rm -rf /


# s = open('/etc/init', 'w')


# try:
#     print(4 / 3)
# except NameError:
#     print('Уля ла жа')

# except ZeroDivisionError:
#     print('На ноль не дели')
# else:
#     print('ok')
# finally:
#     print('ывдоладылваодлвао')



# from os import system

# try:
#     s = open('text.txt', 'r')
# except FileNotFoundError:
#     system('nano text.txt')

# finally:
#     s = open('text.txt', 'r')
#     print(s.read())



# while True:
#     action = input('>> ')
    
#     if action in '+-//%**':
#         num1 = input(': ')
#         num2 = input(': ')
#         if not num1.isdigit() or not num2.isdigit():
#             print('Invalid number')
#             continue
#         print(eval(f'{num1} {action} {num2}'))

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

# new = []

# for i in values:
#     try:
#         set().add(i)
#         new.append(True)
#     except TypeError:
#         new.append(False)

# print(new)



# new = set()
# for i in range(5):
#     number = int(input('enter 5 digits: '))
#     new.add(number)
# print(new)    
# print(min(new))   

# function = input("enter python function: ")

# try:
#     eval(function)
#     print(True)
# except Exception:
#     print(False)    
       

# loan = int(input('enter sum more than 50000: '))
# percent = 3.47
# credit = 0
# if loan >= 50000:
#         credit += loan * (percent/100)
# print(round(credit, 4))



# at = 10
# inr = 15
# wo = 20

# for e in range(-at, at):
#     try:
#         print(wo / e) 
#         if at > 5:
#             print("at > 5")
#     except (ZeroDivisionError, TypeError) as e:
#        print('i have error', e)


# Code #2:
# lst = []
# for i in range(10):
#     lst.append(i)

# a = list(reversed(lst))
# sls_obj = slice(0,8)
# print(a)
# print(a[sls_obj])


# Code #3:
# a = 5
# b = 10
# numbers = []
# while b > a:
#     numbers.append(b)
#     b -= 1
#     print(b)
# print(numbers)    

# Code #3:
# a = 0
# b = 1
# numbers = []
# if b > a:
#         numbers.append(b)
# print(numbers)    
# b += 1

# tuple = (123, 12, 23)
# n = 123
# try:
#      tuple.index(1)
#      tuple[123]
# except ValueError as e:
#      print(f"{n} not in tuple", e)
# except NameError:
#      print(f" not in tuple")
# else:
#      print(tuple.index(n))
# finally:
#      print("Finished")     