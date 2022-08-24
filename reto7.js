let texto = "Hola, como estas?. Hola que onda? que como"
texto = texto.replace(/[?]/g,"").replace(/[,]/g,"").replace(/[.]/g,"").toLowerCase().split(" ")

let repetida = {}
let cont = 0
for (let i of texto) {
    if (cont == 0){
        repetida[i]=1
    }else{
        if (!(Object.entries(repetida).some(j=> j[0]==i))) {
            repetida[i]=1
        } else {
            repetida[i] +=1
        }
    }
    cont +=1
}

Object.entries(repetida).forEach(([clave,valor])=>{
    console.log("hay "+valor+" palabra "+clave)})