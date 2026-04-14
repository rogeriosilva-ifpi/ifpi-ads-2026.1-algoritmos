def votar():
    voto = int(input("Digite seu voto (1-4 para candidatos, 0 branco, 5 nulo): "))
    if voto < 0 or voto > 5:
        print("Voto_inválido!")
        return None
    return voto

def contar_votos(c1, c2, c3, c4, brancos, nulos):
    return c1, c2, c3, c4, brancos, nulos

def mostrar_resultado(c1, c2, c3, c4, brancos, nulos):
    c1, c2, c3, c4, brancos, nulos = contar_votos(c1, c2, c3, c4, brancos, nulos)
    validos = c1 + c2 + c3 + c4
    
    print("=== RESULTADO DA ELEIÇÃO ===")
    print("Votos_válidos:", validos)
    print("Votos_branco:", brancos)
    print("Votos_nulos:", nulos)
    
    if validos == 0:
        print("Nenhum voto válido!")
        return
    
    p1 = (c1 * 100) / validos
    p2 = (c2 * 100) / validos
    p3 = (c3 * 100) / validos
    p4 = (c4 * 100) / validos
    
    print(f"Candidato 1: {c1} votos ({p1:.1f}%)")
    print(f"Candidato 2: {c2} votos ({p2:.1f}%)")
    print(f"Candidato 3: {c3} votos ({p3:.1f}%)")
    print(f"Candidato 4: {c4} votos ({p4:.1f}%)")
    
    maximo = c1
    if c2 > maximo:
        maximo = c2
    if c3 > maximo:
        maximo = c3
    if c4 > maximo:
        maximo = c4
    
    vencedores = ""
    if c1 == maximo:
        vencedores = vencedores + "1 "
    if c2 == maximo:
        vencedores = vencedores + "2 "
    if c3 == maximo:
        vencedores = vencedores + "3 "
    if c4 == maximo:
        vencedores = vencedores + "4 "
    
    print("Vencedor(es):", vencedores.strip())
    
    if maximo == c1 and c1 <= (validos * 50) / 100:
        print("SEGUNDO TURNO NECESSÁRIO!")
    elif maximo == c2 and c2 <= (validos * 50) / 100:
        print("SEGUNDO TURNO NECESSÁRIO!")
    elif maximo == c3 and c3 <= (validos * 50) / 100:
        print("SEGUNDO TURNO NECESSÁRIO!")
    elif maximo == c4 and c4 <= (validos * 50) / 100:
        print("SEGUNDO TURNO NECESSÁRIO!")

def main():
    c1 = c2 = c3 = c4 = brancos = nulos = 0
    encerrado = False
    
    while not encerrado:
        print("\n=== MENU ELEIÇÃO ===")
        print("1 - Votar")
        print("2 - Ver resultado")
        print("3 - Encerrar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            v = votar()
            if v is not None:
                if v == 1:
                    c1 += 1
                elif v == 2:
                    c2 += 1
                elif v == 3:
                    c3 += 1
                elif v == 4:
                    c4 += 1
                elif v == 0:
                    brancos += 1
                elif v == 5:
                    nulos += 1
                print("Voto registrado!")
        elif opcao == "2":
            mostrar_resultado(c1, c2, c3, c4, brancos, nulos)
        elif opcao == "3":
            encerrado = True
            print("Eleição encerrada.")
        else:
            print("Opção inválida!")

main()
