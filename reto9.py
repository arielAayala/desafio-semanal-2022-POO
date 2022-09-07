expresion = "{[3+4(1/2)]*2}"


def verificarExpresion(text):
    cont = 0
    for i in text:
        if i == "{" or i == "(" or i == "[":
            cont += 1
        elif i == "}" or i == ")" or i == "]":
            cont -=1
    return cont == 0


print(verificarExpresion(expresion))


    