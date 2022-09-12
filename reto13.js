class Factorial{
    constructor() {
        this.suma = 1
    }

    numeroFactorial(num){
        if (num == 0){
            return 1
        }else{  
            for( let i = 1; i <= num; i++){
                this.suma *= i       
                if (this.suma == num){
                    return i
                }
            }
            return "No tiene factorial"
        }       
    }
};

let numero1 = new Factorial
console.log(numero1.numeroFactorial(24))