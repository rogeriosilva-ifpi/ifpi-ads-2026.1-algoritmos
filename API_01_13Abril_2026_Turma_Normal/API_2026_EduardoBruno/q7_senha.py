
import random
def main():
    contador = 0
    num = ''
    while contador < 6:
        for pc in range(0,10):
            pc = random.randint(0,9)
            contador += 1
            num = str(pc) + num
            break
    print(f'Senha: {num}')







main()