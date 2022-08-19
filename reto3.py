# Escribe un programa que se encargue de comprobar si un número es o no primo. 
# Hecho esto, imprime los números primos entre 1 y 100.

def primo(a):
    cont =0
    for i in range(a):
        if a%(i+1) == 0:
            cont +=1
    if cont == 2:
        print(a)


for i in range(99):
    primo(i+1)