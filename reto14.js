class Armstrong{
    constructor(){
        this.suma = 0
    }

    esArmstrong(num){
        let lst = (num.toString().split("")).map(function(i){return parseInt(i)**(num.toString()).length})
        lst.forEach(i => {
            this.suma += i
        })
        return this.suma == num
    }
}

let num1 = new Armstrong
console.log(num1.esArmstrong(1634))