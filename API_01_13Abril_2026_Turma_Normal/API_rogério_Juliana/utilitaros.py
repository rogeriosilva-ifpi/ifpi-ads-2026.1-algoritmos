def inteiro(label):
    while True:
        try:
            numero = int(input(label))
            return numero
        except:
            print('esse numero não é inteiro, tente novamente')

def positivo(label):
    while True:
        try:
            numero = float(input(label))

            while numero < 0:
                print('esse numero não é positivo, tente novamente')
                numero = float(input(label))
            return numero
        
        except:
            print('esse numero não é inteiro, tente novamente')