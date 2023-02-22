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

# while True:
#     x =input()
#     w = ""
#     for i in x:
#         w = i + w
    
#     if (x == w):
#         print("Yes")
#     else:
#         print("No")

#  PROBLEM № 6
# Подтверждения пароля 
# спросите у пользователя логин и пароль и подтверждения пороля
# создайте условие где проверяется логин он должен состоять и из цифр и из букв. пример 'aktan2002' (используйте isdigit() и isaplha() для проверки)
# cоздайте условие где проверяется пароль он должен совпадать с подтверждением пароля
# если пройдет все проверки тогда сохраните в списке users. пример users = [('aktan2002', 'qwerty'),('ilim12', '12345')]

# login = input('enter login: ')
# users = []
# storedpassword = 'Zhake123'
# chk1 = login.isalpha()
# chk2 = login.isdigit()
# if login == '' or ' ' in login:
#     print('no empty logins with space allowed')
# elif not chk1 or not chk2:
#     print('good login')
#     pswrd = input('enter paswrd: ')
#     if pswrd == storedpassword:
#         users.append(login)
#         print(users, 'you are stored as new user')
#     else: 
#         print('incorrect pswrd')
# else: 
#     print('login must be alphnumeric')     

# 'Задание №3': 
#             1 Практика методов ключ значение
#             Написать скрипт который проходится по ключам и проверяет значения
#             a) Если значение делиться на 3, то записываем строку “Hi”
#             b) Если значение делиться на 5, то записываем строку “Bye”
#             ПРИМЕР:
#             Дано -> dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}
#             Результат -> a = Bye
#             b = Hi

# dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}

# a = 'Bye'
# b = 'Hi'   

# for i in dict1:
#     if dict1[i] % 3 ==0:
#         dict1[i] = b
#     elif dict1[i] % 5 ==0:
#         dict1[i] = a    
# print(dict1)

#  'Задание №4': """
#             Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, 
#             то получим 3, 5, 6 и 9. 
#             Сумма этих чисел равна 23 (3+5+6+9) = 23.
#             Найдите сумму всех чисел меньше 1000, кратных 3 или 5.""",
# sum = 0
# dividables = []
# for i in range (1000):
# #     if i % 3 == 0 or i % 5 == 0:
# #         sum += i
# #         dividables.append(i)
# # print(sum)        
# # print(dividables)

#     # 'Задание №6': 
#     #         Создайте input() который принимает от пользователя 
#     #         дату в формате: "2022-10-24 18:30" и возвращает dictionary 
#     #         разделённую по значениям даты:

#     #         date = {
#     #         "year": "2022",
#     #         "month": "10",
#     #         .....
# # date = {
# #     'year': '',
# #     'month':'',
# #     'day': '',
# #     'hour': '',
# #     'min': ''
# # }
# # e1=[]
# # e2=[]
# # entry = input('>>> дату в формате: "2022-10-24 18:30 ')
# # entry = entry.split()
# # print(entry)
# # e1 = entry[0]
# # e2 = entry[1]

# # e1 = e1.split('-')
# # e2 = e2.split(':')

# # print(e1, 'e1')
# # print(e2, 'e2')

# # date['year'] = e1[0]
# # date['month'] = e1[1]
# # date['day'] = e1[2]
# # date['hour'] = e2[0]
# # date['min'] = e2[1]

# # print(date)


# # y = input('Year: ')
# # m = input("Month: ")
# # d = input('Day: ')
# # h = input('Hour: ')
# # min = input('Min: ')
# # if len(y) == 4:
# #     date['year'] = y
# # if len(m) <=2:
# #     date['month'] = m  
# # if len(d) <= 2:
# #     date['Day'] = d
# # if len(h) <= 2:
# #     date['hour'] = h
# # if len(m) <=2:
# #     date['min'] = min              
# # print(date)    


# # Написать программу, которая запрашивает у пользователя строку и выводит на экран все символы, которые встречаются в ней более одного раза. 
# # Символы необходимо выводить в порядке их появления в строке.

# # Пример:
# # Введите строку: abracadabra
# # Повторяющиеся символы: ['a', 'r']

# # n = input('enter symbols: ')
# # l = []
# # for i in n:
# #     sd = n.count(i)
# #     if sd>1:
# #         l.append(i)
# # print(l) 
# # print(n.count(i))       

# # Задание №13:

# # Написать программу, которая запрашивает у пользователя список чисел и выводит на экран все уникальные числа из списка в порядке их появления.

# # Пример:
# # Введите список чисел через пробел: 1 2 3 4 2 3 5
# # Уникальные числа: [1, 4, 5]    

# # n = input()
# # n = n.split()
# # l = []

# # # for i in n:
# # #     c = n.count(i)
# # #     if c ==1:
# # #         l.append(i)
# # # print(l)    
# # print("Ноль в качестве знака операции"
# #       "\n завершит работу программы")
# # while True:
# #     s = input("Знак (+,-,*,/,//,%): ")
# #     if s == '0':
# #         break
# #     if s in ('+', '-', '*', '/','//','%'):
# #         x = float(input("x="))
# #         y = float(input("y="))
# #         if s == '+':
# #             print("x + y =",  (x+y))
# #         elif s == '-':
# #             print("x - y =",  (x-y))
# #         elif s == '*':
# #             print("x * y =", (x*y))
# #         elif s =="//":
# #             print("x // y =",(x//y))
# #         elif s == "%":
# #             print("x % y =", (x%y))
# #         elif s == '/':
# #             if y != 0:
# #                 print(f"{x}  {y} = {x/y}")
# #             else:
# #                 print("Деление на ноль!")
# #     else:
# #         print("Неверный знак операции!")

# # '''Задание №2':
# # 1. Зарегистрируйте пользователя запросив логин и пароль
# # 2. Добавьте полученные данные в список users = [ ]
# # 3. Попросите Пользователя Войти запросив пороль и логин 
# # 4. если данные есть в списке users выведите ДОБРО ПОЖАЛОВАТЬ 
# # 5. Если данные не окажутся или были введены неправильные данные выведите НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ'''

# dataBase = ['Adlet:Great', 'Data:12354']
# x = input('Login: ')
# y = input('Pass: ')
# a = 0
# z = x + ':' + y
# dataBase.append(z)
# x = input('Enter Login: ')
# y = input('Enter Pass: ')
# z = x + ':' + y
# for i in dataBase:
#     if i == z:
#         a += 1
#     else:
#         pass
# if a > 0:
#     print("Welcome")
# else:
#     print("Wrong login or password")

# '''Задание №3':
# 1 Практика методов ключ значение
# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”
# ПРИМЕР:
# Дано -> dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}
# Результат -> a = Bye
# b = Hi"""'''

# dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}
# a = 'Bye'
# b = 'Hi'   
# for i in dict1:
#     if dict1[i] % 3 ==0:
#         dict1[i] = b
#     elif dict1[i] % 5 ==0:
#         dict1[i] = a    
# print(dict1)

# """'Задание №4': 
# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, 
# то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""

sum = 0
dividables = []
for i in range (1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        dividables.append(i)
print(sum)        
print(dividables)


