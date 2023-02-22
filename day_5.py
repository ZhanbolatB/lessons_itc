# list, set, dict = changable
# int, float, bool, string, tuple = unchangebale

# a = set()
# a.add(10)
# a.add('yes')
# a.pop()
# print(a)


# a= [1,2,2,4,5,6,6,6,7,7]
# a= list(set(a))
# print(a)

# a1 = [1,4,2,6,7]
# a2 = [1,4,56,8]

# a1 = set(a1)
# a2 = set(a2)

# a3 = a1.difference(a2)
# a4 = a1.intersection(a2)

# print(a3, a4)


# int = 12.   
# float = 1.2 
# bool = True
# string = "True"

# Массивы
# tuple = ('asd')
# list = []
# set = {}
# dict = {}

# s = {1,1,2,2,2,2,45,6,77,7,7,7,7,1,1,1}
# print(s)

# list, set, dict = Изменяемые
# int, float, bool, string, tuple = Неизменяемые

# a = set()
# a.add(10)
# a.add('asd')
# a.add(1324)
# a.add(3)
# a.add(4234)
# a.add(53463)
# a.add(7)


# a.pop()
# a.pop()
# a.pop()

# print(a)

# s = a + b
# print(id(b))
# print(id(s))




# a1 = [1,4,2,5,6]
# a2 = [1,4,14,5]

# a1 = set(a1)
# a2 = set(a2)

# a3 = a1.difference(a2)
# a4 = a1.intersection(a2)


# print(a4)

# a = {1,3,8, 4}
# b = {23, 4, 1}

# # print(a)
# a.intersection_update(b)
# # b = a
# # print(b)
# # print(a)
# # print(a)
# print(a.intersection(b))
# print(a)

# print()
# len()
# input()
# int()


# Ничего == None


# a = len('kjdshfkjdshfkj')

# print(a)


# a = [1,1,1,1,1, 2, 3, 4, 5, 6, 7]

# b = a.count(1)
# s = a.append('asdasd')
# print(s)
# print(a)
# print(b)


# a = [1,6,44,87,3,5,6,8]

# print(sorted(a))
# print(a)
# a.sort()
# print(a)

# print(a)
# print(a)

# a = {12,56,6,7,8,9}

# a.remove(12312)
# a.clear()
# a.pop()
# a.discard(2134)

# print(a)

# a.pop()
# a.pop()

# print(a)


# a = ['Alex', 18]
# print(a[0], a[1])

# list, set, dict = Изменяемые
# int, float, bool, string, tuple = Неизменяемые

# a = {
#     'name': 'Alex',
#     'age': '12',
#     'name': 'asd'
#     }
# print(a)



# users = {
#     'asik': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'kirill': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
# }

# users = [
#     ['asik', ['a@gmail.com', 'asdads', '7790454545']],
#     ['kirill', ['a@gmail.com', 'asdads', '+7790454545']],
# ]


# print(users['asik'])

# print(users[1][1])





# users = {
#     'asik': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'kirill': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'erj': {''}
# }


# users.update({
#     'asdasd': 'asd'
# })

# users['kirill']['phone'] = '700000000000'

# print(users.keys())
# print(users)



# a = {
#     'Kirill': 18
# }

# a.update({
#     'erj': 19
# })

# a.update({
#     'asik': 231,
#     'qweqw':'qwe'
# })

# print(a.items())

#problem1
# dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)

#problem2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_1.intersection(farm_2)
# print(farm_3)

# problem3
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_2.difference(farm_1)
# print(farm_3)

# problem4
# s = {1,2,3,4,5}
# s.add(6)
# s.pop()
# print(s)

# problem5
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({
#     'beshbarmak': 130
# }

# )

# menu.update({'lagman':135})
# menu['plov'] = 500
# menu.pop('borsh')
# print(menu)

# problem6
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# # menu.update({'drinks': ['Coca-cola','Fanta','Sprite']})
# # menu['drinks']=['Coca-cola','Fanta','Sprite']
# print(menu)

# problem7
# s = {'add','update','intersection','remove','difference','clear','discard','pop','intersection_update'}
# d = {'clear','get','values','keys','items','update'}
# o = s.intersection(d)
# print(o)

# problem8
# d ={}
# n = (input('Enter name: '))
# n1 = (input('Enter name: '))
# n2 = (input('Enter name: '))
# n3= int(input('Enter password: '))
# n4= int(input('Enter password: '))
# n5= int(input('Enter password: '))
# d.update({n:n3})
# d.update({n1:n4})
# d.update({n2:n5})
# print(d)

# problem9
# d = [
#     {'name' : input('enter name'),
#     'prof':input('prof'),
#     },
    
#     {
#     'name': 'Zhan',
#     'prof':'doctor'
#     },
# ]

# print('Hello {}  nice job {}'.format(d[0]['name'], d[0]['prof']))
# print('Hello {}  nice job {}'.format(d[1]['name'], d[1]['prof']))
# print(f'Hello {d[1]["name"]}  nice job {d[1]["prof"]}')
# print(d)


# for name, prof in d.items():
#     print(f'Hello {name}  nice job {prof}')

# # Список № 2
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
#   'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries = set(south_american_countries)
# print(south_american_countries)

# problem10
# suitcase = []
# s = [1,2,3,4,5]
# suitcase.extend(s)
# suitcase.pop(-1)
# print(suitcase)
