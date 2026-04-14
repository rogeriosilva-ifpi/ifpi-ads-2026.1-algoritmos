def senha():
    senha=int(input('digite sua senha: '))
    senha_extra=str(senha)
    while True:
      if len(senha_extra)<6:
       print(' a senha deve ter mais de 6 dígitos')
       senha=int(input('digite outra senha: '))
      elif senha[0]==senha[1] or senha[1]==senha[2] or senha[2]==senha[3] or senha[3]==senha[4] or senha[4]==senha[5]:
        print('a senha nãompode ter numeros repetidos um após o outro')
        senha=int(input('digite outra senha: '))
      elif senha[0]+senha[1]+senha[2]+senha[3]+senha[4]+senha[5]<20:
         print(' a soma dos algarismos deve ser maior que 20')
         senha=int(input('digite outra senha: '))
      elif senha[0]==0:
        print(' a senha não pode começar com o dígito 0')
        senha=int(input('digite outra senha: '))
      else:
        print('sua senha foi cadastrada')
        break
senha()


