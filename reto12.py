class Palindromo():
    def esPalindromo(self,palabra):
        reversedWord = "".join(list(reversed(palabra)))
        return reversedWord.lower() == palabra.lower()


palabra1 = Palindromo()
print(palabra1.esPalindromo("hola aloh"))
