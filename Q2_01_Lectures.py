          # Файл для работы на лекциях.
import os
os.system('cls||clear')


          # Лекция 3

users = ['user1','user3','user3','user4','user5']
ids = [4,5,7,8,14]
years = [1970,1980,1990]

data = list(zip(users, ids, years))
print(data)
data2 = list(enumerate(users))
print(data2)

# List = [x for x in range(10)]
# Result = list(filter(lambda x: not x%2, List))
# print(Result)       # Выбор и печать четных элементов c помощью filter

# li = [x for x in range(1, 11)]
# li = list(map(lambda x: x+10, li))
# print(li)
'''          # Задание 1
Result = []
with open("Q2_01_L3_01.txt",'r') as f:
     ImportedNums = list(map(int,f.read().split(' ')))
print (ImportedNums)
Result = [(ImportedNums[i], ImportedNums[i]**2) for i in range(len(ImportedNums))\
          if ImportedNums[i]%2 == 0]
print (Result)
          # Задание (вариант 0)
Result = []
with open("Q2_01_L3_01.txt",'r') as f:
     SelectedNums = f.read().split(' ')
print (SelectedNums)
Result = [(int(SelectedNums[i]), int(SelectedNums[i])**2) for i in range(len(SelectedNums))\
          if int(SelectedNums[i])%2 == 0]
print (Result)
          # Задание (вариант преподавателя)
def select (f, col):
    return [f(x) for x in col]
def where (f,col): 
    return [ x for x in col if f(x)]    
Result = []
with open("Q2_01_L3_01.txt",'r') as f:
     ReadNums = f.read().split(' ')
res = select(int, ReadNums)   # конвертация в int
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print (res)
'''
'''          # Заполнение списков
list = []
for i in range (1, 11):
    list.append(i)
print(list)
list2 = [i for i in range(1, 11)]
print(list2)
          # Заполнение с условием
list3 = [i for i in range(1, 11) if i%2 == 0]
print(list3)
          # Заполнение кортежами
list4 = [(i, i) for i in range(1, 11) if i%2 == 0]
print(list4)
          # Заполнение с функцией
def f(x):
    return x**3
list5 = [(i, f(i)) for i in range(1, 11) if i%2 == 0]
print(list5)
'''
'''       # Подстановка lambda вместо функции
# def sum (x, y):
#     return x + y
# sum = lambda x, y: x + y + 1
def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a,b))
#     return op(a,b)
calc(lambda x, y: x + y + 1, 4, 5)
'''
'''       # Вызов функции как аргумента у другой функции
def f(x):
    return x**2
def calc(x):
    return x*10
def m(op, x):
    print(op(x))
m(calc, 10)
# print(calc(10))   
'''
