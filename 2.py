NA=int(input('Введите желаемый размер массива A - '))
A=[0]*NA
NB=int(input('Введите желаемый размер массива B - '))
B=[0]*NB
a=int(input('Как Вы хотите ввести элементы массивов? 1 - рандомные значения; 2 - заполнить массив самим (Введите 1 или 2) -- '))
from random import randint
if a==1:
    for i in range(NA):
       A[i]=randint(-10,10)
    for i in range(NB):
       B[i]=randint(-10,10)
if a==2:
    for i in range(NA):
        print('Введите значение массива A с индексом', i, '- ',end='')
        A[i]=float(input())
    for i in range(NB):
        print('Введите значение массива B с индексом', i, '- ',end='')
        B[i]=float(input())
print('Входной массив A:',A)
print('Входной массив B:',B)
print('Одинаковые элементы массивов:',end=' ')
с=0
for i in range(NA):
    for j in range(NB):
        if A[i]==B[j]:
            print(A[i], end=' ')
            с=с+1
if с==0:
    print('не имеется')