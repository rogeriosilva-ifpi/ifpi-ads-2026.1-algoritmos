def main():
    N = int(input())
    quantidade = 0
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
            quantidade += 1
    
    print(f"Quantidade: {quantidade}")
           
main()