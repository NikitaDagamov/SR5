from random import random
N = int(input("Введите размерность массива A:"))
R = int(input("Введите размерность массива В:"))
A = [0] * N
B = [0] * R
C = [0] * max(N, R)
for i in range(N):
    A[i] = round(random() * 10, 1)
print("Массив A:")
print(A)
for i in range(R):
    B[i] = round(random() * 10, 1)
print("Массив В:")
print(B)
L = 0
for i in range(len(A)):
    for v in range(len(B)):
        if A[i] == B[v]:
            C[L] = A[i]
            L += 1
print("Совпадающие элементы(ноль не является элементом, который совпал):")
for i in range(len(C)):
    print(C[L])
