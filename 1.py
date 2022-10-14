N=int(input('Введите желаемый размер массива - '))
A=[0]*N
a=int(input('Как Вы хотите ввести элементы массива? 1 - рандомные значения; 2 - заполнить массив самим (Введите 1 или 2) -- '))
from random import randint
if a==1:
    for i in range(N):
       A[i]=randint(-100,100)
if a==2:
    for i in range(N):
        print('Введите значение массива с индексом', i, '- ',end='')
        A[i]=float(input())
print('Входной массив:',A)
max=A[0]
for i in range(N):
    if (A[i]>=max) :
        max=A[i]
        i1=i
for i in range(N):
    if i>i1:
        A[i]=0
print('Результат:',A)

