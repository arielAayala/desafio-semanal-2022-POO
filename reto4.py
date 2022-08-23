#Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#- La función recibirá por parámetro sólo UN polígono a la vez.
#- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#- Imprime el cálculo del área de un polígono de cada tipo.


def areaPoligono(poligono):
    if poligono == "triangulo" :
        alto = float(input(f"largo del {poligono}: "))
        ancho = float(input(f"ancho del {poligono}: "))
        calculo = (alto * ancho)/2
    elif poligono == "rectangulo":
        alto = float(input(f"largo del {poligono}: "))
        ancho = float(input(f"ancho del {poligono}: "))
        calculo = alto * ancho
    elif poligono == "cuadrado":
        lado = float(input(f"lado del {poligono}: "))
        calculo = lado * 4 
    else:
        print("error")
    print(f"el area del {poligono} es: {calculo}")

areaPoligono("triangulo")