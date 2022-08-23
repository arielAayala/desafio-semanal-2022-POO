function primos (num){
    let cont = 0
    let i = 1
    while (i <= num) {
        if (num % i== 0){
            cont += 1
        }
        i +=1
    }
    if (cont == 2){
        console.log(num)
    }
}

let num = 1
while (num <= 100){
    primos(num)
    num +=1
}