#codigo morse

morse = {
"a":".-","b":"-...","c":"-.-.",
"d":"-..","e":".","f":"..-.",
"g":"--.","h":"....","i":"..",
"j":".---","k":"-.-","l":".-..",
"m":"--","n":"-.","o":"---",
"p":".--.","q":"--.-","r":".-.",
"s":"...","t":"-","u":"..-",
"v":"...-","w":".--","x":"-..-",
"y":"-.--","z":"--.."}

texto = "hola como estas"

def traducir(text):
    text = text.strip()
    text = text.lower()
    if text[0].isalpha():
        abcAMorse(text)
    else:
        morseAAbc(text)



def abcAMorse(text):
    morseText = ""
    for i in text:
        if i == " ":
            morseText += " "
        else:
            for clave,valor in morse.items():
                if i == clave and i != " ":
                    morseText += valor + " "

    print(f"El texto '{text}' en codigo morse es:\n '{morseText}'")

def morseAAbc(text):
    abcText = ""
    textConvertido = text.replace("  ", " ° ")
    textConvertido = textConvertido.split(" ")
    for i in textConvertido:
        if i == "°":
            abcText += " "
        else:
            for clave,valor in morse.items():
                if i == valor:
                    abcText += clave
    
    print(f"El codigo morse'{text}' significa:\n '{abcText}'")



traducir(texto)