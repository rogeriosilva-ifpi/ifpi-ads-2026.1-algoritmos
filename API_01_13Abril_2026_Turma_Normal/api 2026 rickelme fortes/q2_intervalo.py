def main():
    
    N = int(input("Digite um valor N: "))
    M = int(input("DIgite um valor M: "))

    if N > M:
        M == N
        N == M
    
    for i in range(N, M):
        if i % 2 != 0 and i % 3 == 0:
         soma = i + i
         print(i)
         
        





main()