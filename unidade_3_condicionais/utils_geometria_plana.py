def eh_triangulo(a, b, c):
  if c <= (a + b) and a <= (b + c) and b <= (a + c):
    return True
  else:
    return False
  

def obter_tipo_triangulo(a: int, b: int, c: int) -> str:
  if a == b and a == c and b == c:
    return 'Equilátero'
  elif a != b and b != c and a != c:
    return 'Escaleno'
  else:
    return 'Isósceles'
  

def obter_area_triangulo_by_heron(a: int, b: int, c: int):
  s = (a + b + c) / 2
  area = (s*(s-a) * (s-b) * (s-c))**0.5
  return area