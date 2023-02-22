
# def main(stop, start=0, step=1):
#     return list(range(start, stop, step))
# print(main(10))


# def selery(salary, percent=12):
#     print(salary * percent)

# selery(15000)
# selery(salary=15000, percent=15)




# def main(*students):
#     return sum(students) / len(students)
# a = main(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# print(a)


# def avg(**kwargs):
#     for i in kwargs.values():
#         print(i)

# avg(name='Sultan', age=30, language='python')




# a = (1,1,3,5,7,9,0,7)

# def avg(*args):
#     print(args)

# avg(*a)


# def avg(**kwargs):
#     for i in kwargs.values():
#         print(i)


# data = {
#     'name':'Sultan', 
#     'age':30, 
#     "language":'python'
# }

# avg(**data)
# avg(name='Sultan', age=30, language='python')


# def my_function(*args, **kwargs): 
#     for a in args: 
#         print(a, end=". ") 
  
#     print() 
  
#     for key, value in kwargs.items(): 
#         print("%s = %s" % (key, value), end=' ') 


# data = {
#     'name':'Sultan', 
#     'age':30, 
#     "language":'python'
# }
# a = (1,1,3,5,7,9,0,7)

# my_function(*a, **data)


# def add_numbers(*args): 
#     total = 0
#     for a in args: 
#         total += a 
#     return total 

# a = (1,1,3,5,7,9,0,7)
# b = (1,1,3,5,7,9,0,7)

# print(add_numbers(*a, *b))


# def anyArgs(arg1=1, *vartuple, **kwargs): 
#     print("Output is:")  
#     print(arg1) 
#     for var in vartuple: 
#         print(var)  


# anyArgs(12,12,3)



# def calculate(**kwargs): 
#     if 'operation' in kwargs: 
#         operation = kwargs['operation'] 
#         if operation == 'add': 
#             if 'num1' and 'num2' in kwargs: 
#                 return kwargs['num1'] + kwargs['num2']

#             else: 
#                 return "Cannot perform Addition. Missing arguments!" 

#         elif operation == 'sub': 
#             if 'num1' and 'num2' in kwargs: 
#                 return kwargs['num1'] - kwargs['num2'] 

#             else : 
#                 return "Cannot perform Subtraction. Missing arguments!" 

#         else: 
#             return "Invalid input."

# print(calculate(operation='addasd'))

# Создайте 4 функции: add(), substract(), multiply(), divide() которые будут принимать по 2 аргумента и возвращать 
# результат: сложения, вычитания, умножения и деления.

# def add(*a):
#     try:
#         return a[0] + a[1]
#     except IndexError:
#         return "Not enough args"
# result = add(2)
# print(result)

# def sub(a, b):
#     return a -b
# result = sub(7, 9)
# print(result)

# def multiply(a, b):
#     return a * b
# result = multiply(7, 9)
# print(result)

# def divide(a, b):
#     return a / b
# result = divide(7, 9)
# print(result)

# Написать Функцию которая принимает предложение как аргумент, считает количество букв и возвращает сколько символов он ввёл. 
# НЕ ИСПОЛЬЗОВАТЬ функцию len()

# def length(a):
#     for a in l:
#     return count(args)

# l = length('dfsgbdfhgh')
# print(l)        



# a = 'htdeyrktfdjkfh'

# def new_func(a):
#     count = 0

#     for i in a:
#         count +=1
#     return count

# print(new_func(a))

# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.

# d1 = {'name':'zhak', 'age':36}
# d2 = {'name1':'Faks', 'age1':55}


# def dicts(d1, d2):
#     d = d1.copy()
#     for key, value in d2.items():
#         d[key] = value
#     return d   



# res = dicts(d1, d2)
# print(res)
# print(d1)
# print(d2)

# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить. А затем записывает это всё в файл на рабочем столе menu.txt

# import os


# def create_file(drinks, food):
#     os.system(f'touch menu.txt')
        
#     with open('menu.txt', 'a') as f:
#         f.write(f'napitok: {drinks}, eda: {food}\n') 
#     with open('menu.txt', 'r')as f:
#         print(f.read())

# drinks = 'Cola'
# food = 'pizza'       
# create_file(drinks, food)    

# Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории, где был запущен Ваш .py файл.
#import os
# def create_file_dir(name):
    
#     #os.system(f'touch {name}')

#     file = open(name, 'a')

# file_name = input()
# create_file_dir(file_name)

# Создайте 2 функции где одна функция вложена в другую. 
# Главная функция должна выводить на экран текст: "Я главная функция". А вложенная функция должна выводить на экран: "Я вложенная функция."
        

# def main():
#     print('Iam main')
#     def inserted():
#         print('Iam inserted')
#     inserted()
# main()    

# Создайте функцию которая принмает тип данных dictionary, но возвращает два Tuple в одном из них все ключи, в другом только значения.

# def converter(d: dict):
#     y = []
#     z = []
#     for key, value in d.items():        
#         y.append(key)        
#         z.append(value)
#     return tuple(y), tuple(z)

# d = {'name':'zhak', 'age':36,'name1':'Faks', 'age1':55}      
# res = converter(d)   
# print(*res)        

# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. Простое число - это число которое делится только на себя и на 1.

# def simple():
#     l=[]
#     for i in range(1,100):
#         k = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 k += 1
#         if k == 0:
#             l.append(i)

#     return l
# res = simple()
# print(res)


# Напишите функцию которая принимает 2 аргумента. 
# Эти аргументы могут быть любого типа данных но функция должна Вам вернуть эти аргументы как тип данных List.

# def converted(a, b):
#     return list(a) + list(b)

# a= 'sdsds'
# b = (1,5,6,6)
# res = converted(a, b)
# print(res)

# Напишите функцию которая спрашивает у пользователя число и выводит ему на экран именно столько строк самой себя как текст.
# def stroka(n):
#     return str(n)*n
# n = int(input())

# print(stroka(n))



# Создайте функцию которая принимает Имя пользователя и его зарплату и возвращает это строкой как: 
# ИМЯ - ЗАРПЛАТА. Если в функции не была указана зарплата - подставьте её сами. Значение по умолчанию - 5000.

# name = input("enter name: ")
# salary = int(input('enter salary: '))
# def name_salary(name, salary=5000):
#     return f'{name} - {salary}'
# res = name_salary(name, salary)
# print(res)    

# Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.

