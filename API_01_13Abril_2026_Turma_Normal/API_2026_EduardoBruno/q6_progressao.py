def main():
    a = int(input('1° termo: '))
    r = int(input('Razão: '))
    quant_termos = int(input('Termos: '))
    contador = 0
    soma = 0
    novo_valor = a
    if r >= 2:
        while quant_termos != 0:
            for i in range(a):
                novo_valor += r
                quant_termos -= 1
                contador +=1
                soma += novo_valor
                print(novo_valor,end='->')
                break
        print(f'\nSoma total: {soma}')
        print(f'Média: {soma / contador}')
        play_again = input('Deseja usar novamente?(S/N): ').strip().upper()
        while play_again != 'N':
            return main()
    
    else:
        print('A razão não pode ser menor que 2')
        return main()





main()