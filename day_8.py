# Craete files.

# file = open('test.txt', 'w')
# text = "Hello world"
# file.write(text) 
# file.close()

# file = open('test.txt', 'a')
# s = '\n'
# for i in range(10):
#     s += str(i)
# file.write(s)
# file.close()

# ls > files.txt  -- write list  to Files.txt
# ls / --go to root directory
# ls / > files.txt --write list to files.txt
# ls >> append --list to files.txt

# file = open('files.txt', 'r')
# print(file.read())
# file = open('files.txt', 'r')
# text = file.read().split('\n')
# for i in text:
#     print(i)


# file = open('files.txt', 'r')
# text = file.read().split('\n')
# s = 0
# for i in text:
#     if i.startswith('day') and i.endswith('.py'):
#         s += 1
# print(s)       
#
# file = open('files.txt', 'r')
# text = file.read().split('\n')
# s = 0
# for i in text:
#     if i[0:3] =='day':
    
#         s += 1
# print(s)   

# file = open('files.txt', 'r')
# text = file.read().split('\n')
# s = 0
# for i in text:
#     if i.find('day') >=0:
    
#         s += 1
# print(s) 

# file = open('files.txt', 'r')
# text = file.read().split('\n')
# s = 0
# for i in text:
#     if 'day'in i:
#         s += 1
# print(s) 

# with open('file.txt', 'w') as d:
#     d.write('asd')

# with open('file.txt', 'r') as d:
#     text = d.read().splitlines()
#     for i in text:
#         print(i)    

# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
# В итоге у вас на рабочем столе должен появиться файл directories.txt. Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.
# from os import system as sys
# sys('ls / > directories.txt')
# file = open('directories.txt','r')
# text = file.read().split('\n')
# print(text)

# Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.
# file = open('users.txt', 'w')
# login = input('enter login: ')
# pswrd = input('enter password: ')
# text = file.write(f'login:{login}, pswrd:{pswrd}')

# a ="""
# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, 
# то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in."""
# with open("text_all.txt","w") as file:
#     file.write(a)


# with open("text_all.txt", "r") as file:
#     s = file.read()


#     for i in s:
#         if i == "w":
#               print('Да, в тексте есть w', i)
#               break
#         else:
#           print('Нет, в тексте нет w', i)    

# a = """"
# Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom:

# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит

# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,

# выведите на экран все полученные слова. Подсказка: используйте for."""

# with open('python.txt', 'w') as file:
#     file.write(a)
# t_words = []
# with open('python.txt','r') as file:
#     s = file.read().split()
#     print(s)
#     for i in s:
#         if 't' in i or 'T' in i:
#             t_words.append(i)
# print(t_words)            

# Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться. Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите авторизоваться спросив пароль. 
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

# with open('database.txt', 'a') as file:
#     file.write('parol, password, 123, 321\n')



# with open('database.txt', 'r') as file:
#     s = file.read().splitlines()
#     n = input('enter login: ')    
#     while True:
#         if n in s:
#             print("login is correct please enter password")
#             p = input('enter password: ')
#             p2 = input('enter password again: ')
#             if p == p2:
#                 with open('database.txt', 'a') as f:
#                     f.write(f'{p2=}')
#                     break
#         else:
#             n = input('enter login: ')

# while True:
#     a = input('1.рег  2.логин: ')
#     if a == '1':
#         n = input('enter login: ')
#         with open('database.txt', 'r') as file:
#             s = file.read()
#             if n in s:
#                 print('user is exist, please choose 2')
#                 continue
#             else:
#                 p = input('enter password: ')
#                 p2 = input('enter password again: ')
#                 if p == p2:
#                     with open('database.txt', 'a') as f:
#                         f.write(f'{n}, {p2}\n')
#                         print('success reg')
#                         continue
#     elif a == '2':
#         pass
# with open('city.txt', 'w') as file:
#     file.write('New York , Moscow , London , Almaty ')

n = input('1. Добавить новый город  2. Отобразить список городов 3. Заменить город 4. Удалить город 5. Выход: ')
if n =='1':
    c = input('Введите название города: ')

