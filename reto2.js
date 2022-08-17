let num = []
let cont = 0
while (cont < 50 ){
    if (cont <=1){
        console.log(cont)
        num.push(cont)
    }else{
        let suma = num[cont-1] + num[cont-2]
        console.log(suma)
        num.push(suma)
    }
    cont +=1
}
