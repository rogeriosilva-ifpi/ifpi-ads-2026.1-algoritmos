def main():
    nota1 = validar_valor_positivo("Digite a nota: ")
    nota2 = validar_valor_positivo("Digite a nota: ")
    nota3 = validar_valor_positivo("Digite a nota: ")
    nota4 = validar_valor_positivo("Digite a nota: ")
    nota5 = validar_valor_positivo("Digite a nota: ")
    nota6 = validar_valor_positivo("Digite a nota: ")
    nota7 = validar_valor_positivo("Digite a nota: ")
    nota8 = validar_valor_positivo("Digite a nota: ")
    nota9 = validar_valor_positivo("Digite a nota: ")
    nota10 = validar_valor_positivo("Digite a nota: ")

    for i in [nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10]:
       print(classificando_nota(i))


    print(maior_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10))
    print(menor_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10))
    print(media_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10))
    


def classificando_nota(nota):
   if nota >= 7:
      return "APROVADO"
   elif nota < 5:
      return "REPROVADO"
   elif nota >= 5 and nota < 7:
      "RECUPERAÇÃO"


def maior_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10):
   maior = nota1

   if nota2 > menor:
      maior = nota2

   if nota3 > menor:
      maior = nota3

   if nota4 > menor:
      maior = nota4

   if nota5 > menor:
      maior = nota5

   if nota6 > menor:
      maior = nota6

   if nota7 > menor:
      maior = nota7

   if nota8 > menor:
      maior = nota8

   if nota9 > menor:
      maior = nota9

   if nota10 > menor:
      maior = nota10

   return maior


def menor_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10):
   menor = nota1

   if nota2 < menor:
      menor = nota2

   if nota3 < menor:
      menor = nota3

   if nota4 < menor:
      menor = nota4

   if nota5 < menor:
      menor = nota5

   if nota6 < menor:
      menor = nota6

   if nota7 < menor:
      menor = nota7

   if nota8 < menor:
      menor = nota8

   if nota9 < menor:
      menor = nota9

   if nota10 < menor:
      menor = nota10

   return menor


def media_nota(nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10):
   soma = 0
   for i in [nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10]:
      soma = soma + i

   return  soma / 10


def validar_valor_positivo(instruções):
    valor = float(input(instruções))
    
    if valor < 0 and valor > 10:
        while valor < 0 and valor > 10:
            valor = float(input("Valor digitado não é valido. Digite um novo valor: "))
    else:
     return valor    


main()