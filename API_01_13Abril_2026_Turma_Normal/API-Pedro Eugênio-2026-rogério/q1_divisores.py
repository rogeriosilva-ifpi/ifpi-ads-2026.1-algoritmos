def divisores():
    count=0
    try:
     num=int(input('digite um número inteiro positivo: '))
    except:
      print('digite o valor adequado')

    print('divisores: ', end=' ')

    if num<0:
        num=int(input('por favor, digite um numero positivo: '))


    for i in range(1,num+1):
     if num%i==0:
      count+=1
      print(i, end=' ')
    
    print(f'\nTotal: {count} divisores')

    
divisores()

