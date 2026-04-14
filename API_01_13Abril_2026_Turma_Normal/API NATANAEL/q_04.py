def main():
 n1= int(input('Nota do Aluno: '))
 n2= int(input('Nota do Aluno: '))
 n3= int(input('Nota do Aluno: '))
 n4= int(input('Nota do Aluno: '))
 n5= int(input('Nota do Aluno: '))
 n6= int(input('Nota do Aluno: '))
 n7= int(input('Nota do Aluno: '))
 n8= int(input('Nota do Aluno: '))
 n9= int(input('Nota do Aluno: '))
 n10= int(input('Nota do Aluno: '))

 for i in range(0,10+1):
  if i >= 7:
   print("Aprovado")
  elif i >= 5 and i < 7:
   print('Recuperação')
  elif i < 5:
   print('Reprovado')
 
 media = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10) // 10
 print(media)

main()