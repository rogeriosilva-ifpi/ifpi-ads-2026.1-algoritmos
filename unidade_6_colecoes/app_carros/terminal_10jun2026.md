Python 3.13.1 (main, Jan  8 2025, 12:52:48) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> carros = []
>>> len(carros)
0
>>> c1 = {'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabr\
icante_id': None}
>>> 
>>> c1
{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': None}
>>> 



>>> carros.append(c1)
>>> len(carros)
1
>>> 
>>> fabricantes = []
>>> 
>>> fabricantes = list()
>>> 
>>> fabricantes.append({'id': 1, 'nome': 'GEELY', 'pais': 'China'})
>>> 
>>> len(fabricantes)
1
>>> carros[0]
{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': None}
>>> carros
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': None}]
>>> 
>>> carros[0]
{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': None}
>>> carros[0]['fabricante_id'] = 1
>>> 
>>> carros
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}]
>>> 
>>> carros.append({'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 20\
25, 'fabricante_id': 1})
>>> 
>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China'}]
>>> fabricantes.append({'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'})
>>> 


>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China'}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'}]
>>> 
>>> carros
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}, {'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}]
>>> 
>>> r = {'id': 3, 'nome': 'EX 30', 'valor': 230900, 'ano_fabricacao': 2024, 'fabr\
icante_id': 2}
>>> 
>>> len(carros)
2
>>> carros.append(r)
>>> 


>>> len(carros)
3
>>> len(fabricantes)
2
>>> for carro in carros:
...     print('>', carro['fabricante_id'], carro['nome'], carro['valor'])
...     
> 1 EX 2 126000
> 1 EX 5 200900
> 2 EX 30 230900
>>> 
>>> def obter_montadora_por_carro(lista_montadoras, carro):
...     for m in lista_montadoras 
...     




>>> def obter_montadora_por_carro(lista_montadoras, carro):
...     for m in lista_montadoras:
...         if carro['fabricante_id'] == m['id']:
...             return m
...     return None
...     
>>> for carro in carros:
...     print('>', carro['fabricante_id'], carro['nome'], carro['valor'])
...     
> 1 EX 2 126000
> 1 EX 5 200900
> 2 EX 30 230900
>>> for carro in carros:
...     fabricante
...     print('>', carro['fabricante_id'], carro['nome'], carro['valor'])
KeyboardInterrupt
>>> 

>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China'}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'}]
>>> def obter_fabricante_por_carro(lista_fabricantes, carro):
...     for m in lista_fabricantes:
...         if carro['fabricante_id'] == m['id']:
...             return m
...     return None
...     
>>> obter_fabricante_por_carro(fabricantes, carros[1])
{'id': 1, 'nome': 'GEELY', 'pais': 'China'}
>>> obter_fabricante_por_carro(fabricantes, carros[0])
{'id': 1, 'nome': 'GEELY', 'pais': 'China'}
>>> obter_fabricante_por_carro(fabricantes, carros[2])
{'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'}
>>> obter_fabricante_por_carro(fabricantes, carros[2])


>>> obter_fabricante_por_carro(fabricantes, carros[0])
KeyboardInterrupt
>>> fabricantes
KeyboardInterrupt
>>> 
>>> 
>>> for carro in carros:
...     fabricante = obter_fabricante_por_carro(fabricantes, carro)
...     print('>', fabricante['nome'], carro['nome'], carro['valor'])
...     
> GEELY EX 2 126000
> GEELY EX 5 200900
> VOLVO EX 30 230900
>>> 




>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China'}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'}]
>>> fabricantes.append('id': 2, 'nome': 'FIAT', 'pais': 'ITÁLIA')
  File "<python-input-50>", line 1
    fabricantes.append('id': 2, 'nome': 'FIAT', 'pais': 'ITÁLIA')
                           ^
