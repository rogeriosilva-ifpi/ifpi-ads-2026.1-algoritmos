def main():
 n = int(input('Digite um número inteiro positivo: '))
 divisores = 0 

 if n<=0:
  print('Numero Inválido')

 for i in range(1,n+1):
   if n % i == 0:
    print(i)
    divisores = divisores + 1
    
 print(f"total: {divisores} divisores")


def divisores(n):
  for i in range(n):
   if n % i == 0:
    print(i)
  return False
 

main()