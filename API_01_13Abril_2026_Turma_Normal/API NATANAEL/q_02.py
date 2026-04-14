def main():
 n = int(input('valor de n:'))
 m = int(input('valor de m:'))
 soma = 0


 for i in range(n, m +1):
  if i % 2 != 0 and i % 3 == 0:
    soma = soma + i
    print(f'números: {i}')
    print(f'a soma dos divisores: {soma}')
   
main()