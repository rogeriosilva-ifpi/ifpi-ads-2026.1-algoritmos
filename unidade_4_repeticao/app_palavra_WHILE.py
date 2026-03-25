def main():
  print('*** Palavra 7 ****')

  palavra = input('Digite uma palavra: ')

  while len(palavra) != 7:
    print(f'ERROU!!! A palavra {palavra} não tem 7 letras.')
    
    palavra = input('Digite outra palavra: ')
  
  print("ACERTOU!!!")


main()