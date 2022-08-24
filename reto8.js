let numero = 12
let lstBit = []
let resto = 0
while (numero > 1){
    resto = parseInt(numero % 2)
    numero = numero/2
    lstBit.push(resto)
}
console.log(lstBit.reverse())