def main():

    candidato_1_voto = 0
    candidato_2_voto = 0
    candidato_3_voto = 0
    candidato_4_voto = 0


    porcentual_cand_1 = 0
    porcentual_cand_2 = 0
    porcentual_cand_3 = 0
    porcentual_cand_4 = 0

    nulo = 0

    branco =0

    



    votos_totais = 0

    while True:
        

        votos_totais += 1


        print()
        print('**Tabela**')
        print()
        print('Candidato n° 1: voto >> 1')
        print()
        print('Candidato n° 2: voto >> 2')
        print()
        print('Candidato n° 3: voto >> 3')
        print()
        print('Candidato n° 4: voto >> 4')

        
        print()

        print('voto Branco: voto >>> 0')
        print()
        print('Voto nulo: voto >>> 5')
        print()

        voto = int(input('Digite seu voto(mostrar resultado = 10): '))
        print('>>>>>')

        if voto == 10:
            break


        if voto == 1:
            candidato_1_voto += 1


        elif voto == 2:
            candidato_2_voto += 1

        
        elif voto == 3:
            
            candidato_3_voto += 1

        
        elif voto == 4:

            candidato_4_voto += 1
        
        elif voto == 5 :

            nulo += 1

        elif voto == 0:

            branco += 1


    
    
    
    
    
    porcentual_cand_1 = (candidato_1_voto/votos_totais) * 100

    porcentual_cand_2 = (candidato_2_voto / votos_totais) * 100

    porcentual_cand_3 = (candidato_3_voto / votos_totais) * 100

    porcentual_cand_4 = (candidato_4_voto / votos_totais) * 100

    turno = segundo_turno(porcentual_cand_1, porcentual_cand_2, porcentual_cand_3, porcentual_cand_4)


    if candidato_1_voto > candidato_2_voto and candidato_1_voto > candidato_3_voto and candidato_1_voto > candidato_4_voto:
        print()
        print('***Resultado***')
        print()
        print('candidato n° 1: ')
        print(f'Votos: {candidato_1_voto} >>> {porcentual_cand_1}')
        print()
   
        print('candidato n° 2: ')
        print(f'Votos: {candidato_2_voto} >>> {porcentual_cand_2}')
        print()
        print('candidato n° 3: ')
        print(f'Votos: {candidato_3_voto} >>> {porcentual_cand_3}')
    
        print()
        print('candidato n° 4: ')
        print(f'Votos: {candidato_4_voto} >>> {porcentual_cand_4}')
        print()
        print(f'Vencedor: cadidato_1')
        print()
        print(f'Voto nulos: {nulos}')
        print(f'Brancos: {branco}')
        print()
        print(turno)
    
    elif  candidato_2_voto > candidato_3_voto and candidato_2_voto > candidato_1_voto and candidato_2_voto > candidato_4_voto:
        
        print()
        print('***Resultado***')
        print()
        print('candidato n° 1: ')
        print(f'Votos: {candidato_1_voto} >>> {porcentual_cand_1}')
        print()
   
        print('candidato n° 2: ')
        print(f'Votos: {candidato_2_voto} >>> {porcentual_cand_2}')
        print()
        print('candidato n° 3: ')
        print(f'Votos: {candidato_3_voto} >>> {porcentual_cand_3}')
    
        print()
        print('candidato n° 4: ')
        print(f'Votos: {candidato_4_voto} >>> {porcentual_cand_4}')
        print()
        print(f'Vencedor: cadidato_2')
        print()
        print()
        print(f'Voto nulos: {nulo}')
        print(f'Brancos: {branco}')
        print()
        print(turno)

    elif  candidato_3_voto > candidato_4_voto and candidato_3_voto > candidato_2_voto and candidato_3_voto > candidato_1_voto:
        
        print()
        print('***Resultado***')
        print()
        print('candidato n° 1: ')
        print(f'Votos: {candidato_1_voto} >>> {porcentual_cand_1}')
        print()
   
        print('candidato n° 2: ')
        print(f'Votos: {candidato_2_voto} >>> {porcentual_cand_2}')
        print()
        print('candidato n° 3: ')
        print(f'Votos: {candidato_3_voto} >>> {porcentual_cand_3}')
    
        print()
        print('candidato n° 4: ')
        print(f'Votos: {candidato_4_voto} >>> {porcentual_cand_4}')
        print()
        print(f'Vencedor: cadidato_3')
        print()
        print()
        print(f'Voto nulos: {nulo}')
        print(f'Brancos: {branco}')
        print()
        print(turno)

    elif  candidato_4_voto > candidato_3_voto and candidato_4_voto > candidato_1_voto and candidato_4_voto > candidato_2_voto:
        
        print()
        print('***Resultado***')
        print()
        print('candidato n° 1: ')
        print(f'Votos: {candidato_1_voto} >>> {porcentual_cand_1}')
        print()
   
        print('candidato n° 2: ')
        print(f'Votos: {candidato_2_voto} >>> {porcentual_cand_2}')
        print()
        print('candidato n° 3: ')
        print(f'Votos: {candidato_3_voto} >>> {porcentual_cand_3}')
    
        print()
        print('candidato n° 4: ')
        print(f'Votos: {candidato_4_voto} >>> {porcentual_cand_4}')
        print()
        print(f'Vencedor: cadidato_4')
        print()
        print()
        print(f'Voto nulos: {nulo}')
        print(f'Brancos: {branco}')
        print()
        print(truno)






    


   



    
    
    





def segundo_turno(n1, n2, n3, n4):

    if n1 > 50 or n2 > 50 or n3 > 50 or n4 > 50 :

        return 'não vai  ter segundo turno'
    
    else: 
        return 'vai ter segundo turno'






















main()