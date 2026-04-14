def main():
    pergunta = input("deseja vota? s - sim, n - não, encerrar")




  
    while pergunta == 's':
        voto = int(input("Vote em uns dos candidatos: 1- Candidato 1, 2 - candidato 2, 3 - candidato 3, 4 - Candidato 4, 0 - branco e 5 - nulo"))
        total_votos = 0
        brancos = 0
        nulos = 0
        pecent_cand1 = 0
        cand1 = 0
        pecent_cand2 = 0
        cand2 = 0
        pecent_cand3 = 0
        cand3 = 0
        pecent_cand4 = 0
        cand4 = 0

        if voto == 1:
            total_votos += 1
            cand1 += 1
            percent_cand1 = (cand1 / total_votos) * 100
        elif voto == 2:
            total_votos += 1
            cand2 += 1
            percent_cand2 = (cand2/ total_votos) * 100
        elif voto == 3:
            total_votos += 1
            cand3 += 1
            percent_cand3 = (cand3 / total_votos) * 100
        else:
            total_votos += 1
            cand4 += 1
            percent_cand4 = (cand4 / total_votos) * 100



        pergunta = input('Digite n para encerar e ver o resultado')
 
    print(f"votos brancos: {brancos}")
    print(f"votos nulos; {nulos}")
    print(f"votos válidos: {total_votos}")
    print(f"Percentual candidato 1 {percent_cand1}")
    print(f"Percentual candidato 2 {percent_cand2}")
    print(f"Percentual candidato 3 {percent_cand3}")
    print(f"Percentual candidato 4 {percent_cand4}")

    
    if percent_cand1 > (percent_cand2 and percent_cand3 and percent_cand4):
        print(f"O vencedor é: {percent_cand1}")
    elif percent_cand2 > (percent_cand1 and percent_cand3 and percent_cand4):
        print(f"O vencedor é: {percent_cand2}")
    elif percent_cand3 > (percent_cand2 and percent_cand1 and percent_cand4):
        print(f"O vencedor é: {percent_cand3}")
    elif percent_cand4 > (percent_cand2 and percent_cand3 and percent_cand1):
        print(f"O vencedor é: {percent_cand4}")
    
        
  

  














main()