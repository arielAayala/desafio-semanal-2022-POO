class Palindromo{
    constructor(palabra){
        this.palabra = palabra
    }
    esPalindromo(){
        let reversedWord = this.palabra.split("").reverse().join()
        console.log(reversedWord)
        console.log(this.palabra)
        return reversedWord == this.palabra
    }
}
let palabra1 = new Palindromo("neuquen")

palabra1.esPalindromo()