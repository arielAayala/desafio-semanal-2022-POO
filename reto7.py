#Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el 
# recuento final de todas ellas. - Los signos de puntuación no forman parte de la palabra. 
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas. 
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.


texto = "hola, como estas?. hola que onda? que como"
for i in (("?", ""), (".", ""),(",","")):
    texto = texto.replace(*i)
texto = texto.lower()
texto = (texto.split(" "))



repetida = {}
cont = 0
for i in texto:
    if cont == 0:     
        repetida[i] = 1
    else:
        if  not any(i == clave for clave,valor in repetida.items()):
            repetida[i] = 1
        else:
            repetida[i] +=1
    cont +=1


for clave,valor in repetida.items():
    print(f"hay {valor} palabra {clave} ")

        