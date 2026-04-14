def main():
 a = float(input('Primeiro termo: '))
 r = int(input('razão:'))
 n = int(input('numero termos:'))

 for i in range(a,n+1,r):
  print(i)


main()