#Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#- La función recibirá por parámetro sólo UN polígono a la vez.
#- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#- Imprime el cálculo del área de un polígono de cada tipo.


def areaPoligono(alto,ancho):
    print(f"{(alto*ancho)/2} area de triangulo")
    print(f"{alto*2} area de cuadrado")
    print(f"{alto*ancho} area de rectangulo")

areaPoligono(2, 4)