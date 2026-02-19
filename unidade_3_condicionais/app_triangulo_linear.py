
print('>>> App Triângulo <<<')

lado_1 = int(input('Lado 1: '))
lado_2 = int(input('Lado 2: '))
lado_3 = int(input('Lado 3: '))

eh_triangulo = ''

if lado_3 <= (lado_1 + lado_2) and lado_1 <= (lado_2 + lado_3) and lado_2 <= (lado_1 + lado_3):
  print('SIM. Os lados formam um triângulo.')
else:
  print('NÃO. Os lados não formam um triângulo.')

eh_triangulo = False

if eh_triangulo == True:
  print('SIM. Os lados formam um triângulo.')
  if lado_1 == lado_2 and lado_1 == lado_3 and lado_2 == lado_3:
    print(f'\t > E o tipo do triângulo é Equilátero')
  elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
    print(f'\t > E o tipo do triângulo é Escaleno')
  else:
    print(f'\t > E o tipo do triângulo é Isósceles')
else:
  print('NÃO. Os lados não formam um triângulo.')
