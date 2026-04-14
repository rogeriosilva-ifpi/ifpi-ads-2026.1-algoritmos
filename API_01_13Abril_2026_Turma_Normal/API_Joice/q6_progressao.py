AO = int(input("Informe o valorr inicial:"))
R = int(input(("Informe o valor de R:")))

razão = AO

for i in range (AO, R + razão):
    razão += i 
    print(razão)

