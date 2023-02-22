# a = [1,2,3,4,5,6,7,8,9]
# for i in a:
#     print(i)
# sum = 0
# for i in a:
#     if i ==5:
#         print('break')
#         break
#     sum +=i
#     print(i)
# print(sum)  

# b = 0
# for i in range(1,100):
#     if i % 3==0 or i % 5== 0:
#         b += i
# print(b) 
  
# Find maximum value
# a = [5,6,8,7,8,9,2,1,5,5,74,14,5]

# max = a[0]

# for i in a:
#     if i >= max:
#         max =i
# print(max)  

# Skip Value (Continue)

# n = 0
# for i in range(10+1):
#     if i ==5:
#         continue
#     n += i
# print(n)    

# Dictionary
# a = {'key':'value','name':'Alex'}
# for i in a:
#     if i =='name':
#         print(a[i])
#     print(i, a[i])    

# While
# i = 0
# while i <10:
#     print(i, 'hello wrld')
#     i += 1

# PASSWORD
# password1 = input('Enter your password1: ')
# password2 = input('Enter your password2: ')

# i =0

# while password1 != password2:
#     i += 1
#     if i == 5:
#         print('Repeat after 10 min')
#         break
#     print("password ddint match repeat again")
#     print(f'You have {5-i} tries')
#     password1 = input('Enter your password1: ')
#     password2 = input('Enter your password2: ')
# else:
#     print('successful')    

# 1. Допустим у нас есть список языков программирования. lang1 = 'Rust'
#  languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#  Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
#  Если этого языка нет в списке, ничего не нужно выводить.

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# lang1  = 'Rust'
# for i in languages:
#     if i == lang1:
#         print('this languages is in list')
# else:
#     print('none')   

# 2. Будем работать с тем же списком: languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, цикл должен быть прерван.         

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
# #         break
#     print(i)

#  3. Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз. 

# n =7
# for i in range(10):
#     n = n*n
#     print(i)

# 4. Напишите код, который выведет на экран список языков с нумерацией.
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# Вывод:
#  0 go
#  1 java
#  2 php
#  3 python
#  4 javascript
#  5 ruby

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(len(languages)):
#     print(i, languages[i])


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     print(languages.index(i), i)

# 5. Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиление:
# Получите такой же результат но с ОДНИМ циклом

# for i in range(1,10+1):
    
#     print(i, end=',')

# for i in range(9,0,-1):
#     print(i, end=',')   

#  6. У вас есть список имён: 
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#   Если первое имя = 0, второе имя = 1 и т.д.
#  Выведите на экран всё имена которые лежат на чётных числах    

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names:
#     if names.index(i) % 2 ==0:
#         print(i)
# 7. У вас всё тот же список имён:
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#  Выведите каждое 2 имя.
#  Подсказка: Всего имён 13.        

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names:
#     if names.index(i) % 2 !=0:
#         print(i)

# 8. Есть переменная которая хранит в себе число:
#  Необходимо написать следующие условия для проверки переменной:
#     1. Это число трёхзначное?
#      2. Это число положительное и чётное?
#     3. Это число делится на 31 без остатка?
#    4. Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число        

# n = 100
# while True:
#     print(n)
#     if n>=100 and n<1000:
#         print('3digits')
#         if n % 2 == 0 and n > 0:
#             print('positive and even')
#             if n % 31 == 0:
#                 print('divisible by 31')                        
#                 if n > 100 :
#                     print("more 100 and div by 17")
#                     print(n)
#                     break
#                 else:
#                     print('less 100 and not div by 17')  
#             else:
#                 print('not divisble by 31')
#         else:
#             print('negative and odd')
#     else:
#         print('not 3 digits')

#     n+=1

# 9. Сгенерировать 200 чисел от -100 до 100:
#   1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
#   2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
#   3. Посчитать сколько чисел подходят под первое условие
#   4. Посчитать сколько чисел подходят под второе условие
# l=[]
# l2=[]
# for i in range(-100,100+1):
#     if i % 13 == 0:
#         i=i**2
#         l.append(i)
# print(l, len(l))
# for i in range(-100,100+1, 7):
#     if i % 2 != 0:
#         l2.append(i)

# print(l2, len(l2))