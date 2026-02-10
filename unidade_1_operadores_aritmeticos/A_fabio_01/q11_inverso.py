#entrada
numero = int(input('Insira um número de 3 dígitos: '))

#processo
primeiro_numero = numero // 100
segundo_numero = (numero % 100) // 10
terceiro_numero = (numero % 100) % 10
inverso = (terceiro_numero * 100) + (segundo_numero * 10) + primeiro_numero

#saída
print(f'O inverso do número {numero} é {inverso}')
      
