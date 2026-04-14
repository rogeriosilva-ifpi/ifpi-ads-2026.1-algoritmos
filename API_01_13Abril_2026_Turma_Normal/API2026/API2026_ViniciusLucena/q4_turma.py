def main():
    n = int(input("digite o número de alunos: "))

    maior, menor, media, ap, rec, rep = calcular(n)

    print("maior: ", maior)
    print("menor: ", menor)
    print("médio: ", media)
    print("aprovados: ", ap)
    print("recuperação: ", rec)
    print("reprovados: ", rep)


def calcular(n):
    soma = 0
    maior = -1
    menor =11
    ap = 0
    rec = 0
    rep = 0

    for i in range(n):
        nota = float(input("digite uma nota: "))

        soma+=nota

        if nota > maior:
            maior=nota

        if nota < menor:
            menor = nota

        if nota>=7:
            ap += 1
        elif nota >=5:
            rec += 1
        else:
            rep += 1

    media = soma/n

    return maior, menor, media, ap, rep








# não consegui fazer 100% :(#

main()