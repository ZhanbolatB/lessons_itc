# s = [3, 4, 2, 4, 5, 5, 5, 4]
# s.append(66)
# s.append(True)
# s.append([123,123])
# print(s)



# s = [1569,2,3,4,5,5,5, 4, 5, 4, 5, 4, 5, 4, 5]
# s.append(True)
# s.remove(1569)
# s.pop(0)
# print(s)


# s1 = [1569,2,3,4, 4, 5, 4, 5, 4, 5, 4, 5]
# s2 = [15, 4, 5, 4, 5, 4, 5, 12]

# # s1.append(s2)

# # # s1 += s2
# s1.extend(s2)

# # s1.sort(reverse=True)

# print(s1)


# s1 = [1569,2,3,4, 4, 5, 4, 5, 4, 5, 4, 5]

# s1.reverse()
# print(s1)

# print(s1.count(4))

# a = (1, 2,'sdfkjhsdkjf',True,  4, 5, 5, 5, 5, 5, 5)


# print(a[2])
# b = []
# print(type(a))
# print(type(b))
# b = []
# b.extend(a)
# print(b)


# a = [1,2,3,3,4,5,7,8]

# print(a.index(7))

# a.reverse()

# print(a)
# print(a)
# print(a)

# print(a[3:6])
# print(a)

# s = []
# k = (1,2,3,4,5)
# k2 = (6,7,8,9,10)
# k3 = (11,12)
# k4 = (13,14)
# k5 = ('ermek', True)
# s.append(k)
# s.append(k2)
# s.append(k3)
# s.append(k4)
# s.append(k5)
# print(s)

# a = (1, "yes", True)
# print(a[0],a[1],a[2])

# a = []
# s = 'yes'
# i = 6
# f = 2.5
# b = True
# t = (1,2,3)
# a.extend(t)
# print(a)

# a = ['hello', 'asikkk', "yes", 'asik','q']
# b = '|'

# print(b.join(a))

# a = [1,2,3]
# b = [3,4,5]
# b.extend(a)
# print(b)

# list_1 = []
# list_2 = []
# n = int(input("enter 5 digits: "))
# if n % 2 == 0:
#     list_1.append(n)
# else:
#     list_2.append(n) 
# print(list_1,list_2)     


# a, b, c, d, e = int(input("a: ")),int(input('b: ')), int(input('c: ')),int(input('d: ')),int(input('e: '))
# list =[]
# list.extend([a,b,c,d,e])
# print(list)

# s = [123, 1,2,4]
# f = [123]
# g = [132125,545,45,88,70]

# d = []
# a = (*s,*f,*g) # *arg unpack list
# d.extend(a)
# print(d)

# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин'
# ]
# print(products)
# p =  str(input("enter product: "))
# if p in products:
#     products.remove(p)
# else:
#     print("not correct")    
# print(products)

# points = 0
# a1 = "good"
# a2 = 'almaty'
# a3 = '18'
# q1 = input('how r u?: ')
# q2 = input('where u from?: ')
# q3 = input('How old r u: ')
# if q1 == a1:
#     points = points +1
# if q2 == a2:
#     points = points+1
# if q3 == a3:
#     points = points+1


# print(points)

# abc = range(1,10+1,1)
# print(list(abc))
# entry = int(input("enter digit before 10: "))
# # abc = range (entry+1,10+1,1)
# print(list(abc))

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
