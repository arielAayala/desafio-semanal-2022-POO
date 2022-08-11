def anagrama(a,b):
    if len(a) == len(b) and a != b:
        cont = 0
        lstA = sorted((list(a)))
        lstB = sorted((list(b)))
        for i in lstA:
            if i == lstB[lstA.index(i)]:
                cont +=1
        return cont == len(a) and cont == len(b)     
    else:
        return False

print(anagrama("alan", "lana"))