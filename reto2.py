cont = 0
num = []
while cont < 50:
    if cont <=1:
        num.append(cont)
        print(cont)
    else:
        suma = num[cont-1] + num[cont-2]
        num.append(suma)
        print(suma)
    cont +=1