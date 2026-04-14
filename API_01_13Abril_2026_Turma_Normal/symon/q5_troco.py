def pagar(qt, pago):
    
    total = 0
    for i in qt:
        total += float("Digite o valor do produto: ")

    if pago > total:
        
        cem = pago // 100
        restocem = pago % 100
        
        ciquenta = restocem // 50
        restociquenta = ciquenta % 50
        
        dez = restociquenta // 10
        restodez = dez % 10

        

