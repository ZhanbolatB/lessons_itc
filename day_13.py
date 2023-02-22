# #Functions

# a =[1,5,6,6,9,8,7,4]

# def length(a: list) -> int:
#     count = 0
#     for _ in a:
#         count +=1
#     return count  
# s = length(a)  
# print(s)
# print(length(a))
# print(len(a))

# def main(a, b):
#     return a+b
# print(main(12,23))

# s = main(a = 12, b = 39)
# print(s)

from random import choice
from string import ascii_letters, digits
import os
import time

# def generate_password(n: int)-> str:
#     return ''.join(choice(ascii_letters + digits) for _ in range(n))

# def loading():
#     for i in range(6):
#         os.system('clear')
#         print("Generating password" + '.' * i, i,'%')
#         time.sleep(0.5)
# loading()
# loading()
# loading()
# pas = generate_password(13)
# print(pas)

def validate_login(login: str) -> bool:
    for i in login:
        if i not in ascii_letters + digits:
            return False
    if not login.isdigit() and not login.isalpha():
        return True
    return False
# def validate_login(login: str) -> bool:
#     return True if not login.isdigit() and not login.isalpha() else False

# print(validate_login("gdghdf123ght"))
# print(validate_login("123"))


# def reverse(list1):
#     length = len(list1) //2
#     firsthalf = list1[:length][::-1]
#     secondhalf = list1[length:][::-1]
#     return  firsthalf + secondhalf 





# list1 = ['name', 'age', '1', '19']
# g = reverse(list1)
# print(g)


# def fibonacci():
#     a,b=0,1
#     fib_numbers =[]
#     for i in range(10):
#         fib_numbers.append(a)
#         a,b = b, a+b

#     return fib_numbers
        
# print(fibonacci())

# def add(a,b):
#     return a+b

# def  minus(a,b):
#     return a-b

# def main(a,b):
#     print(add(a,b))
#     print(minus(a,b))

# a = int(input('Enter: '))          
# b = int(input('Enter: '))  

# main(a,b)

# Спросите у пользователя имя файла. 
# Создайте функцию которая создаёт файл с именем которое передал пользователь. 
# Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную

# import os

# def create_file():
#     filename = input("enter file name: ")
#     os.system(f'touch {filename}.txt')
        
# Namefile = create_file
# Namefile()    

# Представьте Вы работаете в Мобильной Компании и вас попросили создать генератор номеров. 
# Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444 _ _ _ _ _ _. 
# Номера которые вы можете генерировать могут содержать в себе только числа 145790. Пример: 0444150971 0444111777 0444457901
# import random
# def gen_number():
    
#     begin = "0444"
#     digits = (random.choice('145790') for i in range(6))
#     number = begin + "".join(digits)
#     return number
# print(gen_number())

# 1.Напишите функцию, которая вычисляет квадрат числа.

# def kvadrat(s: int):
#     return s**2
# square = kvadrat()
# print(square)

# .Напишите функцию, которая возвращает массив из 10 рандомных целых чисел.

# import random

# def generate():
#     a=[]
#     for i in range(10):
#         a.append(random.randint(1,10))
#     return a
# randomnumbers = generate()
# print(randomnumbers)    

# 3.Напишите функцию, которая принимает строку и возвращает ее в обратном порядке.

# def reverse_list(s=[]):
#     return s[::-1]

# s = input('enter list: ')
# print(reverse_list(s))

# 4.Напишите функцию для подсчета суммы элементов массива.

# def sum_list(list1):
#     return sum(list1)
# list1 = [1,2,5]

# print(sum_list(list1))