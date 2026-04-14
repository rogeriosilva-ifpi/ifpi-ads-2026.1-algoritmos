        
def main():
    num = int(input("Insira o numero: "))
    count = 0
    print("Divisores: ", end=" ")
    for i in range (1, num+1):
        for j in range (1, num+1):
            if(i * j == num):   
                print(f"{i}", end=" ")
                count += 1
    print(f"\nTotal: {count} divisores")

main()
