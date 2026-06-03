➜  python
Python 3.13.1 (main, Jan  8 2025, 12:52:48) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 








>>> 













>>> 
>>> carros = ['Corsa', 'Celta', 'Seal', 'X4', 'Virtus', 'Corsel'] 
>>> 













>>> carros
['Corsa', 'Celta', 'Seal', 'X4', 'Virtus', 'Corsel']
>>> for c in carros:
...     print(c)
...     
Corsa
Celta
Seal
X4
Virtus
Corsel
>>> 




>>> 
>>> sorted(carros)
['Celta', 'Corsa', 'Corsel', 'Seal', 'Virtus', 'X4']
>>> sorted(carros, reverse=True)
['X4', 'Virtus', 'Seal', 'Corsel', 'Corsa', 'Celta']
>>> sorted(carros, reverse=True, key=len)
['Virtus', 'Corsel', 'Corsa', 'Celta', 'Seal', 'X4']
>>> sorted(carros, key=len)
['X4', 'Seal', 'Corsa', 'Celta', 'Virtus', 'Corsel']
>>> 






>>> carro = ['FIAT', 'Argo', 87000, 2025, 2026, 'Branco']
>>> carro[1]
'Argo'
>>> carro[2]
87000
>>> 










>>> carro
['FIAT', 'Argo', 87000, 2025, 2026, 'Branco']
>>> carros = []
>>> carros.append(carro)
>>> 
>>> len(carros)
1
>>> carros[0][4]
2026
>>> carros
[['FIAT', 'Argo', 87000, 2025, 2026, 'Branco']]
>>> 




>>> carros
[['FIAT', 'Argo', 87000, 2025, 2026, 'Branco']]
>>> carro2 = ['HONDA', 'Fit', 7000, 2001, 2002, 'Preto']
>>> 
>>> len(carros)
1
>>> carros.append(carro2)
>>> 
>>> len(carros)
2
>>> carros
[['FIAT', 'Argo', 87000, 2025, 2026, 'Branco'], ['HONDA', 'Fit', 7000, 2001, 2002, 'Preto']]
>>> 


>>> carros
[['FIAT', 'Argo', 87000, 2025, 2026, 'Branco'], ['HONDA', 'Fit', 7000, 2001, 2002, 'Preto']]
>>> for carro in carros:
...     print(carro[0], carro[2])
...     
FIAT 87000
HONDA 7000
>>> 







>>> carro
['HONDA', 'Fit', 7000, 2001, 2002, 'Preto']
>>> carro[0]
'HONDA'
>>> carro[]
  File "<python-input-31>", line 1
    carro[]
          ^
SyntaxError: invalid syntax
>>> 






>>> nome
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    nome
NameError: name 'nome' is not defined. Did you mean: 'None'?
>>> 










>>> carro
['HONDA', 'Fit', 7000, 2001, 2002, 'Preto']
>>> carro[0]
'HONDA'
>>> carro['nome']
Traceback (most recent call last):
  File "<python-input-35>", line 1, in <module>
    carro['nome']
    ~~~~~^^^^^^^^
TypeError: list indices must be integers or slices, not str
>>> 





>>> carro = {'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_\
fabricacao': 2025, 'cor': 'Azul', 'preco': 288_000}
>>> 
>>> carro
{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000}
>>> 
>>> carro['nome']
'Seal'
>>> carro['preco']
288000
>>> 




>>> carro
{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000}
>>> carro['km'] = 1800
>>> carro
{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}
>>> 
>>> carros = []
>>> carros.append(carro)
>>> 





>>> len(carros)
1
>>> fiat_uno = {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_m\
odelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}
>>> 
>>> len(carros)
1
>>> carros.append(fiat_uno)
>>> len(carros)
2
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}]
>>> 
>>> carros.append({'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco',\
 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 210000})
>>> 
>>> 
>>> len(carros)
3
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 210000}]
>>> 


>>> 510000
510000
>>> carros[2]['preco'] = 510_000
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> 





>>> for carro in carros:
...     print(carro['fabricante'], carro['nome'], carro['preco'])
...     
BYD Seal 288000
FIAT Uno 6500
Volvo XC 60 510000
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> 


>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> 








>>> def filtrar_por_fabricante(carros, nome_fabricante):
...     cestinha = []
...     for carro in carros:
...         if carro['fabricante'] == nome_fabricante:
...             cestinha.append(carro)
...             
>>> def filtrar_por_fabricante(carros, nome_fabricante):
...     cestinha = []
...     for carro in carros:
...         if carro['fabricante'] == nome_fabricante:
...             cestinha.append(carro)
...     return cestinha
...     
>>> 


>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> r = filtrar_por_fabricante(carros, 'FIAT')
>>> r
[{'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}]
>>> r = filtrar_por_fabricante(carros, 'Toyota')
>>> r
[]
>>> 

>>> r = filtrar_por_fabricante(carros, 'BYD')
>>> r
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}]
>>> 











>>> numeros = [0, 6, -1, 10]
>>> sorted(numeros)
[-1, 0, 6, 10]
>>> sorted(numeros, reverse=True)
[10, 6, 0, -1]
>>> nomes = ['Joaquim', 'Jeremias', 'Paloma', 'João'] 
>>> sorted(nomes)
['Jeremias', 'Joaquim', 'João', 'Paloma']
>>> sorted(nomes, reverse=True)
['Paloma', 'João', 'Joaquim', 'Jeremias']
>>> sorted(nomes, key=len)
['João', 'Paloma', 'Joaquim', 'Jeremias']
>>> sorted(nomes, key=len, reverse=True)
['Jeremias', 'Joaquim', 'Paloma', 'João']
>>> def get_ultima_letra(nome):
...     return nome[-1]
...     
>>> sorted(nomes, key=get_ultima_letra, reverse=True)
['Jeremias', 'João', 'Joaquim', 'Paloma']
>>> sorted(nomes, key=get_ultima_letra)
['Paloma', 'Joaquim', 'João', 'Jeremias']
>>> sorted(nomes, key=lambda n:n[-1])
['Paloma', 'Joaquim', 'João', 'Jeremias']
>>> 
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> 



>>> sorted(carros)
Traceback (most recent call last):
  File "<python-input-88>", line 1, in <module>
    sorted(carros)
    ~~~~~~^^^^^^^^
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> carros
[{'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}, {'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}]
>>> 
>>> def get_ano_fab(c):
...     return c['ano_fabricacao']
...     
>>> sorted(carros, key=get_ano_fab)
[{'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}, {'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}]
>>> sorted(carros, key=lambda c:c['ano_fabricacao'])
[{'fabricante': 'FIAT', 'nome': 'Uno', 'cor': 'Prata', 'ano_modelo': 1997, 'ano_fabricacao': 1997, 'preco': 6500, 'km': 210000}, {'fabricante': 'Volvo', 'nome': 'XC 60', 'cor': 'Branco', 'ano_fabricacao': 2024, 'ano_modelo': 2025, 'km': 210, 'preco': 510000}, {'nome': 'Seal', 'fabricante': 'BYD', 'ano_modelo': 2026, 'ano_fabricacao': 2025, 'cor': 'Azul', 'preco': 288000, 'km': 1800}]
>>> 