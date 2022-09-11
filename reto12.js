class Palindromo{
    esPalindromo(palabra){
        let reversedWord = palabra.split("").reverse().join("")
        return reversedWord.toLowerCase() == palabra.toLowerCase()
    }
}
let palabra1 = new Palindromo()

console.log(palabra1.esPalindromo("hola aloH")) 