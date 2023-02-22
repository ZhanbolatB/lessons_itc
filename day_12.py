# in built modules in Python

# os, sys, random, time, datetime, string, math, 

# import os
# print(os.name)

# os.system("ls") "terminal runs"

# code = """
# import os

# os.system("ls / > data.txt")

# """

# with open("virus.py", "w") as file:
#     file.write(code)
# os.system('python3 virus.py')
# os.system('rm -rf virus.py')

# print(os.getcwd())

# import sys
# # print(sys.argv)

# argv = sys.argv
# if argv[1] == 'run':
#     print('hello')
# elif sys.argv[1] == 'test':
#     print('testing')

from random import choice, randint, randrange
from string import ascii_letters, digits

# print(randint(1, 100))
# print(randrange(1, 100 , 5))

# names = ['alw', 'asik', 'kkk']
# print(choice(names))

# names.remove(choice(names))
# print(names)

# print(choice(ascii_letters))

# ascii_letters += digits
# a = []

# for i in range(8):
#     b = choice(ascii_letters)
#     a.append(b)
# print(''.join(a))    

# ascii_letters += digits
# a = ''

# for i in range(8):
#     b = choice(ascii_letters)
#     a += b
# print(a)  

# print(''.join(choice(ascii_letters+digits) for _ in range(8)))

# import time
# import datetime
# from datetime import datetime, timedelta

# # s= datetime(year = 2002, month=3, day=31, hour=6)

# # today = datetime.today()
# # print(today -s)
# # print(today.year -s.year)

# # today = datetime.datetime.today()
# # print(today)
# # print(today.strftime('%b %d %H: %M:'))

# # a = '23-01-2023 12:34'.replace('-',' ').replace(':', ' ')
# # d,m,y,H,M = list(map(int, a.split()))
# # s = datetime(year=y, month=m, day=d, hour=H, minute=M)
# # today = datetime.today()

# # print(s)

# a = ['dfdfd','ewewewqew', 'wwwww', 'wddwdwkmkmllmlmo']
# s = list(map(len, a))
# d = [len(i) for i in a]

# print(s)