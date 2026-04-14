def intervalo():
    N=int(input('Digite o limite inferior: '))
    M=int(input('Digite o limite superior: '))


    somatorio=0

    print('NÚMEROS: ', end=' ')


    if M<N:
      M=int(input('Por favor, digite o número adequado: '))
    for i in range(N, M+1):
       if i%2!=0 and i%3==0:
          somatorio+=i
          print(i, end=' ')
        
         
    print(f'\nSOMA: {somatorio}') 

intervalo()