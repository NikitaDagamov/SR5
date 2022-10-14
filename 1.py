from random import random
F = int(input("Введите размер массива:"))
A = [0] * F
for i in range(F):
    A[i] = round(random() * 10, 1)
print("Исходный массив:", A)
M = max(A)
for i in range(F):
    if A[i] == M:
        for i in range(i + 1, F):
            A[i] = 0
print("Результат:", A)
