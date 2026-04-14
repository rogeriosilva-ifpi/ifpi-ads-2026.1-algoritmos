m = 30
n = 1

if n < 1:
     print("Erro! Digite o numero 1")
     if m > 30:
         print("Erro! Digite o numero 30")
for i in range( n, m, +2):
    if m // i == 0:
        print(i)