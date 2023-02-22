# a = []

# for _ in range(5):
    
#     n = int(input('>> '))
#     while n % 2 != 0:
#         print('enter even number')
#         n = int(input('>> '))
#     else:
        
#         a.append(n)
# print(a)        

# numbers = []
# n = int(input('>> '))
# while len(numbers) < 5:
#     if n % 2 ==0:
#         numbers.append(n)
#     n = int(input('>> '))
# print(numbers)

# a =[]
# while True:
#     if len(a) == 5:
#         break
#     n = int(input('enter number: '))
#     if n % 2 == 0:
#         a.append(n)
#     else:
#         print('enter even number')    
# print(a)        

# import time
# import os

# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             print(f"{h}:{m}:{s}")
#             time.sleep(0.00001)
#             os.system('clear')
# print(f"{h}:{m}:{s}")        

# for i in range(1,10,3):
#     for j in range(1,10):
        
#         print(f"{i} * {j} = {i * j} \t\
# {i+1}*{j} = {(i+1)*j} \t\
# {i+2}*{j} = {(i+2)*j}")

#     print()

# s=[]
# for i in range(100):
#     if i % 2 ==0 and i % 3 == 0:
#         s.append(i)
# print(s)


# print([i for i in range(100) if i % 2 ==0 and i % 3 == 0])
# print([i if i % 2 == 0 and i % 3 == 0 else 0 for i in range(100)])


# list comprehensions
# dict comprehensions

# s = ['Sultan', 'Asik', 'Mars', 'Sasha', 'ERJ', \
#      'Alibek', 'Kirill', 'Rustam', 'Janbolat', 'Vlad']

# # dict_users = {}
# # for key, value in enumerate(s):
# #     dict_users[key] = value
# # print(dict_users)  

# print({key: value for key, value in enumerate(s)})

# a,b = ('key', 'value')
# print(a)
# print(b)

# n = int(input())
 
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
 
# print(factorial)


# n = int(input('Введите целое число: '))
# for a in range(2,n + 1 ):
#     for i in range(2,a):
#         if (a%i==0):
#             break
#     else:
#             print(a)


# n = int(input('Введите n: '))
# for i in range(1, 11):
#     print(f'{n} * {i} = {n*i}')

# n = int(input())
# num = 1
# cnt = 1
# for i in range(n):
#     for j in range(cnt):
#         print(num, end = ' ')
#         num += 1
#     print()
#     cnt += 1

# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)

# n = int(input("Введите число:"))
# temp = n
# rev = 0
# while(n > 0):
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10
# if(temp == rev):
#     print("Это палиндром!")
# else:
#     print("Это не палиндром!")