SyntaxError: invalid syntax
>>> 
>>> fabricantes.append({'id': 3, 'nome': 'FIAT', 'pais': 'ITÁLIA'})
>>> 
>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China'}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia'}, {'id': 3, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 



>>> 
>>> 
>>> for fabricante in fabricantes:
...     print(fabricante['nome'])
...     
GEELY
VOLVO
FIAT
>>> for fabricante in fabricantes:
...     print(fabricante['nome'], f'Carros: 3')
...     
GEELY Carros: 3
VOLVO Carros: 3
FIAT Carros: 3
>>> 



>>> def map_fabricante_com_qtd_carros(lista_fabricantes, lista_carros):
...     lista_mapeada = []
...     for fabricante in lista_fabricantes:
...         qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
...         fabricante['qtd_carros'] = qtd_carros
...         lista_mapeada.append(fabricante)
...     return lista_mapeada
...     
>>> map_fabricante_com_qtd_carros(fabricantes, carros)
Traceback (most recent call last):
  File "<python-input-60>", line 1, in <module>
    map_fabricante_com_qtd_carros(fabricantes, carros)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "<python-input-59>", line 4, in map_fabricante_com_qtd_carros
    qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'contar_carros_por_fabricante' is not defined
>>> 
>>> def contar_carros_por_fabricante(fabricante, lista_carros):
...     contador = 0
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante['id']:
...             contador = contador + 1
...             
>>> def contar_carros_por_fabricante(fabricante, lista_carros):
...     contador = 0
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante['id']:
...             contador = contador + 1
...     return contador
...     
>>> def contar_carros_por_fabricante(fabricante, lista_carros):
...     contador = 0
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante['id']:
...             contador = contador + 1
...     return contador
KeyboardInterrupt
>>> 
>>> def contar_carros_por_fabricante(lista_carros, fabricante):
...     contador = 0
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante['id']:
...             contador = contador + 1
...     return contador
...     
>>> map_fabricante_com_qtd_carros(carros, fabricantes[0])
Traceback (most recent call last):
  File "<python-input-64>", line 1, in <module>
    map_fabricante_com_qtd_carros(carros, fabricantes[0])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "<python-input-59>", line 4, in map_fabricante_com_qtd_carros
    qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
  File "<python-input-63>", line 4, in contar_carros_por_fabricante
    if carro['fabricante_id'] == fabricante['id']:
       ~~~~~^^^^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
>>> 
>>> map_fabricante_com_qtd_carros(carros, fabricantes[0])
KeyboardInterrupt
>>> 
>>> fabricantes[0]
{'id': 1, 'nome': 'GEELY', 'pais': 'China'}
>>> map_fabricante_com_qtd_carros(carros, fabricantes[0])
Traceback (most recent call last):
  File "<python-input-67>", line 1, in <module>
    map_fabricante_com_qtd_carros(carros, fabricantes[0])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "<python-input-59>", line 4, in map_fabricante_com_qtd_carros
    qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
  File "<python-input-63>", line 4, in contar_carros_por_fabricante
    if carro['fabricante_id'] == fabricante['id']:
       ~~~~~^^^^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
>>> 

>>> def map_fabricante_com_qtd_carros(lista_fabricantes, lista_carros):
...     lista_mapeada = []
...     for fabricante in lista_fabricantes:
...         qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
...         fabricante['qtd_carros'] = qtd_carros
...         lista_mapeada.append(fabricante)
...     return lista_mapeada
...     
>>> map_fabricante_com_qtd_carros(fabricantes, carros)
Traceback (most recent call last):
  File "<python-input-69>", line 1, in <module>
    map_fabricante_com_qtd_carros(fabricantes, carros)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "<python-input-68>", line 4, in map_fabricante_com_qtd_carros
    qtd_carros = contar_carros_por_fabricante(fabricante, lista_carros)
  File "<python-input-63>", line 4, in contar_carros_por_fabricante
    if carro['fabricante_id'] == fabricante['id']:
       ~~~~~^^^^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
>>> def contar_carros_por_fabricante(fabricante, lista_carros):
...     contador = 0
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante['id']:
...             contador = contador + 1
...     return contador
...     
>>> 
>>> map_fabricante_com_qtd_carros(fabricantes, carros)
[{'id': 1, 'nome': 'GEELY', 'pais': 'China', 'qtd_carros': 2}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia', 'qtd_carros': 1}, {'id': 3, 'nome': 'FIAT', 'pais': 'ITÁLIA', 'qtd_carros': 0}]
>>> 
>>> for fab in map_fabricante_com_qtd_carros(fabricantes, carros):
...     print(fab['id'], fab['nome'], fab['qtd_carros'])
...     
1 GEELY 2
2 VOLVO 1
3 FIAT 0
>>> 






>>> 
>>> def filtrar_carros_por_fabricante(lista_carros, fabricante_id):
...     lista_filtrados = []
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante_id:
...             lista_filtrados.append(carro)
...     return lista_filtrados
...     
>>> fabricantes
[{'id': 1, 'nome': 'GEELY', 'pais': 'China', 'qtd_carros': 2}, {'id': 2, 'nome': 'VOLVO', 'pais': 'Suécia', 'qtd_carros': 1}, {'id': 3, 'nome': 'FIAT', 'pais': 'ITÁLIA', 'qtd_carros': 0}]
>>> for carro in filtrar_carros_por_fabricante(carros, 2):
...     print(carro['nome'])
...     
EX 30
>>> for carro in filtrar_carros_por_fabricante(carros, 1):
...     print(carro['nome'])
...     
EX 2
EX 5
>>> 
>>> def filtrar(colecao, fn_criterio):
...     lista_filtrada = []
...     for item in colecao:
...         if fn_criterio(item):
...             lista_filtrada.append(item)
...     return lista_filtrada
...     
>>> r = filtrar(carros, lambda c:c['valor']>120000)
>>> 
>>> r
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}, {'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}, {'id': 3, 'nome': 'EX 30', 'valor': 230900, 'ano_fabricacao': 2024, 'fabricante_id': 2}]
>>> 



>>> r = filtrar(carros, lambda c:c['valor']>150000)
KeyboardInterrupt
>>> carros
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}, {'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}, {'id': 3, 'nome': 'EX 30', 'valor': 230900, 'ano_fabricacao': 2024, 'fabricante_id': 2}]
>>> r = filtrar(carros, lambda c:c['valor']>150000)
>>> 
>>> r
[{'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}, {'id': 3, 'nome': 'EX 30', 'valor': 230900, 'ano_fabricacao': 2024, 'fabricante_id': 2}]
>>> 




>>> carros
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}, {'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}, {'id': 3, 'nome': 'EX 30', 'valor': 230900, 'ano_fabricacao': 2024, 'fabricante_id': 2}]
>>> 
>>> def por_ano_2025_mais(carro):
...     return carro['ano_fabricacao'] >= 2025
...     
>>> r = filtrar(carros, por_ano_2025_mais)
>>> 
>>> r
[{'id': 1, 'nome': 'EX 2', 'valor': 126000, 'ano_fabricacao': 2026, 'fabricante_id': 1}, {'id': 2, 'nome': 'EX 5', 'valor': 200900, 'ano_fabricacao': 2025, 'fabricante_id': 1}]
>>> 


>>> def filtrar(colecao, fn_criterio):
...     lista_filtrada = []
...     for item in colecao:
...         if fn_criterio(item):
...             lista_filtrada.append(item)
...     return lista_filtrada
...     
>>> def filtrar_carros_por_fabricante(lista_carros, fabricante_id):
...     lista_filtrados = []
...     for carro in lista_carros:
...         if carro['fabricante_id'] == fabricante_id:
...             lista_filtrados.append(carro)
...     return lista_filtrados