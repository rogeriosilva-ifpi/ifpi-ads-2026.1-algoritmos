N = int(input("Valor de N: "))

for i in range(0, N + 1):
    N = i
    if N % 2 == 0:
        print(i)
