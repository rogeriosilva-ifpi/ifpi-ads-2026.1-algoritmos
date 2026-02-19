def main():
  print('*** Sistema Dia/Noite ***')

  horas = int(input('Alexa, são que horas? '))

  eh_noite = verificar_se_eh_noite(horas)

  if eh_noite == True:
    print('É noite!')
  else:
    print('É dia de alegria!')


def verificar_se_eh_noite(h):
  if (h >= 18 and h <= 24) or (h >= 0 and h < 6):
    return True
  else:
    return False

# Executando a função chamada "main"
main()