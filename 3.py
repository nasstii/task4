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
print(A)
c=0
min=A[0]
delta=float(input('Введите значение дельта -- '))
for i in range(N):
    if A[i]<min:
        min=A[i]
for i in range(N):
    if A[i]-min==delta:
        c+=1
print('Количество элементов отличающихся от минимального элемента (',min,') равно ',c, sep=(''))