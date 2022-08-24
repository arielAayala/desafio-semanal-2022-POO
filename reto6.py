# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones 
# propias del lenguaje que lo hagan de forma automática. 
# - Si le pasamos 'Hola mundo' nos retornaría 'odnum aloH'

cadena= "hola mundo"
for i in reversed(range(len(cadena))):
    print(cadena[i])