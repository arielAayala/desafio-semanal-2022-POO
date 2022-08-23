# Escribe un programa que se encargue de comprobar si un número es o no primo. 
# Hecho esto, imprime los números primos entre 1 y 100.

def primo(a):
    cont =0
    i = 1
    while(i <= a):
        if a%(i) == 0:
            cont +=1
        i +=1
    if cont == 2:
        print(a)


while(i <=100):
    primo(i)