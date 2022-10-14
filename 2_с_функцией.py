def array():
    N=int(input('Введите желаемый размер массива - '))
    A=[0]*N
    for i in range(N):
        A[i]=float(input())
    return A
def common():
    A = array()
    B = array()
    print('Первый массив: ',A)
    print('Второй массив: ',B)
    print('Одинаковые элементы массивов:', end=' ')
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i]==B[j]:
                print(A[i],end=' ')
    return ''
print(common())