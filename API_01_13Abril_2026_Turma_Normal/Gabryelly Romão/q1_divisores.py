def main():
    while True:
        try:
            n = int(input('Digite um numero: '))
            divisor = n/2

            for i in range(0,101):
                if divisor % 2:
                    return divisor
        
        except:
            print('Digite um numero: ')

main()




