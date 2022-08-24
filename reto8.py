numero = 12
lstBit = []
while (numero>1):
    resto = int(numero % 2)
    numero = numero / 2
    lstBit.append(resto)
lstBit = lstBit[::-1]
print(lstBit)