from utils_io import escrever, obter_texto, obter_numero_real

def main():
  nome = obter_texto('Qual seu nome? ')
  altura = obter_numero_real('Qual sua Altura (m)? ')
  peso = obter_numero_real('Qual seu Peso (kg)? ')

  imc = calcular_imc(altura, peso)
  classificacao = classificar_imc(imc)

  escrever(f'{nome} seu IMC é {imc:.1f} ({classificacao})')
  


def calcular_imc(altura: float, peso: float):
  imc = peso / (altura*altura)
  return imc


def classificar_imc(imc: float):
  if imc < 18.5:
    return 'Abaixo do Peso Normal'
  elif imc < 25:
    return 'Peso Normal'
  elif imc < 30:
    return 'Sobrepeso'
  elif imc < 35:
    return 'Obesidade Grau I'
  elif imc < 40:
    return 'Obesidade Grau II'
  else:
    return 'Obesidade Grau III'


main()