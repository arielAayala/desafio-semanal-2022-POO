cont = 0
num = [0,1]
while cont < 50:
    if cont <=1:
        print(num[cont])
    else:
        suma = num[cont-1] + num[cont-2]
        num.append(suma)
        print(suma)
    cont +=1