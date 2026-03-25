def main():
  idade_dias = int(input())
  anos = idade_dias // 365
  meses = (idade_dias % 365) // 30
  dias = (idade_dias % 365) % 30
  
  print(f'{anos} ano(s)')
  print(f'{meses} mes(es)')
  print(f'{dias} dia(s)')

main()